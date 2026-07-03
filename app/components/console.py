import reflex as rx
from app.states.session_state import SessionState
from app.states.language_state import LanguageState
from app.states.servers_state import ServersState
from app.components.manage_tabs import render_manage_tab_content


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


def _sidebar_item(
    icon: str, label: rx.Var, active: bool = False, href: str = "#"
) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon,
            size=16,
            class_name=rx.cond(
                active, "text-cyan-300 shrink-0", "text-slate-400 shrink-0"
            ),
        ),
        rx.el.span(label, class_name="text-sm font-medium truncate"),
        href=href,
        class_name=rx.cond(
            active,
            "flex items-center gap-3 px-3 py-2 rounded-lg bg-cyan-500/10 border border-cyan-500/30 text-cyan-100 shadow-lg shadow-cyan-500/5 transition-all",
            "flex items-center gap-3 px-3 py-2 rounded-lg text-slate-300 hover:text-white hover:bg-white/5 border border-transparent hover:border-white/10 transition-all",
        ),
    )


def _sidebar_group(title: rx.Var, children: list[rx.Component]) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            title,
            class_name="px-3 mb-2 text-[10px] uppercase tracking-widest font-bold text-slate-500",
        ),
        rx.el.div(*children, class_name="flex flex-col gap-0.5"),
        class_name="flex flex-col mb-5",
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
                _sidebar_group(
                    rx.cond(LanguageState.is_zh, "仪表盘", "Dashboard"),
                    [
                        _sidebar_item_btn(
                            "layout-dashboard",
                            rx.cond(LanguageState.is_zh, "总览", "Overview"),
                            "overview",
                        ),
                        _sidebar_item(
                            "activity",
                            rx.cond(LanguageState.is_zh, "监控", "Monitoring"),
                        ),
                        _sidebar_item(
                            "bell",
                            rx.cond(
                                LanguageState.is_zh, "通知", "Notifications"
                            ),
                        ),
                    ],
                ),
                _sidebar_group(
                    rx.cond(LanguageState.is_zh, "产品", "Products"),
                    [
                        _sidebar_item_btn(
                            "server",
                            rx.cond(
                                LanguageState.is_zh, "云服务器", "Cloud Servers"
                            ),
                            "servers",
                        ),
                        _sidebar_item(
                            "zap",
                            rx.cond(
                                LanguageState.is_zh, "轻量云", "Light Servers"
                            ),
                        ),
                        _sidebar_item(
                            "hard-drive",
                            rx.cond(
                                LanguageState.is_zh, "物理服务器", "Dedicated"
                            ),
                        ),
                        _sidebar_item(
                            "shield",
                            rx.cond(LanguageState.is_zh, "云高防", "Anti-DDoS"),
                        ),
                        _sidebar_item(
                            "radio-tower",
                            rx.cond(
                                LanguageState.is_zh, "流媒体解锁", "Streaming"
                            ),
                        ),
                    ],
                ),
                _sidebar_group(
                    rx.cond(LanguageState.is_zh, "账户", "Account"),
                    [
                        _sidebar_item(
                            "wallet",
                            rx.cond(LanguageState.is_zh, "余额", "Balance"),
                        ),
                        _sidebar_item(
                            "receipt",
                            rx.cond(LanguageState.is_zh, "订单", "Orders"),
                        ),
                        _sidebar_item(
                            "credit-card",
                            rx.cond(LanguageState.is_zh, "账单", "Billing"),
                        ),
                        _sidebar_item(
                            "user",
                            rx.cond(LanguageState.is_zh, "个人资料", "Profile"),
                        ),
                        _sidebar_item(
                            "settings",
                            rx.cond(LanguageState.is_zh, "设置", "Settings"),
                        ),
                    ],
                ),
                _sidebar_group(
                    rx.cond(LanguageState.is_zh, "支持", "Support"),
                    [
                        _sidebar_item(
                            "life-buoy",
                            rx.cond(LanguageState.is_zh, "工单", "Tickets"),
                        ),
                        _sidebar_item(
                            "book-open",
                            rx.cond(LanguageState.is_zh, "文档", "Docs"),
                        ),
                        _sidebar_item(
                            "message-circle",
                            rx.cond(LanguageState.is_zh, "在线客服", "Chat"),
                        ),
                    ],
                ),
                class_name="flex-1 overflow-y-auto px-3 py-5",
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
                    rx.cond(
                        SessionState.is_vip,
                        rx.el.span(
                            rx.icon(
                                "crown", size=10, class_name="text-amber-300"
                            ),
                            class_name="w-6 h-6 rounded-md bg-gradient-to-br from-amber-400/20 to-rose-400/20 border border-amber-400/40 flex items-center justify-center shrink-0",
                        ),
                        rx.fragment(),
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
                rx.icon(
                    "search",
                    size=14,
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                ),
                rx.el.input(
                    placeholder=rx.cond(
                        LanguageState.is_zh,
                        "搜索服务器、订单、工单...",
                        "Search servers, orders, tickets...",
                    ),
                    class_name="w-72 pl-9 pr-4 py-2 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-xs",
                ),
                class_name="relative hidden md:block",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages", size=14, class_name="text-cyan-300 mr-1"
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-slate-200 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("plus", size=14, class_name="mr-1"),
                        rx.cond(
                            LanguageState.is_zh, "购买服务器", "Buy Server"
                        ),
                        class_name="flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-orange-500/30 transition-all cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                rx.el.button(
                    rx.icon("bell", size=16, class_name="text-slate-300"),
                    rx.el.span(
                        class_name="absolute top-1.5 right-1.5 w-1.5 h-1.5 rounded-full bg-rose-400 shadow-lg shadow-rose-400/50"
                    ),
                    class_name="relative w-9 h-9 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 flex items-center justify-center transition-all cursor-pointer",
                ),
                rx.cond(
                    SessionState.is_vip,
                    rx.el.span(
                        rx.icon("crown", size=10, class_name="mr-1"),
                        "VIP",
                        class_name="hidden sm:inline-flex items-center text-[10px] font-bold text-amber-200 bg-gradient-to-r from-amber-400/20 to-rose-400/20 px-2 py-1.5 rounded-lg border border-amber-400/40",
                    ),
                    rx.fragment(),
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
            class_name="absolute inset-0 rounded-2xl bg-gradient-to-r from-indigo-600/30 via-cyan-500/20 to-transparent -z-10 blur-2xl"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2 shadow-lg shadow-emerald-400/50 animate-pulse"
                ),
                rx.el.span(
                    rx.cond(
                        LanguageState.is_zh,
                        "所有系统运行正常",
                        "All systems operational",
                    ),
                    class_name="text-[10px] text-slate-200 font-bold uppercase tracking-wider",
                ),
                class_name="inline-flex items-center px-2.5 py-1 rounded-full bg-white/5 border border-white/10 mb-3",
            ),
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
                    "欢迎回到 AiarksCloud 控制台。以下是您的账户概览。",
                    "Welcome back to AiarksCloud console.",
                ),
                class_name="text-sm text-slate-400 font-medium",
            ),
            class_name="relative flex-1 min-w-0",
        ),
        class_name="relative flex items-start gap-4 rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 overflow-hidden",
    )


