import reflex as rx
from app.states.servers_state import ServersState
from app.states.language_state import LanguageState


TOOLTIP_PROPS = {
    "content_style": {
        "background": "rgba(15, 23, 42, 0.95)",
        "borderColor": "rgba(255,255,255,0.1)",
        "borderRadius": "0.5rem",
        "fontFamily": "Inter, sans-serif",
        "fontSize": "0.75rem",
        "fontWeight": "600",
        "padding": "0.5rem 0.75rem",
        "color": "#e2e8f0",
    },
    "item_style": {"color": "#e2e8f0"},
    "label_style": {"color": "#94a3b8", "fontWeight": "700"},
    "separator": " ",
}


def _card(
    title, icon: str, body, extra=None, accent: str = "cyan"
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(icon, size=13, class_name=f"text-{accent}-300"),
                rx.el.span(
                    title, class_name="text-xs text-white font-bold ml-1.5"
                ),
                class_name="flex items-center",
            ),
            rx.cond(extra != None, extra, rx.fragment()),
            class_name="flex items-center justify-between px-4 py-3 border-b border-white/5 bg-white/[0.02]",
        ),
        rx.el.div(body, class_name="p-4"),
        class_name="rounded-xl bg-slate-900/60 backdrop-blur-xl border border-white/5 overflow-hidden",
    )


def _progress_bar(pct: int, color: str = "cyan") -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name=f"h-full rounded-full bg-gradient-to-r from-indigo-500 to-{color}-400 shadow-lg shadow-{color}-500/30",
            style={"width": f"{pct}%"},
        ),
        class_name="h-2 bg-white/5 rounded-full overflow-hidden",
    )


