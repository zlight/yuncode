import reflex as rx
from app.states.ui_state import UIState


NAV_ITEMS: list[dict[str, str]] = [
    {"label": "Home", "href": "#hero", "badge": "", "highlight": "false"},
    {
        "label": "Products",
        "href": "#products",
        "badge": "",
        "highlight": "false",
    },
    {
        "label": "Light Server",
        "href": "#products",
        "badge": "New",
        "highlight": "false",
    },
    {"label": "Network", "href": "#nodes", "badge": "", "highlight": "false"},
    {"label": "Pricing", "href": "#pricing", "badge": "", "highlight": "false"},
    {"label": "Trust", "href": "#trust", "badge": "", "highlight": "false"},
    {"label": "ATerminal", "href": "#", "badge": "", "highlight": "true"},
    {"label": "FAQ", "href": "#faq", "badge": "", "highlight": "false"},
]


def _nav_link(item: dict[str, str]) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            item["label"],
            class_name=rx.cond(
                item["highlight"] == "true",
                "text-yellow-400 font-medium",
                "text-gray-300 hover:text-white transition-colors font-medium",
            ),
        ),
        rx.cond(
            item["badge"] != "",
            rx.el.span(
                item["badge"],
                class_name="ml-1.5 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-semibold",
            ),
            rx.fragment(),
        ),
        href=item["href"],
        class_name="flex items-center text-sm px-3 py-2",
    )


def _mobile_link(item: dict[str, str]) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            item["label"],
            class_name=rx.cond(
                item["highlight"] == "true",
                "text-yellow-400 font-medium text-base",
                "text-gray-200 font-medium text-base",
            ),
        ),
        rx.cond(
            item["badge"] != "",
            rx.el.span(
                item["badge"],
                class_name="ml-2 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-semibold",
            ),
            rx.fragment(),
        ),
        rx.icon("chevron-right", size=16, class_name="ml-auto text-gray-500"),
        href=item["href"],
        on_click=UIState.close_mobile_menu,
        class_name="flex items-center px-4 py-3 rounded-lg hover:bg-white/5 border border-transparent hover:border-white/10 transition-colors",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-blue-400"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/30 flex items-center justify-center",
                ),
                rx.el.span(
                    "AkileCloud",
                    class_name="text-white font-semibold text-base tracking-tight",
                ),
                href="#hero",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.foreach(NAV_ITEMS, _nav_link),
                class_name="hidden lg:flex items-center gap-1",
                aria_label="Main navigation",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("languages", size=16, class_name="text-gray-400"),
                    class_name="hidden sm:flex p-2 rounded-md hover:bg-white/5 transition-colors",
                    aria_label="Change language",
                ),
                rx.el.button(
                    "Log In",
                    class_name="hidden sm:inline-block text-sm text-gray-300 hover:text-white px-3 py-1.5 font-medium transition-colors",
                ),
                rx.el.button(
                    "Sign up",
                    class_name="hidden sm:inline-block text-sm bg-blue-500 hover:bg-blue-400 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-lg shadow-blue-500/20",
                ),
                rx.el.button(
                    rx.icon(
                        rx.cond(UIState.mobile_menu_open, "x", "menu"),
                        size=20,
                        class_name="text-white",
                    ),
                    on_click=UIState.toggle_mobile_menu,
                    class_name="lg:hidden p-2 rounded-md hover:bg-white/5 transition-colors",
                    aria_label="Toggle menu",
                    aria_expanded=UIState.mobile_menu_open.to_string(),
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
        ),
        rx.cond(
            UIState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    rx.foreach(NAV_ITEMS, _mobile_link),
                    class_name="flex flex-col gap-1 p-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Log In",
                        class_name="flex-1 text-sm text-gray-300 border border-white/10 hover:border-white/20 px-4 py-2.5 rounded-md font-medium transition-colors",
                    ),
                    rx.el.button(
                        "Sign up",
                        class_name="flex-1 text-sm bg-blue-500 hover:bg-blue-400 text-white px-4 py-2.5 rounded-md font-medium transition-colors",
                    ),
                    class_name="flex items-center gap-2 p-4 border-t border-white/5",
                ),
                class_name="lg:hidden border-t border-white/5 bg-[#0a0d14]/95 backdrop-blur-xl",
            ),
            rx.fragment(),
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-[#0a0d14]/70 border-b border-white/5",
    )