def _account_stat(
    icon: str, label: rx.Var, value: str, sub: rx.Var, accent: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, size=14, class_name=f"text-{accent}-300"),
                class_name=f"w-9 h-9 rounded-lg bg-{accent}-500/10 border border-{accent}-500/30 flex items-center justify-center shrink-0",
            ),
            rx.el.p(
                label,
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold ml-auto",
            ),
            class_name="flex items-center mb-3",
        ),
        rx.el.p(
            value,
            class_name="text-2xl text-white font-extrabold tracking-tight leading-none mb-1",
        ),
        rx.el.p(sub, class_name="text-[11px] text-slate-400 font-medium"),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-4 hover:border-white/15 transition-all",
    )


def _instance_card(inst: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(inst["region_flag"], class_name="text-2xl"),
                class_name="w-11 h-11 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        inst["name"],
                        class_name="text-sm text-white font-bold font-mono truncate",
                    ),
                    rx.el.span(
                        rx.el.span(
                            class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                        ),
                        rx.cond(LanguageState.is_zh, "运行中", "Running"),
                        class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/30 shrink-0",
                    ),
                    class_name="flex items-center gap-2 mb-1",
                ),
                rx.el.div(
                    rx.icon(
                        "globe", size=11, class_name="text-cyan-300 shrink-0"
                    ),
                    rx.el.span(
                        inst["ip"],
                        class_name="text-xs text-slate-300 font-mono ml-1",
                    ),
                    rx.el.span("·", class_name="text-slate-600 mx-2"),
                    rx.el.span(
                        inst["region"],
                        class_name="text-xs text-slate-400 font-medium",
                    ),
                    class_name="flex items-center flex-wrap",
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
                class_name="flex items-center px-3 py-1.5 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-[11px] font-bold shadow-lg shadow-indigo-500/25 transition-all cursor-pointer",
            ),
            rx.el.button(
                rx.icon("refresh-cw", size=12, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "续费", "Renew"),
                class_name="ml-2 flex items-center px-3 py-1.5 rounded-md bg-orange-500/10 hover:bg-orange-500/20 border border-orange-500/40 text-orange-300 text-[11px] font-bold transition-all cursor-pointer",
            ),
            class_name="flex items-center",
        ),
        class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 hover:shadow-xl hover:shadow-cyan-500/5 transition-all",
    )


