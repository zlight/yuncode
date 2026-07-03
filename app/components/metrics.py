import reflex as rx
from app.states.language_state import LanguageState


def _metric_card(m) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(m["icon"], size=18, class_name="text-indigo-600"),
            class_name="w-11 h-11 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center mb-4",
        ),
        rx.el.p(
            m["value"],
            class_name="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight mb-1",
        ),
        rx.el.p(
            m["label"],
            class_name="text-xs text-indigo-600 uppercase tracking-wider font-bold mb-3",
        ),
        rx.el.p(
            m["desc"],
            class_name="text-sm text-slate-500 leading-relaxed font-medium",
        ),
        class_name="rounded-2xl bg-white border border-slate-200/80 p-6 shadow-xs hover:border-indigo-500 hover:-translate-y-1 transition-all duration-300",
    )


def _guarantee_card(g) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(g["icon"], size=18, class_name="text-emerald-600"),
                class_name="w-11 h-11 rounded-xl bg-emerald-50 border border-emerald-100 flex items-center justify-center",
            ),
            rx.el.span(
                g["tag"],
                class_name="text-[10px] font-bold px-2 py-0.5 rounded-md bg-slate-50 text-slate-500 border border-slate-200 uppercase tracking-wider",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            g["title"],
            class_name="text-slate-900 text-base font-bold mb-2",
        ),
        rx.el.p(
            g["desc"],
            class_name="text-sm text-slate-500 leading-relaxed font-medium",
        ),
        class_name="rounded-2xl bg-white border border-slate-200/80 p-6 shadow-xs hover:border-emerald-500 transition-all duration-300",
    )


def metrics_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "bar-chart-3", size=14, class_name="text-indigo-600"
                    ),
                    rx.el.span(
                        LanguageState.metrics_badge,
                        class_name="text-xs text-indigo-600 font-bold tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 mb-4",
                ),
                rx.el.h2(
                    LanguageState.metrics_title_prefix,
                    rx.el.span(
                        LanguageState.metrics_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.metrics_desc,
                    class_name="text-slate-500 max-w-2xl mx-auto font-medium",
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
                        "shield-check", size=14, class_name="text-emerald-600"
                    ),
                    rx.el.span(
                        LanguageState.guarantees_badge,
                        class_name="text-xs text-emerald-600 font-bold tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 border border-emerald-100 mb-4",
                ),
                rx.el.h2(
                    LanguageState.guarantees_title_prefix,
                    rx.el.span(
                        LanguageState.guarantees_title_highlight,
                        class_name="bg-gradient-to-r from-emerald-600 to-cyan-500 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.guarantees_desc,
                    class_name="text-slate-500 max-w-2xl mx-auto font-medium",
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
        class_name="relative py-24 bg-white border-b border-slate-100",
    )
