import reflex as rx
from app.states.language_state import LanguageState


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="absolute inset-0 bg-[radial-gradient(ellipse_60%_100%_at_50%_50%,rgba(59,130,246,0.25),transparent)] pointer-events-none",
                ),
                rx.el.div(
                    class_name="absolute inset-0 opacity-[0.15] [background-image:linear-gradient(rgba(255,255,255,0.08)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.08)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_50%,black_40%,transparent_100%)]",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "sparkles", size=14, class_name="text-blue-300"
                        ),
                        rx.el.span(
                            LanguageState.cta_badge,
                            class_name="text-xs text-blue-200 font-medium tracking-wide uppercase",
                        ),
                        class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 mb-6",
                    ),
                    rx.el.h2(
                        LanguageState.cta_title_prefix,
                        rx.el.span(
                            LanguageState.cta_title_highlight,
                            class_name="bg-gradient-to-r from-blue-300 via-cyan-200 to-blue-300 bg-clip-text text-transparent",
                        ),
                        class_name="text-3xl md:text-5xl font-semibold text-white tracking-tight mb-4 max-w-3xl mx-auto",
                    ),
                    rx.el.p(
                        LanguageState.cta_desc,
                        class_name="text-gray-300 text-base md:text-lg mb-8 max-w-2xl mx-auto",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.cta_btn_primary,
                                rx.icon(
                                    "arrow-right", size=16, class_name="ml-1.5"
                                ),
                                class_name="flex items-center gap-1 bg-white hover:bg-gray-100 text-gray-900 px-6 py-3 rounded-lg font-medium shadow-2xl shadow-blue-500/40 transition-all",
                            ),
                            href="#pricing",
                        ),
                        rx.el.a(
                            rx.el.button(
                                rx.icon(
                                    "book-open", size=16, class_name="mr-1.5"
                                ),
                                LanguageState.cta_btn_secondary,
                                class_name="flex items-center gap-1 bg-white/10 hover:bg-white/15 border border-white/20 text-white px-6 py-3 rounded-lg font-medium backdrop-blur-sm transition-all",
                            ),
                            href="#",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-3 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-400"
                            ),
                            rx.el.span(
                                LanguageState.cta_check1,
                                class_name="text-xs text-gray-300",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-400"
                            ),
                            rx.el.span(
                                LanguageState.cta_check2,
                                class_name="text-xs text-gray-300",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-400"
                            ),
                            rx.el.span(
                                LanguageState.cta_check3,
                                class_name="text-xs text-gray-300",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        rx.el.div(
                            rx.icon(
                                "check", size=14, class_name="text-emerald-400"
                            ),
                            rx.el.span(
                                LanguageState.cta_check4,
                                class_name="text-xs text-gray-300",
                            ),
                            class_name="flex items-center gap-1.5",
                        ),
                        class_name="flex flex-wrap items-center justify-center gap-x-6 gap-y-2",
                    ),
                    class_name="relative text-center py-16 md:py-20 px-6",
                ),
                class_name="relative rounded-3xl bg-gradient-to-b from-blue-600/20 via-blue-900/20 to-[#0a0d14] border border-blue-500/20 overflow-hidden",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="cta",
        class_name="relative py-16 border-t border-white/5",
    )