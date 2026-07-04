import reflex as rx
from app.admin.admin_state import AdminState
from app.states.language_state import LanguageState
from app.components.ui_styles import style_badge


def _admin_users_stats() -> rx.Component:
    return rx.el.div(
        # Total Users - Blue theme
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Total Users / 总用户数",
                        class_name="text-xs text-slate-400 font-semibold uppercase tracking-wider",
                    ),
                    rx.el.p(
                        "1,482",
                        class_name="text-3xl font-extrabold text-white tracking-tight leading-none mt-2",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.icon("users", size=18, class_name="text-blue-300"),
                    class_name="w-10 h-10 rounded-lg bg-blue-500/10 border border-blue-500/30 flex items-center justify-center shrink-0",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-blue-500/30 transition-all",
        ),
        # Active Users - Green theme
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Active Users / 活跃用户数",
                        class_name="text-xs text-slate-400 font-semibold uppercase tracking-wider",
                    ),
                    rx.el.p(
                        "1,245",
                        class_name="text-3xl font-extrabold text-white tracking-tight leading-none mt-2",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.icon(
                        "user-check", size=18, class_name="text-emerald-300"
                    ),
                    class_name="w-10 h-10 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center shrink-0",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-emerald-500/30 transition-all",
        ),
        # Today's Calls/Transactions - Purple theme
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Today's Transactions / 今日调用交易",
                        class_name="text-xs text-slate-400 font-semibold uppercase tracking-wider",
                    ),
                    rx.el.p(
                        "8,432",
                        class_name="text-3xl font-extrabold text-white tracking-tight leading-none mt-2",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.icon("activity", size=18, class_name="text-violet-300"),
                    class_name="w-10 h-10 rounded-lg bg-violet-500/10 border border-violet-500/30 flex items-center justify-center shrink-0",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-violet-500/30 transition-all",
        ),
        class_name="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6",
    )


def _stat_card(st: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                st["title"],
                class_name="text-xs text-slate-400 font-semibold uppercase tracking-wider",
            ),
            rx.el.div(
                rx.icon(st["icon"], size=14, class_name="text-cyan-300"),
                class_name="w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center ml-auto shrink-0",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.p(
            st["value"],
            class_name="text-3xl font-extrabold text-white tracking-tight leading-none mb-1",
        ),
        rx.el.p(
            st["trend"], class_name="text-[11px] text-emerald-400 font-medium"
        ),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 transition-all",
    )


