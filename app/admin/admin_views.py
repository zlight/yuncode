import reflex as rx
from app.admin.admin_state import AdminState
from app.states.language_state import LanguageState
from app.components.ui_styles import style_badge


def _kv_row(label, value) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            label,
            class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold",
        ),
        rx.el.p(
            value,
            class_name="text-xs text-white font-semibold font-mono mt-1 truncate",
        ),
        class_name="rounded-lg bg-white/[0.02] border border-white/5 p-3",
    )


def _detail_section(title, icon: str, body) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=13, class_name="text-cyan-300"),
            rx.el.span(title, class_name="text-xs text-white font-bold ml-1.5"),
            class_name="flex items-center mb-3",
        ),
        body,
        class_name="mb-4",
    )


def _server_details_dialog() -> rx.Component:
    srv = AdminState.detail_server
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/60 backdrop-blur-sm z-40",
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(srv["region_flag"], class_name="text-3xl"),
                        class_name="w-14 h-14 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.title(
                            srv["name"],
                            class_name="text-lg font-extrabold text-white tracking-tight",
                        ),
                        rx.el.div(
                            rx.el.span(
                                srv["id"],
                                class_name="text-xs text-cyan-300 font-mono font-bold",
                            ),
                            rx.el.span(
                                "·",
                                class_name="text-slate-600 mx-2",
                            ),
                            rx.el.span(
                                srv["region"],
                                class_name="text-xs text-slate-300",
                            ),
                            rx.el.span(
                                "·",
                                class_name="text-slate-600 mx-2",
                            ),
                            _server_status_badge(srv["status"]),
                            class_name="flex items-center flex-wrap mt-1",
                        ),
                        rx.radix.primitives.dialog.description(
                            "Full server operational profile / 完整服务器运营档案",
                            class_name="text-[11px] text-slate-500 font-medium mt-1",
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
                            class_name="w-8 h-8 rounded-lg hover:bg-white/5 flex items-center justify-center cursor-pointer transition-all shrink-0",
                        ),
                    ),
                    class_name="flex items-start gap-3 p-5 border-b border-white/5",
                ),
                rx.el.div(
                    _detail_section(
                        "Basic Information / 基础信息",
                        "info",
                        rx.el.div(
                            _kv_row("Instance ID", srv["id"]),
                            _kv_row("Instance Name", srv["name"]),
                            _kv_row("Owner", srv["owner_email"]),
                            _kv_row("Node", srv["node"]),
                            _kv_row("Region", srv["region"]),
                            _kv_row("Created", srv["created"]),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
                        ),
                    ),
                    _detail_section(
                        "Resource Configuration / 资源配置",
                        "cpu",
                        rx.el.div(
                            _kv_row("CPU", srv["cpu"]),
                            _kv_row("Memory", srv["ram"]),
                            _kv_row("Disk", srv["disk"]),
                            _kv_row("Bandwidth", srv["bandwidth"]),
                            _kv_row("OS", srv["os"]),
                            _kv_row("Spec", srv["spec"]),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
                        ),
                    ),
                    _detail_section(
                        "Network Information / 网络信息",
                        "network",
                        rx.el.div(
                            _kv_row("IPv4", srv["ip"]),
                            _kv_row("Node Route", srv["node"]),
                            _kv_row("Bandwidth Cap", srv["bandwidth"]),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
                        ),
                    ),
                    _detail_section(
                        "Billing Information / 计费信息",
                        "wallet",
                        rx.el.div(
                            _kv_row("Price", srv["price"]),
                            _kv_row("Expires", srv["expires"]),
                            _kv_row(
                                "Days Left",
                                srv["days_left"].to_string() + " days",
                            ),
                            _kv_row(
                                "Auto Renew",
                                rx.cond(
                                    srv["auto_renew"], "Enabled", "Disabled"
                                ),
                            ),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-2",
                        ),
                    ),
                    class_name="p-5 max-h-[65vh] overflow-y-auto",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("rotate-cw", size=12, class_name="mr-1.5"),
                        "Restart",
                        on_click=lambda: AdminState.restart_server(
                            srv["id"].to(str)
                        ),
                        class_name="flex items-center px-3 py-1.5 rounded-md bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 text-[11px] text-cyan-300 font-bold transition-all cursor-pointer",
                    ),
                    rx.el.button(
                        rx.icon("refresh-cw", size=12, class_name="mr-1.5"),
                        "Renew +30d",
                        on_click=lambda: AdminState.renew_server(
                            srv["id"].to(str)
                        ),
                        class_name="flex items-center px-3 py-1.5 rounded-md bg-orange-500/10 hover:bg-orange-500/20 border border-orange-500/30 text-[11px] text-orange-300 font-bold transition-all cursor-pointer",
                    ),
                    rx.cond(
                        srv["status"] == "Suspended",
                        rx.el.button(
                            rx.icon("lock_open", size=12, class_name="mr-1.5"),
                            "Unlock",
                            on_click=lambda: AdminState.unsuspend_server(
                                srv["id"].to(str)
                            ),
                            class_name="flex items-center px-3 py-1.5 rounded-md bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-[11px] text-emerald-300 font-bold transition-all cursor-pointer",
                        ),
                        rx.el.button(
                            rx.icon("ban", size=12, class_name="mr-1.5"),
                            "Suspend",
                            on_click=lambda: AdminState.suspend_server(
                                srv["id"].to(str)
                            ),
                            class_name="flex items-center px-3 py-1.5 rounded-md bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-[11px] text-rose-300 font-bold transition-all cursor-pointer",
                        ),
                    ),
                    rx.el.button(
                        rx.icon("pencil", size=12, class_name="mr-1.5"),
                        "Edit",
                        on_click=lambda: AdminState.open_edit_server(
                            srv["id"].to(str)
                        ),
                        class_name="ml-auto flex items-center px-3 py-1.5 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-[11px] font-bold shadow-lg shadow-indigo-500/25 transition-all cursor-pointer",
                    ),
                    class_name="flex flex-wrap items-center gap-2 p-4 border-t border-white/5 bg-white/[0.02]",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-3xl rounded-2xl bg-slate-900/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/60 z-50 overflow-hidden",
            ),
        ),
        open=AdminState.detail_dialog_open,
        on_open_change=AdminState.set_detail_dialog_open,
    )


