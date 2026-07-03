import reflex as rx
from app.states.session_state import SessionState
from app.states.language_state import LanguageState


def _vip_badge_dark(size: str = "sm") -> rx.Component:
    cls_sm = "inline-flex items-center px-2 py-0.5 rounded-md bg-gradient-to-r from-amber-400/20 via-orange-400/20 to-rose-400/20 border border-amber-400/40 text-amber-200 text-[10px] font-bold shadow-lg shadow-amber-500/10"
    cls_md = "inline-flex items-center px-3 py-1.5 rounded-lg bg-gradient-to-r from-amber-400/20 via-orange-400/20 to-rose-400/20 border border-amber-400/40 text-amber-200 text-xs font-bold shadow-lg shadow-amber-500/10"
    return rx.el.span(
        rx.icon("crown", size=12, class_name="mr-1.5 text-amber-300"),
        rx.cond(LanguageState.is_zh, "VIP 会员", "VIP Member"),
        class_name=cls_md if size == "md" else cls_sm,
    )


def _free_badge_dark(size: str = "sm") -> rx.Component:
    cls_sm = "inline-flex items-center px-2 py-0.5 rounded-md bg-white/5 border border-white/10 text-slate-400 text-[10px] font-bold"
    cls_md = "inline-flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 text-slate-300 text-xs font-bold"
    return rx.el.span(
        rx.icon("user", size=12, class_name="mr-1.5 text-slate-400"),
        rx.cond(LanguageState.is_zh, "普通用户", "Free User"),
        class_name=cls_md if size == "md" else cls_sm,
    )


def _console_navbar() -> rx.Component:
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
                href="/",
                class_name="flex items-center gap-2",
                aria_label="AiarksCloud home",
            ),
            rx.el.nav(
                rx.el.a(
                    LanguageState.nav_home,
                    href="/",
                    class_name="text-sm text-slate-300 hover:text-white font-medium transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_products,
                    href="/shop/server",
                    class_name="text-sm text-slate-300 hover:text-white font-medium transition-colors",
                ),
                rx.el.a(
                    rx.cond(LanguageState.is_zh, "控制台", "Console"),
                    href="/console",
                    class_name="text-sm text-cyan-300 font-semibold",
                    aria_current="page",
                ),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages",
                        size=16,
                        class_name="text-cyan-300 mr-1.5",
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-slate-200 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 focus:outline-hidden focus:ring-2 focus:ring-cyan-500/30 transition-all cursor-pointer",
                    aria_label="Toggle language",
                ),
                rx.cond(
                    SessionState.is_vip,
                    rx.el.span(
                        rx.icon(
                            "crown", size=12, class_name="mr-1 text-amber-300"
                        ),
                        "VIP",
                        class_name="hidden sm:inline-flex items-center text-[10px] font-bold text-amber-200 bg-gradient-to-r from-amber-400/20 to-rose-400/20 px-2 py-1 rounded-md border border-amber-400/40 shadow-lg shadow-amber-500/10",
                    ),
                    rx.fragment(),
                ),
                rx.el.div(
                    rx.el.button(
                        SessionState.avatar_initial,
                        class_name="size-8 rounded-full bg-gradient-to-br from-indigo-500 to-cyan-500 text-white font-bold text-xs flex items-center justify-center border border-white/20 hover:brightness-110 transition-all shadow-lg shadow-indigo-500/30 cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-cyan-500/40",
                        aria_label="Account menu",
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
                                _vip_badge_dark(),
                                _free_badge_dark(),
                            ),
                            class_name="px-4 py-3 border-b border-white/10 flex flex-col gap-1",
                        ),
                        rx.el.button(
                            rx.cond(
                                LanguageState.is_zh, "退出登录", "Sign Out"
                            ),
                            on_click=SessionState.logout_user,
                            class_name="w-full text-left text-sm text-rose-400 hover:bg-rose-500/10 px-4 py-2.5 transition-colors cursor-pointer",
                        ),
                        class_name="invisible opacity-0 translate-y-1 group-hover/avatar:visible group-hover/avatar:opacity-100 group-hover/avatar:translate-y-0 absolute right-0 mt-2 w-56 rounded-xl bg-slate-950/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/50 transition-all duration-200 z-50 overflow-hidden",
                    ),
                    class_name="group/avatar relative",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-[1400px] mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-slate-950/70 border-b border-white/5",
    )


