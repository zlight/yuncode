import reflex as rx
from app.states.ui_state import UIState
from app.states.language_state import LanguageState
from app.states.shop_state import ShopState
from app.states.session_state import SessionState
from app.states.theme_state import ThemeState
from app.components.ui_styles import theme_toggle, theme_navbar_class


def _nav_link(label: rx.Var, href: str) -> rx.Component:
    return rx.el.a(
        rx.el.span(
            label,
            class_name="text-slate-300 hover:text-white transition-colors font-medium",
        ),
        href=href,
        class_name="flex items-center text-sm px-3 py-2",
    )


def _mobile_link(label: rx.Var, href: str) -> rx.Component:
    return rx.el.a(
        rx.el.span(label, class_name="text-slate-200 font-medium text-base"),
        rx.icon("chevron-right", size=16, class_name="ml-auto text-slate-500"),
        href=href,
        on_click=UIState.close_mobile_menu,
        class_name="flex items-center px-4 py-3 rounded-lg hover:bg-white/5 border border-transparent hover:border-white/10 transition-colors",
    )


def _region_dropdown_item(region: rx.Var) -> rx.Component:
    name = rx.cond(LanguageState.is_zh, region["name_zh"], region["name_en"])
    return rx.el.a(
        rx.el.span(region["flag"], class_name="text-lg"),
        rx.el.div(
            rx.el.p(name, class_name="text-sm text-slate-100 font-medium"),
            rx.el.p(
                region["id"].to(str).upper() + "BGP",
                class_name="text-[10px] text-slate-500 tracking-wider",
            ),
            class_name="flex flex-col",
        ),
        rx.icon(
            "arrow-up-right",
            size=12,
            class_name="ml-auto text-slate-600 group-hover/item:text-cyan-300 transition-colors",
        ),
        href=f"/shop/server?region={region['id']}",
        class_name="group/item flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-white/5 border border-transparent hover:border-white/10 transition-all",
    )


def _products_dropdown() -> rx.Component:
    return rx.el.div(
        rx.el.a(
            rx.el.span(
                LanguageState.nav_products,
                class_name="text-slate-300 group-hover/products:text-white transition-colors font-medium",
            ),
            rx.icon(
                "chevron-down",
                size=14,
                class_name="ml-1 text-slate-500 group-hover/products:text-cyan-300 group-hover/products:rotate-180 transition-all",
            ),
            href="#products",
            class_name="flex items-center text-sm px-3 py-2 cursor-pointer",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "全球地区节点",
                            "Global Regions",
                        ),
                        class_name="text-xs font-bold text-cyan-300 uppercase tracking-wider",
                    ),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "选择您需要的地区，一键跳转购买",
                            "Choose a region to get started",
                        ),
                        class_name="text-[11px] text-slate-500 mt-0.5",
                    ),
                    class_name="px-3 pb-3 mb-2 border-b border-white/10",
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
                        class_name="mt-3 pt-3 border-t border-white/10 flex items-center px-3 py-2 rounded-lg text-xs text-cyan-300 hover:text-cyan-200 hover:bg-cyan-500/5 font-semibold transition-all",
                    ),
                ),
                class_name="p-3",
            ),
            class_name="invisible opacity-0 translate-y-1 group-hover/products:visible group-hover/products:opacity-100 group-hover/products:translate-y-0 absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[440px] rounded-2xl bg-slate-950/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-indigo-950/50 transition-all duration-200 z-50",
        ),
        class_name="group/products relative",
    )