def _region_option(node: rx.Var) -> rx.Component:
    return rx.el.option(node, value=node)


def _no_servers_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("server-off", size=32, class_name="text-cyan-300"),
            class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            rx.cond(
                LanguageState.is_zh,
                "尚未购买任何服务器",
                "No servers yet",
            ),
            class_name="text-white font-bold text-lg mb-1 text-center",
        ),
        rx.el.p(
            rx.cond(
                LanguageState.is_zh,
                "购买您的第一台云服务器,60 秒内即可开通并出现在此列表。",
                "Purchase your first cloud server — provisioned in under 60 seconds and shown here.",
            ),
            class_name="text-sm text-slate-400 mb-5 text-center max-w-md mx-auto font-medium",
        ),
        rx.el.a(
            rx.el.button(
                rx.icon("plus", size=14, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "购买服务器", "Buy Server"),
                class_name="inline-flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-orange-500/30 transition-all cursor-pointer",
            ),
            href="/shop/server",
            class_name="flex justify-center",
        ),
        class_name="rounded-2xl bg-slate-900/40 backdrop-blur-xl border border-dashed border-white/10 px-6 py-16",
    )


def _no_match_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search-x", size=28, class_name="text-slate-500"),
            class_name="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mx-auto mb-3",
        ),
        rx.el.h3(
            rx.cond(
                LanguageState.is_zh, "没有匹配的服务器", "No matching servers"
            ),
            class_name="text-white font-bold text-base text-center mb-1",
        ),
        rx.el.p(
            rx.cond(
                LanguageState.is_zh,
                "请调整搜索关键词或地区筛选。",
                "Try adjusting your search or region filter.",
            ),
            class_name="text-sm text-slate-400 text-center font-medium",
        ),
        class_name="rounded-2xl bg-slate-900/40 backdrop-blur-xl border border-dashed border-white/10 px-6 py-12",
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
                    rx.icon("refresh-cw", size=13, class_name="mr-1.5"),
                    rx.cond(LanguageState.is_zh, "刷新", "Refresh"),
                    on_click=ServersState.load_console,
                    class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 text-slate-200 text-xs font-semibold transition-all cursor-pointer",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("plus", size=14, class_name="mr-1"),
                        rx.cond(
                            LanguageState.is_zh, "购买服务器", "Buy Server"
                        ),
                        class_name="flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-orange-500/30 transition-all cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-start gap-4 mb-6",
        ),
        rx.cond(
            ServersState.has_instances,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "search",
                            size=14,
                            class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                        ),
                        rx.el.input(
                            placeholder=rx.cond(
                                LanguageState.is_zh,
                                "搜索名称、IP、地区...",
                                "Search name, IP, region...",
                            ),
                            default_value=ServersState.search_query,
                            on_change=ServersState.set_search_query.debounce(
                                300
                            ),
                            class_name="w-72 pl-9 pr-4 py-2 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-xs",
                        ),
                        class_name="relative",
                    ),
                    rx.el.div(
                        rx.el.select(
                            rx.el.option(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "全部地区",
                                    "All Regions",
                                ),
                                value="all",
                            ),
                            rx.foreach(
                                ServersState.region_options, _region_option
                            ),
                            default_value=ServersState.filter_region,
                            key=ServersState.filter_region,
                            on_change=ServersState.set_filter_region,
                            class_name="appearance-none pl-3 pr-9 py-2 bg-slate-900/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-xs cursor-pointer font-semibold",
                        ),
                        rx.icon(
                            "chevron-down",
                            size=12,
                            class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                        ),
                        class_name="relative",
                    ),
                    class_name="flex items-center gap-3 mb-5",
                ),
                rx.cond(
                    ServersState.filtered_instances.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            ServersState.filtered_instances, _instance_card
                        ),
                        class_name="flex flex-col gap-4",
                    ),
                    _no_match_state(),
                ),
            ),
            _no_servers_state(),
        ),
    )


