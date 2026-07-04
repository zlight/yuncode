import reflex as rx
from app.admin.admin_state import AdminState
from app.states.language_state import LanguageState


def _sidebar_btn(
    icon: str, label_zh: str, label_en: str, tab: str
) -> rx.Component:
    is_active = AdminState.current_tab == tab
    label = rx.cond(LanguageState.is_zh, label_zh, label_en)
    return rx.el.button(
        rx.icon(
            icon,
            size=16,
            class_name=rx.cond(
                is_active, "text-cyan-300 shrink-0", "text-slate-400 shrink-0"
            ),
        ),
        rx.el.span(label, class_name="text-sm font-medium truncate"),
        on_click=lambda: AdminState.set_tab(tab),
        class_name=rx.cond(
            is_active,
            "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-100 shadow-lg shadow-cyan-500/5 transition-all cursor-pointer text-left",
            "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 transition-all cursor-pointer text-left",
        ),
    )


def admin_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            # Branding Logo
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-white"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-indigo-500/30",
                ),
                rx.el.div(
                    rx.el.p(
                        "AiarksCloud",
                        class_name="text-white font-bold text-sm leading-none",
                    ),
                    rx.el.p(
                        "Management",
                        class_name="text-[10px] text-cyan-400 font-bold font-mono tracking-wider mt-0.5",
                    ),
                    class_name="flex flex-col",
                ),
                href="/admin",
                class_name="flex items-center gap-3 px-4 h-16 border-b border-white/5 shrink-0",
            ),
            # Nav Group
            rx.el.nav(
                rx.el.div(
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh, "管理核心", "CORE OPERATIONS"
                        ),
                        class_name="px-3 mb-2 text-[10px] uppercase tracking-widest font-bold text-slate-500",
                    ),
                    rx.el.div(
                        _sidebar_btn(
                            "layout-dashboard",
                            "控制台概览 / 运营数据",
                            "Console Overview",
                            "overview",
                        ),
                        _sidebar_btn(
                            "server",
                            "云服务器管理",
                            "Server Management",
                            "servers",
                        ),
                        _sidebar_btn(
                            "users", "用户管理", "User Management", "users"
                        ),
                        _sidebar_btn(
                            "settings",
                            "系统设置",
                            "System Settings",
                            "settings",
                        ),
                        class_name="flex flex-col gap-1",
                    ),
                    class_name="flex flex-col mt-6 px-3",
                ),
                class_name="flex-1 overflow-y-auto",
            ),
            # Back to Public Website
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        rx.icon("home", size=14, class_name="mr-1.5"),
                        rx.cond(
                            LanguageState.is_zh, "返回主页", "Back to Site"
                        ),
                        class_name="w-full flex items-center justify-center px-3 py-2.5 rounded-lg bg-white/5 hover:bg-white/10 text-xs text-slate-300 font-bold transition-all border border-white/5 cursor-pointer",
                    ),
                    href="/",
                ),
                class_name="p-4 border-t border-white/5 shrink-0",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="fixed left-0 top-0 h-screen w-64 bg-slate-950 border-r border-white/5 z-40 hidden lg:flex flex-col",
    )
