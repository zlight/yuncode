import reflex as rx
from app.states.language_state import LanguageState


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_100%_at_50%_50%,rgba(99,102,241,0.08),transparent)] pointer-events-none",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "sparkles", size=14, class_name="text-indigo-600"
                        ),
                        rx.el.span(
                            LanguageState.cta_badge,
                            class_name="text-xs text-indigo-600 font-bold tracking-wide uppercase",
                        ),
                        class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 mb-6",
                    ),
                    rx.el.h2(
                        LanguageState.cta_title_prefix,
                        rx.el.span(
                            LanguageState.cta_title_highlight,
                            class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                        ),
                        class_name="text-3xl md:text-5xl font-bold text-slate-900 tracking-tight mb-4 max-w-3xl mx-auto",
                    ),
                    rx.el.p(
                        LanguageState.cta_desc,
                        class_name="text-slate-500 text-base md:text-lg mb-8 max-w-2xl mx-auto font-medium",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.cta_btn_primary,
                                rx.icon(
                                    "arrow-right", size=16, class_name="ml-1.5"
                                ),
                                class_name="flex items-center gap-1 bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-3 rounded-lg font-bold shadow-md hover:shadow-lg transition-all cursor-pointer",
                            ),
                            href="#pricing",
                        ),
                        rx.el.a(
                            rx.el.button(
                                rx.icon(
                                    "book-open", size=16, class_name="mr-1.5"
                                ),
                                LanguageState.cta_btn_secondary,
                                class_name="flex items-center gap-1 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-6 py-3 rounded-lg font-bold shadow-xs transition-all cursor-pointer",
                            ),
                            href="#",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-3 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-600"
                            ),
                            rx.el.span(
                                LanguageState.cta_check1,
                                class_name="text-xs text-slate-500 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-600"
                            ),
                            rx.el.span(
                                LanguageState.cta_check2,
                                class_name="text-xs text-slate-500 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-600"
                            ),
                            rx.el.span(
                                LanguageState.cta_check3,
                                class_name="text-xs text-slate-500 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-600"
                            ),
                            rx.el.span(
                                LanguageState.cta_check4,
                                class_name="text-xs text-slate-500 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-x-6 gap-y-2",
                    ),
                    class_name="relative text-center py-16 md:py-20 px-6",
                ),
                class_name="relative rounded-3xl bg-white border border-slate-200 overflow-hidden shadow-sm",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="cta",
        class_name="relative py-16 bg-white border-b border-slate-100",
    )