def _manage_sidebar_item(inst: rx.Var) -> rx.Component:
    is_selected = ServersState.selected_instance_id == inst["id"]
    return rx.el.button(
        rx.el.div(
            rx.el.span(inst["region_flag"], class_name="text-lg shrink-0"),
            rx.el.div(
                rx.el.p(
                    inst["name"],
                    class_name="text-[11px] text-white font-bold font-mono truncate",
                ),
                rx.el.p(
                    inst["ip"],
                    class_name="text-[10px] text-slate-500 font-mono",
                ),
                class_name="min-w-0 flex-1",
            ),
            rx.el.span(
                class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0 shadow-lg shadow-emerald-400/50 animate-pulse"
            ),
            class_name="flex items-center gap-2",
        ),
        on_click=lambda: ServersState.select_instance(inst["id"].to(str)),
        class_name=rx.cond(
            is_selected,
            "w-full text-left px-3 py-2.5 rounded-lg bg-cyan-500/10 border border-cyan-500/40 shadow-lg shadow-cyan-500/5 transition-all cursor-pointer",
            "w-full text-left px-3 py-2.5 rounded-lg bg-white/[0.02] border border-transparent hover:border-white/10 hover:bg-white/5 transition-all cursor-pointer",
        ),
    )


def _manage_tab_btn(icon: str, label: rx.Var, tab: str) -> rx.Component:
    active = ServersState.manage_tab == tab
    return rx.el.button(
        rx.icon(
            icon,
            size=14,
            class_name=rx.cond(active, "text-cyan-300", "text-slate-400"),
        ),
        rx.el.span(label, class_name="text-xs font-semibold ml-1.5"),
        on_click=lambda: ServersState.set_manage_tab(tab),
        class_name=rx.cond(
            active,
            "flex items-center px-3 py-2.5 border-b-2 border-cyan-400 text-cyan-200 transition-all cursor-pointer",
            "flex items-center px-3 py-2.5 border-b-2 border-transparent text-slate-400 hover:text-slate-200 hover:border-white/20 transition-all cursor-pointer",
        ),
    )


def _action_btn(
    icon: str, label: rx.Var, variant: str = "default"
) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=13, class_name="mr-1.5"),
        rx.el.span(label, class_name="text-xs font-bold"),
        class_name=rx.match(
            variant,
            (
                "danger",
                "flex items-center px-3.5 py-2 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/40 text-rose-300 transition-all cursor-pointer",
            ),
            (
                "warning",
                "flex items-center px-3.5 py-2 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/40 text-amber-300 transition-all cursor-pointer",
            ),
            (
                "primary",
                "flex items-center px-3.5 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white shadow-lg shadow-indigo-500/25 transition-all cursor-pointer",
            ),
            (
                "orange",
                "flex items-center px-3.5 py-2 rounded-lg bg-orange-500/10 hover:bg-orange-500/20 border border-orange-500/40 text-orange-300 transition-all cursor-pointer",
            ),
            "flex items-center px-3.5 py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 transition-all cursor-pointer",
        ),
    )


