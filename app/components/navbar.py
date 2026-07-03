import reflex as rx
from app.states.ui_state import UIState
from app.states.language_state import LanguageState
from app.states.shop_state import ShopState


def _nav_link_element(
    label: rx.Var, href: str, badge: str = "", highlight: str = "false"
) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            label,
            class_name=rx.cond(
                highlight == "true",
                "text-indigo-600 font-semibold",
                "text-slate-600 hover:text-indigo-600 transition-colors font-medium",
            ),
        ),
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-1.5 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-100 text-emerald-700 font-semibold",
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
                "text-indigo-600 font-semibold text-base",
                "text-slate-800 font-medium text-base",
            ),
        ),
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-2 text-[10px] px-1.5 py-0.5 rounded-md bg-emerald-100 text-emerald-700 font-semibold",
            ),
            rx.fragment(),
        ),
        rx.icon("chevron-right", size=16, class_name="ml-auto text-slate-400"),
        href=href,
        on_click=UIState.close_mobile_menu,
        class_name="flex items-center px-4 py-3 rounded-lg hover:bg-slate-50 border border-transparent hover:border-slate-100 transition-colors",
    )


def _region_dropdown_item(region: rx.Var) -> rx.Component:
    name = rx.cond(LanguageState.is_zh, region["name_zh"], region["name_en"])
    return rx.el.a(
        rx.el.span(region["flag"], class_name="text-lg"),
        rx.el.div(
            rx.el.p(name, class_name="text-sm text-slate-800 font-medium"),
            rx.el.p(
                region["id"].to(str).upper() + "BGP",
                class_name="text-[10px] text-slate-400 tracking-wider",
            ),
            class_name="flex flex-col",
        ),
        rx.icon(
            "arrow-up-right",
            size=12,
            class_name="ml-auto text-slate-300 group-hover/item:text-indigo-600 transition-colors",
        ),
        href=f"/shop/server?region={region['id']}",
        class_name="group/item flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-slate-50 border border-transparent hover:border-slate-100 transition-all",
    )