def _edit_server_dialog() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.portal(
            rx.radix.primitives.dialog.overlay(
                class_name="fixed inset-0 bg-black/60 backdrop-blur-sm z-40",
            ),
            rx.radix.primitives.dialog.content(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "server-cog",
                            size=18,
                            class_name="text-cyan-300",
                        ),
                        class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center shrink-0",
                    ),
                    rx.el.div(
                        rx.radix.primitives.dialog.title(
                            "Edit Server / 编辑服务器",
                            class_name="text-base font-extrabold text-white tracking-tight",
                        ),
                        rx.radix.primitives.dialog.description(
                            "Modify instance name, owner, status, expiration and auto-renew. / 修改实例名称、所属用户、状态、到期时间与自动续费。",
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
                            "Instance ID / 实例 ID",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.p(
                            AdminState.edit_server_id,
                            class_name="text-xs text-cyan-300 font-mono font-bold",
                        ),
                        class_name="flex flex-col mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Name / 名称",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.input(
                            name="name",
                            type="text",
                            default_value=AdminState.edit_server_name,
                            key=AdminState.edit_server_id + "-name",
                            required=True,
                            class_name="w-full px-3 py-2 bg-slate-950/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm font-mono",
                        ),
                        class_name="flex flex-col mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Owner Email / 所属用户邮箱",
                            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                        ),
                        rx.el.input(
                            name="owner_email",
                            type="email",
                            default_value=AdminState.edit_server_owner,
                            key=AdminState.edit_server_id + "-owner",
                            required=True,
                            class_name="w-full px-3 py-2 bg-slate-950/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm font-mono",
                        ),
                        class_name="flex flex-col mb-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Status / 状态",
                                class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                            ),
                            rx.el.div(
                                rx.el.select(
                                    rx.el.option("Running", value="Running"),
                                    rx.el.option("Stopped", value="Stopped"),
                                    rx.el.option(
                                        "Suspended", value="Suspended"
                                    ),
                                    name="status",
                                    default_value=AdminState.edit_server_status,
                                    key=AdminState.edit_server_id + "-status",
                                    on_change=AdminState.set_edit_server_status,
                                    class_name="appearance-none w-full pl-3 pr-9 py-2 bg-slate-950/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-sm cursor-pointer font-semibold",
                                ),
                                rx.icon(
                                    "chevron-down",
                                    size=12,
                                    class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                                ),
                                class_name="relative",
                            ),
                            class_name="flex flex-col flex-1",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Expires / 到期时间",
                                class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1.5",
                            ),
                            rx.el.input(
                                name="expires",
                                type="date",
                                default_value=AdminState.edit_server_expires,
                                key=AdminState.edit_server_id + "-expires",
                                required=True,
                                class_name="w-full px-3 py-2 bg-slate-950/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm font-mono",
                            ),
                            class_name="flex flex-col flex-1",
                        ),
                        class_name="flex gap-3 mb-4",
                    ),
                    rx.el.label(
                        rx.el.input(
                            type="checkbox",
                            name="auto_renew",
                            default_checked=AdminState.edit_server_auto_renew,
                            class_name="rounded border-white/20 bg-slate-900 text-cyan-500 focus:ring-cyan-500/30 mr-2 size-4",
                        ),
                        rx.el.span(
                            "Enable auto-renewal / 启用自动续费",
                            class_name="text-xs text-white font-semibold",
                        ),
                        class_name="flex items-center cursor-pointer p-2 rounded-lg hover:bg-white/5 mb-6",
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
                    on_submit=AdminState.submit_edit_server,
                    reset_on_submit=False,
                    class_name="p-5",
                ),
                class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-xl rounded-2xl bg-slate-900/95 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/60 z-50 overflow-hidden",
            ),
        ),
        open=AdminState.edit_server_dialog_open,
        on_open_change=AdminState.set_edit_server_dialog_open,
    )