def _server_manage_view() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.cond(
        ServersState.has_instances,
        _server_manage_view_body(inst),
        _no_servers_state(),
    )


def _server_manage_view_body(inst) -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("arrow-left", size=14, class_name="mr-1.5"),
            rx.cond(LanguageState.is_zh, "返回列表", "Back to list"),
            on_click=ServersState.back_to_list,
            class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 text-xs font-semibold transition-all cursor-pointer mb-4 w-fit",
        ),
        rx.el.div(
            rx.el.aside(
                rx.el.div(
                    rx.el.div(
                        rx.icon("server", size=13, class_name="text-cyan-300"),
                        rx.el.span(
                            rx.cond(
                                LanguageState.is_zh, "实例列表", "Instances"
                            ),
                            class_name="text-xs text-white font-bold ml-1.5",
                        ),
                        rx.el.span(
                            ServersState.instances.length().to_string(),
                            class_name="ml-auto text-[10px] font-bold text-cyan-300 bg-cyan-500/10 px-1.5 py-0.5 rounded border border-cyan-500/30",
                        ),
                        class_name="flex items-center px-3 py-3 border-b border-white/5",
                    ),
                    rx.el.div(
                        rx.foreach(
                            ServersState.instances, _manage_sidebar_item
                        ),
                        class_name="flex flex-col gap-1 p-2",
                    ),
                    class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden",
                ),
                class_name="w-64 shrink-0 hidden lg:block",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                inst["region_flag"], class_name="text-3xl"
                            ),
                            class_name="w-14 h-14 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h2(
                                    inst["name"],
                                    class_name="text-xl text-white font-extrabold font-mono tracking-tight",
                                ),
                                rx.el.span(
                                    rx.el.span(
                                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                                    ),
                                    rx.cond(
                                        LanguageState.is_zh, "运行中", "Running"
                                    ),
                                    class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-1 rounded-full border border-emerald-500/30 shrink-0",
                                ),
                                class_name="flex items-center gap-3 flex-wrap mb-2",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    inst["region"],
                                    class_name="text-xs text-slate-300 font-medium",
                                ),
                                rx.el.span(
                                    "·", class_name="text-slate-600 mx-2"
                                ),
                                rx.el.span(
                                    inst["node"],
                                    class_name="text-[10px] text-cyan-300 font-bold px-1.5 py-0.5 rounded bg-cyan-500/10 border border-cyan-500/30",
                                ),
                                rx.el.span(
                                    "·", class_name="text-slate-600 mx-2"
                                ),
                                rx.el.span(
                                    inst["plan"],
                                    class_name="text-xs text-slate-300 font-semibold",
                                ),
                                rx.el.span(
                                    "·", class_name="text-slate-600 mx-2"
                                ),
                                rx.el.span(
                                    inst["ip"],
                                    class_name="text-xs text-cyan-300 font-mono",
                                ),
                                class_name="flex items-center flex-wrap",
                            ),
                            class_name="min-w-0 flex-1",
                        ),
                        class_name="flex items-start gap-4 mb-5",
                    ),
                    rx.el.div(
                        _action_btn(
                            "power-off",
                            rx.cond(LanguageState.is_zh, "关机", "Shutdown"),
                            "danger",
                        ),
                        _action_btn(
                            "rotate-cw",
                            rx.cond(LanguageState.is_zh, "重启", "Restart"),
                            "warning",
                        ),
                        _action_btn(
                            "terminal",
                            rx.cond(LanguageState.is_zh, "终端", "Terminal"),
                            "primary",
                        ),
                        _action_btn(
                            "refresh-cw",
                            rx.cond(LanguageState.is_zh, "续费", "Renew"),
                            "orange",
                        ),
                        _action_btn(
                            "git-branch",
                            rx.cond(LanguageState.is_zh, "快照", "Snapshot"),
                        ),
                        class_name="flex items-center flex-wrap gap-2",
                    ),
                    class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 mb-4",
                ),
                rx.el.div(
                    _manage_tab_btn(
                        "layout-dashboard",
                        rx.cond(LanguageState.is_zh, "仪表盘", "Dashboard"),
                        "dashboard",
                    ),
                    _manage_tab_btn(
                        "shield",
                        rx.cond(LanguageState.is_zh, "访问控制", "Access"),
                        "access",
                    ),
                    _manage_tab_btn(
                        "network",
                        rx.cond(LanguageState.is_zh, "网络", "Network"),
                        "network",
                    ),
                    _manage_tab_btn(
                        "receipt",
                        rx.cond(LanguageState.is_zh, "计费信息", "Billing"),
                        "billing",
                    ),
                    _manage_tab_btn("globe", "DNS", "dns"),
                    _manage_tab_btn(
                        "activity",
                        rx.cond(LanguageState.is_zh, "监控", "Monitoring"),
                        "monitor",
                    ),
                    class_name="flex items-center gap-1 border-b border-white/5 mb-6 overflow-x-auto",
                ),
                render_manage_tab_content(),
                class_name="flex-1 min-w-0",
            ),
            class_name="flex gap-4",
        ),
    )


