"""
Unified local backend facade.

This module is the single entry point for frontend state classes to make
"backend requests". Every function returns a unified response envelope
(see app/services/api_response.py) — the same shape a real HTTP/DB backend
would return — so wiring up new UI features and swapping to a real backend
later requires no envelope changes on the caller side.

Coverage:
- Auth & sessions:      register / login / logout / current session profile
- User profile:         get_profile / refresh_profile / upgrade_vip / adjust_balance
- Catalog config:       regions / machine types / systems / cycles / nodes
- Plans catalog:        query with filter+sort+pagination, get one plan
- Coupons:              list / validate
- Orders:               list, get, create (with balance & stock)
- Instances:            list, get, update (auto_renew, etc.)
- Billing:              list per user (derived from orders)
- DNS:                  list / add / update / delete
- Firewall:             list / add / toggle / delete
- Monitoring:           snapshot / series / peaks / events
"""

from __future__ import annotations

import logging
import secrets
from datetime import datetime, timezone

from app.services import (
    api_response,
    catalog_store,
    coupon_store,
    dns_store,
    firewall_store,
    monitor_store,
    user_store,
)
from app.services.api_response import BizCode


# ==================== Small helpers ====================
def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _order_to_billing_row(order: dict) -> dict:
    created = str(order.get("created_at", ""))
    date_part = created.split("T")[0] if "T" in created else created[:10] or "-"
    plan_name = str(order.get("plan_name", "-"))
    currency = str(order.get("currency", "CNY")).upper()
    symbol = "¥" if currency == "CNY" else "$"
    try:
        amount = float(order.get("amount", 0.0))
    except (TypeError, ValueError):
        amount = 0.0
    return {
        "id": "#" + str(order.get("id", "")),
        "date": date_part,
        "item": f"{plan_name} · 开通",
        "cycle": str(order.get("cycle", "-")),
        "amount": f"{symbol}{amount:.2f}",
        "status": str(order.get("status", "paid")),
    }


