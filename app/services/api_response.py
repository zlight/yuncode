"""
Unified API response format utilities for AiarksCloud.

Provides pure-Python, reusable helpers for constructing consistent success,
error, list, and paginated responses. Designed to be transport-agnostic:
callable from Reflex state event handlers today (backed by JSON files) and
easily portable to a real HTTP/DB backend tomorrow.

Response envelope shape
-----------------------
Every response is a dict with the following shape:

    {
        "ok": bool,                         # True on success, False on error
        "http_status": int,                 # HTTP-style status code
        "code": str,                        # Business status code (see BizCode)
        "message": {                        # Bilingual human-readable message
            "en": str,
            "zh": str,
        },
        "data": Any | None,                 # Payload on success (None on error)
        "error": {                          # Structured error (None on success)
            "code": str,
            "field": str,                   # Optional field-level pointer
            "details": dict,                # Extra context (safe to expose)
            "message": {"en": str, "zh": str},
        } | None,
        "meta": {                           # Standard metadata block
            "request_id": str,
            "timestamp": str,               # ISO-8601 UTC
            "trace_id": str,                # Optional distributed trace id
            "duration_ms": int,             # Optional server processing time
            "pagination": {                 # Present only for list responses
                "page": int,
                "page_size": int,
                "total": int,
                "total_pages": int,
                "has_next": bool,
                "has_prev": bool,
            } | None,
        },
    }

The envelope is deliberately verbose so the same shape can be returned by
JSON files today and by an HTTP/DB backend later, without breaking clients.
"""

from __future__ import annotations

import secrets
from datetime import datetime, timezone
from typing import Any, TypedDict


# ==================== HTTP status codes ====================
class HttpStatus:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    GONE = 410
    UNPROCESSABLE = 422
    TOO_MANY_REQUESTS = 429
    INTERNAL_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504


# ==================== Business status codes ====================
class BizCode:
    """Application-level status codes.

    These are stable strings that survive HTTP status changes and are the
    primary discriminator for clients. Use these in tests, logs and UI
    branching, not the raw HTTP status.
    """

    # Success
    OK = "ok"
    CREATED = "created"
    ACCEPTED = "accepted"

    # Client / validation
    BAD_REQUEST = "bad_request"
    VALIDATION_ERROR = "validation_error"
    MISSING_FIELD = "missing_field"
    INVALID_FIELD = "invalid_field"

    # Auth
    UNAUTHENTICATED = "unauthenticated"
    INVALID_CREDENTIALS = "invalid_credentials"
    SESSION_EXPIRED = "session_expired"
    FORBIDDEN = "forbidden"
    VIP_REQUIRED = "vip_required"

    # Resource
    NOT_FOUND = "not_found"
    ALREADY_EXISTS = "already_exists"
    EMAIL_EXISTS = "email_exists"
    USERNAME_EXISTS = "username_exists"
    CONFLICT = "conflict"
    GONE = "gone"

    # Business
    INSUFFICIENT_BALANCE = "insufficient_balance"
    OUT_OF_STOCK = "out_of_stock"
    PLAN_UNAVAILABLE = "plan_unavailable"
    QUOTA_EXCEEDED = "quota_exceeded"
    RATE_LIMITED = "rate_limited"
    ORDER_FAILED = "order_failed"
    PAYMENT_FAILED = "payment_failed"
    COUPON_INVALID = "coupon_invalid"

    # System
    INTERNAL_ERROR = "internal_error"
    SERVICE_UNAVAILABLE = "service_unavailable"
    UPSTREAM_ERROR = "upstream_error"
    TIMEOUT = "timeout"