def _user_row(u: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            u["id"].to_string(),
            class_name="px-6 py-4 border-b border-white/5 text-slate-400 font-mono text-xs",
        ),
        rx.el.td(
            u["name"],
            class_name="px-6 py-4 border-b border-white/5 text-white font-semibold text-sm",
        ),
        rx.el.td(
            u["email"],
            class_name="px-6 py-4 border-b border-white/5 text-slate-300 font-mono text-xs",
        ),
        rx.el.td(
            rx.el.span(
                u["role"],
                class_name="inline-block text-[10px] font-bold px-2 py-0.5 rounded bg-white/5 text-slate-300 border border-white/10",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.cond(
                u["status"] == "Active",
                style_badge("Active / 激活", color="emerald"),
                style_badge("Suspended / 禁用", color="rose"),
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("pencil", size=12, class_name="mr-1"),
                "Edit",
                on_click=lambda: AdminState.open_edit_dialog(u["id"].to(int)),
                class_name="px-2.5 py-1 rounded bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 text-[11px] text-cyan-300 font-bold transition-all cursor-pointer inline-flex items-center",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        class_name="hover:bg-white/[0.01] transition-colors",
    )


def _edit_user_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/60 backdrop-blur-sm z-40",
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "user-cog", size=18, class_name="text-cyan-300"
                        ),
                        class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center shrink-0",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.title(
                            "Edit User / 编辑用户",
                            class_name="text-base font-extrabold text-white tracking-tight",
                        ),
                        rx.radix.primitives.dialog.description(
                            "Update the user's display name and email. / 修改用户显示名称和邮箱。",
                            class_name="text-xs text-slate-400 font-medium mt-0.5",
                        ),
                        class_name="flex-1 min-w-0",
                    ),
                    rx.radix.primitives.dialog.close(
                        rx.el.button(
                            rx.icon(
                                "x",
                                size=16,
                                class_name="text-slate-400 hover:text-white",
                            ),
                            type="button",
                            class_name="w-8 h-8 rounded-lg hover:bg-white/5 flex items-center justify-center cursor-pointer transition-all",
                        ),
                    ),
                    class_name="flex items-start gap-3 p-5 border-b border-white/5",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "User ID / 用户 ID",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.p(
                            "#" + AdminState.edit_user_id.to_string(),
                            class_name="text-xs text-cyan-300 font-mono font-bold",
                        ),
                        class_name="flex flex-col mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Name / 姓名",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "user",
                                size=14,
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                            ),
                            rx.el.input(
                                name="name",
                                type="text",
                                default_value=AdminState.edit_name,
                                key=AdminState.edit_user_id.to_string()
                                + "-name",
                                placeholder="Enter name",
                                required=True,
                                class_name="w-full pl-9 pr-3 py-2 bg-slate-950/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm",
                            ),
                            class_name="relative",
                        ),
                        class_name="flex flex-col mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email / 邮箱",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "mail",
                                size=14,
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                            ),
                            rx.el.input(
                                name="email",
                                type="email",
                                default_value=AdminState.edit_email,
                                key=AdminState.edit_user_id.to_string()
                                + "-email",
                                placeholder="user@aiarks.com",
                                required=True,
                                class_name="w-full pl-9 pr-3 py-2 bg-slate-950/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm font-mono",
                            ),
                            class_name="relative",
                        ),
                        class_name="flex flex-col mb-6",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.close(
                            rx.el.button(
                                "Cancel / 取消",
                                type="button",
                                class_name="px-4 py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-200 text-xs font-bold transition-all cursor-pointer",
                            ),
                        ),
                        rx.el.button(
                            rx.icon("check", size=13, class_name="mr-1.5"),
                            "Save Changes / 保存修改",
                            type="submit",
                            class_name="flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-indigo-500/25 transition-all cursor-pointer",
                        ),
                        class_name="flex items-center justify-end gap-2 pt-4 border-t border-white/5",
                    ),
                    on_submit=AdminState.submit_edit_user,
                    reset_on_submit=False,
                    class_name="p-5",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-md rounded-2xl bg-slate-900/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/60 z-50 overflow-hidden",
            ),
        ),
        open=AdminState.edit_dialog_open,
        on_open_change=AdminState.set_edit_dialog_open,
    )


def overview_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Dashboard Overview / 系统运行总览",
                class_name="text-xl font-extrabold text-white tracking-tight mb-1",
            ),
            rx.el.p(
                "Real-time cluster infrastructure and business parameters.",
                class_name="text-xs text-slate-400 font-medium",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.foreach(AdminState.stats, _stat_card),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6",
        ),
        # Secondary visual block
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Node Clusters Health / 节点可用性概览",
                        class_name="text-xs text-slate-400 font-bold uppercase tracking-wider mb-3",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "🇭🇰 HK-BGP-Pro",
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            rx.el.span(
                                "99.98% SLA",
                                class_name="text-xs text-emerald-400 font-bold font-mono ml-auto",
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "🇯🇵 JP-Direct-Tokyo",
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            rx.el.span(
                                "100.0% SLA",
                                class_name="text-xs text-emerald-400 font-bold font-mono ml-auto",
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "🇺🇸 US-West-LosAngeles",
                                class_name="text-xs text-slate-200 font-semibold",
                            ),
                            rx.el.span(
                                "99.95% SLA",
                                class_name="text-xs text-emerald-400 font-bold font-mono ml-auto",
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="space-y-2.5",
                    ),
                    class_name="p-5 rounded-xl bg-slate-900/50 border border-white/5",
                ),
                class_name="lg:col-span-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Quick System Bulletins / 系统置顶公告",
                        class_name="text-xs text-slate-400 font-bold uppercase tracking-wider mb-3",
                    ),
                    rx.el.p(
                        "1. The deployment pipeline for native IP has been scaled to ensure Under-60s provisioning standard.",
                        class_name="text-xs text-slate-300 leading-relaxed mb-2",
                    ),
                    rx.el.p(
                        "2. Upcoming network maintenance schedule in the MO BroadCast HK segment on Nov 15.",
                        class_name="text-xs text-slate-300 leading-relaxed",
                    ),
                    class_name="p-5 rounded-xl bg-slate-900/50 border border-white/5",
                ),
                class_name="lg:col-span-2",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4",
        ),
        class_name="animate-fadeIn",
    )