def _op_log_row(log: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                log["action_icon"],
                size=13,
                class_name=rx.match(
                    log["action_color"],
                    ("emerald", "text-emerald-300"),
                    ("cyan", "text-cyan-300"),
                    ("rose", "text-rose-300"),
                    ("amber", "text-amber-300"),
                    ("orange", "text-orange-300"),
                    ("violet", "text-violet-300"),
                    "text-slate-300",
                ),
            ),
            class_name=rx.match(
                log["action_color"],
                (
                    "emerald",
                    "w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "cyan",
                    "w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "rose",
                    "w-8 h-8 rounded-lg bg-rose-500/10 border border-rose-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "amber",
                    "w-8 h-8 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "orange",
                    "w-8 h-8 rounded-lg bg-orange-500/10 border border-orange-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "violet",
                    "w-8 h-8 rounded-lg bg-violet-500/10 border border-violet-500/30 flex items-center justify-center shrink-0",
                ),
                "w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center shrink-0",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    log["action"],
                    class_name="text-xs text-white font-bold",
                ),
                rx.el.span(
                    "·",
                    class_name="text-slate-600 mx-1.5",
                ),
                rx.el.span(
                    log["instance_name"],
                    class_name="text-[11px] text-cyan-300 font-mono font-bold",
                ),
                rx.el.span(
                    "(" + log["instance_id"] + ")",
                    class_name="text-[10px] text-slate-500 font-mono ml-1",
                ),
                class_name="flex items-center flex-wrap",
            ),
            rx.el.div(
                rx.icon("user", size=10, class_name="text-slate-500 mr-1"),
                rx.el.span(
                    log["operator"],
                    class_name="text-[10px] text-slate-400 font-medium",
                ),
                rx.el.span(
                    "·",
                    class_name="text-slate-600 mx-1.5",
                ),
                rx.icon("clock", size=10, class_name="text-slate-500 mr-1"),
                rx.el.span(
                    log["timestamp"],
                    class_name="text-[10px] text-slate-400 font-mono",
                ),
                class_name="flex items-center mt-1",
            ),
            class_name="flex-1 min-w-0 ml-3",
        ),
        rx.el.span(
            log["result"],
            class_name=rx.cond(
                log["result"] == "success",
                "inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30 shrink-0 uppercase",
                "inline-flex items-center text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded-full border border-rose-500/30 shrink-0 uppercase",
            ),
        ),
        class_name="flex items-center px-3 py-2.5 rounded-lg bg-white/[0.02] border border-white/5 hover:border-white/10 transition-all",
    )