def _stat_card(
    icon: str, label: rx.Var, value: str, sub: rx.Var
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-cyan-300"),
            class_name="w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mb-4 shadow-lg shadow-indigo-500/10",
        ),
        rx.el.p(
            label,
            class_name="text-[10px] text-cyan-300 uppercase tracking-wider font-bold mb-1",
        ),
        rx.el.p(
            value,
            class_name="text-2xl text-white font-extrabold tracking-tight",
        ),
        rx.el.p(sub, class_name="text-xs text-slate-400 font-medium mt-1"),
        class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 hover:-translate-y-0.5 transition-all duration-300",
    )


def _membership_card() -> rx.Component:
    return rx.el.div(
        rx.cond(
            SessionState.is_vip,
            rx.el.div(
                rx.el.div(
                    class_name="absolute -inset-px rounded-2xl bg-gradient-to-b from-amber-400/40 via-orange-400/20 to-transparent blur-sm -z-10",
                ),
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_120%_at_20%_30%,rgba(251,191,36,0.15),transparent)] pointer-events-none rounded-2xl",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "crown",
                                size=18,
                                class_name="text-amber-300",
                            ),
                            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-amber-400/20 to-rose-400/20 border border-amber-400/40 flex items-center justify-center shadow-lg shadow-amber-500/20",
                        ),
                        rx.el.div(
                            rx.el.p(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "VIP 会员",
                                    "VIP Member",
                                ),
                                class_name="text-white text-lg font-bold",
                            ),
                            rx.el.p(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "享受专属特权与优先支持",
                                    "Enjoy exclusive perks & priority support",
                                ),
                                class_name="text-slate-400 text-xs font-medium",
                            ),
                        ),
                        rx.el.span(
                            "PREMIUM",
                            class_name="ml-auto text-[10px] font-bold px-2 py-1 rounded-md bg-gradient-to-r from-amber-400/20 to-rose-400/20 border border-amber-400/40 text-amber-200",
                        ),
                        class_name="flex items-center gap-3 mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "check", size=12, class_name="text-amber-300"
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "全部套餐 15% 折扣",
                                    "15% off all plans",
                                ),
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=12, class_name="text-amber-300"
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "优先技术支持",
                                    "Priority support",
                                ),
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=12, class_name="text-amber-300"
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "免费快照与备份",
                                    "Free snapshots & backup",
                                ),
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="flex flex-col gap-2",
                    ),
                    class_name="relative p-6",
                ),
                class_name="relative rounded-2xl bg-slate-900/70 backdrop-blur-xl border border-amber-400/30 overflow-hidden shadow-2xl shadow-amber-500/10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("user", size=18, class_name="text-cyan-300"),
                        class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center shadow-lg shadow-indigo-500/10",
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "普通用户",
                                "Free User",
                            ),
                            class_name="text-white text-lg font-bold",
                        ),
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "升级到 VIP 解锁更多权益",
                                "Upgrade to VIP for more perks",
                            ),
                            class_name="text-slate-400 text-xs font-medium",
                        ),
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon(
                            "crown",
                            size=14,
                            class_name="mr-1.5 text-amber-300",
                        ),
                        rx.cond(
                            LanguageState.is_zh,
                            "升级到 VIP",
                            "Upgrade to VIP",
                        ),
                        rx.icon("arrow-right", size=14, class_name="ml-1"),
                        class_name="mt-6 flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-amber-400/20 via-orange-400/20 to-rose-400/20 hover:brightness-125 border border-amber-400/40 text-amber-100 text-sm font-bold shadow-lg shadow-amber-500/10 transition-all cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-amber-400/40",
                    ),
                    href="/shop/server",
                ),
                class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 hover:border-white/15 transition-all",
            ),
        ),
    )