# Default bilingual messages per business code. Callers may override.
_DEFAULT_MESSAGES: dict[str, dict[str, str]] = {
    BizCode.OK: {"en": "OK", "zh": "成功"},
    BizCode.CREATED: {"en": "Created", "zh": "创建成功"},
    BizCode.ACCEPTED: {"en": "Accepted", "zh": "已受理"},
    BizCode.BAD_REQUEST: {"en": "Bad request", "zh": "请求参数有误"},
    BizCode.VALIDATION_ERROR: {
        "en": "Validation failed",
        "zh": "请求参数校验失败",
    },
    BizCode.MISSING_FIELD: {"en": "Missing field", "zh": "缺少必填字段"},
    BizCode.INVALID_FIELD: {"en": "Invalid field value", "zh": "字段值无效"},
    BizCode.UNAUTHENTICATED: {
        "en": "Please log in to continue",
        "zh": "请先登录后再继续",
    },
    BizCode.INVALID_CREDENTIALS: {
        "en": "Invalid email or password",
        "zh": "邮箱或密码错误",
    },
    BizCode.SESSION_EXPIRED: {
        "en": "Session expired, please log in again",
        "zh": "会话已过期,请重新登录",
    },
    BizCode.FORBIDDEN: {
        "en": "You do not have permission",
        "zh": "无权访问此资源",
    },
    BizCode.VIP_REQUIRED: {
        "en": "This feature requires VIP membership",
        "zh": "该功能仅面向 VIP 用户",
    },
    BizCode.NOT_FOUND: {"en": "Resource not found", "zh": "资源不存在"},
    BizCode.ALREADY_EXISTS: {
        "en": "Resource already exists",
        "zh": "资源已存在",
    },
    BizCode.EMAIL_EXISTS: {
        "en": "This email is already registered",
        "zh": "该邮箱已被注册",
    },
    BizCode.USERNAME_EXISTS: {
        "en": "This username is already taken",
        "zh": "该用户名已被占用",
    },
    BizCode.CONFLICT: {"en": "Resource conflict", "zh": "资源冲突"},
    BizCode.GONE: {"en": "Resource is gone", "zh": "资源已下线"},
    BizCode.INSUFFICIENT_BALANCE: {
        "en": "Insufficient balance, please top up",
        "zh": "账户余额不足,请先充值",
    },
    BizCode.OUT_OF_STOCK: {
        "en": "This plan is currently out of stock",
        "zh": "该套餐当前无库存",
    },
    BizCode.PLAN_UNAVAILABLE: {
        "en": "Selected plan is not available",
        "zh": "所选套餐不可用",
    },
    BizCode.QUOTA_EXCEEDED: {"en": "Quota exceeded", "zh": "已超过配额限制"},
    BizCode.RATE_LIMITED: {
        "en": "Too many requests, please slow down",
        "zh": "请求过于频繁,请稍后再试",
    },
    BizCode.ORDER_FAILED: {"en": "Order creation failed", "zh": "订单创建失败"},
    BizCode.PAYMENT_FAILED: {"en": "Payment failed", "zh": "支付失败"},
    BizCode.COUPON_INVALID: {"en": "Invalid coupon code", "zh": "优惠码无效"},
    BizCode.INTERNAL_ERROR: {
        "en": "Internal server error",
        "zh": "服务器内部错误",
    },
    BizCode.SERVICE_UNAVAILABLE: {
        "en": "Service temporarily unavailable",
        "zh": "服务暂时不可用",
    },
    BizCode.UPSTREAM_ERROR: {
        "en": "Upstream service error",
        "zh": "上游服务异常",
    },
    BizCode.TIMEOUT: {"en": "Request timed out", "zh": "请求超时"},
}


