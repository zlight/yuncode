import reflex as rx
from app.states.session_state import SessionState
from app.states.language_state import LanguageState


def _console_navbar() -> rx.Component:
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
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.el.a(
                    LanguageState.nav_home,
                    href="/",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_products,
                    href="/shop/server",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                rx.el.a(
                    rx.cond(LanguageState.is_zh, "控制台", "Console"),
                    href="/console",
                    class_name="text-sm text-indigo-600 font-semibold",
                ),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.div(
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
                ),
                rx.cond(
                    SessionState.is_vip,
                    rx.el.span(
                        rx.icon("crown", size=12, class_name="mr-1"),
                        "VIP",
                        class_name="inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-1 rounded-md border border-amber-200",
                    ),
                    rx.fragment(),
                ),
                rx.el.div(
                    rx.el.button(
                        SessionState.avatar_initial,
                        class_name="size-8 rounded-full bg-indigo-50 text-indigo-700 font-bold text-xs flex items-center justify-center border border-indigo-200 hover:bg-indigo-100 transition-colors shadow-xs cursor-pointer",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                SessionState.auth_username,
                                class_name="text-sm font-bold text-slate-800",
                            ),
                            rx.el.p(
                                SessionState.auth_email,
                                class_name="text-xs text-slate-500 truncate",
                            ),
                            rx.cond(
                                SessionState.is_vip,
                                rx.el.span(
                                    rx.icon(
                                        "crown", size=10, class_name="mr-1"
                                    ),
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "VIP 会员",
                                        "VIP Member",
                                    ),
                                    class_name="mt-2 inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200 w-fit",
                                ),
                                rx.el.span(
                                    rx.icon("user", size=10, class_name="mr-1"),
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "普通用户",
                                        "Free User",
                                    ),
                                    class_name="mt-2 inline-flex items-center text-[10px] font-bold text-slate-600 bg-slate-50 px-2 py-0.5 rounded-md border border-slate-200 w-fit",
                                ),
                            ),
                            class_name="px-4 py-3 border-b border-slate-100 flex flex-col",
                        ),
                        rx.el.button(
                            rx.cond(
                                LanguageState.is_zh, "退出登录", "Sign Out"
                            ),
                            on_click=SessionState.logout_user,
                            class_name="w-full text-left text-sm text-rose-600 hover:bg-rose-50 px-4 py-2.5 transition-colors cursor-pointer",
                        ),
                        class_name="invisible opacity-0 translate-y-1 group-hover/avatar:visible group-hover/avatar:opacity-100 group-hover/avatar:translate-y-0 absolute right-0 mt-2 w-56 rounded-xl bg-white border border-slate-200 shadow-lg transition-all duration-200 z-50 overflow-hidden",
                    ),
                    class_name="group/avatar relative",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-[1400px] mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-white/85 border-b border-slate-200/60",
    )


def _stat_card(icon: str, label, value, sub) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-indigo-600"),
            class_name="w-10 h-10 rounded-lg bg-indigo-50 border border-indigo-100 flex items-center justify-center mb-4",
        ),
        rx.el.p(
            label,
            class_name="text-[10px] text-slate-400 uppercase tracking-wider font-bold mb-1",
        ),
        rx.el.p(
            value,
            class_name="text-2xl text-slate-900 font-extrabold tracking-tight",
        ),
        rx.el.p(sub, class_name="text-xs text-slate-500 font-medium mt-1"),
        class_name="rounded-2xl bg-white border border-slate-200 p-5 shadow-xs hover:border-indigo-300 transition-all",
    )


def _membership_card() -> rx.Component:
    return rx.el.div(
        rx.cond(
            SessionState.is_vip,
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_120%_at_20%_50%,rgba(255,255,255,0.15),transparent)] pointer-events-none",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon("crown", size=18, class_name="text-white"),
                            class_name="w-11 h-11 rounded-xl bg-white/15 border border-white/20 flex items-center justify-center",
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
                                class_name="text-white/80 text-xs font-medium",
                            ),
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon("check", size=12, class_name="text-white"),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "全部套餐 15% 折扣",
                                    "15% off all plans",
                                ),
                                class_name="text-xs text-white/90 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon("check", size=12, class_name="text-white"),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "优先技术支持",
                                    "Priority support",
                                ),
                                class_name="text-xs text-white/90 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon("check", size=12, class_name="text-white"),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "免费快照与备份",
                                    "Free snapshots & backup",
                                ),
                                class_name="text-xs text-white/90 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="flex flex-col gap-2 mt-6",
                    ),
                    class_name="relative p-6",
                ),
                class_name="relative rounded-2xl bg-gradient-to-r from-amber-500 via-orange-500 to-rose-500 overflow-hidden shadow-md",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("user", size=18, class_name="text-slate-600"),
                        class_name="w-11 h-11 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-center",
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "普通用户",
                                "Free User",
                            ),
                            class_name="text-slate-900 text-lg font-bold",
                        ),
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "升级到 VIP 解锁更多权益",
                                "Upgrade to VIP for more perks",
                            ),
                            class_name="text-slate-500 text-xs font-medium",
                        ),
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("crown", size=14, class_name="mr-1.5"),
                        rx.cond(
                            LanguageState.is_zh,
                            "升级到 VIP",
                            "Upgrade to VIP",
                        ),
                        rx.icon("arrow-right", size=14, class_name="ml-1"),
                        class_name="mt-6 flex items-center px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-bold shadow-sm hover:shadow-md transition-all cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                class_name="rounded-2xl bg-white border border-slate-200 p-6 shadow-xs",
            ),
        ),
    )