# ==================== Auth & sessions ====================
async def register(
    email: str,
    username: str,
    password: str,
    invitation_code: str = "",
) -> dict:
    email = (email or "").strip().lower()
    username = (username or "").strip()
    password = password or ""

    if not email or "@" not in email:
        return api_response.validation_error(
            field="email",
            message_en="Please provide a valid email address",
            message_zh="请提供有效的电子邮箱地址",
        )
    if not username or len(username) < 3:
        return api_response.validation_error(
            field="username",
            message_en="Username must be at least 3 characters",
            message_zh="用户名长度不能少于 3 位",
        )
    if len(password) < 6:
        return api_response.validation_error(
            field="password",
            message_en="Password must be at least 6 characters",
            message_zh="密码长度不能少于 6 位",
        )

    try:
        ok, code, rec = await user_store.create_user(
            email=email,
            username=username,
            password=password,
            invitation_code=invitation_code,
        )
    except Exception as e:
        logging.exception(f"register error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    if not ok:
        if code == "email_exists":
            return api_response.error(code=BizCode.EMAIL_EXISTS, field="email")
        if code == "username_exists":
            return api_response.error(
                code=BizCode.USERNAME_EXISTS, field="username"
            )
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    profile = await user_store.get_public_profile(email)
    return api_response.created(data=profile)


async def login(email: str, password: str) -> dict:
    email = (email or "").strip().lower()
    if not email or not password:
        return api_response.validation_error(
            field="email" if not email else "password",
            message_en="Email and password are required",
            message_zh="邮箱和密码为必填项",
            code=BizCode.MISSING_FIELD,
        )
    try:
        ok, code, rec = await user_store.verify_password(email, password)
    except Exception as e:
        logging.exception(f"login error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    if not ok:
        if code == "not_found":
            return api_response.error(code=BizCode.NOT_FOUND, field="email")
        return api_response.error(code=BizCode.INVALID_CREDENTIALS)

    try:
        token = await user_store.create_session(email)
    except Exception as e:
        logging.exception(f"login create_session error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    profile = await user_store.get_public_profile(email)
    return api_response.success(data={"token": token, "profile": profile})


async def logout(token: str) -> dict:
    try:
        await user_store.destroy_session(token)
    except Exception as e:
        logging.exception(f"logout error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    return api_response.success(data={"logged_out": True})


async def current_session(token: str) -> dict:
    if not token:
        return api_response.unauthorized()
    try:
        sess = await user_store.get_session(token)
    except Exception as e:
        logging.exception(f"session lookup error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    if not sess:
        return api_response.error(code=BizCode.SESSION_EXPIRED)
    email = str(sess.get("email", ""))
    profile = await user_store.get_public_profile(email)
    return api_response.success(
        data={"email": email, "profile": profile, "token": token}
    )


# ==================== User profile ====================
async def get_user_profile(email: str) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    profile = await user_store.get_public_profile(email)
    return api_response.user_profile_response(profile)


async def upgrade_vip(email: str) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        await user_store.upgrade_vip(email)
    except Exception as e:
        logging.exception(f"upgrade_vip error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    return api_response.success(data=await user_store.get_public_profile(email))


# ==================== Catalog config ====================
async def get_regions() -> dict:
    return api_response.success(data=await catalog_store.get_regions())


async def get_machine_types() -> dict:
    return api_response.success(data=await catalog_store.get_machine_types())


async def get_systems() -> dict:
    return api_response.success(data=await catalog_store.get_systems())


async def get_cycles() -> dict:
    return api_response.success(data=await catalog_store.get_cycles())


async def get_nodes(region: str) -> dict:
    nodes = await catalog_store.get_available_nodes(region)
    return api_response.success(data={"region": region, "nodes": nodes})


# ==================== Plans catalog ====================
async def query_plans(
    region: str = "",
    node: str = "",
    search: str = "",
    price_min: float | None = None,
    price_max: float | None = None,
    sort_by: str = "recommended",
    page: int = 1,
    page_size: int = 20,
) -> dict:
    try:
        items, total = await catalog_store.query_plans(
            region=region,
            node=node,
            search=search,
            price_min=price_min,
            price_max=price_max,
            sort_by=sort_by,
            page=page,
            page_size=page_size,
        )
    except Exception as e:
        logging.exception(f"query_plans error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    filters = {
        "region": region,
        "node": node,
        "search": search,
        "price_min": price_min,
        "price_max": price_max,
        "sort_by": sort_by,
    }
    return api_response.plans_catalog_response(
        plans=items,
        page=page,
        page_size=page_size,
        total=total,
        filters=filters,
    )


async def get_plan(plan_id: str) -> dict:
    plan = await catalog_store.get_plan(plan_id)
    if plan is None:
        return api_response.not_found(resource="plan")
    return api_response.success(data=plan)


# ==================== Coupons ====================
async def list_coupons() -> dict:
    return api_response.success(data=await coupon_store.list_coupons())


async def validate_coupon(code: str, order_amount: float) -> dict:
    ok, reason, pct = await coupon_store.validate_coupon(code, order_amount)
    if ok:
        return api_response.success(
            data={"code": (code or "").strip().upper(), "discount_pct": pct}
        )
    if reason == "not_found":
        return api_response.error(
            code=BizCode.COUPON_INVALID,
            field="coupon",
            details={"reason": "not_found"},
        )
    if reason == "min_amount":
        return api_response.error(
            code=BizCode.COUPON_INVALID,
            field="coupon",
            details={"reason": "min_amount", "order_amount": order_amount},
        )
    return api_response.error(code=BizCode.COUPON_INVALID, field="coupon")


# ==================== Orders ====================
async def list_orders(email: str, page: int = 1, page_size: int = 20) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        orders = await user_store.get_user_orders(email)
    except Exception as e:
        logging.exception(f"list_orders error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    orders = list(reversed(orders))
    total = len(orders)
    page = max(1, int(page))
    page_size = max(1, int(page_size))
    start = (page - 1) * page_size
    end = start + page_size
    return api_response.orders_response(
        orders=orders[start:end],
        page=page,
        page_size=page_size,
        total=total,
    )


async def get_order(email: str, order_id: str) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        orders = await user_store.get_user_orders(email)
    except Exception as e:
        logging.exception(f"get_order error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    for o in orders:
        if str(o.get("id")) == order_id:
            return api_response.success(data=o)
    return api_response.not_found(resource="order")


async def create_order(
    email: str,
    plan_id: str,
    cycle_id: str,
    system_id: str,
    coupon_code: str = "",
    region: str = "",
    node: str = "",
) -> dict:
    """End-to-end order creation: validates plan+coupon, decrements stock,
    charges balance, creates order and instance records, returns envelope."""
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()

    plan = await catalog_store.get_plan(plan_id)
    if plan is None:
        return api_response.not_found(resource="plan")
    if plan["stock"] <= 0:
        return api_response.error(
            code=BizCode.OUT_OF_STOCK, details={"plan_id": plan_id}
        )

    # Cycle lookup
    cycles = await catalog_store.get_cycles()
    cycle = None
    for c in cycles:
        if c["id"] == cycle_id:
            cycle = c
            break
    if cycle is None:
        return api_response.validation_error(
            field="cycle_id",
            message_en="Invalid billing cycle",
            message_zh="无效的计费周期",
        )
    try:
        multiplier = float(cycle["mult"])
    except (TypeError, ValueError):
        multiplier = 1.0
    try:
        months = int(cycle_id)
    except (TypeError, ValueError):
        months = 1

    base_amount = round(plan["price"] * multiplier, 2)

    # Coupon
    ok_c, reason_c, pct = await coupon_store.validate_coupon(
        coupon_code, base_amount
    )
    if not ok_c and reason_c != "ok":
        return api_response.error(
            code=BizCode.COUPON_INVALID,
            field="coupon",
            details={"reason": reason_c},
        )
    final_amount = round(base_amount * (1.0 - pct / 100.0), 2)

    # Balance & charge
    try:
        (
            ok_bal,
            code_bal,
            new_balance,
        ) = await user_store.deduct_balance_and_charge(email, final_amount)
    except Exception as e:
        logging.exception(f"charge error: {e}")
        return api_response.error(code=BizCode.PAYMENT_FAILED)

    if not ok_bal:
        if code_bal == "insufficient_balance":
            return api_response.error(
                code=BizCode.INSUFFICIENT_BALANCE,
                details={"required": final_amount, "current": new_balance},
            )
        return api_response.error(code=BizCode.PAYMENT_FAILED)

    # Decrement stock
    ok_s, new_stock = await catalog_store.decrement_stock(plan_id)
    if not ok_s:
        return api_response.error(code=BizCode.OUT_OF_STOCK)

    # System label
    system_label = system_id
    for s in await catalog_store.get_systems():
        if s["id"] == system_id:
            system_label = s["label"]
            break

    # Timestamps
    now_utc = datetime.now(timezone.utc)
    ts = now_utc.strftime("%Y%m%d%H%M%S")
    node_lower = plan["node"].lower()
    instance_id = f"{node_lower}s1-{ts}{secrets.token_hex(3)}"

    # Compute expiry (approximate month math)
    year = now_utc.year + (months // 12)
    month = ((now_utc.month - 1 + (months % 12)) % 12) + 1
    try:
        expires = now_utc.replace(year=year, month=month)
    except ValueError:
        expires = now_utc

    order_data = {
        "plan_id": plan_id,
        "plan_name": plan["name"],
        "region": region or plan["region"],
        "region_flag": plan["region_flag"],
        "node": node or plan["node"],
        "system": system_label,
        "cycle": cycle["label_en"],
        "cycle_months": months,
        "coupon": (coupon_code or "").strip().upper(),
        "discount_pct": pct,
        "base_amount": base_amount,
        "amount": final_amount,
        "currency": "CNY",
        "status": "paid",
        "instance_id": instance_id,
    }
    try:
        order_id = await user_store.create_order(email, order_data)
    except Exception as e:
        logging.exception(f"create_order error: {e}")
        return api_response.error(code=BizCode.ORDER_FAILED)

    instance_data = {
        "id": instance_id,
        "name": instance_id,
        "status": "running",
        "ip": f"103.28.{secrets.randbelow(250)}.{secrets.randbelow(250)}",
        "region": plan["region"],
        "region_flag": plan["region_flag"],
        "node": plan["node"],
        "plan": plan["name"],
        "plan_id": plan_id,
        "cpu": plan["cpu"],
        "ram": plan["ram"],
        "disk": plan["disk"],
        "bandwidth": plan["bandwidth"],
        "traffic_used": "0 MB",
        "traffic_total": plan["traffic"],
        "traffic_percent": 0,
        "reset_price": plan["reset_traffic"],
        "price": f"¥{plan['price']:.2f}/月",
        "expires": expires.strftime("%Y-%m-%d %H:%M:%S"),
        "auto_renew": True,
        "health": "healthy",
        "os": system_label,
        "system": system_id,
        "order_id": order_id,
    }
    try:
        await user_store.create_instance(email, instance_data)
    except Exception as e:
        logging.exception(f"create_instance error: {e}")

    return api_response.created(
        data={
            "order_id": order_id,
            "instance_id": instance_id,
            "amount": final_amount,
            "new_balance": new_balance,
            "new_stock": new_stock,
            "order": {"id": order_id, **order_data, "created_at": _now_iso()},
        }
    )


# ==================== Instances ====================
async def list_instances(
    email: str, page: int = 1, page_size: int = 20
) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        instances = await user_store.get_user_instances(email)
    except Exception as e:
        logging.exception(f"list_instances error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    total = len(instances)
    page = max(1, int(page))
    page_size = max(1, int(page_size))
    start = (page - 1) * page_size
    end = start + page_size
    return api_response.instances_response(
        instances=instances[start:end],
        page=page,
        page_size=page_size,
        total=total,
    )


async def get_instance(email: str, instance_id: str) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        instances = await user_store.get_user_instances(email)
    except Exception as e:
        logging.exception(f"get_instance error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    for i in instances:
        if str(i.get("id")) == instance_id:
            return api_response.success(data=i)
    return api_response.not_found(resource="instance")


async def update_instance(email: str, instance_id: str, updates: dict) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    if not updates:
        return api_response.validation_error(
            field="updates",
            message_en="No update fields provided",
            message_zh="未提供更新字段",
        )
    try:
        ok = await user_store.update_instance(email, instance_id, updates)
    except Exception as e:
        logging.exception(f"update_instance error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)
    if not ok:
        return api_response.not_found(resource="instance")
    return await get_instance(email, instance_id)


# ==================== Billing ====================
async def list_billing(email: str, page: int = 1, page_size: int = 20) -> dict:
    email = (email or "").strip().lower()
    if not email:
        return api_response.unauthorized()
    try:
        orders = await user_store.get_user_orders(email)
    except Exception as e:
        logging.exception(f"list_billing error: {e}")
        return api_response.error(code=BizCode.INTERNAL_ERROR)

    records = [_order_to_billing_row(o) for o in reversed(orders)]
    total_paid = 0.0
    for o in orders:
        try:
            total_paid += float(o.get("amount", 0.0))
        except (TypeError, ValueError):
            continue

    total = len(records)
    page = max(1, int(page))
    page_size = max(1, int(page_size))
    start = (page - 1) * page_size
    end = start + page_size
    return api_response.billing_response(
        records=records[start:end],
        page=page,
        page_size=page_size,
        total=total,
        summary={"total_paid": round(total_paid, 2), "currency": "CNY"},
    )


# ==================== DNS ====================
async def list_dns(instance_id: str = "default") -> dict:
    records = await dns_store.list_records(instance_id)
    return api_response.dns_response(records=records, domain=instance_id)


async def add_dns(instance_id: str, record: dict) -> dict:
    if not record.get("name") or not record.get("value"):
        return api_response.validation_error(
            field="name" if not record.get("name") else "value",
            message_en="Both name and value are required",
            message_zh="主机名与记录值均为必填项",
        )
    rec = await dns_store.add_record(instance_id, record)
    return api_response.created(data=rec)


async def update_dns(instance_id: str, record_id: str, updates: dict) -> dict:
    rec = await dns_store.update_record(instance_id, record_id, updates)
    if rec is None:
        return api_response.not_found(resource="dns_record")
    return api_response.success(data=rec)


async def delete_dns(instance_id: str, record_id: str) -> dict:
    ok = await dns_store.delete_record(instance_id, record_id)
    if not ok:
        return api_response.not_found(resource="dns_record")
    return api_response.success(data={"deleted": record_id})


# ==================== Firewall ====================
async def list_firewall(instance_id: str = "default") -> dict:
    rules = await firewall_store.list_rules(instance_id)
    return api_response.firewall_response(rules=rules, instance_id=instance_id)


async def add_firewall(instance_id: str, rule: dict) -> dict:
    if not rule.get("port"):
        return api_response.validation_error(
            field="port",
            message_en="Port is required",
            message_zh="端口为必填项",
        )
    r = await firewall_store.add_rule(instance_id, rule)
    return api_response.created(data=r)


async def toggle_firewall(instance_id: str, rule_id: str) -> dict:
    r = await firewall_store.toggle_rule(instance_id, rule_id)
    if r is None:
        return api_response.not_found(resource="firewall_rule")
    return api_response.success(data=r)


async def delete_firewall(instance_id: str, rule_id: str) -> dict:
    ok = await firewall_store.delete_rule(instance_id, rule_id)
    if not ok:
        return api_response.not_found(resource="firewall_rule")
    return api_response.success(data={"deleted": rule_id})


# ==================== Monitoring ====================
async def get_monitor_snapshot(
    instance_id: str = "", range_key: str = "24h"
) -> dict:
    snap = await monitor_store.get_snapshot(instance_id, range_key)
    return api_response.monitor_response(
        series=snap["series"],
        range_key=snap["range"],
        events=snap["events"],
        peaks=snap["peaks"],
    )


async def get_monitor_series(
    instance_id: str = "", range_key: str = "24h"
) -> dict:
    return api_response.success(
        data={
            "instance_id": instance_id,
            "range": range_key,
            "series": await monitor_store.get_series(instance_id, range_key),
        }
    )


async def get_monitor_events(instance_id: str = "", limit: int = 20) -> dict:
    events = await monitor_store.get_events(instance_id, limit)
    return api_response.list_response(
        items=events, page=1, page_size=len(events) or 1, total=len(events)
    )


__all__ = [
    "register",
    "login",
    "logout",
    "current_session",
    "get_user_profile",
    "upgrade_vip",
    "get_regions",
    "get_machine_types",
    "get_systems",
    "get_cycles",
    "get_nodes",
    "query_plans",
    "get_plan",
    "list_coupons",
    "validate_coupon",
    "list_orders",
    "get_order",
    "create_order",
    "list_instances",
    "get_instance",
    "update_instance",
    "list_billing",
    "list_dns",
    "add_dns",
    "update_dns",
    "delete_dns",
    "list_firewall",
    "add_firewall",
    "toggle_firewall",
    "delete_firewall",
    "get_monitor_snapshot",
    "get_monitor_series",
    "get_monitor_events",
]