def _service_row(item: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(item["flag"], class_name="text-xl"),
                rx.el.div(
                    rx.el.p(
                        item["name"],
                        class_name="text-sm text-white font-semibold",
                    ),
                    rx.el.p(
                        item["region"],
                        class_name="text-[10px] text-slate-500 font-bold tracking-wider",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                item["ip"],
                class_name="text-xs text-slate-300 font-mono",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                ),
                item["status"],
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                item["expires"],
                class_name="text-xs text-slate-300 font-medium",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("external-link", size=12, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "管理", "Manage"),
                class_name="inline-flex items-center px-2.5 py-1 rounded-md bg-white/5 hover:bg-cyan-500/10 border border-white/10 hover:border-cyan-500/40 text-xs text-slate-300 hover:text-cyan-200 font-semibold transition-all cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-cyan-500/30",
            ),
            class_name="px-4 py-3 text-right",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.03] transition-colors",
    )


def _order_row(o: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                o["id"],
                class_name="text-xs text-cyan-300 font-mono",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["item"],
                class_name="text-sm text-white font-semibold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["date"],
                class_name="text-xs text-slate-400 font-medium",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["amount"],
                class_name="text-sm text-white font-bold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["status"],
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30 w-fit",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.03] transition-colors",
    )


def _resource_bar(
    label: rx.Var, value: str, percent: int, color: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                label, class_name="text-xs text-slate-300 font-semibold"
            ),
            rx.el.span(
                value,
                class_name="text-xs text-white font-mono font-bold ml-auto",
            ),
            class_name="flex items-center mb-1.5",
        ),
        rx.el.div(
            rx.el.div(
                class_name=f"h-full {color} rounded-full shadow-lg",
                style={"width": f"{percent}%"},
            ),
            class_name="h-1.5 bg-white/5 rounded-full overflow-hidden border border-white/5",
        ),
        class_name="",
    )


def _support_link(icon: str, title: rx.Var, desc: rx.Var) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-cyan-300"),
            class_name="w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center shrink-0 shadow-lg shadow-indigo-500/10",
        ),
        rx.el.div(
            rx.el.p(
                title,
                class_name="text-sm text-white font-bold",
            ),
            rx.el.p(
                desc,
                class_name="text-xs text-slate-400 font-medium",
            ),
        ),
        rx.icon(
            "arrow-right",
            size=14,
            class_name="ml-auto text-slate-500",
        ),
        href="#",
        class_name="flex items-center gap-3 p-4 rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 hover:border-cyan-500/40 hover:bg-cyan-500/5 transition-all focus:outline-hidden focus:ring-2 focus:ring-cyan-500/30",
    )