services_en = [
    {
        "flag": "🇭🇰",
        "name": "HK-Pro-竞技A",
        "region": "HKBGP",
        "ip": "103.28.***.42",
        "status": "Running",
        "expires": "2025-12-14",
    },
]
services_zh = [
    {
        "flag": "🇭🇰",
        "name": "HK-Pro-竞技A",
        "region": "HKBGP",
        "ip": "103.28.***.42",
        "status": "运行中",
        "expires": "2025-12-14",
    },
]


def _overview_content() -> rx.Component:
    return rx.fragment(
        _welcome_card(),
        rx.el.div(
            _account_stat(
                "wallet",
                rx.cond(LanguageState.is_zh, "账户余额", "Balance"),
                "¥" + f"{SessionState.balance:.2f}",
                rx.cond(LanguageState.is_zh, "可用于自动续费", "Available"),
                "cyan",
            ),
            _account_stat(
                "coins",
                rx.cond(LanguageState.is_zh, "AK 币", "AK Coins"),
                SessionState.ak_coins.to_string(),
                rx.cond(LanguageState.is_zh, "可兑换商品", "Redeemable"),
                "amber",
            ),
            _account_stat(
                "trending-up",
                rx.cond(LanguageState.is_zh, "总消费", "Total Spending"),
                "¥" + f"{SessionState.total_spending:.2f}",
                rx.cond(
                    LanguageState.is_zh,
                    ServersState.instances.length().to_string() + " 台实例",
                    ServersState.instances.length().to_string() + " instances",
                ),
                "indigo",
            ),
            _account_stat(
                "gift",
                rx.cond(LanguageState.is_zh, "邀请奖励", "Referral"),
                "¥" + f"{SessionState.referral_earnings:.2f}",
                rx.cond(
                    LanguageState.is_zh,
                    "邀请码 " + SessionState.invitation_code,
                    "Code " + SessionState.invitation_code,
                ),
                "emerald",
            ),
            class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6",
        ),
    )


def _login_prompt() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("lock", size=32, class_name="text-cyan-300"),
                class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-5 shadow-lg shadow-indigo-500/10",
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
            rx.el.div(
                rx.el.a(
                    rx.el.button(
                        rx.cond(LanguageState.is_zh, "登录", "Log In"),
                        rx.icon("arrow-right", size=14, class_name="ml-1.5"),
                        class_name="flex items-center px-5 py-2.5 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-sm font-bold shadow-xl shadow-indigo-500/30 transition-all cursor-pointer",
                    ),
                    href="/login",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.cond(LanguageState.is_zh, "免费注册", "Sign up"),
                        class_name="px-5 py-2.5 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-100 text-sm font-bold transition-all cursor-pointer",
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
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none [background-image:linear-gradient(to_right,rgba(99,102,241,0.05)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.05)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_0%,black_50%,transparent_100%)]"
        ),
        rx.el.div(
            class_name="fixed -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-indigo-600/15 blur-[160px] pointer-events-none"
        ),
        rx.el.div(
            class_name="fixed top-[40%] -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/8 blur-[140px] pointer-events-none"
        ),
        rx.el.div(
            class_name="fixed top-[70%] -right-40 w-[600px] h-[600px] rounded-full bg-violet-600/12 blur-[140px] pointer-events-none"
        ),
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