# ============ DASHBOARD TAB ============
def dashboard_tab_content() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.el.div(
        rx.el.div(
            _card(
                rx.cond(LanguageState.is_zh, "CPU 占用", "CPU Usage"),
                "cpu",
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "42",
                            class_name="text-3xl text-white font-extrabold font-mono tracking-tight",
                        ),
                        rx.el.span(
                            "%", class_name="text-lg text-slate-400 ml-1"
                        ),
                        class_name="flex items-baseline mb-2",
                    ),
                    _progress_bar(42, "cyan"),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "1 核 · 平均负载 0.42",
                            "1 Core · Load avg 0.42",
                        ),
                        class_name="text-[11px] text-slate-500 mt-2 font-medium",
                    ),
                ),
                accent="cyan",
            ),
            _card(
                rx.cond(LanguageState.is_zh, "内存占用", "Memory Usage"),
                "memory-stick",
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "612",
                            class_name="text-3xl text-white font-extrabold font-mono tracking-tight",
                        ),
                        rx.el.span(
                            " / 1024 MB",
                            class_name="text-xs text-slate-400 ml-1",
                        ),
                        class_name="flex items-baseline mb-2",
                    ),
                    _progress_bar(60, "violet"),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "缓存 234 MB · 空闲 178 MB",
                            "Cache 234 MB · Free 178 MB",
                        ),
                        class_name="text-[11px] text-slate-500 mt-2 font-medium",
                    ),
                ),
                accent="violet",
            ),
            _card(
                rx.cond(LanguageState.is_zh, "实时网络", "Live Network"),
                "activity",
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "arrow-down",
                                size=11,
                                class_name="text-emerald-300",
                            ),
                            rx.el.span(
                                "▲ 8.4",
                                class_name="text-xl text-white font-extrabold font-mono ml-1",
                            ),
                            rx.el.span(
                                " Mbps",
                                class_name="text-[10px] text-slate-500 ml-1",
                            ),
                            class_name="flex items-baseline",
                        ),
                        rx.el.div(
                            rx.icon(
                                "arrow-up", size=11, class_name="text-cyan-300"
                            ),
                            rx.el.span(
                                "▼ 2.1",
                                class_name="text-xl text-white font-extrabold font-mono ml-1",
                            ),
                            rx.el.span(
                                " Mbps",
                                class_name="text-[10px] text-slate-500 ml-1",
                            ),
                            class_name="flex items-baseline",
                        ),
                        class_name="grid grid-cols-2 gap-2 mb-2",
                    ),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "峰值 24.6 Mbps · 上行 · 下行",
                            "Peak 24.6 Mbps · in/out",
                        ),
                        class_name="text-[11px] text-slate-500 mt-1 font-medium",
                    ),
                ),
                accent="emerald",
            ),
            _card(
                rx.cond(LanguageState.is_zh, "流量使用", "Traffic Usage"),
                "gauge",
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            inst["traffic_used"],
                            class_name="text-2xl text-white font-extrabold font-mono tracking-tight",
                        ),
                        rx.el.span(" / ", class_name="text-slate-500 mx-1"),
                        rx.el.span(
                            inst["traffic_total"],
                            class_name="text-xs text-slate-400 font-mono",
                        ),
                        class_name="flex items-baseline mb-2",
                    ),
                    _progress_bar(3, "orange"),
                    rx.el.p(
                        rx.cond(
                            LanguageState.is_zh,
                            "距重置还有 21 天",
                            "Resets in 21 days",
                        ),
                        class_name="text-[11px] text-slate-500 mt-2 font-medium",
                    ),
                ),
                accent="orange",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 mb-4",
        ),
        rx.el.div(
            _card(
                rx.cond(LanguageState.is_zh, "配置信息", "Configuration"),
                "settings",
                rx.el.div(
                    _config_item(
                        rx.cond(LanguageState.is_zh, "CPU", "CPU"),
                        inst["cpu"],
                        "cpu",
                    ),
                    _config_item(
                        rx.cond(LanguageState.is_zh, "内存", "Memory"),
                        inst["ram"],
                        "memory-stick",
                    ),
                    _config_item(
                        rx.cond(LanguageState.is_zh, "硬盘", "Disk"),
                        inst["disk"],
                        "hard-drive",
                    ),
                    _config_item(
                        rx.cond(LanguageState.is_zh, "带宽", "Bandwidth"),
                        inst["bandwidth"],
                        "gauge",
                    ),
                    _config_item(
                        rx.cond(LanguageState.is_zh, "系统", "OS"),
                        inst["os"],
                        "layers",
                    ),
                    _config_item(
                        rx.cond(LanguageState.is_zh, "创建时间", "Created"),
                        inst["created"],
                        "calendar",
                    ),
                    class_name="grid grid-cols-2 gap-3",
                ),
            ),
            _card(
                rx.cond(LanguageState.is_zh, "访问控制入口", "Access Control"),
                "shield",
                rx.el.div(
                    rx.el.button(
                        rx.icon(
                            "terminal", size=14, class_name="text-cyan-300"
                        ),
                        rx.el.div(
                            rx.el.p(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "SSH 终端",
                                    "SSH Terminal",
                                ),
                                class_name="text-xs text-white font-bold",
                            ),
                            rx.el.p(
                                "Port 22 · Enabled",
                                class_name="text-[10px] text-slate-500 font-mono",
                            ),
                            class_name="ml-2",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=12,
                            class_name="ml-auto text-slate-500",
                        ),
                        on_click=lambda: ServersState.set_manage_tab("access"),
                        class_name="w-full flex items-center px-3 py-2.5 rounded-lg bg-white/[0.02] border border-white/5 hover:border-cyan-500/40 hover:bg-cyan-500/5 transition-all cursor-pointer",
                    ),
                    rx.el.button(
                        rx.icon(
                            "shield", size=14, class_name="text-violet-300"
                        ),
                        rx.el.div(
                            rx.el.p(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "防火墙规则",
                                    "Firewall Rules",
                                ),
                                class_name="text-xs text-white font-bold",
                            ),
                            rx.el.p(
                                "7 rules · 6 active",
                                class_name="text-[10px] text-slate-500 font-mono",
                            ),
                            class_name="ml-2",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=12,
                            class_name="ml-auto text-slate-500",
                        ),
                        on_click=lambda: ServersState.set_manage_tab("access"),
                        class_name="w-full flex items-center px-3 py-2.5 rounded-lg bg-white/[0.02] border border-white/5 hover:border-violet-500/40 hover:bg-violet-500/5 transition-all cursor-pointer",
                    ),
                    rx.el.button(
                        rx.icon(
                            "key-round", size=14, class_name="text-emerald-300"
                        ),
                        rx.el.div(
                            rx.el.p(
                                rx.cond(
                                    LanguageState.is_zh, "SSH 密钥", "SSH Keys"
                                ),
                                class_name="text-xs text-white font-bold",
                            ),
                            rx.el.p(
                                "2 keys · rotated 12d ago",
                                class_name="text-[10px] text-slate-500 font-mono",
                            ),
                            class_name="ml-2",
                        ),
                        rx.icon(
                            "arrow-right",
                            size=12,
                            class_name="ml-auto text-slate-500",
                        ),
                        on_click=lambda: ServersState.set_manage_tab("access"),
                        class_name="w-full flex items-center px-3 py-2.5 rounded-lg bg-white/[0.02] border border-white/5 hover:border-emerald-500/40 hover:bg-emerald-500/5 transition-all cursor-pointer",
                    ),
                    class_name="flex flex-col gap-2",
                ),
                accent="violet",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        _card(
            rx.cond(LanguageState.is_zh, "控制台预览", "Console Preview"),
            "terminal",
            rx.el.div(
                rx.el.p(
                    "root@" + inst["name"] + ":~# uptime",
                    class_name="text-[11px] text-emerald-300 font-mono",
                ),
                rx.el.p(
                    " 20:48:15 up 47 days,  3:12,  1 user,  load average: 0.42, 0.31, 0.22",
                    class_name="text-[11px] text-slate-300 font-mono",
                ),
                rx.el.p(
                    "root@" + inst["name"] + ":~# df -h /",
                    class_name="text-[11px] text-emerald-300 font-mono mt-1",
                ),
                rx.el.p(
                    "Filesystem      Size  Used Avail Use% Mounted on",
                    class_name="text-[11px] text-slate-400 font-mono",
                ),
                rx.el.p(
                    "/dev/vda1        10G  3.4G  6.6G  34% /",
                    class_name="text-[11px] text-slate-300 font-mono",
                ),
                rx.el.p(
                    "root@" + inst["name"] + ":~# systemctl is-active nginx",
                    class_name="text-[11px] text-emerald-300 font-mono mt-1",
                ),
                rx.el.p(
                    "active",
                    class_name="text-[11px] text-emerald-400 font-mono",
                ),
                rx.el.p(
                    "root@" + inst["name"] + ":~# _",
                    class_name="text-[11px] text-emerald-300 font-mono mt-1 animate-pulse",
                ),
                class_name="p-4 bg-slate-950/70 rounded-lg font-mono",
            ),
            extra=rx.el.button(
                rx.icon("external-link", size=11, class_name="mr-1"),
                rx.cond(
                    LanguageState.is_zh, "打开完整终端", "Open full terminal"
                ),
                class_name="flex items-center px-2.5 py-1 rounded-md bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-[10px] font-bold hover:bg-cyan-500/20 transition-all cursor-pointer",
            ),
            accent="cyan",
        ),
    )


