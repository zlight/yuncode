import reflex as rx
from app.states.language_state import LanguageState


def _metric_card(m) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(m["icon"], size=18, class_name="text-blue-400"),
            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/20 flex items-center justify-center mb-4",
        ),
        rx.el.p(
            m["value"],
            class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-1",
        ),
        rx.el.p(
            m["label"],
            class_name="text-xs text-blue-400 uppercase tracking-wider font-semibold mb-3",
        ),
        rx.el.p(
            m["desc"],
            class_name="text-sm text-gray-400 leading-relaxed",
        ),
        class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 backdrop-blur-sm hover:border-blue-500/30 hover:-translate-y-1 transition-all duration-300",
    )


def _guarantee_card(g) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(g["icon"], size=18, class_name="text-emerald-400"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-emerald-500/20 to-emerald-500/5 border border-emerald-500/20 flex items-center justify-center",
            ),
            rx.el.span(
                g["tag"],
                class_name="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-white/5 text-gray-400 border border-white/10 uppercase tracking-wider",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            g["title"],
            class_name="text-white text-base font-semibold mb-2",
        ),
        rx.el.p(
            g["desc"],
            class_name="text-sm text-gray-400 leading-relaxed",
        ),
        class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 backdrop-blur-sm hover:border-emerald-500/30 transition-all duration-300",
    )


def metrics_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("bar-chart-3", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        LanguageState.metrics_badge,
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    LanguageState.metrics_title_prefix,
                    rx.el.span(
                        LanguageState.metrics_title_highlight,
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.metrics_desc,
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(LanguageState.metrics_list, _metric_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-20",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "shield-check", size=14, class_name="text-emerald-400"
                    ),
                    rx.el.span(
                        LanguageState.guarantees_badge,
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    LanguageState.guarantees_title_prefix,
                    rx.el.span(
                        LanguageState.guarantees_title_highlight,
                        class_name="bg-gradient-to-r from-emerald-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.guarantees_desc,
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(LanguageState.guarantees_list, _guarantee_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="trust",
        class_name="relative py-24 border-t border-white/5",
    )