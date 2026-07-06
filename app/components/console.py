import reflex as rx
from app.states.session_state import SessionState
from app.states.language_state import LanguageState
from app.states.servers_state import ServersState
from app.states.theme_state import ThemeState
from app.components.manage_tabs import render_manage_tab_content
from app.components.ui_styles import theme_toggle
from app.components.error_banner import error_banner


def _sidebar_item_btn(icon: str, label: rx.Var, view: str) -> rx.Component:
    active = ServersState.console_view == view
    return rx.el.button(
        rx.icon(
            icon,
            size=16,
            class_name=rx.cond(
                active, "text-cyan-300 shrink-0", "text-slate-400 shrink-0"
            ),
        ),
        rx.el.span(label, class_name="text-sm font-medium truncate"),
        on_click=lambda: ServersState.set_view(view),
        class_name=rx.cond(
            active,
            "w-full flex items-center gap-3 px-3 py-2 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-100 shadow-lg shadow-cyan-500/5 transition-all cursor-pointer",
            "w-full flex items-center gap-3 px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 transition-all cursor-pointer",
        ),
    )


def _console_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=16, class_name="text-white"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-indigo-500/30",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-white font-bold text-sm tracking-tight",
                ),
                href="/",
                class_name="flex items-center gap-2 px-4 h-16 border-b border-white/5 shrink-0",
            ),
            rx.el.nav(
                rx.el.div(
                    _sidebar_item_btn(
                        "layout-dashboard",
                        rx.cond(LanguageState.is_zh, "总览", "Overview"),
                        "overview",
                    ),
                    _sidebar_item_btn(
                        "server",
                        rx.cond(
                            LanguageState.is_zh, "云服务器", "Cloud Servers"
                        ),
                        "servers",
                    ),
                    class_name="flex flex-col gap-1 p-3",
                ),
                class_name="flex-1 overflow-y-auto",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        SessionState.avatar_initial,
                        class_name="size-9 rounded-full bg-gradient-to-br from-indigo-500 to-cyan-500 text-white font-bold text-xs flex items-center justify-center shadow-lg shadow-indigo-500/30 shrink-0",
                    ),
                    rx.el.div(
                        rx.el.p(
                            SessionState.auth_username,
                            class_name="text-xs font-bold text-white truncate",
                        ),
                        rx.el.p(
                            SessionState.auth_email,
                            class_name="text-[10px] text-slate-400 truncate",
                        ),
                        class_name="min-w-0 flex-1",
                    ),
                    class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-white/5 border border-white/10 mb-2",
                ),
                rx.el.button(
                    rx.icon("log-out", size=14, class_name="mr-1.5"),
                    rx.cond(LanguageState.is_zh, "退出登录", "Sign Out"),
                    on_click=SessionState.logout_user,
                    class_name="w-full flex items-center justify-center px-3 py-2 rounded-lg bg-white/5 hover:bg-rose-500/10 border border-white/10 hover:border-rose-500/30 text-xs text-slate-300 hover:text-rose-300 font-semibold transition-all cursor-pointer",
                ),
                class_name="p-3 border-t border-white/5 shrink-0",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="fixed left-0 top-0 h-screen w-64 bg-slate-950/80 backdrop-blur-xl border-r border-white/5 z-40 flex flex-col",
    )


def _console_topbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages", size=14, class_name="text-slate-200 mr-1"
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-slate-200 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 transition-all cursor-pointer",
                ),
                theme_toggle(),
                rx.el.a(
                    rx.el.button(
                        rx.icon("plus", size=14, class_name="mr-1"),
                        rx.cond(
                            LanguageState.is_zh, "购买服务器", "Buy Server"
                        ),
                        class_name="flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 text-white text-xs font-bold shadow-lg shadow-orange-500/30 cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                class_name="flex items-center gap-2 ml-auto",
            ),
            class_name="max-w-[1600px] mx-auto px-6 h-16 flex items-center gap-4",
        ),
        class_name="fixed top-0 left-0 lg:left-64 right-0 z-30 backdrop-blur-xl bg-slate-950/70 border-b border-white/5",
    )


def _welcome_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                rx.cond(LanguageState.is_zh, "你好, ", "Hello, "),
                rx.el.span(
                    SessionState.auth_username,
                    class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                ),
                " 👋",
                class_name="text-2xl md:text-3xl font-extrabold text-white tracking-tight mb-1",
            ),
            rx.el.p(
                rx.cond(
                    LanguageState.is_zh,
                    "欢迎回到 AiarksCloud 控制台。",
                    "Welcome back to AiarksCloud console.",
                ),
                class_name="text-sm text-slate-400 font-medium",
            ),
            class_name="flex-1 min-w-0",
        ),
        class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6",
    )