def _products_dropdown() -> rx.Component:
    return rx.el.div(
        # Trigger
        rx.el.a(
            rx.el.span(
                LanguageState.nav_products,
                class_name="text-slate-600 group-hover/products:text-indigo-600 transition-colors font-medium",
            ),
            rx.icon(
                "chevron-down",
                size=14,
                class_name="ml-1 text-slate-400 group-hover/products:text-indigo-600 group-hover/products:rotate-180 transition-all",
            ),
            href="#products",
            class_name="flex items-center text-sm px-3 py-2 cursor-pointer",
        ),
        # Dropdown panel
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "全球地区节点",
                            "Global Regions",
                        ),
                        class_name="text-xs font-semibold text-indigo-600 uppercase tracking-wider",
                    ),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "选择您需要的地区，一键跳转购买",
                            "Choose a region to get started",
                        ),
                        class_name="text-[11px] text-slate-400 mt-0.5",
                    ),
                    class_name="px-3 pb-3 mb-2 border-b border-slate-100",
                ),
                rx.el.div(
                    rx.foreach(ShopState.regions_data, _region_dropdown_item),
                    class_name="grid grid-cols-2 gap-1",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon("layout-grid", size=12, class_name="mr-1.5"),
                        rx.cond(
                            LanguageState.is_zh,
                            "查看全部产品",
                            "View all products",
                        ),
                        rx.icon("arrow-right", size=12, class_name="ml-auto"),
                        href="/shop/server",
                        class_name="mt-3 pt-3 border-t border-slate-100 flex items-center px-3 py-2 rounded-lg text-xs text-indigo-600 hover:text-indigo-700 hover:bg-indigo-50/50 font-medium transition-all",
                    ),
                ),
                class_name="p-3",
            ),
            class_name="invisible opacity-0 translate-y-1 group-hover/products:visible group-hover/products:opacity-100 group-hover/products:translate-y-0 absolute top-full left-1/2 -translate-x-1/2 mt-1 w-[420px] rounded-xl bg-white border border-slate-200/80 shadow-lg transition-all duration-200 z-50",
        ),
        class_name="group/products relative",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-indigo-600"),
                    class_name="w-8 h-8 rounded-lg bg-indigo-50 border border-indigo-100 flex items-center justify-center",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-slate-900 font-bold text-base tracking-tight",
                ),
                href="#hero",
                class_name="flex items-center gap-2",
            ),
            # Navigation links
            rx.el.nav(
                _nav_link_element(LanguageState.nav_home, "#hero"),
                _products_dropdown(),
                _nav_link_element(LanguageState.nav_network, "#nodes"),
                _nav_link_element(LanguageState.nav_pricing, "#pricing"),
                _nav_link_element(LanguageState.nav_trust, "#trust"),
                _nav_link_element(LanguageState.nav_faq, "#faq"),
                class_name="hidden lg:flex items-center gap-1",
                aria_label="Main navigation",
            ),
            # Right actions
            rx.el.div(
                # Language Switch Button (Desktop)
                rx.el.button(
                    rx.icon(
                        "languages",
                        size=16,
                        class_name="text-indigo-600 mr-1.5",
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-slate-600 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 hover:bg-slate-100 hover:border-slate-300 transition-all cursor-pointer",
                    aria_label="Switch language",
                ),
                rx.el.a(
                    rx.el.button(
                        LanguageState.nav_login,
                        class_name="hidden sm:inline-block text-sm text-slate-600 hover:text-indigo-600 px-3 py-1.5 font-medium transition-colors cursor-pointer",
                    ),
                    href="/login",
                ),
                rx.el.a(
                    rx.el.button(
                        LanguageState.nav_signup,
                        class_name="hidden sm:inline-block text-sm bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-xs hover:shadow-md cursor-pointer",
                    ),
                    href="/register",
                ),
                rx.el.button(
                    rx.icon(
                        rx.cond(UIState.mobile_menu_open, "x", "menu"),
                        size=20,
                        class_name="text-slate-700",
                    ),
                    on_click=UIState.toggle_mobile_menu,
                    class_name="lg:hidden p-2 rounded-md hover:bg-slate-100 transition-colors cursor-pointer",
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
                    _mobile_link_element(LanguageState.nav_network, "#nodes"),
                    _mobile_link_element(LanguageState.nav_pricing, "#pricing"),
                    _mobile_link_element(LanguageState.nav_trust, "#trust"),
                    _mobile_link_element(LanguageState.nav_faq, "#faq"),
                    class_name="flex flex-col gap-1 p-4",
                ),
                # Language Switch Button (Mobile)
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            "languages",
                            size=16,
                            class_name="text-indigo-600 mr-2",
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
                        class_name="w-full flex items-center justify-center py-2.5 rounded-lg bg-slate-50 border border-slate-200 text-sm text-slate-600 hover:text-slate-800 transition-all cursor-pointer",
                    ),
                    class_name="px-4 pb-2",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            LanguageState.nav_login,
                            class_name="w-full text-sm text-slate-600 border border-slate-200 hover:bg-slate-50 px-4 py-2.5 rounded-md font-medium transition-colors cursor-pointer",
                        ),
                        href="/login",
                        class_name="flex-1",
                    ),
                    rx.el.a(
                        rx.el.button(
                            LanguageState.nav_signup,
                            class_name="w-full text-sm bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2.5 rounded-md font-medium transition-colors cursor-pointer",
                        ),
                        href="/register",
                        class_name="flex-1",
                    ),
                    class_name="flex items-center gap-2 p-4 border-t border-slate-100",
                ),
                class_name="lg:hidden border-t border-slate-100 bg-white/95 backdrop-blur-xl",
            ),
            rx.fragment(),
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-white/85 border-b border-slate-200/60",
    )
