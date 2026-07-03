import reflex as rx
from app.states.language_state import LanguageState


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 rounded-3xl bg-gradient-to-r from-indigo-600/40 via-violet-500/30 to-cyan-500/40 blur-2xl -z-10",
                ),
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_100%_at_50%_50%,rgba(103,232,249,0.15),transparent)] pointer-events-none",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "sparkles", size=14, class_name="text-cyan-300"
                        ),
                        rx.el.span(
                            LanguageState.cta_badge,
                            class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                        ),
                        class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-6",
                    ),
                    rx.el.h2(
                        LanguageState.cta_title_prefix,
                        rx.el.span(
                            LanguageState.cta_title_highlight,
                            class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                        ),
                        class_name="text-3xl md:text-5xl font-extrabold text-white tracking-tight mb-4 max-w-3xl mx-auto",
                    ),
                    rx.el.p(
                        LanguageState.cta_desc,
                        class_name="text-slate-300 text-base md:text-lg mb-8 max-w-2xl mx-auto font-medium",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.cta_btn_primary,
                                rx.icon(
                                    "arrow-right", size=16, class_name="ml-1.5"
                                ),
                                class_name="flex items-center gap-1 bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white px-6 py-3 rounded-lg font-bold shadow-xl shadow-indigo-500/40 transition-all cursor-pointer",
                            ),
                            href="#pricing",
                        ),
                        rx.el.a(
                            rx.el.button(
                                rx.icon(
                                    "book-open", size=16, class_name="mr-1.5"
                                ),
                                LanguageState.cta_btn_secondary,
                                class_name="flex items-center gap-1 bg-white/5 hover:bg-white/10 backdrop-blur-sm border border-white/10 text-white px-6 py-3 rounded-lg font-bold transition-all cursor-pointer",
                            ),
                            href="#",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-3 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-300"
                            ),
                            rx.el.span(
                                LanguageState.cta_check1,
                                class_name="text-xs text-slate-300 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-300"
                            ),
                            rx.el.span(
                                LanguageState.cta_check2,
                                class_name="text-xs text-slate-300 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-300"
                            ),
                            rx.el.span(
                                LanguageState.cta_check3,
                                class_name="text-xs text-slate-300 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-300"
                            ),
                            rx.el.span(
                                LanguageState.cta_check4,
                                class_name="text-xs text-slate-300 font-semibold",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-x-6 gap-y-2",
                    ),
                    class_name="relative text-center py-16 md:py-20 px-6 z-10",
                ),
                class_name="relative rounded-3xl bg-slate-900/70 backdrop-blur-xl border border-white/10 overflow-hidden",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="cta",
        class_name="relative py-16",
    )