# Default HTTP status per business code (used when caller doesn't override).
_DEFAULT_HTTP_STATUS: dict[str, int] = {
    BizCode.OK: HttpStatus.OK,
    BizCode.CREATED: HttpStatus.CREATED,
    BizCode.ACCEPTED: HttpStatus.ACCEPTED,
    BizCode.BAD_REQUEST: HttpStatus.BAD_REQUEST,
    BizCode.VALIDATION_ERROR: HttpStatus.UNPROCESSABLE,
    BizCode.MISSING_FIELD: HttpStatus.UNPROCESSABLE,
    BizCode.INVALID_FIELD: HttpStatus.UNPROCESSABLE,
    BizCode.UNAUTHENTICATED: HttpStatus.UNAUTHORIZED,
    BizCode.INVALID_CREDENTIALS: HttpStatus.UNAUTHORIZED,
    BizCode.SESSION_EXPIRED: HttpStatus.UNAUTHORIZED,
    BizCode.FORBIDDEN: HttpStatus.FORBIDDEN,
    BizCode.VIP_REQUIRED: HttpStatus.FORBIDDEN,
    BizCode.NOT_FOUND: HttpStatus.NOT_FOUND,
    BizCode.ALREADY_EXISTS: HttpStatus.CONFLICT,
    BizCode.EMAIL_EXISTS: HttpStatus.CONFLICT,
    BizCode.USERNAME_EXISTS: HttpStatus.CONFLICT,
    BizCode.CONFLICT: HttpStatus.CONFLICT,
    BizCode.GONE: HttpStatus.GONE,
    BizCode.INSUFFICIENT_BALANCE: HttpStatus.UNPROCESSABLE,
    BizCode.OUT_OF_STOCK: HttpStatus.CONFLICT,
    BizCode.PLAN_UNAVAILABLE: HttpStatus.CONFLICT,
    BizCode.QUOTA_EXCEEDED: HttpStatus.UNPROCESSABLE,
    BizCode.RATE_LIMITED: HttpStatus.TOO_MANY_REQUESTS,
    BizCode.ORDER_FAILED: HttpStatus.UNPROCESSABLE,
    BizCode.PAYMENT_FAILED: HttpStatus.UNPROCESSABLE,
    BizCode.COUPON_INVALID: HttpStatus.UNPROCESSABLE,
    BizCode.INTERNAL_ERROR: HttpStatus.INTERNAL_ERROR,
    BizCode.SERVICE_UNAVAILABLE: HttpStatus.SERVICE_UNAVAILABLE,
    BizCode.UPSTREAM_ERROR: HttpStatus.BAD_GATEWAY,
    BizCode.TIMEOUT: HttpStatus.GATEWAY_TIMEOUT,
}


# ==================== TypedDicts (for typing consumers) ====================
class BilingualMessage(TypedDict):
    en: str
    zh: str


class PaginationMeta(TypedDict):
    page: int
    page_size: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool


class ResponseMeta(TypedDict, total=False):
    request_id: str
    timestamp: str
    trace_id: str
    duration_ms: int
    pagination: PaginationMeta | None


class ErrorObject(TypedDict, total=False):
    code: str
    field: str
    details: dict
    message: BilingualMessage


# ==================== Utilities ====================
def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def _new_request_id() -> str:
    return "req_" + secrets.token_hex(8)


def _resolve_message(
    code: str,
    message_en: str | None,
    message_zh: str | None,
) -> BilingualMessage:
    default = _DEFAULT_MESSAGES.get(code, {"en": code, "zh": code})
    return {
        "en": message_en or default["en"],
        "zh": message_zh or default["zh"],
    }


def _base_meta(
    request_id: str | None = None,
    trace_id: str = "",
    duration_ms: int = 0,
) -> ResponseMeta:
    meta: ResponseMeta = {
        "request_id": request_id or _new_request_id(),
        "timestamp": _now_iso(),
        "trace_id": trace_id,
        "duration_ms": int(duration_ms),
        "pagination": None,
    }
    return meta


