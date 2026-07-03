import reflex as rx
from app.states.language_state import LanguageState


def _step_card(step: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                step["num"],
                class_name="text-xs font-bold text-cyan-300",
            ),
            class_name="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center mb-4",
        ),
        rx.el.div(
            rx.icon(step["icon"], size=18, class_name="text-white"),
            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mb-4",
        ),
        rx.el.h3(
            step["title"],
            class_name="text-white text-base font-bold mb-2",
        ),
        rx.el.p(
            step["desc"],
            class_name="text-sm text-slate-400 leading-relaxed font-medium",
        ),
        class_name="relative rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 hover:border-cyan-500/30 hover:-translate-y-0.5 transition-all",
    )


def _data_stat(icon: str, value: str, label: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-cyan-300"),
            class_name="w-9 h-9 rounded-lg bg-white/10 border border-white/20 flex items-center justify-center",
        ),
        rx.el.div(
            rx.el.p(
                value,
                class_name="text-white text-2xl font-extrabold tracking-tight leading-none",
            ),
            rx.el.p(
                label,
                class_name="text-[11px] text-white/70 uppercase tracking-wider font-bold mt-1",
            ),
        ),
        class_name="flex items-center gap-3",
    )


def workflow_section() -> rx.Component:
    steps_en = [
        {
            "num": "01",
            "icon": "mouse-pointer-click",
            "title": "Choose region & plan",
            "desc": "Pick from 12+ regions and 20+ plans. Filter by bandwidth, stock and price.",
        },
        {
            "num": "02",
            "icon": "credit-card",
            "title": "Secure checkout",
            "desc": "Pay with card, PayPal, Alipay, WeChat Pay or USDT. Encrypted end-to-end.",
        },
        {
            "num": "03",
            "icon": "rocket",
            "title": "Auto provisioning",
            "desc": "Server boots and native IP assigned in under 60 seconds. Instant credentials.",
        },
        {
            "num": "04",
            "icon": "line-chart",
            "title": "Monitor & scale",
            "desc": "Real-time dashboards, one-click resize, snapshots and 24/7 support.",
        },
    ]
    steps_zh = [
        {
            "num": "01",
            "icon": "mouse-pointer-click",
            "title": "选择地区与方案",
            "desc": "12+ 地区,20+ 方案。按带宽、库存和价格筛选,匹配业务需求。",
        },
        {
            "num": "02",
            "icon": "credit-card",
            "title": "安全结账",
            "desc": "支持信用卡、PayPal、支付宝、微信支付与 USDT,全流程加密。",
        },
        {
            "num": "03",
            "icon": "rocket",
            "title": "自动开通",
            "desc": "60 秒内完成部署并分配原生 IP,凭据即时送达邮箱与控制台。",
        },
        {
            "num": "04",
            "icon": "line-chart",
            "title": "监控与扩容",
            "desc": "实时仪表盘、一键升配、快照备份与 7×24 工程师支持。",
        },
    ]

    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("workflow", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh, "服务流程", "How it works"
                        ),
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    rx.cond(
                        LanguageState.is_zh,
                        "从下单到上线,",
                        "From order to online, ",
                    ),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh, "四步搞定", "in four steps"
                        ),
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    rx.cond(
                        LanguageState.is_zh,
                        "无需咨询,无需等待,几分钟内即可获得一台可用于生产的云服务器。",
                        "No sales calls, no waiting. Production-ready cloud servers in minutes.",
                    ),
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(
                    rx.cond(LanguageState.is_zh, steps_zh, steps_en),
                    _step_card,
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 mb-16",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_120%_at_20%_50%,rgba(255,255,255,0.15),transparent)] pointer-events-none",
                ),
                rx.el.div(
                    class_name="absolute inset-0 rounded-3xl bg-gradient-to-r from-indigo-600/40 via-indigo-500/30 to-cyan-500/40 blur-2xl -z-10",
                ),
                rx.el.div(
                    _data_stat(
                        "globe",
                        "100+",
                        rx.cond(LanguageState.is_zh, "全球节点", "Global PoPs"),
                    ),
                    _data_stat(
                        "gauge",
                        "10 Gbps",
                        rx.cond(
                            LanguageState.is_zh, "单节点峰值", "Peak / node"
                        ),
                    ),
                    _data_stat(
                        "zap",
                        "< 60s",
                        rx.cond(
                            LanguageState.is_zh, "开通时间", "Provisioning"
                        ),
                    ),
                    _data_stat(
                        "shield",
                        "200 Gbps",
                        rx.cond(
                            LanguageState.is_zh, "DDoS 防护", "DDoS Shield"
                        ),
                    ),
                    _data_stat(
                        "users",
                        "50k+",
                        rx.cond(LanguageState.is_zh, "活跃客户", "Customers"),
                    ),
                    _data_stat(
                        "trending-up",
                        "99.99%",
                        rx.cond(
                            LanguageState.is_zh, "SLA 可用性", "SLA Uptime"
                        ),
                    ),
                    class_name="relative grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6 px-8 py-8",
                ),
                class_name="relative rounded-3xl bg-gradient-to-r from-indigo-600 via-indigo-500 to-cyan-500 overflow-hidden shadow-2xl shadow-indigo-500/30 border border-white/10",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="workflow",
        class_name="relative py-24",
    )