def _config_item(label, value, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=11, class_name="text-cyan-300"),
            rx.el.span(
                label,
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold ml-1.5",
            ),
            class_name="flex items-center mb-1",
        ),
        rx.el.p(
            value, class_name="text-xs text-white font-bold font-mono truncate"
        ),
        class_name="rounded-lg bg-white/[0.02] border border-white/5 p-3",
    )


# ============ ACCESS TAB ============
def _fw_row(rule) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                rule["action"],
                class_name=rx.cond(
                    rule["action"] == "ALLOW",
                    "inline-flex text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30",
                    "inline-flex text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30",
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rule["protocol"],
                class_name="text-xs text-slate-200 font-mono font-semibold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rule["port"],
                class_name="text-xs text-cyan-300 font-mono font-bold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rule["source"], class_name="text-xs text-slate-300 font-mono"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rule["desc"], class_name="text-xs text-slate-400 font-medium"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.button(
                rx.el.span(
                    rx.cond(
                        rule["enabled"],
                        rx.cond(LanguageState.is_zh, "启用", "Enabled"),
                        rx.cond(LanguageState.is_zh, "禁用", "Disabled"),
                    ),
                    class_name=rx.cond(
                        rule["enabled"],
                        "inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
                        "inline-flex items-center text-[10px] font-bold text-slate-400 bg-white/5 px-2 py-0.5 rounded-full border border-white/10",
                    ),
                ),
                on_click=lambda: ServersState.toggle_firewall_rule(
                    rule["id"].to(str)
                ),
                class_name="cursor-pointer",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.02] transition-colors",
    )


def access_tab_content() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.el.div(
        rx.el.div(
            _card(
                rx.cond(
                    LanguageState.is_zh, "SSH / RDP 访问", "SSH / RDP Access"
                ),
                "terminal",
                rx.el.div(
                    _kv(
                        "SSH",
                        "root@" + inst["ip"].to(str) + " -p 22",
                        "terminal",
                    ),
                    _kv(
                        rx.cond(LanguageState.is_zh, "认证方式", "Auth Method"),
                        "SSH Key + Password",
                        "key-round",
                    ),
                    _kv(
                        rx.cond(LanguageState.is_zh, "RDP 端口", "RDP Port"),
                        "3389 (disabled)",
                        "monitor",
                    ),
                    _kv(
                        rx.cond(LanguageState.is_zh, "Fail2ban", "Fail2ban"),
                        rx.cond(
                            LanguageState.is_zh,
                            "启用 · 3 次尝试封禁",
                            "Active · ban after 3 tries",
                        ),
                        "shield-check",
                    ),
                    class_name="flex flex-col gap-2",
                ),
                accent="cyan",
            ),
            _card(
                rx.cond(LanguageState.is_zh, "IP 白名单", "IP Whitelist"),
                "list-checks",
                rx.el.div(
                    _wl_row(
                        "192.168.1.100",
                        rx.cond(LanguageState.is_zh, "办公室", "Office"),
                    ),
                    _wl_row(
                        "103.28.201.42",
                        rx.cond(LanguageState.is_zh, "本机", "Self"),
                    ),
                    _wl_row(
                        "59.42.11.98",
                        rx.cond(
                            LanguageState.is_zh, "家庭网络", "Home network"
                        ),
                    ),
                    rx.el.button(
                        rx.icon("plus", size=12, class_name="mr-1"),
                        rx.cond(LanguageState.is_zh, "添加 IP", "Add IP"),
                        class_name="mt-2 w-full flex items-center justify-center px-3 py-2 rounded-lg border border-dashed border-white/10 hover:border-cyan-500/40 hover:bg-cyan-500/5 text-[11px] text-slate-300 hover:text-cyan-300 font-bold transition-all cursor-pointer",
                    ),
                    class_name="flex flex-col gap-1.5",
                ),
                accent="emerald",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        _card(
            rx.cond(LanguageState.is_zh, "防火墙规则", "Firewall Rules"),
            "shield",
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            _th(rx.cond(LanguageState.is_zh, "动作", "Action")),
                            _th(
                                rx.cond(LanguageState.is_zh, "协议", "Protocol")
                            ),
                            _th(rx.cond(LanguageState.is_zh, "端口", "Port")),
                            _th(rx.cond(LanguageState.is_zh, "来源", "Source")),
                            _th(
                                rx.cond(
                                    LanguageState.is_zh, "描述", "Description"
                                )
                            ),
                            _th(rx.cond(LanguageState.is_zh, "状态", "Status")),
                        ),
                        class_name="bg-white/[0.02] border-b border-white/10",
                    ),
                    rx.el.tbody(
                        rx.foreach(ServersState.firewall_rules, _fw_row)
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="overflow-x-auto -mx-4",
            ),
            extra=rx.el.div(
                rx.el.button(
                    rx.icon("plus", size=11, class_name="mr-1"),
                    rx.cond(LanguageState.is_zh, "新建规则", "Add Rule"),
                    class_name="flex items-center px-2.5 py-1 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-[10px] font-bold transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("upload", size=11, class_name="mr-1"),
                    rx.cond(LanguageState.is_zh, "导入模板", "Import"),
                    class_name="ml-2 flex items-center px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-slate-200 text-[10px] font-bold hover:bg-white/10 transition-all cursor-pointer",
                ),
                class_name="flex items-center",
            ),
            accent="violet",
        ),
        rx.el.div(
            _security_action(
                "shield-check",
                rx.cond(
                    LanguageState.is_zh, "重置 Root 密码", "Reset Root Password"
                ),
                "amber",
            ),
            _security_action(
                "key-round",
                rx.cond(
                    LanguageState.is_zh, "生成 SSH 密钥", "Generate SSH Key"
                ),
                "cyan",
            ),
            _security_action(
                "lock",
                rx.cond(LanguageState.is_zh, "启用 2FA", "Enable 2FA"),
                "violet",
            ),
            _security_action(
                "history",
                rx.cond(LanguageState.is_zh, "登录审计日志", "Audit Log"),
                "emerald",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4",
        ),
    )


def _kv(k, v, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=11, class_name="text-cyan-300"),
            rx.el.span(
                k,
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold ml-1.5",
            ),
            class_name="flex items-center mb-1",
        ),
        rx.el.p(
            v, class_name="text-xs text-white font-mono font-semibold truncate"
        ),
        class_name="rounded-lg bg-white/[0.02] border border-white/5 p-3",
    )