def _operation_logs_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("history", size=13, class_name="text-cyan-300"),
                rx.el.span(
                    "Operation Logs / 操作日志",
                    class_name="text-xs text-white font-bold ml-1.5",
                ),
                class_name="flex items-center",
            ),
            rx.el.span(
                AdminState.operation_logs.length().to_string() + " entries",
                class_name="ml-auto text-[10px] font-bold text-slate-400 bg-white/5 px-2 py-0.5 rounded border border-white/10",
            ),
            class_name="flex items-center px-4 py-3 border-b border-white/5 bg-white/[0.02]",
        ),
        rx.el.div(
            rx.cond(
                AdminState.operation_logs.length() > 0,
                rx.el.div(
                    rx.foreach(AdminState.recent_operation_logs, _op_log_row),
                    class_name="flex flex-col gap-2",
                ),
                rx.el.div(
                    rx.icon(
                        "inbox",
                        size=24,
                        class_name="text-slate-500 mx-auto mb-2",
                    ),
                    rx.el.p(
                        "No operations recorded yet / 暂无操作记录",
                        class_name="text-xs text-slate-400 text-center font-medium",
                    ),
                    class_name="py-8",
                ),
            ),
            class_name="p-4 max-h-[500px] overflow-y-auto",
        ),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden mt-6",
    )


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


def _server_status_badge(status: rx.Var) -> rx.Component:
    return rx.match(
        status,
        (
            "Running",
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                ),
                "Running / 运行中",
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30 w-fit",
            ),
        ),
        (
            "Stopped",
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-slate-400 mr-1.5"
                ),
                "Stopped / 已停止",
                class_name="inline-flex items-center text-[10px] font-bold text-slate-300 bg-slate-500/10 px-2 py-0.5 rounded-full border border-slate-500/30 w-fit",
            ),
        ),
        (
            "Suspended",
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-rose-400 mr-1.5"
                ),
                "Suspended / 已封禁",
                class_name="inline-flex items-center text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded-full border border-rose-500/30 w-fit",
            ),
        ),
        rx.el.span(
            status,
            class_name="inline-flex items-center text-[10px] font-bold text-slate-300 bg-white/5 px-2 py-0.5 rounded-full border border-white/10 w-fit",
        ),
    )


def _expiry_cell(srv: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            srv["expires"],
            class_name="text-slate-300 font-mono text-xs",
        ),
        rx.cond(
            srv["days_left"] <= 0,
            rx.el.span(
                "Expired / 已过期",
                class_name="text-[9px] font-bold text-rose-300 bg-rose-500/10 px-1.5 py-0.5 rounded border border-rose-500/30 mt-1 inline-block w-fit",
            ),
            rx.cond(
                srv["days_left"] <= 15,
                rx.el.span(
                    srv["days_left"].to_string() + "d left / 天到期",
                    class_name="text-[9px] font-bold text-amber-300 bg-amber-500/10 px-1.5 py-0.5 rounded border border-amber-500/30 mt-1 inline-block w-fit",
                ),
                rx.el.span(
                    srv["days_left"].to_string() + "d",
                    class_name="text-[9px] font-medium text-slate-500 mt-1 inline-block",
                ),
            ),
        ),
        class_name="flex flex-col",
    )


