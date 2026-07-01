import reflex as rx
from app.states.language_state import LanguageState


def _stat_card(icon: str, value: str, label) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-blue-400"),
            class_name="w-10 h-10 rounded-lg bg-blue-500/10 border border-blue-500/20 flex items-center justify-center mb-3",
        ),
        rx.el.p(value, class_name="text-2xl font-semibold text-white"),
        rx.el.p(
            label,
            class_name="text-xs text-gray-500 uppercase tracking-wider min-h-[1rem]",
        ),
        class_name="rounded-xl bg-white/[0.03] border border-white/10 p-5 backdrop-blur-sm hover:bg-white/[0.06] transition-colors",
    )


def _node_row(n) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(n["flag"], class_name="text-xl"),
                rx.el.div(
                    rx.el.p(
                        n["region"], class_name="text-white text-sm font-medium"
                    ),
                    rx.el.p(
                        n["code"],
                        class_name="text-[10px] text-gray-500 tracking-wider",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon("gauge", size=12, class_name="text-blue-400"),
                rx.el.span(
                    n["bandwidth"], class_name="text-sm text-gray-300 font-mono"
                ),
                class_name="flex items-center gap-1.5",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                n["latency"], class_name="text-sm text-emerald-400 font-mono"
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(n["line"], class_name="text-sm text-gray-400"),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="h-full bg-gradient-to-r from-blue-500 to-cyan-400 rounded-full",
                        style={"width": f"{n['load']}%"},
                    ),
                    class_name="w-24 h-1.5 bg-white/5 rounded-full overflow-hidden",
                ),
                rx.el.span(
                    f"{n['load']}%",
                    class_name="text-xs text-gray-400 font-mono",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"
                ),
                LanguageState.nodes_status_online,
                class_name="inline-flex items-center text-[10px] font-medium text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20",
            ),
            class_name="px-6 py-4",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.03] transition-colors",
    )


def nodes_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("globe", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        LanguageState.nodes_badge,
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    LanguageState.nodes_title_prefix,
                    rx.el.span(
                        LanguageState.nodes_title_highlight,
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.nodes_desc,
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                _stat_card("globe", "100+", LanguageState.nodes_stat_pops),
                _stat_card(
                    "activity", "10 Gbps", LanguageState.nodes_stat_peak
                ),
                _stat_card("zap", "< 30 ms", LanguageState.nodes_stat_latency),
                _stat_card("shield", "200 Gbps", LanguageState.nodes_stat_ddos),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                class_name="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"
                            ),
                            rx.el.span(
                                LanguageState.nodes_live_status,
                                class_name="text-xs text-gray-300 font-medium",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.span(
                            LanguageState.nodes_updated,
                            class_name="text-xs text-gray-500",
                        ),
                        class_name="flex items-center justify-between px-6 py-4 border-b border-white/5",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        LanguageState.nodes_col_region,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        LanguageState.nodes_col_bandwidth,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        LanguageState.nodes_col_latency,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        LanguageState.nodes_col_line,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        LanguageState.nodes_col_load,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        LanguageState.nodes_col_status,
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                ),
                                class_name="bg-white/[0.02]",
                            ),
                            rx.el.tbody(
                                rx.foreach(LanguageState.nodes_list, _node_row),
                            ),
                            class_name="table-auto w-full",
                        ),
                        class_name="overflow-x-auto",
                    ),
                    class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 backdrop-blur-sm overflow-hidden",
                ),
                class_name="",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="nodes",
        class_name="relative py-24 border-t border-white/5",
    )