def _instance_card(inst: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(inst["region_flag"], class_name="text-2xl"),
                class_name="w-11 h-11 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.p(
                    inst["name"],
                    class_name="text-sm text-white font-bold font-mono truncate",
                ),
                rx.el.p(
                    inst["ip"] + " · " + inst["region"],
                    class_name="text-xs text-slate-400 font-mono",
                ),
                class_name="min-w-0 flex-1",
            ),
            class_name="flex items-start gap-3 mb-4 pb-4 border-b border-white/5",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("settings", size=12, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "管理", "Manage"),
                on_click=lambda: ServersState.open_manage(inst["id"].to(str)),
                class_name="flex items-center px-3 py-1.5 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-[11px] font-bold cursor-pointer",
            ),
            class_name="flex items-center",
        ),
        class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 transition-all",
    )


def _no_servers_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("server-off", size=32, class_name="text-cyan-300"),
            class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            rx.cond(
                LanguageState.is_zh, "尚未购买任何服务器", "No servers yet"
            ),
            class_name="text-white font-bold text-lg mb-1 text-center",
        ),
        rx.el.p(
            rx.cond(
                LanguageState.is_zh,
                "购买您的第一台云服务器,60 秒内即可开通。",
                "Purchase your first cloud server — provisioned in 60 seconds.",
            ),
            class_name="text-sm text-slate-400 mb-5 text-center max-w-md mx-auto font-medium",
        ),
        rx.el.a(
            rx.el.button(
                rx.icon("plus", size=14, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "购买服务器", "Buy Server"),
                class_name="inline-flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 text-white text-xs font-bold shadow-lg shadow-orange-500/30 cursor-pointer",
            ),
            href="/shop/server",
            class_name="flex justify-center",
        ),
        class_name="rounded-2xl bg-slate-900/40 backdrop-blur-xl border border-dashed border-white/10 px-6 py-16",
    )


def _servers_error_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("circle_alert", size=28, class_name="text-rose-300"),
            class_name="w-14 h-14 rounded-2xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            rx.cond(
                LanguageState.is_zh,
                "无法加载服务器列表",
                "Failed to load servers",
            ),
            class_name="text-white font-bold text-base mb-1 text-center",
        ),
        rx.el.p(
            rx.cond(
                LanguageState.is_zh,
                ServersState.error_message_zh,
                ServersState.error_message_en,
            ),
            class_name="text-sm text-slate-400 mb-4 font-medium text-center max-w-md mx-auto",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("refresh-cw", size=12, class_name="mr-1.5"),
                rx.cond(LanguageState.is_zh, "重新加载", "Retry"),
                on_click=ServersState.load_console,
                class_name="inline-flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 text-white text-xs font-bold shadow-lg shadow-indigo-500/20 cursor-pointer",
            ),
            rx.el.button(
                rx.icon("x", size=12, class_name="mr-1.5"),
                rx.cond(LanguageState.is_zh, "忽略", "Dismiss"),
                on_click=ServersState.clear_error,
                class_name="ml-2 inline-flex items-center px-4 py-2 rounded-lg bg-white/5 border border-white/10 text-slate-200 text-xs font-bold hover:border-rose-500/40 cursor-pointer",
            ),
            class_name="flex items-center justify-center",
        ),
        class_name="rounded-2xl bg-slate-900/40 backdrop-blur-xl border border-rose-500/20 px-6 py-16",
    )


def _action_error_banner() -> rx.Component:
    """Persistent rose-toned banner for console-level action errors."""
    return rx.cond(
        ServersState.has_action_error,
        rx.el.div(
            error_banner(
                message_en=ServersState.action_error_en,
                message_zh=ServersState.action_error_zh,
                on_dismiss=ServersState.clear_action_error,
                on_retry=ServersState.load_console,
                retry_label_en="Refresh",
                retry_label_zh="刷新",
            ),
            class_name="mb-4",
        ),
        rx.fragment(),
    )