def _admin_servers_row(srv: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(
                    srv["id"],
                    class_name="text-cyan-300 font-mono text-[11px] font-bold block truncate",
                ),
                rx.el.span(
                    srv["node"],
                    class_name="text-[9px] font-bold text-slate-500 uppercase tracking-widest",
                ),
                class_name="flex flex-col min-w-0",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon(
                    "server", size=13, class_name="text-slate-500 shrink-0"
                ),
                rx.el.span(
                    srv["name"],
                    class_name="text-white font-semibold text-sm ml-2",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon("mail", size=12, class_name="text-slate-500 shrink-0"),
                rx.el.span(
                    srv["owner_email"],
                    class_name="text-slate-300 font-mono text-xs ml-1.5",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.span(srv["region_flag"], class_name="text-lg"),
                rx.el.span(
                    srv["region"],
                    class_name="text-slate-200 font-medium text-xs ml-1.5",
                ),
                class_name="flex items-center",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(
                srv["spec"],
                class_name="text-slate-300 font-mono text-[11px]",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(
                srv["price"],
                class_name="text-cyan-300 font-bold font-mono text-xs",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            _server_status_badge(srv["status"]),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            _expiry_cell(srv),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.div(
                rx.cond(
                    srv["status"] == "Running",
                    rx.el.button(
                        rx.icon("power", size=11, class_name="mr-1"),
                        "Stop",
                        on_click=lambda: AdminState.toggle_server_status(
                            srv["id"].to(str)
                        ),
                        title="Stop / 停止",
                        class_name="flex items-center px-2 py-1 rounded bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-[10px] text-amber-300 font-bold transition-all cursor-pointer",
                    ),
                    rx.el.button(
                        rx.icon("play", size=11, class_name="mr-1"),
                        "Start",
                        on_click=lambda: AdminState.toggle_server_status(
                            srv["id"].to(str)
                        ),
                        title="Start / 启动",
                        class_name="flex items-center px-2 py-1 rounded bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-[10px] text-emerald-300 font-bold transition-all cursor-pointer",
                    ),
                ),
                rx.el.button(
                    rx.icon("rotate-cw", size=11),
                    on_click=lambda: AdminState.restart_server(
                        srv["id"].to(str)
                    ),
                    title="Restart / 重启",
                    class_name="flex items-center justify-center w-7 h-7 rounded bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 text-cyan-300 transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("refresh-cw", size=11),
                    on_click=lambda: AdminState.renew_server(srv["id"].to(str)),
                    title="Renew / 续费",
                    class_name="flex items-center justify-center w-7 h-7 rounded bg-orange-500/10 hover:bg-orange-500/20 border border-orange-500/30 text-orange-300 transition-all cursor-pointer",
                ),
                rx.cond(
                    srv["status"] == "Suspended",
                    rx.el.button(
                        rx.icon("lock_open", size=11),
                        on_click=lambda: AdminState.unsuspend_server(
                            srv["id"].to(str)
                        ),
                        title="Unlock / 解封",
                        class_name="flex items-center justify-center w-7 h-7 rounded bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 transition-all cursor-pointer",
                    ),
                    rx.el.button(
                        rx.icon("ban", size=11),
                        on_click=lambda: AdminState.suspend_server(
                            srv["id"].to(str)
                        ),
                        title="Suspend / 封禁",
                        class_name="flex items-center justify-center w-7 h-7 rounded bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-rose-300 transition-all cursor-pointer",
                    ),
                ),
                rx.el.button(
                    rx.icon("pencil", size=11),
                    on_click=lambda: AdminState.open_edit_server(
                        srv["id"].to(str)
                    ),
                    title="Edit / 编辑",
                    class_name="flex items-center justify-center w-7 h-7 rounded bg-violet-500/10 hover:bg-violet-500/20 border border-violet-500/30 text-violet-300 transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("eye", size=11),
                    on_click=lambda: AdminState.open_server_details(
                        srv["id"].to(str)
                    ),
                    title="Details / 详情",
                    class_name="flex items-center justify-center w-7 h-7 rounded bg-cyan-500/10 hover:bg-cyan-500/20 border border-cyan-500/30 text-cyan-300 transition-all cursor-pointer",
                ),
                class_name="flex items-center gap-1.5 flex-wrap",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        class_name="hover:bg-white/[0.01] transition-colors",
    )


def _server_stat_card(
    icon: str, title_en: str, title_zh: str, value: str, sub: str, accent: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    f"{title_en} / {title_zh}",
                    class_name="text-xs text-slate-400 font-semibold uppercase tracking-wider",
                ),
                rx.el.p(
                    value,
                    class_name="text-3xl font-extrabold text-white tracking-tight leading-none mt-2",
                ),
                rx.el.p(
                    sub,
                    class_name="text-[11px] text-slate-500 font-medium mt-1",
                ),
                class_name="flex flex-col",
            ),
            rx.el.div(
                rx.icon(icon, size=18, class_name=f"text-{accent}-300"),
                class_name=f"w-10 h-10 rounded-lg bg-{accent}-500/10 border border-{accent}-500/30 flex items-center justify-center shrink-0",
            ),
            class_name="flex items-start justify-between",
        ),
        class_name=f"rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-{accent}-500/30 transition-all",
    )


def _server_stats_grid() -> rx.Component:
    return rx.el.div(
        _server_stat_card(
            "activity",
            "Running",
            "运行中",
            AdminState.running_count.to_string(),
            "Instances active now / 当前正在运行",
            "emerald",
        ),
        _server_stat_card(
            "power-off",
            "Stopped / Suspended",
            "已停止/封禁",
            AdminState.stopped_count.to_string(),
            "Idle or restricted / 空闲或受限",
            "rose",
        ),
        _server_stat_card(
            "clock",
            "Expiring Soon",
            "即将到期",
            AdminState.expiring_count.to_string(),
            "≤ 15 days remaining / 15 天内",
            "amber",
        ),
        _server_stat_card(
            "wallet",
            "Monthly Revenue",
            "月收入",
            AdminState.monthly_revenue_display,
            "From active servers / 来自运行中",
            "cyan",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 mb-6",
    )


def _region_option(region: rx.Var) -> rx.Component:
    return rx.el.option(region, value=region)


def _servers_filter_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "search",
                size=14,
                class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
            ),
            rx.el.input(
                placeholder="Search by name, ID, email, region... / 搜索实例名/ID/邮箱/地区",
                default_value=AdminState.server_search,
                on_change=AdminState.set_server_search.debounce(300),
                class_name="w-full min-w-[280px] pl-9 pr-4 py-2 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-xs",
            ),
            class_name="relative flex-1 min-w-0",
        ),
        rx.el.div(
            rx.el.select(
                rx.el.option("All Regions / 全部地区", value="all"),
                rx.foreach(AdminState.server_region_options, _region_option),
                default_value=AdminState.server_region_filter,
                key=AdminState.server_region_filter,
                on_change=AdminState.set_server_region_filter,
                class_name="appearance-none pl-8 pr-9 py-2 bg-slate-900/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-xs cursor-pointer font-semibold",
            ),
            rx.icon(
                "globe",
                size=12,
                class_name="absolute left-2.5 top-1/2 -translate-y-1/2 text-cyan-300 pointer-events-none",
            ),
            rx.icon(
                "chevron-down",
                size=12,
                class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.select(
                rx.el.option("All Status / 全部状态", value="all"),
                rx.el.option("Running / 运行中", value="Running"),
                rx.el.option("Stopped / 已停止", value="Stopped"),
                rx.el.option("Suspended / 已封禁", value="Suspended"),
                default_value=AdminState.server_status_filter,
                key=AdminState.server_status_filter,
                on_change=AdminState.set_server_status_filter,
                class_name="appearance-none pl-8 pr-9 py-2 bg-slate-900/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-xs cursor-pointer font-semibold",
            ),
            rx.icon(
                "activity",
                size=12,
                class_name="absolute left-2.5 top-1/2 -translate-y-1/2 text-emerald-300 pointer-events-none",
            ),
            rx.icon(
                "chevron-down",
                size=12,
                class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.select(
                rx.el.option("Expires ↑ / 到期近→远", value="expires-asc"),
                rx.el.option("Expires ↓ / 到期远→近", value="expires-desc"),
                rx.el.option("Price ↑ / 价格低→高", value="price-asc"),
                rx.el.option("Price ↓ / 价格高→低", value="price-desc"),
                rx.el.option("Name / 名称", value="name"),
                default_value=AdminState.server_sort_by,
                key=AdminState.server_sort_by,
                on_change=AdminState.set_server_sort,
                class_name="appearance-none pl-8 pr-9 py-2 bg-slate-900/60 text-white rounded-lg border border-white/10 focus:border-cyan-500/50 focus:outline-hidden text-xs cursor-pointer font-semibold",
            ),
            rx.icon(
                "arrow-up-down",
                size=12,
                class_name="absolute left-2.5 top-1/2 -translate-y-1/2 text-violet-300 pointer-events-none",
            ),
            rx.icon(
                "chevron-down",
                size=12,
                class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
            ),
            class_name="relative",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", size=12, class_name="mr-1"),
            "Reset / 重置",
            on_click=AdminState.reset_server_filters,
            class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-cyan-500/30 text-xs text-slate-300 font-semibold transition-all cursor-pointer",
        ),
        class_name="flex flex-wrap items-center gap-3 mb-4",
    )


def _servers_result_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2 shadow-lg shadow-emerald-400/50"
            ),
            rx.el.span(
                AdminState.filtered_servers_count.to_string()
                + " / "
                + AdminState.total_servers.to_string()
                + " servers",
                class_name="text-xs text-slate-200 font-semibold",
            ),
            class_name="inline-flex items-center px-3 py-1.5 rounded-full bg-white/5 border border-white/10",
        ),
        rx.cond(
            AdminState.servers_has_active_filter,
            rx.el.div(
                rx.icon("filter", size=11, class_name="text-cyan-300 mr-1.5"),
                rx.el.span(
                    "Filters applied / 已应用筛选",
                    class_name="text-xs text-cyan-200 font-semibold",
                ),
                class_name="inline-flex items-center px-3 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 ml-2",
            ),
            rx.fragment(),
        ),
        class_name="flex items-center mb-3",
    )


