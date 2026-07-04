"""Coupon validation service (local, in-memory)."""

from __future__ import annotations

from typing import TypedDict


class CouponRecord(TypedDict):
    code: str
    discount_pct: float
    description_en: str
    description_zh: str
    active: bool
    min_amount: float


COUPONS: dict[str, CouponRecord] = {
    "SAVE10": {
        "code": "SAVE10",
        "discount_pct": 10.0,
        "description_en": "10% off any order",
        "description_zh": "任意订单立减 10%",
        "active": True,
        "min_amount": 0.0,
    },
    "SAVE20": {
        "code": "SAVE20",
        "discount_pct": 20.0,
        "description_en": "20% off orders over ¥100",
        "description_zh": "满 100 元立减 20%",
        "active": True,
        "min_amount": 100.0,
    },
    "WELCOME": {
        "code": "WELCOME",
        "discount_pct": 15.0,
        "description_en": "Welcome bonus 15% off",
        "description_zh": "新客户 15% 折扣",
        "active": True,
        "min_amount": 0.0,
    },
}


async def list_coupons() -> list[CouponRecord]:
    return [c for c in COUPONS.values() if c["active"]]


async def get_coupon(code: str) -> CouponRecord | None:
    if not code:
        return None
    return COUPONS.get(code.strip().upper())


async def validate_coupon(
    code: str, order_amount: float
) -> tuple[bool, str, float]:
    """Validate a coupon for a given amount.

    Returns (ok, code_reason, discount_pct).
    code_reason ∈ {"ok", "not_found", "inactive", "min_amount"}.
    """
    if not code or not code.strip():
        return True, "ok", 0.0
    c = COUPONS.get(code.strip().upper())
    if c is None:
        return False, "not_found", 0.0
    if not c["active"]:
        return False, "inactive", 0.0
    if float(order_amount) < float(c["min_amount"]):
        return False, "min_amount", 0.0
    return True, "ok", float(c["discount_pct"])


__all__ = [
    "CouponRecord",
    "COUPONS",
    "list_coupons",
    "get_coupon",
    "validate_coupon",
]