def console_page() -> rx.Component:
    services_en = [
        {
            "flag": "🇭🇰",
            "name": "HK-Pro-竞技A",
            "region": "HKBGP",
            "ip": "103.28.***.42",
            "status": "Running",
            "expires": "2025-12-14",
        },
        {
            "flag": "🇯🇵",
            "name": "JP-Standard",
            "region": "JPBGP",
            "ip": "45.32.***.108",
            "status": "Running",
            "expires": "2025-11-02",
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
        {
            "flag": "🇯🇵",
            "name": "JP-Standard",
            "region": "JPBGP",
            "ip": "45.32.***.108",
            "status": "运行中",
            "expires": "2025-11-02",
        },
    ]
    orders_en = [
        {
            "id": "#AC-20250912",
            "item": "HK-Pro-竞技A · 1 mo",
            "date": "2025-09-12",
            "amount": "¥50.00",
            "status": "Paid",
        },
        {
            "id": "#AC-20250820",
            "item": "JP-Standard · 3 mo",
            "date": "2025-08-20",
            "amount": "¥199.47",
            "status": "Paid",
        },
        {
            "id": "#AC-20250714",
            "item": "MOLite-Starter · 1 mo",
            "date": "2025-07-14",
            "amount": "¥43.74",
            "status": "Paid",
        },
    ]
    orders_zh = [
        {
            "id": "#AC-20250912",
            "item": "HK-Pro-竞技A · 1 个月",
            "date": "2025-09-12",
            "amount": "¥50.00",
            "status": "已支付",
        },
        {
            "id": "#AC-20250820",
            "item": "JP-Standard · 3 个月",
            "date": "2025-08-20",
            "amount": "¥199.47",
            "status": "已支付",
        },
        {
            "id": "#AC-20250714",
            "item": "MOLite-Starter · 1 个月",
            "date": "2025-07-14",
            "amount": "¥43.74",
            "status": "已支付",
        },
    ]

    return rx.el.main(
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none [background-image:linear-gradient(to_right,rgba(99,102,241,0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.06)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_0%,black_50%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-indigo-600/20 blur-[160px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed top-[40%] -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/10 blur-[140px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed top-[70%] -right-40 w-[600px] h-[600px] rounded-full bg-violet-600/15 blur-[140px] pointer-events-none",
        ),
        _console_navbar(),
        rx.el.div(
            # Header
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2 shadow-lg shadow-emerald-400/50 animate-pulse"
                        ),
                        rx.el.span(
                            rx.cond(
                                LanguageState.is_zh,
                                "控制台在线",
                                "Console online",
                            ),
                            class_name="text-xs text-slate-200 font-semibold",
                        ),
                        class_name="inline-flex items-center px-3 py-1 rounded-full bg-white/5 border border-white/10 backdrop-blur-sm mb-4",
                    ),
                    rx.el.h1(
                        rx.cond(
                            LanguageState.is_zh,
                            "欢迎回来,",
                            "Welcome back, ",
                        ),
                        rx.el.span(
                            SessionState.auth_username,
                            class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                        ),
                        class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight",
                    ),
                    rx.el.p(
                        SessionState.auth_email,
                        class_name="text-sm text-slate-400 font-medium mt-1",
                    ),
                    class_name="",
                ),
                rx.cond(
                    SessionState.is_vip,
                    _vip_badge_dark(size="md"),
                    _free_badge_dark(size="md"),
                ),
                class_name="flex items-start justify-between mb-8 flex-wrap gap-4",
            ),
            # Stats grid
            rx.el.div(
                _stat_card(
                    "server",
                    rx.cond(LanguageState.is_zh, "已购服务", "Active Services"),
                    "2",
                    rx.cond(LanguageState.is_zh, "运行中", "Running"),
                ),
                _stat_card(
                    "wallet",
                    rx.cond(LanguageState.is_zh, "账户余额", "Balance"),
                    "¥128.50",
                    rx.cond(
                        LanguageState.is_zh,
                        "可用于自动续费",
                        "Available for auto-renewal",
                    ),
                ),
                _stat_card(
                    "gauge",
                    rx.cond(LanguageState.is_zh, "本月流量", "Traffic (mo)"),
                    "3.2 TB",
                    rx.cond(
                        LanguageState.is_zh,
                        "剩余 6.8 TB",
                        "6.8 TB remaining",
                    ),
                ),
                _stat_card(
                    "receipt",
                    rx.cond(LanguageState.is_zh, "累计订单", "Total Orders"),
                    "12",
                    rx.cond(
                        LanguageState.is_zh,
                        "全部已完成",
                        "All completed",
                    ),
                ),
                class_name="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8",
            ),
            # Membership + Resources
            rx.el.div(
                _membership_card(),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "activity",
                                size=16,
                                class_name="text-cyan-300",
                            ),
                            rx.el.h3(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "资源使用状态",
                                    "Resource Usage",
                                ),
                                class_name="text-white font-bold text-base",
                            ),
                            class_name="flex items-center gap-2 mb-5",
                        ),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "CPU", "CPU"),
                            "42%",
                            42,
                            "bg-gradient-to-r from-indigo-50 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "内存", "Memory"),
                            "58%",
                            58,
                            "bg-gradient-to-r from-indigo-50 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "磁盘", "Disk"),
                            "31%",
                            31,
                            "bg-gradient-to-r from-emerald-50 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "流量", "Traffic"),
                            "3.2 / 10 TB",
                            32,
                            "bg-gradient-to-r from-amber-50 to-orange-500",
                        ),
                        class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6",
                    ),
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-8",
            ),
            # Services table
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("box", size=16, class_name="text-cyan-300"),
                        rx.el.h3(
                            rx.cond(
                                LanguageState.is_zh,
                                "已购服务",
                                "My Services",
                            ),
                            class_name="text-white font-bold text-base",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.a(
                        rx.cond(LanguageState.is_zh, "购买新服务", "Buy new"),
                        rx.icon("plus", size=12, class_name="ml-1"),
                        href="/shop/server",
                        class_name="inline-flex items-center px-3 py-1.5 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-indigo-500/25 transition-all cursor-pointer focus:outline-hidden focus:ring-2 focus:ring-cyan-500/40",
                    ),
                    class_name="flex items-center justify-between px-6 py-4 border-b border-white/5 bg-white/[0.02]",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh, "服务", "Service"
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    "IP",
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh, "状态", "Status"
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "到期时间",
                                        "Expires",
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    "",
                                    class_name="px-4 py-3",
                                ),
                                class_name="bg-white/[0.02] border-b border-white/10",
                            ),
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                rx.cond(
                                    LanguageState.is_zh,
                                    services_zh,
                                    services_en,
                                ),
                                _service_row,
                            ),
                        ),
                        class_name="table-auto w-full",
                    ),
                    class_name="overflow-x-auto",
                ),
                class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden mb-8",
            ),
            # Recent orders + Support
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "receipt",
                                size=16,
                                class_name="text-cyan-300",
                            ),
                            rx.el.h3(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "最近订单",
                                    "Recent Orders",
                                ),
                                class_name="text-white font-bold text-base",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.cond(
                            SessionState.is_vip,
                            rx.el.span(
                                rx.icon(
                                    "crown",
                                    size=10,
                                    class_name="mr-1 text-amber-300",
                                ),
                                "VIP",
                                class_name="inline-flex items-center text-[10px] font-bold text-amber-200 bg-gradient-to-r from-amber-400/20 to-rose-400/20 px-2 py-0.5 rounded-md border border-amber-400/40",
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "普通用户",
                                    "Free",
                                ),
                                class_name="text-[10px] font-bold text-slate-400 bg-white/5 px-2 py-0.5 rounded-md border border-white/10",
                            ),
                        ),
                        class_name="flex items-center justify-between px-6 py-4 border-b border-white/5 bg-white/[0.02]",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh,
                                            "订单号",
                                            "Order",
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh, "商品", "Item"
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh, "日期", "Date"
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh,
                                            "金额",
                                            "Amount",
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh,
                                            "状态",
                                            "Status",
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-3",
                                    ),
                                    class_name="bg-white/[0.02] border-b border-white/10",
                                ),
                            ),
                            rx.el.tbody(
                                rx.foreach(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        orders_zh,
                                        orders_en,
                                    ),
                                    _order_row,
                                ),
                            ),
                            class_name="table-auto w-full",
                        ),
                        class_name="overflow-x-auto",
                    ),
                    class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "life-buoy", size=16, class_name="text-cyan-300"
                        ),
                        rx.el.h3(
                            rx.cond(
                                LanguageState.is_zh,
                                "支持中心",
                                "Support",
                            ),
                            class_name="text-white font-bold text-base",
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    _support_link(
                        "message-circle",
                        rx.cond(LanguageState.is_zh, "在线聊天", "Live Chat"),
                        rx.cond(
                            LanguageState.is_zh,
                            "响应 < 2 分钟",
                            "Reply < 2 min",
                        ),
                    ),
                    rx.el.div(class_name="h-2"),
                    _support_link(
                        "send",
                        rx.cond(LanguageState.is_zh, "电报群", "Telegram"),
                        rx.cond(
                            LanguageState.is_zh,
                            "社区与优先支持",
                            "Community support",
                        ),
                    ),
                    rx.el.div(class_name="h-2"),
                    _support_link(
                        "book-open",
                        rx.cond(LanguageState.is_zh, "文档", "Docs"),
                        rx.cond(
                            LanguageState.is_zh,
                            "指南与 API 参考",
                            "Guides & API",
                        ),
                    ),
                    class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-8",
            ),
            class_name="max-w-[1400px] mx-auto px-6 pt-24 pb-16 relative z-10",
        ),
        class_name="font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
    )