def _wl_row(ip: str, label) -> rx.Component:
    return rx.el.div(
        rx.icon("check", size=12, class_name="text-emerald-300 shrink-0"),
        rx.el.span(
            ip, class_name="text-xs text-white font-mono font-bold ml-2"
        ),
        rx.el.span(
            label, class_name="text-[10px] text-slate-500 font-medium ml-2"
        ),
        rx.el.button(
            rx.icon(
                "x", size=10, class_name="text-slate-500 hover:text-rose-300"
            ),
            class_name="ml-auto p-1 rounded hover:bg-rose-500/10 cursor-pointer",
        ),
        class_name="flex items-center px-2.5 py-1.5 rounded-md bg-white/[0.02] border border-white/5",
    )


def _security_action(icon: str, label, accent: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=14, class_name=f"text-{accent}-300"),
        rx.el.span(
            label, class_name="text-xs text-slate-100 font-semibold ml-2"
        ),
        class_name=f"flex items-center px-4 py-3 rounded-xl bg-slate-900/60 border border-white/5 hover:border-{accent}-500/40 hover:bg-{accent}-500/5 transition-all cursor-pointer",
    )


def _th(label) -> rx.Component:
    return rx.el.th(
        label,
        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-2.5",
    )


# ============ NETWORK TAB ============
def network_tab_content() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.el.div(
        rx.el.div(
            _kv(
                rx.cond(LanguageState.is_zh, "公网 IPv4", "Public IPv4"),
                inst["ip"],
                "globe",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "IPv6", "IPv6"),
                "2001:db8::1a2b:3c4d",
                "globe",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "网关", "Gateway"),
                "103.28.201.1",
                "route",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "子网掩码", "Netmask"),
                "255.255.255.0",
                "network",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "DNS 主", "Primary DNS"),
                "8.8.8.8",
                "server",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "DNS 备", "Secondary DNS"),
                "1.1.1.1",
                "server",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "MAC 地址", "MAC"),
                "00:1A:2B:3C:4D:5E",
                "wifi",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "MTU", "MTU"),
                "1500",
                "arrow-left-right",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4",
        ),
        rx.el.div(
            _card(
                rx.cond(
                    LanguageState.is_zh, "带宽 & 路由", "Bandwidth & Routing"
                ),
                "gauge",
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh, "总带宽", "Total Bandwidth"
                            ),
                            class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold",
                        ),
                        rx.el.p(
                            inst["bandwidth"],
                            class_name="text-2xl text-white font-extrabold font-mono tracking-tight mt-1",
                        ),
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "峰值 · 独享",
                                "Peak · Dedicated",
                            ),
                            class_name="text-[10px] text-emerald-300 font-bold mt-1",
                        ),
                        class_name="mb-4 pb-4 border-b border-white/5",
                    ),
                    rx.el.div(
                        _route_row("CN2 GIA · Premium", "12ms", "primary"),
                        _route_row("HKIX · Direct Peering", "18ms", "backup"),
                        _route_row("Cogent · Level3", "42ms", "backup"),
                        class_name="flex flex-col gap-2",
                    ),
                ),
                accent="cyan",
            ),
            _card(
                rx.cond(LanguageState.is_zh, "流量包", "Traffic Packages"),
                "package",
                rx.el.div(
                    _traffic_pack(
                        "Base 1500 GB/mo", "377.06 MB", 3, "included"
                    ),
                    _traffic_pack("Extra 500 GB · Sep", "0 MB", 0, "extra"),
                    _traffic_pack("Reset (¥20 each)", "-", 0, "reset"),
                    rx.el.button(
                        rx.icon("plus", size=12, class_name="mr-1"),
                        rx.cond(
                            LanguageState.is_zh,
                            "购买流量包",
                            "Buy Traffic Pack",
                        ),
                        class_name="w-full mt-2 flex items-center justify-center px-3 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 hover:brightness-110 text-white text-[11px] font-bold shadow-lg shadow-orange-500/20 transition-all cursor-pointer",
                    ),
                    class_name="flex flex-col gap-2",
                ),
                accent="orange",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        rx.el.div(
            _network_action(
                "refresh-cw",
                rx.cond(LanguageState.is_zh, "更换 IP", "Change IP"),
                "cyan",
            ),
            _network_action(
                "shield",
                rx.cond(LanguageState.is_zh, "启用高防", "Enable Anti-DDoS"),
                "violet",
            ),
            _network_action(
                "upload",
                rx.cond(LanguageState.is_zh, "带宽升级", "Upgrade BW"),
                "emerald",
            ),
            _network_action(
                "wifi",
                rx.cond(LanguageState.is_zh, "网络诊断", "Diagnose"),
                "amber",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3",
        ),
    )


def _route_row(name: str, latency: str, tag: str) -> rx.Component:
    return rx.el.div(
        rx.icon("route", size=12, class_name="text-cyan-300 shrink-0"),
        rx.el.span(name, class_name="text-xs text-white font-semibold ml-2"),
        rx.el.span(
            tag,
            class_name=rx.cond(
                tag == "primary",
                "ml-2 text-[9px] font-bold text-cyan-300 bg-cyan-500/10 px-1.5 py-0.5 rounded border border-cyan-500/30",
                "ml-2 text-[9px] font-bold text-slate-400 bg-white/5 px-1.5 py-0.5 rounded border border-white/10",
            ),
        ),
        rx.el.span(
            latency,
            class_name="ml-auto text-[11px] text-emerald-300 font-mono font-bold",
        ),
        class_name="flex items-center px-3 py-2 rounded-lg bg-white/[0.02] border border-white/5",
    )


def _traffic_pack(name: str, used: str, pct: int, kind: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(name, class_name="text-xs text-white font-semibold"),
            rx.el.span(
                used,
                class_name="ml-auto text-[11px] text-cyan-300 font-mono font-bold",
            ),
            class_name="flex items-center mb-1.5",
        ),
        _progress_bar(pct if pct > 0 else 1, "cyan"),
        class_name="rounded-lg bg-white/[0.02] border border-white/5 p-3",
    )