def _servers_no_results() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search-x", size=32, class_name="text-slate-500"),
            class_name="w-16 h-16 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            "No servers matching your filters / 没有匹配的服务器",
            class_name="text-white font-bold text-base mb-1 text-center",
        ),
        rx.el.p(
            "Try adjusting your search, region, or status filters. / 请尝试调整搜索、地区或状态筛选。",
            class_name="text-sm text-slate-400 mb-4 font-medium text-center max-w-md mx-auto",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("rotate-ccw", size=12, class_name="mr-1"),
                "Reset filters / 重置筛选",
                on_click=AdminState.reset_server_filters,
                class_name="inline-flex items-center px-4 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold transition-all cursor-pointer shadow-lg shadow-indigo-500/20",
            ),
            class_name="flex items-center justify-center",
        ),
        class_name="text-center py-16 rounded-xl bg-slate-900/40 border border-dashed border-white/10",
    )


def _servers_empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("server-off", size=32, class_name="text-cyan-300"),
            class_name="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            "No cloud servers registered / 尚无云服务器实例",
            class_name="text-white font-bold text-lg mb-1 text-center",
        ),
        rx.el.p(
            "Once users purchase servers, they will appear here for management. / 用户购买服务器后将显示于此处以供管理。",
            class_name="text-sm text-slate-400 font-medium text-center max-w-md mx-auto",
        ),
        class_name="text-center py-16 rounded-xl bg-slate-900/40 border border-dashed border-white/10",
    )


