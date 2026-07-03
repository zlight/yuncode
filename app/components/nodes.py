import reflex as rx
from app.states.language_state import LanguageState


def _stat_card(icon: str, value: str, label) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-cyan-300"),
            class_name="w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mb-3 shadow-lg shadow-indigo-500/10",
        ),
        rx.el.p(value, class_name="text-2xl font-extrabold text-white"),
        rx.el.p(
            label,
            class_name="text-xs text-slate-400 uppercase tracking-wider font-bold",
        ),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 transition-colors",
    )


def _node_row(n) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(n["flag"], class_name="text-xl"),
                rx.el.div(
                    rx.el.p(
                        n["region"],
                        class_name="text-white text-sm font-semibold",
                    ),
                    rx.el.p(
                        n["code"],
                        class_name="text-[10px] text-slate-500 font-bold tracking-wider",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon("gauge", size=12, class_name="text-cyan-300"),
                rx.el.span(
                    n["bandwidth"],
                    class_name="text-sm text-slate-200 font-mono font-semibold",
                ),
                class_name="flex items-center gap-1.5",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                n["latency"],
                class_name="text-sm text-emerald-300 font-mono font-bold",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                n["line"], class_name="text-sm text-slate-300 font-medium"
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="h-full bg-gradient-to-r from-indigo-500 to-cyan-400 rounded-full shadow-lg shadow-cyan-500/40",
                        style={"width": f"{n['load']}%"},
                    ),
                    class_name="w-24 h-1.5 bg-white/5 rounded-full overflow-hidden",
                ),
                rx.el.span(
                    f"{n['load']}%",
                    class_name="text-xs text-slate-400 font-mono font-bold",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                ),
                LanguageState.nodes_status_online,
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
            ),
            class_name="px-6 py-4",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.02] transition-colors",
    )


def nodes_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("globe", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        LanguageState.nodes_badge,
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    LanguageState.nodes_title_prefix,
                    rx.el.span(
                        LanguageState.nodes_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.nodes_desc,
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
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
                        rx.el.span(
                            class_name="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shadow-lg shadow-emerald-400/50"
                        ),
                        rx.el.span(
                            LanguageState.nodes_live_status,
                            class_name="text-xs text-slate-100 font-bold",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.span(
                        LanguageState.nodes_updated,
                        class_name="text-xs text-slate-500 font-semibold",
                    ),
                    class_name="flex items-center justify-between px-6 py-4 border-b border-white/5 bg-white/[0.02]",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    LanguageState.nodes_col_region,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                                rx.el.th(
                                    LanguageState.nodes_col_bandwidth,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                                rx.el.th(
                                    LanguageState.nodes_col_latency,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                                rx.el.th(
                                    LanguageState.nodes_col_line,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                                rx.el.th(
                                    LanguageState.nodes_col_load,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                                rx.el.th(
                                    LanguageState.nodes_col_status,
                                    class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-6 py-3",
                                ),
                            ),
                            class_name="bg-white/[0.02] border-b border-white/10",
                        ),
                        rx.el.tbody(
                            rx.foreach(LanguageState.nodes_list, _node_row),
                        ),
                        class_name="table-auto w-full",
                    ),
                    class_name="overflow-x-auto",
                ),
                class_name="rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 overflow-hidden",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="nodes",
        class_name="relative py-24",
    )