def _service_row(item) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(item["flag"], class_name="text-xl"),
                rx.el.div(
                    rx.el.p(
                        item["name"],
                        class_name="text-sm text-slate-800 font-semibold",
                    ),
                    rx.el.p(
                        item["region"],
                        class_name="text-[10px] text-slate-400 font-bold tracking-wider",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                item["ip"],
                class_name="text-xs text-slate-600 font-mono",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1.5 animate-pulse"
                ),
                item["status"],
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                item["expires"],
                class_name="text-xs text-slate-600 font-medium",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("external-link", size=12, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "管理", "Manage"),
                class_name="inline-flex items-center px-2.5 py-1 rounded-md bg-slate-50 hover:bg-indigo-50 border border-slate-200 hover:border-indigo-300 text-xs text-slate-600 hover:text-indigo-600 font-semibold transition-all cursor-pointer",
            ),
            class_name="px-4 py-3 text-right",
        ),
        class_name="border-b border-slate-100 hover:bg-slate-50/50 transition-colors",
    )


def _order_row(o) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                o["id"],
                class_name="text-xs text-slate-600 font-mono",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["item"],
                class_name="text-sm text-slate-800 font-semibold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["date"],
                class_name="text-xs text-slate-500 font-medium",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["amount"],
                class_name="text-sm text-slate-800 font-bold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                o["status"],
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200 w-fit",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-slate-100 hover:bg-slate-50/50 transition-colors",
    )


def _resource_bar(label, value: str, percent: int, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                label, class_name="text-xs text-slate-600 font-semibold"
            ),
            rx.el.span(
                value,
                class_name="text-xs text-slate-800 font-mono font-bold ml-auto",
            ),
            class_name="flex items-center mb-1.5",
        ),
        rx.el.div(
            rx.el.div(
                class_name=f"h-full {color} rounded-full",
                style={"width": f"{percent}%"},
            ),
            class_name="h-1.5 bg-slate-100 rounded-full overflow-hidden",
        ),
        class_name="",
    )


