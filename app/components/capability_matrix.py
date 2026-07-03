import reflex as rx
from app.states.language_state import LanguageState


def _cap_row(item: rx.Var) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.icon(item["icon"], size=14, class_name="text-cyan-300"),
                rx.el.span(
                    item["name"],
                    class_name="text-sm text-white font-semibold",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-6 py-4 border-b border-white/5",
        ),
        rx.el.td(
            rx.icon("check", size=14, class_name="text-emerald-300 mx-auto"),
            class_name="px-6 py-4 border-b border-white/5 text-center",
        ),
        rx.el.td(
            rx.icon("check", size=14, class_name="text-emerald-300 mx-auto"),
            class_name="px-6 py-4 border-b border-white/5 text-center",
        ),
        rx.el.td(
            rx.icon("check", size=14, class_name="text-emerald-300 mx-auto"),
            class_name="px-6 py-4 border-b border-white/5 text-center",
        ),
        rx.el.td(
            rx.el.span(
                item["highlight"],
                class_name="inline-block text-[10px] font-bold px-2 py-0.5 rounded-md bg-cyan-500/10 text-cyan-300 border border-cyan-500/30",
            ),
            class_name="px-6 py-4 border-b border-white/5 text-center",
        ),
        class_name="hover:bg-white/[0.02] transition-colors",
    )


def capability_matrix_section() -> rx.Component:
    rows_en = [
        {"icon": "cpu", "name": "Dedicated CPU cores", "highlight": "Isolated"},
        {
            "icon": "hard-drive",
            "name": "NVMe SSD storage",
            "highlight": "Enterprise",
        },
        {"icon": "shield", "name": "DDoS mitigation", "highlight": "L3/L4/L7"},
        {
            "icon": "radio-tower",
            "name": "Native IP streaming unlock",
            "highlight": "Global",
        },
        {
            "icon": "git-branch",
            "name": "One-click snapshots & backup",
            "highlight": "Auto",
        },
        {
            "icon": "activity",
            "name": "Real-time monitoring & alerts",
            "highlight": "24/7",
        },
        {
            "icon": "lock",
            "name": "Encryption at rest & in transit",
            "highlight": "AES-256",
        },
        {
            "icon": "terminal",
            "name": "REST API & Terraform provider",
            "highlight": "IaC",
        },
    ]
    rows_zh = [
        {"icon": "cpu", "name": "独享 CPU 核心", "highlight": "隔离"},
        {"icon": "hard-drive", "name": "NVMe SSD 存储", "highlight": "企业级"},
        {"icon": "shield", "name": "DDoS 防护缓解", "highlight": "L3/L4/L7"},
        {
            "icon": "radio-tower",
            "name": "原生 IP 流媒体解锁",
            "highlight": "全球",
        },
        {"icon": "git-branch", "name": "一键快照与备份", "highlight": "自动"},
        {"icon": "activity", "name": "实时监控与告警", "highlight": "7×24"},
        {"icon": "lock", "name": "静态与传输加密", "highlight": "AES-256"},
        {
            "icon": "terminal",
            "name": "REST API 与 Terraform",
            "highlight": "IaC",
        },
    ]

    def _th(label) -> rx.Component:
        return rx.el.th(
            label,
            class_name="text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3 text-center",
            scope="col",
        )

    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layout-grid", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh, "能力矩阵", "Capability Matrix"
                        ),
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    rx.cond(LanguageState.is_zh, "一张表看懂 ", "One matrix, "),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh,
                            "AiarksCloud 全部能力",
                            "every AiarksCloud capability",
                        ),
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    rx.cond(
                        LanguageState.is_zh,
                        "所有方案均包含核心能力,面向不同规模的业务提供一致体验。",
                        "Every plan tier ships with the same core capabilities — consistent experience at any scale.",
                    ),
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "能力",
                                        "Capability",
                                    ),
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                    scope="col",
                                ),
                                _th(
                                    rx.cond(
                                        LanguageState.is_zh, "轻量", "Light"
                                    )
                                ),
                                _th(
                                    rx.cond(
                                        LanguageState.is_zh, "标准", "Standard"
                                    )
                                ),
                                _th(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "企业",
                                        "Enterprise",
                                    )
                                ),
                                _th(
                                    rx.cond(
                                        LanguageState.is_zh, "亮点", "Highlight"
                                    )
                                ),
                                class_name="bg-white/[0.02] border-b border-white/10",
                            ),
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                rx.cond(LanguageState.is_zh, rows_zh, rows_en),
                                _cap_row,
                            ),
                        ),
                        class_name="table-auto w-full",
                    ),
                    class_name="overflow-x-auto",
                ),
                class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden max-w-5xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="capability",
        class_name="relative py-24",
    )