def _network_action(icon: str, label, accent: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=14, class_name=f"text-{accent}-300"),
        rx.el.span(
            label, class_name="text-xs text-slate-100 font-semibold ml-2"
        ),
        class_name=f"flex items-center px-4 py-3 rounded-xl bg-slate-900/60 border border-white/5 hover:border-{accent}-500/40 hover:bg-{accent}-500/5 transition-all cursor-pointer",
    )


# ============ BILLING TAB ============
def _bill_row(b) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                b["id"], class_name="text-xs text-cyan-300 font-mono font-bold"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                b["date"], class_name="text-xs text-slate-300 font-mono"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                b["item"], class_name="text-xs text-white font-semibold"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                b["cycle"], class_name="text-xs text-slate-400 font-medium"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                b["amount"],
                class_name="text-xs text-orange-300 font-mono font-bold",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                b["status"],
                class_name=rx.match(
                    b["status"],
                    (
                        "paid",
                        "inline-flex text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
                    ),
                    (
                        "refunded",
                        "inline-flex text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded-full border border-rose-500/30",
                    ),
                    "inline-flex text-[10px] font-bold text-slate-400 bg-white/5 px-2 py-0.5 rounded-full border border-white/10",
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon(
                    "download",
                    size=12,
                    class_name="text-slate-400 hover:text-cyan-300",
                ),
                class_name="p-1 rounded hover:bg-white/5 cursor-pointer",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.02] transition-colors",
    )


