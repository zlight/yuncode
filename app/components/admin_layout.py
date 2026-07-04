import reflex as rx
from app.components.admin_sidebar import admin_sidebar
from app.components.admin_navbar import admin_header
from app.components.admin_views import overview_view, users_view, settings_view
from app.states.admin_state import AdminState
from app.states.theme_state import ThemeState


def admin_dashboard_layout() -> rx.Component:
    return rx.el.div(
        admin_sidebar(),
        rx.el.div(
            admin_header(),
            rx.el.main(
                rx.match(
                    AdminState.current_tab,
                    ("overview", overview_view()),
                    ("users", users_view()),
                    ("settings", settings_view()),
                    overview_view(),
                ),
                class_name="max-w-[1600px] mx-auto px-6 py-8 relative z-10",
            ),
            class_name="lg:ml-64 min-h-screen flex flex-col",
        ),
        class_name="font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
    )