def users_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "User Management / 用户权限控制",
                    class_name="text-xl font-extrabold text-white tracking-tight mb-1",
                ),
                rx.el.p(
                    "Search and inspect global registered profiles and client ranks.",
                    class_name="text-xs text-slate-400 font-medium",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        size=14,
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                    ),
                    rx.el.input(
                        placeholder="Filter username or emails... / 搜索用户或邮箱",
                        default_value=AdminState.search_query,
                        on_change=AdminState.set_search_query.debounce(400),
                        class_name="w-64 pl-9 pr-4 py-1.5 bg-slate-900/80 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-xs",
                    ),
                    class_name="relative",
                ),
                class_name="ml-auto",
            ),
            class_name="flex flex-col md:flex-row md:items-center gap-4 mb-6 pb-6 border-b border-white/5",
        ),
        _admin_users_stats(),
        rx.el.div(
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "ID",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Name / 用户名",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Email / 注册邮箱",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Role / 角色",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Status / 状态",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                            rx.el.th(
                                "Actions / 操作",
                                class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                            ),
                        ),
                        class_name="bg-white/[0.02] border-b border-white/10",
                    ),
                    rx.el.tbody(
                        rx.foreach(AdminState.filtered_users, _user_row)
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="overflow-x-auto",
            ),
            class_name="rounded-xl bg-slate-900/50 border border-white/5 overflow-hidden",
        ),
        _edit_user_dialog(),
        class_name="animate-fadeIn",
    )


def settings_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Global System Settings / 系统变量设置",
                class_name="text-xl font-extrabold text-white tracking-tight mb-1",
            ),
            rx.el.p(
                "Adjust central routing policies, stock overrides and automated triggers.",
                class_name="text-xs text-slate-400 font-medium",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Gateway & Backends / 网关与路由网卡",
                    class_name="text-xs text-slate-400 font-bold uppercase tracking-wider mb-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Default Port Standard",
                            class_name="text-xs text-slate-200 font-semibold block mb-1",
                        ),
                        rx.el.input(
                            default_value="22",
                            disabled=True,
                            class_name="w-full px-3 py-2 bg-slate-900/60 text-slate-400 rounded-lg border border-white/10 text-xs",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "Automatic Sync Interval",
                            class_name="text-xs text-slate-200 font-semibold block mb-1",
                        ),
                        rx.el.input(
                            default_value="5s",
                            disabled=True,
                            class_name="w-full px-3 py-2 bg-slate-900/60 text-slate-400 rounded-lg border border-white/10 text-xs",
                        ),
                        class_name="flex-1",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                ),
                class_name="p-6 rounded-xl bg-slate-900/50 border border-white/5 mb-4",
            ),
            rx.el.div(
                rx.el.p(
                    "Security Parameters / 安全核心防线",
                    class_name="text-xs text-slate-400 font-bold uppercase tracking-wider mb-3",
                ),
                rx.el.p(
                    "DDoS Scrubbing trigger threshold is permanently bound to 200 Gbps global backbone pipelines. Auto ban rate limited ips after 40 consecutive requests in 10s.",
                    class_name="text-xs text-slate-300 leading-relaxed",
                ),
                class_name="p-6 rounded-xl bg-slate-900/50 border border-white/5",
            ),
            class_name="max-w-3xl",
        ),
        class_name="animate-fadeIn",
    )