def billing_tab_content() -> rx.Component:
    inst = ServersState.selected_instance
    return rx.el.div(
        rx.el.div(
            _kv(
                rx.cond(LanguageState.is_zh, "当前套餐", "Current Plan"),
                inst["plan"],
                "package",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "月付价格", "Monthly Price"),
                inst["price"],
                "credit-card",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "到期时间", "Expires"),
                inst["expires"],
                "clock",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "自动续费", "Auto-renew"),
                rx.cond(
                    inst["auto_renew"],
                    rx.cond(LanguageState.is_zh, "已启用", "Enabled"),
                    rx.cond(LanguageState.is_zh, "已关闭", "Disabled"),
                ),
                "refresh-cw",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4",
        ),
        rx.el.div(
            _card(
                rx.cond(
                    LanguageState.is_zh, "续费 & 升级", "Renewal & Upgrade"
                ),
                "trending-up",
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh, "当月账单", "Current bill"
                            ),
                            class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "¥",
                                class_name="text-lg text-slate-500 font-bold",
                            ),
                            rx.el.span(
                                "42.49",
                                class_name="text-3xl text-white font-extrabold font-mono tracking-tight",
                            ),
                            rx.el.span(
                                rx.cond(LanguageState.is_zh, "/月", "/mo"),
                                class_name="text-xs text-slate-500 ml-1 font-semibold",
                            ),
                            class_name="flex items-baseline",
                        ),
                        rx.el.p(
                            rx.cond(
                                LanguageState.is_zh,
                                "下次扣款: 2025-11-01",
                                "Next charge: 2025-11-01",
                            ),
                            class_name="text-[11px] text-slate-400 mt-1 font-medium",
                        ),
                        class_name="mb-4 pb-4 border-b border-white/5",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.icon("refresh-cw", size=12, class_name="mr-1"),
                            rx.cond(
                                LanguageState.is_zh, "立即续费", "Renew Now"
                            ),
                            class_name="flex-1 flex items-center justify-center px-3 py-2 rounded-lg bg-gradient-to-r from-orange-500 to-amber-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-orange-500/20 transition-all cursor-pointer",
                        ),
                        rx.el.button(
                            rx.icon(
                                "arrow-up-right", size=12, class_name="mr-1"
                            ),
                            rx.cond(
                                LanguageState.is_zh, "升级套餐", "Upgrade Plan"
                            ),
                            class_name="flex-1 flex items-center justify-center px-3 py-2 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold shadow-lg shadow-indigo-500/20 transition-all cursor-pointer",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                ),
                accent="orange",
            ),
            _card(
                rx.cond(
                    LanguageState.is_zh, "自动续费设置", "Auto-Renewal Settings"
                ),
                "settings",
                rx.el.div(
                    rx.el.label(
                        rx.el.input(
                            type="checkbox",
                            default_checked=inst["auto_renew"],
                            on_change=lambda: ServersState.toggle_auto_renew(
                                inst["id"].to(str)
                            ),
                            class_name="rounded border-white/20 bg-slate-900 text-cyan-500 focus:ring-cyan-500/30 mr-2 size-4",
                        ),
                        rx.el.span(
                            rx.cond(
                                LanguageState.is_zh,
                                "启用自动续费",
                                "Enable auto-renewal",
                            ),
                            class_name="text-xs text-white font-semibold",
                        ),
                        class_name="flex items-center cursor-pointer p-2 rounded-lg hover:bg-white/5 mb-2",
                    ),
                    _kv(
                        rx.cond(
                            LanguageState.is_zh, "扣款账户", "Billing account"
                        ),
                        "余额 ¥128.50",
                        "wallet",
                    ),
                    _kv(
                        rx.cond(LanguageState.is_zh, "备用支付", "Fallback"),
                        "Alipay · ****1234",
                        "credit-card",
                    ),
                    _kv(
                        rx.cond(LanguageState.is_zh, "提前提醒", "Reminder"),
                        rx.cond(
                            LanguageState.is_zh, "到期前 3 天", "3 days before"
                        ),
                        "bell",
                    ),
                    class_name="flex flex-col gap-2",
                ),
                accent="cyan",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        _card(
            rx.cond(
                LanguageState.is_zh,
                "账单明细 · 发票记录",
                "Billing History · Invoices",
            ),
            "receipt",
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            _th(
                                rx.cond(LanguageState.is_zh, "订单号", "Order")
                            ),
                            _th(rx.cond(LanguageState.is_zh, "日期", "Date")),
                            _th(rx.cond(LanguageState.is_zh, "项目", "Item")),
                            _th(rx.cond(LanguageState.is_zh, "周期", "Cycle")),
                            _th(rx.cond(LanguageState.is_zh, "金额", "Amount")),
                            _th(rx.cond(LanguageState.is_zh, "状态", "Status")),
                            _th(""),
                        ),
                        class_name="bg-white/[0.02] border-b border-white/10",
                    ),
                    rx.el.tbody(
                        rx.foreach(ServersState.billing_records, _bill_row)
                    ),
                    class_name="table-auto w-full",
                ),
                class_name="overflow-x-auto -mx-4",
            ),
            extra=rx.el.button(
                rx.icon("download", size=11, class_name="mr-1"),
                rx.cond(LanguageState.is_zh, "导出全部", "Export All"),
                class_name="flex items-center px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-slate-200 text-[10px] font-bold hover:bg-white/10 transition-all cursor-pointer",
            ),
            accent="emerald",
        ),
    )


# ============ DNS TAB ============
def _dns_row(rec) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.span(
                rec["name"], class_name="text-xs text-white font-mono font-bold"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rec["type"],
                class_name=rx.match(
                    rec["type"],
                    (
                        "A",
                        "inline-flex text-[10px] font-bold text-cyan-300 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/30 font-mono",
                    ),
                    (
                        "AAAA",
                        "inline-flex text-[10px] font-bold text-violet-300 bg-violet-500/10 px-2 py-0.5 rounded border border-violet-500/30 font-mono",
                    ),
                    (
                        "CNAME",
                        "inline-flex text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30 font-mono",
                    ),
                    (
                        "TXT",
                        "inline-flex text-[10px] font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/30 font-mono",
                    ),
                    (
                        "MX",
                        "inline-flex text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30 font-mono",
                    ),
                    "inline-flex text-[10px] font-bold text-slate-300 bg-white/5 px-2 py-0.5 rounded border border-white/10 font-mono",
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rec["value"],
                class_name="text-xs text-slate-200 font-mono truncate max-w-xs block",
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rec["ttl"], class_name="text-xs text-slate-400 font-mono"
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.span(
                rx.cond(
                    rec["status"] == "active",
                    rx.cond(LanguageState.is_zh, "生效", "Active"),
                    rx.cond(LanguageState.is_zh, "待生效", "Pending"),
                ),
                class_name=rx.cond(
                    rec["status"] == "active",
                    "inline-flex text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
                    "inline-flex text-[10px] font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded-full border border-amber-500/30",
                ),
            ),
            class_name="px-4 py-3",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "pencil",
                        size=11,
                        class_name="text-slate-400 hover:text-cyan-300",
                    ),
                    class_name="p-1 rounded hover:bg-white/5 cursor-pointer",
                ),
                rx.el.button(
                    rx.icon(
                        "trash-2",
                        size=11,
                        class_name="text-slate-400 hover:text-rose-300",
                    ),
                    class_name="p-1 rounded hover:bg-rose-500/10 cursor-pointer",
                ),
                class_name="flex items-center gap-1",
            ),
            class_name="px-4 py-3",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.02] transition-colors",
    )


