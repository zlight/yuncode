import reflex as rx
from app.admin.admin_layout import admin_dashboard_layout as _layout


def admin_dashboard_layout() -> rx.Component:
    return _layout()
