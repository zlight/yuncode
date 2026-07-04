import reflex as rx
import json
from app.services.api_response import (
    user_profile_response,
    plans_catalog_response,
    orders_response,
    monitor_response,
    error,
    validation_error,
    not_found,
    SAMPLE_USER_PROFILE,
    SAMPLE_PLAN,
    SAMPLE_ORDER,
    SAMPLE_MONITOR_SERIES,
    SAMPLE_MONITOR_PEAKS,
    SAMPLE_MONITOR_EVENTS,
    BizCode,
)
import logging


def _pretty(obj: dict) -> str:
    try:
        return json.dumps(obj, indent=2, ensure_ascii=False)
    except Exception:
        logging.exception("Unexpected error")
        return str(obj)


class ApiDemoState(rx.State):
    active_example: str = "user_profile"

    @rx.event
    def set_example(self, key: str):
        self.active_example = key

    @rx.var
    def user_profile_json(self) -> str:
        return _pretty(user_profile_response(SAMPLE_USER_PROFILE))

    @rx.var
    def plans_catalog_json(self) -> str:
        return _pretty(
            plans_catalog_response(
                plans=[SAMPLE_PLAN],
                page=1,
                page_size=20,
                total=1,
                filters={"region": "hk", "node": "HKBGP"},
            )
        )

    @rx.var
    def order_created_json(self) -> str:
        from app.services.api_response import created

        return _pretty(created(data=SAMPLE_ORDER))

    @rx.var
    def orders_list_json(self) -> str:
        return _pretty(
            orders_response(
                orders=[SAMPLE_ORDER], page=1, page_size=20, total=1
            )
        )

    @rx.var
    def monitor_json(self) -> str:
        return _pretty(
            monitor_response(
                series=SAMPLE_MONITOR_SERIES,
                range_key="24h",
                events=SAMPLE_MONITOR_EVENTS,
                peaks=SAMPLE_MONITOR_PEAKS,
            )
        )

    @rx.var
    def not_found_json(self) -> str:
        return _pretty(not_found(resource="user"))

    @rx.var
    def validation_error_json(self) -> str:
        return _pretty(
            validation_error(
                field="password",
                message_en="Password is required",
                message_zh="密码为必填项",
                code=BizCode.MISSING_FIELD,
            )
        )

    @rx.var
    def insufficient_balance_json(self) -> str:
        return _pretty(
            error(
                code=BizCode.INSUFFICIENT_BALANCE,
                details={"required": 45.00, "current": 12.50},
            )
        )

    @rx.var
    def rate_limited_json(self) -> str:
        return _pretty(
            error(
                code=BizCode.RATE_LIMITED,
                details={"retry_after_sec": 30},
            )
        )

    @rx.var
    def current_json(self) -> str:
        mapping = {
            "user_profile": self.user_profile_json,
            "plans_catalog": self.plans_catalog_json,
            "order_created": self.order_created_json,
            "orders_list": self.orders_list_json,
            "monitor": self.monitor_json,
            "not_found": self.not_found_json,
            "validation_error": self.validation_error_json,
            "insufficient_balance": self.insufficient_balance_json,
            "rate_limited": self.rate_limited_json,
        }
        return mapping.get(self.active_example, self.user_profile_json)