def dns_tab_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _kv(
                rx.cond(LanguageState.is_zh, "主域名", "Domain"),
                "aiarks.example.com",
                "globe",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "记录总数", "Total Records"),
                ServersState.dns_records.length().to_string(),
                "list",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "解析状态", "Status"),
                rx.cond(LanguageState.is_zh, "全部生效", "All active"),
                "message_circle_check",
            ),
            _kv(
                rx.cond(LanguageState.is_zh, "DNSSEC", "DNSSEC"),
                rx.cond(LanguageState.is_zh, "已启用", "Enabled"),
                "shield-check",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4",
        ),
        _card(
            rx.cond(LanguageState.is_zh, "域名解析记录", "DNS Records"),
            "globe",
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            _th(
                                rx.cond(LanguageState.is_zh, "主机记录", "Name")
                            ),
                            _th(rx.cond(LanguageState.is_zh, "类型", "Type")),
                            _th(
                                rx.cond(LanguageState.is_zh, "记录值", "Value")
                            ),
                            _th("TTL"),
                            _th(rx.cond(LanguageState.is_zh, "状态", "Status")),
                            _th(""),
                        ),
                        class_name="bg-white/[0.02] border-b border-white/10",
                    ),
                    rx.el.tbody(rx.foreach(ServersState.dns_records, _dns_row)),
                    class_name="table-auto w-full",
                ),
                class_name="overflow-x-auto -mx-4",
            ),
            extra=rx.el.div(
                rx.el.button(
                    rx.icon("plus", size=11, class_name="mr-1"),
                    rx.cond(LanguageState.is_zh, "新增记录", "Add Record"),
                    class_name="flex items-center px-2.5 py-1 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-[10px] font-bold transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("upload", size=11, class_name="mr-1"),
                    rx.cond(LanguageState.is_zh, "批量导入", "Import"),
                    class_name="ml-2 flex items-center px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-slate-200 text-[10px] font-bold hover:bg-white/10 transition-all cursor-pointer",
                ),
                class_name="flex items-center",
            ),
            accent="cyan",
        ),
    )


# ============ MONITOR TAB ============
def _range_btn(label, value: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=lambda: ServersState.set_monitor_range(value),
        class_name=rx.cond(
            ServersState.monitor_range == value,
            "px-3 py-1.5 rounded-md bg-cyan-500/10 border border-cyan-500/40 text-cyan-200 text-[11px] font-bold transition-all cursor-pointer",
            "px-3 py-1.5 rounded-md bg-white/5 border border-white/10 text-slate-300 hover:text-white text-[11px] font-medium transition-all cursor-pointer",
        ),
    )


def _event_row(e) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                e["icon"],
                size=13,
                class_name=rx.match(
                    e["level"],
                    ("critical", "text-rose-300"),
                    ("warn", "text-amber-300"),
                    "text-cyan-300",
                ),
            ),
            class_name=rx.match(
                e["level"],
                (
                    "critical",
                    "w-8 h-8 rounded-lg bg-rose-500/10 border border-rose-500/30 flex items-center justify-center shrink-0",
                ),
                (
                    "warn",
                    "w-8 h-8 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-center justify-center shrink-0",
                ),
                "w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center shrink-0",
            ),
        ),
        rx.el.div(
            rx.el.p(
                e["message"], class_name="text-xs text-white font-semibold"
            ),
            rx.el.p(
                e["time"],
                class_name="text-[10px] text-slate-500 font-mono mt-0.5",
            ),
            class_name="flex-1 min-w-0 ml-3",
        ),
        class_name="flex items-center px-3 py-2.5 rounded-lg bg-white/[0.02] border border-white/5 hover:border-white/10 transition-all",
    )