def make_pagination(page: int, page_size: int, total: int) -> PaginationMeta:
    """Build a normalized pagination metadata block."""
    page = max(1, int(page))
    page_size = max(1, int(page_size))
    total = max(0, int(total))
    total_pages = max(1, -(-total // page_size)) if total > 0 else 1
    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }


# ==================== Success builders ====================
def success(
    data: Any = None,
    code: str = BizCode.OK,
    message_en: str | None = None,
    message_zh: str | None = None,
    http_status: int | None = None,
    request_id: str | None = None,
    trace_id: str = "",
    duration_ms: int = 0,
) -> dict:
    """Build a standard successful response envelope."""
    return {
        "ok": True,
        "http_status": http_status
        or _DEFAULT_HTTP_STATUS.get(code, HttpStatus.OK),
        "code": code,
        "message": _resolve_message(code, message_en, message_zh),
        "data": data,
        "error": None,
        "meta": _base_meta(request_id, trace_id, duration_ms),
    }


def created(data: Any = None, **kwargs) -> dict:
    """Convenience wrapper for 201 Created responses."""
    return success(data=data, code=BizCode.CREATED, **kwargs)


def accepted(data: Any = None, **kwargs) -> dict:
    """Convenience wrapper for 202 Accepted responses."""
    return success(data=data, code=BizCode.ACCEPTED, **kwargs)


def list_response(
    items: list,
    page: int = 1,
    page_size: int = 20,
    total: int | None = None,
    code: str = BizCode.OK,
    message_en: str | None = None,
    message_zh: str | None = None,
    request_id: str | None = None,
    trace_id: str = "",
    duration_ms: int = 0,
    extra: dict | None = None,
) -> dict:
    """Build a paginated list response.

    - `items` is the current page of items.
    - `total` defaults to len(items) if not supplied (for un-paginated calls).
    - `extra` merges additional top-level fields into `data` alongside items.
    """
    if total is None:
        total = len(items)
    pagination = make_pagination(page, page_size, total)
    data: dict = {"items": items}
    if extra:
        data.update(extra)
    envelope = success(
        data=data,
        code=code,
        message_en=message_en,
        message_zh=message_zh,
        request_id=request_id,
        trace_id=trace_id,
        duration_ms=duration_ms,
    )
    envelope["meta"]["pagination"] = pagination
    return envelope


# ==================== Error builders ====================
def error(
    code: str = BizCode.INTERNAL_ERROR,
    message_en: str | None = None,
    message_zh: str | None = None,
    http_status: int | None = None,
    field: str = "",
    details: dict | None = None,
    request_id: str | None = None,
    trace_id: str = "",
    duration_ms: int = 0,
) -> dict:
    """Build a standard error response envelope."""
    msg = _resolve_message(code, message_en, message_zh)
    err: ErrorObject = {
        "code": code,
        "field": field,
        "details": details or {},
        "message": msg,
    }
    return {
        "ok": False,
        "http_status": http_status
        or _DEFAULT_HTTP_STATUS.get(code, HttpStatus.INTERNAL_ERROR),
        "code": code,
        "message": msg,
        "data": None,
        "error": err,
        "meta": _base_meta(request_id, trace_id, duration_ms),
    }


def validation_error(
    field: str,
    message_en: str,
    message_zh: str,
    code: str = BizCode.INVALID_FIELD,
    **kwargs,
) -> dict:
    """Build a 422 validation error scoped to a single field."""
    return error(
        code=code,
        message_en=message_en,
        message_zh=message_zh,
        field=field,
        **kwargs,
    )


def not_found(
    resource: str = "resource",
    message_en: str | None = None,
    message_zh: str | None = None,
    **kwargs,
) -> dict:
    return error(
        code=BizCode.NOT_FOUND,
        message_en=message_en or f"{resource} not found",
        message_zh=message_zh or f"{resource} 不存在",
        details={"resource": resource},
        **kwargs,
    )


def unauthorized(**kwargs) -> dict:
    return error(code=BizCode.UNAUTHENTICATED, **kwargs)


def forbidden(**kwargs) -> dict:
    return error(code=BizCode.FORBIDDEN, **kwargs)


def conflict(code: str = BizCode.CONFLICT, **kwargs) -> dict:
    return error(code=code, **kwargs)


# ==================== Domain-specific example builders ====================
# These builders wrap the raw records produced by app/services/user_store.py
# (the current JSON-file persistence layer) into the unified envelope. They
# are intentionally shape-preserving: swapping the data source (DB / real
# HTTP API) later requires no envelope changes on the caller side.


def user_profile_response(profile: dict, request_id: str | None = None) -> dict:
    """Wrap a public user profile in the unified envelope.

    `profile` is expected to be the shape returned by
    `user_store.get_public_profile`.
    """
    if not profile:
        return not_found(resource="user", request_id=request_id)
    normalized = {
        "email": profile.get("email", ""),
        "username": profile.get("username", ""),
        "is_vip": bool(profile.get("is_vip", False)),
        "balance": float(profile.get("balance", 0.0)),
        "ak_coins": int(profile.get("ak_coins", 0)),
        "total_spending": float(profile.get("total_spending", 0.0)),
        "referral_earnings": float(profile.get("referral_earnings", 0.0)),
        "invitation_code": profile.get("invitation_code", ""),
        "created_at": profile.get("created_at", ""),
    }
    return success(data=normalized, request_id=request_id)


def plans_catalog_response(
    plans: list[dict],
    page: int = 1,
    page_size: int = 20,
    total: int | None = None,
    filters: dict | None = None,
    request_id: str | None = None,
) -> dict:
    """Wrap a filtered plan catalog into a paginated list envelope."""
    return list_response(
        items=plans,
        page=page,
        page_size=page_size,
        total=total,
        request_id=request_id,
        extra={"filters": filters or {}},
    )


def orders_response(
    orders: list[dict],
    page: int = 1,
    page_size: int = 20,
    total: int | None = None,
    request_id: str | None = None,
) -> dict:
    return list_response(
        items=orders,
        page=page,
        page_size=page_size,
        total=total,
        request_id=request_id,
    )


def instances_response(
    instances: list[dict],
    page: int = 1,
    page_size: int = 20,
    total: int | None = None,
    request_id: str | None = None,
) -> dict:
    return list_response(
        items=instances,
        page=page,
        page_size=page_size,
        total=total,
        request_id=request_id,
    )


def billing_response(
    records: list[dict],
    page: int = 1,
    page_size: int = 20,
    total: int | None = None,
    summary: dict | None = None,
    request_id: str | None = None,
) -> dict:
    return list_response(
        items=records,
        page=page,
        page_size=page_size,
        total=total,
        request_id=request_id,
        extra={"summary": summary or {}},
    )


def dns_response(
    records: list[dict],
    domain: str = "",
    request_id: str | None = None,
) -> dict:
    return list_response(
        items=records,
        page=1,
        page_size=max(1, len(records)),
        total=len(records),
        request_id=request_id,
        extra={"domain": domain},
    )


def firewall_response(
    rules: list[dict],
    instance_id: str = "",
    request_id: str | None = None,
) -> dict:
    return list_response(
        items=rules,
        page=1,
        page_size=max(1, len(rules)),
        total=len(rules),
        request_id=request_id,
        extra={"instance_id": instance_id},
    )


def monitor_response(
    series: list[dict],
    range_key: str = "24h",
    events: list[dict] | None = None,
    peaks: dict | None = None,
    request_id: str | None = None,
) -> dict:
    return success(
        data={
            "range": range_key,
            "series": series,
            "events": events or [],
            "peaks": peaks or {},
        },
        request_id=request_id,
    )


# ==================== Sample fixture data ====================
# Sample payloads used for documentation / demo screens (Phase 3). These are
# static, deterministic examples that mirror the real production shapes.

SAMPLE_USER_PROFILE: dict = {
    "email": "demo@aiarks.com",
    "username": "Demo",
    "is_vip": False,
    "balance": 128.50,
    "ak_coins": 2480,
    "total_spending": 1210.00,
    "referral_earnings": 86.40,
    "invitation_code": "AIARKS-DEMO",
    "created_at": "2025-01-14T09:22:11Z",
}

SAMPLE_PLAN: dict = {
    "id": "hk-pro-a",
    "name": "HK-Pro-竞技A",
    "tag": "共享带宽",
    "region": "hk",
    "region_flag": "🇭🇰",
    "region_code": "HKBGP",
    "node": "HKBGP",
    "cpu": "1 Core",
    "ram": "1024 M",
    "disk": "10 GB",
    "bandwidth": "10000M",
    "traffic": "Unlimited",
    "line": "CN2 GIA · HKIX",
    "reset_traffic": "¥99999.99",
    "ipv4": "1 IP",
    "ipv6": "1 IP",
    "price": 50.00,
    "stock": 12,
    "highlight": True,
}

SAMPLE_ORDER: dict = {
    "id": "AC-9F3A2B",
    "email": "demo@aiarks.com",
    "created_at": "2025-10-11T14:03:08Z",
    "plan_id": "hk-pro-a",
    "plan_name": "HK-Pro-竞技A",
    "region": "hk",
    "region_name": "HongKong",
    "region_flag": "🇭🇰",
    "node": "HKBGP",
    "system": "Debian 11",
    "cycle": "1 Month",
    "cycle_months": 1,
    "coupon": "SAVE10",
    "discount_pct": 10.0,
    "base_amount": 50.00,
    "amount": 45.00,
    "currency": "CNY",
    "status": "paid",
    "instance_id": "hkbgps1-2025101114030812ab",
}

SAMPLE_INSTANCE: dict = {
    "id": "hkbgps1-2025101114030812ab",
    "name": "hkbgps1-2025101114030812ab",
    "status": "running",
    "ip": "103.28.201.42",
    "region": "HongKong",
    "region_flag": "🇭🇰",
    "node": "HKBGP",
    "plan": "HK-Pro-竞技A",
    "plan_id": "hk-pro-a",
    "cpu": "1 Core",
    "ram": "1024 M",
    "disk": "10 GB",
    "bandwidth": "10000M",
    "traffic_used": "377.06 MB",
    "traffic_total": "Unlimited",
    "traffic_percent": 3,
    "reset_price": "¥99999.99",
    "price": "¥50.00/月",
    "expires": "2025-12-14 20:48:00",
    "auto_renew": True,
    "health": "healthy",
    "os": "Debian 11",
    "system": "debian-11",
    "created": "2025-10-11T14:03:08Z",
    "order_id": "AC-9F3A2B",
}

SAMPLE_BILLING: list[dict] = [
    {
        "id": "#AC-9F3A2B",
        "date": "2025-10-11",
        "item": "HK-Pro-竞技A · 开通",
        "cycle": "1 Month",
        "amount": "¥45.00",
        "status": "paid",
    },
    {
        "id": "#AC-8B21CC",
        "date": "2025-09-11",
        "item": "MOLite-Standard · 续费",
        "cycle": "1 Month",
        "amount": "¥99.99",
        "status": "paid",
    },
    {
        "id": "#AC-7A1104",
        "date": "2025-09-05",
        "item": "Traffic pack 500 GB",
        "cycle": "One-time",
        "amount": "¥20.00",
        "status": "paid",
    },
]

SAMPLE_DNS_RECORDS: list[dict] = [
    {
        "id": "dns-1",
        "name": "@",
        "type": "A",
        "value": "103.28.201.42",
        "ttl": "600",
        "status": "active",
    },
    {
        "id": "dns-2",
        "name": "www",
        "type": "A",
        "value": "103.28.201.42",
        "ttl": "600",
        "status": "active",
    },
    {
        "id": "dns-3",
        "name": "mail",
        "type": "MX",
        "value": "10 mail.aiarks.com",
        "ttl": "3600",
        "status": "active",
    },
]

SAMPLE_FIREWALL_RULES: list[dict] = [
    {
        "id": "fw-01",
        "action": "ALLOW",
        "protocol": "TCP",
        "port": "22",
        "source": "0.0.0.0/0",
        "desc": "SSH access",
        "enabled": True,
    },
    {
        "id": "fw-02",
        "action": "ALLOW",
        "protocol": "TCP",
        "port": "443",
        "source": "0.0.0.0/0",
        "desc": "HTTPS",
        "enabled": True,
    },
    {
        "id": "fw-05",
        "action": "DENY",
        "protocol": "TCP",
        "port": "23",
        "source": "0.0.0.0/0",
        "desc": "Block Telnet",
        "enabled": True,
    },
]

SAMPLE_MONITOR_SERIES: list[dict] = [
    {
        "time": "12:00",
        "cpu": 58,
        "memory": 68,
        "net_in": 890,
        "net_out": 640,
        "disk": 38,
    },
    {
        "time": "14:00",
        "cpu": 72,
        "memory": 74,
        "net_in": 1120,
        "net_out": 780,
        "disk": 39,
    },
    {
        "time": "16:00",
        "cpu": 66,
        "memory": 71,
        "net_in": 980,
        "net_out": 690,
        "disk": 40,
    },
]

SAMPLE_MONITOR_PEAKS: dict = {
    "cpu": {"value": 72, "at": "14:00"},
    "memory": {"value": 74, "at": "14:00"},
    "network": {"value": 1120, "unit": "KB/s", "at": "14:00"},
    "disk": {"value": 42, "at": "22:00"},
}

SAMPLE_MONITOR_EVENTS: list[dict] = [
    {
        "time": "10 min ago",
        "level": "info",
        "icon": "circle-check",
        "message": "Snapshot 'daily-backup' created successfully",
    },
    {
        "time": "1 hr ago",
        "level": "warn",
        "icon": "triangle-alert",
        "message": "CPU usage exceeded 70% for 3 minutes",
    },
    {
        "time": "1 day ago",
        "level": "critical",
        "icon": "circle_alert",
        "message": "DDoS attack mitigated · 2.4 Gbps peak",
    },
]


# ==================== Sample envelope factory ====================
def build_sample_responses() -> dict[str, dict]:
    """Return a dict of pre-built sample envelopes covering every domain.

    Useful for documentation, developer preview screens, and Phase 3
    demo pages. The keys correspond to business surfaces; each value is a
    fully-formed unified envelope.
    """
    return {
        "user_profile_success": user_profile_response(SAMPLE_USER_PROFILE),
        "user_profile_not_found": not_found(resource="user"),
        "plans_catalog": plans_catalog_response(
            plans=[SAMPLE_PLAN],
            page=1,
            page_size=20,
            total=1,
            filters={"region": "hk", "node": "HKBGP", "sort_by": "recommended"},
        ),
        "plans_out_of_stock": error(
            code=BizCode.OUT_OF_STOCK,
            details={"plan_id": SAMPLE_PLAN["id"]},
        ),
        "orders_list": orders_response(
            orders=[SAMPLE_ORDER], page=1, page_size=20, total=1
        ),
        "order_created": created(data=SAMPLE_ORDER),
        "order_payment_failed": error(
            code=BizCode.PAYMENT_FAILED,
            details={"reason": "insufficient_balance", "shortfall": 12.50},
        ),
        "instances_list": instances_response(
            instances=[SAMPLE_INSTANCE], page=1, page_size=20, total=1
        ),
        "instances_empty": instances_response(
            instances=[], page=1, page_size=20, total=0
        ),
        "billing_list": billing_response(
            records=SAMPLE_BILLING,
            page=1,
            page_size=20,
            total=len(SAMPLE_BILLING),
            summary={"total_paid": 164.99, "currency": "CNY"},
        ),
        "dns_records": dns_response(
            records=SAMPLE_DNS_RECORDS, domain="aiarks.example.com"
        ),
        "firewall_rules": firewall_response(
            rules=SAMPLE_FIREWALL_RULES, instance_id=SAMPLE_INSTANCE["id"]
        ),
        "monitor_snapshot": monitor_response(
            series=SAMPLE_MONITOR_SERIES,
            range_key="24h",
            events=SAMPLE_MONITOR_EVENTS,
            peaks=SAMPLE_MONITOR_PEAKS,
        ),
        "auth_required": unauthorized(),
        "auth_invalid_credentials": error(code=BizCode.INVALID_CREDENTIALS),
        "email_exists": error(code=BizCode.EMAIL_EXISTS, field="email"),
        "validation_missing_password": validation_error(
            field="password",
            message_en="Password is required",
            message_zh="密码为必填项",
            code=BizCode.MISSING_FIELD,
        ),
        "rate_limited": error(
            code=BizCode.RATE_LIMITED,
            details={"retry_after_sec": 30},
        ),
        "internal_error": error(code=BizCode.INTERNAL_ERROR),
    }


__all__ = [
    "HttpStatus",
    "BizCode",
    "BilingualMessage",
    "PaginationMeta",
    "ResponseMeta",
    "ErrorObject",
    "make_pagination",
    "success",
    "created",
    "accepted",
    "list_response",
    "error",
    "validation_error",
    "not_found",
    "unauthorized",
    "forbidden",
    "conflict",
    "user_profile_response",
    "plans_catalog_response",
    "orders_response",
    "instances_response",
    "billing_response",
    "dns_response",
    "firewall_response",
    "monitor_response",
    "build_sample_responses",
    "SAMPLE_USER_PROFILE",
    "SAMPLE_PLAN",
    "SAMPLE_ORDER",
    "SAMPLE_INSTANCE",
    "SAMPLE_BILLING",
    "SAMPLE_DNS_RECORDS",
    "SAMPLE_FIREWALL_RULES",
    "SAMPLE_MONITOR_SERIES",
    "SAMPLE_MONITOR_PEAKS",
    "SAMPLE_MONITOR_EVENTS",
]