def servers_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Cloud Server Management / 云服务器管理",
                    class_name="text-xl font-extrabold text-white tracking-tight mb-1",
                ),
                rx.el.p(
                    "Inspect and orchestrate global cloud server instances across all registered user profiles. / 查看并管理所有已注册用户的全球云服务器实例。",
                    class_name="text-xs text-slate-400 font-medium",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("download", size=13, class_name="mr-1.5"),
                    "Export / 导出",
                    class_name="flex items-center px-3 py-2 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-xs text-slate-200 font-bold transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("plus", size=13, class_name="mr-1.5"),
                    "New Instance / 新建实例",
                    class_name="flex items-center px-3 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-indigo-500/25 transition-all cursor-pointer",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex flex-col md:flex-row md:items-center gap-4 mb-6 pb-6 border-b border-white/5",
        ),
        _server_stats_grid(),
        _servers_filter_bar(),
        _servers_result_bar(),
        rx.cond(
            AdminState.total_servers == 0,
            _servers_empty_state(),
            rx.cond(
                AdminState.filtered_servers_count == 0,
                _servers_no_results(),
                rx.el.div(
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Instance ID / 实例",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Server Name / 名称",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Owner / 所属用户",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Region / 地区",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Spec / 规格",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Price / 价格",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Status / 状态",
                                        class_name="px-6 py-3 text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider",
                                    ),
                                    rx.el.th(
                                        "Expires / 到期",
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
                                rx.foreach(
                                    AdminState.filtered_servers,
                                    _admin_servers_row,
                                )
                            ),
                            class_name="table-auto w-full",
                        ),
                        class_name="overflow-x-auto",
                    ),
                    class_name="rounded-xl bg-slate-900/50 border border-white/5 overflow-hidden",
                ),
            ),
        ),
        _operation_logs_card(),
        _server_details_dialog(),
        _edit_server_dialog(),
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