def monitor_tab_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                _range_btn("1h", "1h"),
                _range_btn("6h", "6h"),
                _range_btn("24h", "24h"),
                _range_btn("7d", "7d"),
                _range_btn("30d", "30d"),
                class_name="inline-flex items-center gap-1 p-1 rounded-lg bg-slate-900/60 border border-white/10",
            ),
            rx.el.div(
                rx.el.span(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                    ),
                    rx.cond(LanguageState.is_zh, "无告警", "No alerts"),
                    class_name="inline-flex items-center text-[11px] font-bold text-emerald-300 bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/30",
                ),
                class_name="ml-auto",
            ),
            class_name="flex items-center flex-wrap gap-3 mb-4",
        ),
        rx.el.div(
            _peak_stat(
                "cpu",
                rx.cond(LanguageState.is_zh, "CPU 峰值", "CPU Peak"),
                "72%",
                "14:00",
                "cyan",
            ),
            _peak_stat(
                "memory-stick",
                rx.cond(LanguageState.is_zh, "内存峰值", "Memory Peak"),
                "74%",
                "14:00",
                "violet",
            ),
            _peak_stat(
                "activity",
                rx.cond(LanguageState.is_zh, "网络峰值", "Network Peak"),
                "1.12 Mbps",
                "14:00",
                "emerald",
            ),
            _peak_stat(
                "hard-drive",
                rx.cond(LanguageState.is_zh, "磁盘峰值", "Disk Peak"),
                "42%",
                "22:00",
                "orange",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4",
        ),
        rx.el.div(
            _card(
                rx.cond(LanguageState.is_zh, "CPU 使用率 (%)", "CPU Usage (%)"),
                "cpu",
                rx.recharts.line_chart(
                    rx.recharts.cartesian_grid(
                        horizontal=True,
                        vertical=False,
                        stroke="rgba(255,255,255,0.05)",
                    ),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.line(
                        data_key="cpu",
                        stroke="#22d3ee",
                        stroke_width=2,
                        type_="natural",
                        dot=False,
                    ),
                    rx.recharts.x_axis(
                        data_key="time",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    data=ServersState.monitor_data,
                    width="100%",
                    height=180,
                    margin={"left": -20, "right": 10, "top": 10, "bottom": 5},
                ),
                accent="cyan",
            ),
            _card(
                rx.cond(
                    LanguageState.is_zh, "内存使用率 (%)", "Memory Usage (%)"
                ),
                "memory-stick",
                rx.recharts.line_chart(
                    rx.recharts.cartesian_grid(
                        horizontal=True,
                        vertical=False,
                        stroke="rgba(255,255,255,0.05)",
                    ),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.line(
                        data_key="memory",
                        stroke="#a78bfa",
                        stroke_width=2,
                        type_="natural",
                        dot=False,
                    ),
                    rx.recharts.x_axis(
                        data_key="time",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    data=ServersState.monitor_data,
                    width="100%",
                    height=180,
                    margin={"left": -20, "right": 10, "top": 10, "bottom": 5},
                ),
                accent="violet",
            ),
            _card(
                rx.cond(
                    LanguageState.is_zh, "网络吞吐 (KB/s)", "Network I/O (KB/s)"
                ),
                "activity",
                rx.recharts.line_chart(
                    rx.recharts.cartesian_grid(
                        horizontal=True,
                        vertical=False,
                        stroke="rgba(255,255,255,0.05)",
                    ),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.line(
                        data_key="net_in",
                        stroke="#34d399",
                        stroke_width=2,
                        type_="natural",
                        dot=False,
                        name="In",
                    ),
                    rx.recharts.line(
                        data_key="net_out",
                        stroke="#fbbf24",
                        stroke_width=2,
                        type_="natural",
                        dot=False,
                        name="Out",
                    ),
                    rx.recharts.x_axis(
                        data_key="time",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    data=ServersState.monitor_data,
                    width="100%",
                    height=180,
                    margin={"left": -20, "right": 10, "top": 10, "bottom": 5},
                ),
                accent="emerald",
            ),
            _card(
                rx.cond(
                    LanguageState.is_zh, "磁盘使用率 (%)", "Disk Usage (%)"
                ),
                "hard-drive",
                rx.recharts.bar_chart(
                    rx.recharts.cartesian_grid(
                        horizontal=True,
                        vertical=False,
                        stroke="rgba(255,255,255,0.05)",
                    ),
                    rx.recharts.graphing_tooltip(**TOOLTIP_PROPS),
                    rx.recharts.bar(
                        data_key="disk", fill="#fb923c", radius=[3, 3, 0, 0]
                    ),
                    rx.recharts.x_axis(
                        data_key="time",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": "10px", "fill": "#64748b"},
                    ),
                    data=ServersState.monitor_data,
                    width="100%",
                    height=180,
                    margin={"left": -20, "right": 10, "top": 10, "bottom": 5},
                ),
                accent="orange",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
        ),
        _card(
            rx.cond(LanguageState.is_zh, "最近事件", "Recent Events"),
            "history",
            rx.el.div(
                rx.foreach(ServersState.recent_events, _event_row),
                class_name="flex flex-col gap-2",
            ),
            accent="cyan",
        ),
    )


def _peak_stat(
    icon: str, label, value: str, at: str, accent: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=13, class_name=f"text-{accent}-300"),
            rx.el.span(
                label,
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold ml-1.5",
            ),
            class_name="flex items-center mb-2",
        ),
        rx.el.p(
            value,
            class_name="text-2xl text-white font-extrabold font-mono tracking-tight leading-none mb-1",
        ),
        rx.el.p(
            rx.cond(LanguageState.is_zh, "于 ", "at ") + at,
            class_name="text-[10px] text-slate-500 font-medium",
        ),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-4",
    )


def render_manage_tab_content() -> rx.Component:
    return rx.match(
        ServersState.manage_tab,
        ("dashboard", dashboard_tab_content()),
        ("access", access_tab_content()),
        ("network", network_tab_content()),
        ("billing", billing_tab_content()),
        ("dns", dns_tab_content()),
        ("monitor", monitor_tab_content()),
        dashboard_tab_content(),
    )
