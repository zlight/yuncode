import reflex as rx
from app.states.ui_state import UIState
from app.states.language_state import LanguageState


def _nav_link_element(
    label: rx.Var, href: str, badge: str = "", highlight: str = "false"
) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            label,
            class_name=rx.cond(
                highlight == "true",
                "text-yellow-400 font-medium",
                "text-gray-300 hover:text-white transition-colors font-medium",
            ),
        ),
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-1.5 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-semibold",
            ),
            rx.fragment(),
        ),
        href=href,
        class_name="flex items-center text-sm px-3 py-2",
    )


def _mobile_link_element(
    label: rx.Var, href: str, badge: str = "", highlight: str = "false"
) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            label,
            class_name=rx.cond(
                highlight == "true",
                "text-yellow-400 font-medium text-base",
                "text-gray-200 font-medium text-base",
            ),
        ),
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-2 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 font-semibold",
            ),
            rx.fragment(),
        ),
        rx.icon("chevron-right", size=16, class_name="ml-auto text-gray-500"),
        href=href,
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
            # Navigation links mapped to localized values from state
            rx.el.nav(
                _nav_link_element(LanguageState.nav_home, "#hero"),
                _nav_link_element(LanguageState.nav_products, "#products"),
                _nav_link_element(
                    LanguageState.nav_light_server, "#products", badge="New"
                ),
                _nav_link_element(LanguageState.nav_network, "#nodes"),
                _nav_link_element(LanguageState.nav_pricing, "#pricing"),
                _nav_link_element(LanguageState.nav_trust, "#trust"),
                _nav_link_element(LanguageState.nav_faq, "#faq"),
                _nav_link_element(
                    rx.Var.create("ATerminal"), "#", highlight="true"
                ),
                class_name="hidden lg:flex items-center gap-1",
                aria_label="Main navigation",
            ),
            # Right actions
            rx.el.div(
                # Language Switch Button (Desktop)
                rx.el.button(
                    rx.icon(
                        "languages", size=16, class_name="text-blue-400 mr-1.5"
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-gray-300 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
                    aria_label="Switch language",
                ),
                rx.el.button(
                    LanguageState.nav_login,
                    class_name="hidden sm:inline-block text-sm text-gray-300 hover:text-white px-3 py-1.5 font-medium transition-colors cursor-pointer",
                ),
                rx.el.button(
                    LanguageState.nav_signup,
                    class_name="hidden sm:inline-block text-sm bg-blue-500 hover:bg-blue-400 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-lg shadow-blue-500/20 cursor-pointer",
                ),
                rx.el.button(
                    rx.icon(
                        rx.cond(UIState.mobile_menu_open, "x", "menu"),
                        size=20,
                        class_name="text-white",
                    ),
                    on_click=UIState.toggle_mobile_menu,
                    class_name="lg:hidden p-2 rounded-md hover:bg-white/5 transition-colors cursor-pointer",
                    aria_label="Toggle menu",
                    aria_expanded=UIState.mobile_menu_open.to_string(),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
        ),
        # Mobile menu
        rx.cond(
            UIState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    _mobile_link_element(LanguageState.nav_home, "#hero"),
                    _mobile_link_element(
                        LanguageState.nav_products, "#products"
                    ),
                    _mobile_link_element(
                        LanguageState.nav_light_server, "#products", badge="New"
                    ),
                    _mobile_link_element(LanguageState.nav_network, "#nodes"),
                    _mobile_link_element(LanguageState.nav_pricing, "#pricing"),
                    _mobile_link_element(LanguageState.nav_trust, "#trust"),
                    _mobile_link_element(LanguageState.nav_faq, "#faq"),
                    _mobile_link_element(
                        rx.Var.create("ATerminal"), "#", highlight="true"
                    ),
                    class_name="flex flex-col gap-1 p-4",
                ),
                # Language Switch Button (Mobile)
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            "languages",
                            size=16,
                            class_name="text-blue-400 mr-2",
                        ),
                        rx.cond(
                            LanguageState.is_zh,
                            "Switch to English",
                            "切换至中文",
                        ),
                        on_click=[
                            LanguageState.toggle_language,
                            UIState.close_mobile_menu,
                        ],
                        class_name="w-full flex items-center justify-center py-2.5 rounded-lg bg-white/5 border border-white/10 text-sm text-gray-300 hover:text-white transition-all cursor-pointer",
                    ),
                    class_name="px-4 pb-2",
                ),
                rx.el.div(
                    rx.el.button(
                        LanguageState.nav_login,
                        class_name="flex-1 text-sm text-gray-300 border border-white/10 hover:border-white/20 px-4 py-2.5 rounded-md font-medium transition-colors cursor-pointer",
                    ),
                    rx.el.button(
                        LanguageState.nav_signup,
                        class_name="flex-1 text-sm bg-blue-500 hover:bg-blue-400 text-white px-4 py-2.5 rounded-md font-medium transition-colors cursor-pointer",
                    ),
                    class_name="flex items-center gap-2 p-4 border-t border-white/5",
                ),
                class_name="lg:hidden border-t border-white/5 bg-[#0a0d14]/95 backdrop-blur-xl",
            ),
            rx.fragment(),
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-[#0a0d14]/70 border-b border-white/5",
    )