def _support_link(icon: str, title, desc) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-indigo-600"),
            class_name="w-10 h-10 rounded-lg bg-indigo-50 border border-indigo-100 flex items-center justify-center shrink-0",
        ),
        rx.el.div(
            rx.el.p(
                title,
                class_name="text-sm text-slate-800 font-bold",
            ),
            rx.el.p(
                desc,
                class_name="text-xs text-slate-500 font-medium",
            ),
        ),
        rx.icon(
            "arrow-right",
            size=14,
            class_name="ml-auto text-slate-300",
        ),
        href="#",
        class_name="flex items-center gap-3 p-4 rounded-xl bg-white border border-slate-200 hover:border-indigo-300 hover:bg-indigo-50/20 transition-all",
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
            class_name="fixed inset-0 pointer-events-none opacity-100 [background-image:linear-gradient(to_right,rgba(99,102,241,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.03)_1px,transparent_1px)] [background-size:24px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,black_70%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -left-40 top-40 w-[500px] h-[500px] rounded-full bg-indigo-100/40 blur-[140px] pointer-events-none",
        ),
        _console_navbar(),
        rx.el.div(
            # Header
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        rx.cond(
                            LanguageState.is_zh,
                            "欢迎回来,",
                            "Welcome back, ",
                        ),
                        rx.el.span(
                            SessionState.auth_username,
                            class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                        ),
                        class_name="text-3xl font-bold text-slate-900 tracking-tight",
                    ),
                    rx.el.p(
                        SessionState.auth_email,
                        class_name="text-sm text-slate-500 font-medium mt-1",
                    ),
                    class_name="",
                ),
                rx.cond(
                    SessionState.is_vip,
                    rx.el.span(
                        rx.icon("crown", size=14, class_name="mr-1.5"),
                        rx.cond(LanguageState.is_zh, "VIP 会员", "VIP Member"),
                        class_name="inline-flex items-center px-3 py-1.5 rounded-lg bg-gradient-to-r from-amber-100 to-orange-100 border border-amber-200 text-amber-800 text-xs font-bold shadow-xs",
                    ),
                    rx.el.span(
                        rx.icon("user", size=14, class_name="mr-1.5"),
                        rx.cond(LanguageState.is_zh, "普通用户", "Free User"),
                        class_name="inline-flex items-center px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 text-slate-600 text-xs font-bold shadow-xs",
                    ),
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
                                class_name="text-indigo-600",
                            ),
                            rx.el.h3(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "资源使用状态",
                                    "Resource Usage",
                                ),
                                class_name="text-slate-900 font-bold text-base",
                            ),
                            class_name="flex items-center gap-2 mb-5",
                        ),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "CPU", "CPU"),
                            "42%",
                            42,
                            "bg-gradient-to-r from-indigo-500 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "内存", "Memory"),
                            "58%",
                            58,
                            "bg-gradient-to-r from-indigo-500 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "磁盘", "Disk"),
                            "31%",
                            31,
                            "bg-gradient-to-r from-emerald-500 to-cyan-500",
                        ),
                        rx.el.div(class_name="h-4"),
                        _resource_bar(
                            rx.cond(LanguageState.is_zh, "流量", "Traffic"),
                            "3.2 / 10 TB",
                            32,
                            "bg-gradient-to-r from-amber-500 to-orange-500",
                        ),
                        class_name="rounded-2xl bg-white border border-slate-200 p-6 shadow-xs",
                    ),
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-8",
            ),
            # Services table
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("box", size=16, class_name="text-indigo-600"),
                        rx.el.h3(
                            rx.cond(
                                LanguageState.is_zh,
                                "已购服务",
                                "My Services",
                            ),
                            class_name="text-slate-900 font-bold text-base",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.a(
                        rx.cond(LanguageState.is_zh, "购买新服务", "Buy new"),
                        rx.icon("plus", size=12, class_name="ml-1"),
                        href="/shop/server",
                        class_name="inline-flex items-center px-3 py-1.5 rounded-md bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition-all cursor-pointer",
                    ),
                    class_name="flex items-center justify-between px-6 py-4 border-b border-slate-100 bg-slate-50/50",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh, "服务", "Service"
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    "IP",
                                    class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh, "状态", "Status"
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "到期时间",
                                        "Expires",
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                ),
                                rx.el.th(
                                    "",
                                    class_name="px-4 py-3",
                                ),
                                class_name="bg-white border-b border-slate-100",
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
                class_name="rounded-2xl bg-white border border-slate-200 shadow-xs overflow-hidden mb-8",
            ),
            # Recent orders + Support
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "receipt",
                                size=16,
                                class_name="text-indigo-600",
                            ),
                            rx.el.h3(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "最近订单",
                                    "Recent Orders",
                                ),
                                class_name="text-slate-900 font-bold text-base",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.cond(
                            SessionState.is_vip,
                            rx.el.span(
                                rx.icon("crown", size=10, class_name="mr-1"),
                                "VIP",
                                class_name="inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200",
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "普通用户",
                                    "Free",
                                ),
                                class_name="text-[10px] font-bold text-slate-500 bg-slate-50 px-2 py-0.5 rounded-md border border-slate-200",
                            ),
                        ),
                        class_name="flex items-center justify-between px-6 py-4 border-b border-slate-100 bg-slate-50/50",
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
                                        class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh, "商品", "Item"
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh, "日期", "Date"
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh,
                                            "金额",
                                            "Amount",
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                    ),
                                    rx.el.th(
                                        rx.cond(
                                            LanguageState.is_zh,
                                            "状态",
                                            "Status",
                                        ),
                                        class_name="text-left text-[10px] font-bold text-slate-500 uppercase tracking-wider px-4 py-3",
                                    ),
                                    class_name="bg-white border-b border-slate-100",
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
                    class_name="rounded-2xl bg-white border border-slate-200 shadow-xs overflow-hidden lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "life-buoy", size=16, class_name="text-indigo-600"
                        ),
                        rx.el.h3(
                            rx.cond(
                                LanguageState.is_zh,
                                "支持中心",
                                "Support",
                            ),
                            class_name="text-slate-900 font-bold text-base",
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
                    class_name="rounded-2xl bg-white border border-slate-200 p-6 shadow-xs",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-8",
            ),
            class_name="max-w-[1400px] mx-auto px-6 pt-24 pb-16 relative z-10",
        ),
        class_name="font-['Inter'] bg-[#f8fafc] min-h-screen relative overflow-x-hidden text-slate-800 antialiased",
    )