def _avatar_menu() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            SessionState.avatar_initial,
            class_name="size-8 rounded-full bg-gradient-to-br from-indigo-500 to-cyan-500 text-white font-bold text-xs flex items-center justify-center border border-white/20 hover:brightness-110 transition-all shadow-lg shadow-indigo-500/30 cursor-pointer",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    SessionState.auth_username,
                    class_name="text-sm font-bold text-white",
                ),
                rx.el.p(
                    SessionState.auth_email,
                    class_name="text-xs text-slate-400 truncate",
                ),
                rx.cond(
                    SessionState.is_vip,
                    rx.el.span(
                        rx.icon("crown", size=10, class_name="mr-1"),
                        rx.cond(LanguageState.is_zh, "VIP 会员", "VIP Member"),
                        class_name="mt-2 inline-flex items-center text-[10px] font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded-md border border-amber-500/30 w-fit",
                    ),
                    rx.el.span(
                        rx.icon("user", size=10, class_name="mr-1"),
                        rx.cond(LanguageState.is_zh, "普通用户", "Free User"),
                        class_name="mt-2 inline-flex items-center text-[10px] font-bold text-slate-400 bg-white/5 px-2 py-0.5 rounded-md border border-white/10 w-fit",
                    ),
                ),
                class_name="px-4 py-3 border-b border-white/10 flex flex-col",
            ),
            rx.el.a(
                rx.cond(LanguageState.is_zh, "控制台", "Console"),
                href="/console",
                class_name="w-full text-left block text-sm text-slate-200 hover:bg-white/5 hover:text-cyan-300 px-4 py-2.5 transition-colors cursor-pointer",
            ),
            rx.el.button(
                rx.cond(LanguageState.is_zh, "退出登录", "Sign Out"),
                on_click=SessionState.logout_user,
                class_name="w-full text-left text-sm text-rose-400 hover:bg-rose-500/10 px-4 py-2.5 transition-colors cursor-pointer",
            ),
            class_name="invisible opacity-0 translate-y-1 group-hover/avatar:visible group-hover/avatar:opacity-100 group-hover/avatar:translate-y-0 absolute right-0 mt-2 w-56 rounded-xl bg-slate-950/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/50 transition-all duration-200 z-50 overflow-hidden",
        ),
        class_name="group/avatar relative",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-white"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-indigo-500/30",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-white font-bold text-base tracking-tight",
                ),
                href="#hero",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                _nav_link(LanguageState.nav_home, "#hero"),
                _products_dropdown(),
                _nav_link(LanguageState.nav_network, "#nodes"),
                _nav_link(LanguageState.nav_pricing, "#pricing"),
                _nav_link(LanguageState.nav_trust, "#trust"),
                _nav_link(LanguageState.nav_faq, "#faq"),
                class_name="hidden lg:flex items-center gap-1",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages",
                        size=16,
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-slate-200 mr-1.5",
                            "text-neutral-800 mr-1.5",
                        ),
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name=rx.cond(
                            ThemeState.is_dark,
                            "text-xs text-slate-200 font-semibold",
                            "text-xs text-neutral-800 font-semibold",
                        ),
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name=rx.cond(
                        ThemeState.is_dark,
                        "flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
                        "flex items-center px-3 py-1.5 rounded-lg bg-neutral-100 border border-neutral-200 hover:bg-neutral-200 transition-all cursor-pointer",
                    ),
                ),
                theme_toggle(),
                rx.cond(
                    SessionState.is_logged_in,
                    rx.fragment(
                        rx.el.a(
                            rx.el.button(
                                rx.cond(
                                    LanguageState.is_zh, "控制台", "Console"
                                ),
                                class_name="text-sm bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white px-4 py-1.5 rounded-md font-semibold transition-all shadow-lg shadow-indigo-500/25 cursor-pointer",
                            ),
                            href="/console",
                        ),
                        rx.cond(
                            SessionState.is_vip,
                            rx.el.span(
                                rx.icon("crown", size=12, class_name="mr-1"),
                                "VIP",
                                class_name="hidden sm:inline-flex items-center text-[10px] font-bold text-amber-300 bg-amber-500/10 px-2 py-1 rounded-md border border-amber-500/30",
                            ),
                            rx.fragment(),
                        ),
                        _avatar_menu(),
                    ),
                    rx.fragment(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_login,
                                class_name="hidden sm:inline-block text-sm text-slate-300 hover:text-white px-3 py-1.5 font-medium transition-colors cursor-pointer",
                            ),
                            href="/login",
                        ),
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_signup,
                                class_name="hidden sm:inline-block text-sm bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white px-4 py-1.5 rounded-md font-semibold transition-all shadow-lg shadow-indigo-500/25 cursor-pointer",
                            ),
                            href="/register",
                        ),
                    ),
                ),
                rx.el.button(
                    rx.icon(
                        rx.cond(UIState.mobile_menu_open, "x", "menu"),
                        size=20,
                        class_name="text-slate-200",
                    ),
                    on_click=UIState.toggle_mobile_menu,
                    class_name="lg:hidden p-2 rounded-md hover:bg-white/5 transition-colors cursor-pointer",
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
        ),
        rx.cond(
            UIState.mobile_menu_open,
            rx.el.div(
                rx.el.div(
                    _mobile_link(LanguageState.nav_home, "#hero"),
                    _mobile_link(LanguageState.nav_products, "#products"),
                    _mobile_link(LanguageState.nav_network, "#nodes"),
                    _mobile_link(LanguageState.nav_pricing, "#pricing"),
                    _mobile_link(LanguageState.nav_trust, "#trust"),
                    _mobile_link(LanguageState.nav_faq, "#faq"),
                    class_name="flex flex-col gap-1 p-4",
                ),
                rx.cond(
                    SessionState.is_logged_in,
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                rx.cond(
                                    LanguageState.is_zh, "控制台", "Console"
                                ),
                                class_name="w-full text-center text-sm bg-gradient-to-r from-indigo-500 to-cyan-500 text-white py-2.5 rounded-md font-semibold cursor-pointer",
                            ),
                            href="/console",
                            on_click=UIState.close_mobile_menu,
                        ),
                        rx.el.button(
                            rx.cond(
                                LanguageState.is_zh, "退出登录", "Sign Out"
                            ),
                            on_click=[
                                SessionState.logout_user,
                                UIState.close_mobile_menu,
                            ],
                            class_name="w-full text-center text-sm text-rose-400 hover:bg-rose-500/10 py-2.5 rounded-md font-semibold border border-rose-500/30 mt-2 cursor-pointer",
                        ),
                        class_name="p-4 border-t border-white/10 flex flex-col",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_login,
                                class_name="w-full text-sm text-slate-200 border border-white/10 hover:bg-white/5 px-4 py-2.5 rounded-md font-medium cursor-pointer",
                            ),
                            href="/login",
                            on_click=UIState.close_mobile_menu,
                            class_name="flex-1",
                        ),
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_signup,
                                class_name="w-full text-sm bg-gradient-to-r from-indigo-500 to-cyan-500 text-white px-4 py-2.5 rounded-md font-semibold cursor-pointer",
                            ),
                            href="/register",
                            on_click=UIState.close_mobile_menu,
                            class_name="flex-1",
                        ),
                        class_name="flex items-center gap-2 p-4 border-t border-white/10",
                    ),
                ),
                class_name="lg:hidden border-t border-white/10 bg-slate-950/95 backdrop-blur-xl",
            ),
            rx.fragment(),
        ),
        class_name=theme_navbar_class(),
    )