def _servers_list_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    rx.cond(LanguageState.is_zh, "云服务器", "Cloud Servers"),
                    class_name="text-2xl font-extrabold text-white tracking-tight",
                ),
                rx.el.p(
                    rx.cond(
                        LanguageState.is_zh,
                        "管理和监控您的所有云服务器实例",
                        "Manage and monitor all your cloud server instances",
                    ),
                    class_name="text-sm text-slate-400 font-medium mt-1",
                ),
                class_name="flex-1 min-w-0",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "refresh-cw",
                        size=13,
                        class_name=rx.cond(
                            ServersState.is_busy,
                            "mr-1.5 animate-spin text-cyan-300",
                            "mr-1.5",
                        ),
                    ),
                    rx.cond(LanguageState.is_zh, "刷新", "Refresh"),
                    on_click=ServersState.load_console,
                    disabled=ServersState.is_busy,
                    class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 text-slate-200 text-xs font-semibold cursor-pointer",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("plus", size=14, class_name="mr-1"),
                        rx.cond(
                            LanguageState.is_zh, "购买服务器", "Buy Server"
                        ),
                        class_name="flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 text-white text-xs font-bold shadow-lg cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-start gap-4 mb-6",
        ),
        _action_error_banner(),
        rx.match(
            ServersState.list_status,
            (
                "loading",
                rx.el.div(
                    rx.el.p(
                        rx.cond(LanguageState.is_zh, "加载中...", "Loading..."),
                        class_name="text-sm text-slate-400 text-center py-16",
                    ),
                ),
            ),
            ("error", _servers_error_state()),
            ("empty", _no_servers_state()),
            rx.el.div(
                rx.foreach(ServersState.filtered_instances, _instance_card),
                class_name="flex flex-col gap-4",
            ),
        ),
    )


def _server_manage_view() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.el.div(
        rx.el.button(
            rx.icon("arrow-left", size=14, class_name="mr-1.5"),
            rx.cond(LanguageState.is_zh, "返回列表", "Back to list"),
            on_click=ServersState.back_to_list,
            class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 text-xs font-semibold cursor-pointer mb-4 w-fit",
        ),
        _action_error_banner(),
        rx.cond(
            ServersState.has_instances,
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        inst["name"],
                        class_name="text-xl text-white font-extrabold font-mono",
                    ),
                    rx.el.p(
                        inst["ip"] + " · " + inst["region"],
                        class_name="text-xs text-slate-400 font-mono mt-1",
                    ),
                    class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 mb-4",
                ),
                render_manage_tab_content(),
            ),
            _no_servers_state(),
        ),
    )


def _overview_content() -> rx.Component:
    return rx.fragment(_welcome_card(), _action_error_banner())


def _login_prompt() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("lock", size=32, class_name="text-cyan-300"),
                class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-5",
            ),
            rx.el.h1(
                rx.cond(
                    LanguageState.is_zh,
                    "请先登录以访问控制台",
                    "Log in to access the console",
                ),
                class_name="text-2xl font-extrabold text-white text-center tracking-tight mb-2",
            ),
            rx.el.p(
                rx.cond(
                    LanguageState.is_zh,
                    "登录后即可查看您的服务器、订单、账单与实时监控数据。",
                    "Sign in to view your servers, orders, billing and real-time monitoring data.",
                ),
                class_name="text-sm text-slate-400 font-medium text-center mb-6 max-w-sm mx-auto",
            ),
            rx.cond(
                ServersState.has_action_error,
                rx.el.div(
                    error_banner(
                        message_en=ServersState.action_error_en,
                        message_zh=ServersState.action_error_zh,
                        on_dismiss=ServersState.clear_action_error,
                    ),
                    class_name="mb-4",
                ),
                rx.fragment(),
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        rx.cond(LanguageState.is_zh, "登录", "Log In"),
                        class_name="flex items-center px-5 py-2.5 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 text-white text-sm font-bold shadow-xl shadow-indigo-500/30 cursor-pointer",
                    ),
                    href="/login",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.cond(LanguageState.is_zh, "免费注册", "Sign up"),
                        class_name="px-5 py-2.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-100 text-sm font-bold cursor-pointer",
                    ),
                    href="/register",
                ),
                class_name="flex items-center justify-center gap-3",
            ),
            class_name="w-full max-w-md rounded-2xl bg-slate-900/70 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/50 p-8",
        ),
        class_name="flex items-center justify-center min-h-[calc(100vh-6rem)] px-6",
    )


def console_page() -> rx.Component:
    return rx.el.main(
        rx.cond(
            SessionState.is_logged_in,
            rx.fragment(
                _console_sidebar(),
                _console_topbar(),
                rx.el.div(
                    rx.match(
                        ServersState.console_view,
                        ("servers", _servers_list_view()),
                        ("manage", _server_manage_view()),
                        _overview_content(),
                    ),
                    class_name="lg:ml-64 pt-24 pb-12 px-6 max-w-[1600px] mx-auto relative z-10",
                ),
            ),
            rx.el.div(_login_prompt(), class_name="pt-24 relative z-10"),
        ),
        class_name="font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
    )
