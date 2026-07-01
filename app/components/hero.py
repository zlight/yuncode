import reflex as rx
from app.states.language_state import LanguageState


def _feature_check(text: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("check", size=12, class_name="text-emerald-400"),
            class_name="w-4 h-4 rounded-full bg-emerald-500/20 flex items-center justify-center",
        ),
        rx.el.span(text, class_name="text-sm text-gray-300"),
        class_name="flex items-center gap-2",
    )


def _floating_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span("🇺🇸", class_name="text-xl"),
                    rx.el.div(
                        rx.el.p(
                            "LOS ANGELES",
                            class_name="text-[10px] text-gray-500 tracking-widest",
                        ),
                        rx.el.p(
                            "USBGP",
                            class_name="text-white text-sm font-semibold",
                        ),
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.span(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"
                    ),
                    "Online",
                    class_name="flex items-center text-[10px] font-medium text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p("VCPU", class_name="text-[10px] text-gray-500"),
                    rx.el.p("8", class_name="text-white font-semibold"),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p("RAM", class_name="text-[10px] text-gray-500"),
                    rx.el.p(
                        "16 GB", class_name="text-white font-semibold text-sm"
                    ),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p("NVME", class_name="text-[10px] text-gray-500"),
                    rx.el.p(
                        "160 G", class_name="text-white font-semibold text-sm"
                    ),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                class_name="grid grid-cols-3 gap-2 mb-3",
            ),
            rx.el.div(
                rx.el.p("Bandwidth", class_name="text-[10px] text-gray-500"),
                rx.el.p(
                    "10 Gbps",
                    class_name="text-blue-400 font-semibold text-sm ml-auto",
                ),
                class_name="flex items-center justify-between mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full w-4/5 bg-gradient-to-r from-blue-500 to-cyan-400 rounded-full"
                ),
                class_name="h-1 bg-white/5 rounded-full mb-3 overflow-hidden",
            ),
            rx.el.div(
                rx.el.span(
                    "● 4.2 ms · BGP optimized",
                    class_name="text-[10px] text-emerald-400",
                ),
                rx.el.span(
                    "99.99%",
                    class_name="text-[10px] text-blue-400 font-semibold ml-auto",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="w-72 rounded-2xl bg-gradient-to-b from-[#141824]/90 to-[#0d1018]/90 backdrop-blur-xl border border-white/10 p-5 shadow-2xl shadow-blue-500/10",
        ),
        rx.el.div(
            rx.icon("play", size=14, class_name="text-white fill-white"),
            rx.el.span(
                LanguageState.hero_streaming,
                class_name="text-xs text-white font-medium",
            ),
            class_name="absolute -top-4 -right-8 flex items-center gap-1.5 bg-[#141824]/95 backdrop-blur-xl border border-white/10 px-3 py-1.5 rounded-full shadow-lg",
        ),
        rx.el.div(
            rx.icon("globe", size=12, class_name="text-blue-400"),
            rx.el.span(
                LanguageState.hero_pops, class_name="text-[10px] text-gray-300"
            ),
            class_name="absolute -bottom-4 left-8 flex items-center gap-1.5 bg-[#141824]/95 backdrop-blur-xl border border-white/10 px-3 py-1.5 rounded-full shadow-lg",
        ),
        class_name="relative",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2"
                    ),
                    rx.el.span(
                        LanguageState.hero_badge,
                        class_name="text-xs text-gray-300 font-medium",
                    ),
                    rx.el.span("→", class_name="text-xs text-gray-500 ml-2"),
                    class_name="inline-flex items-center px-3 py-1 rounded-full bg-white/5 border border-white/10 backdrop-blur-sm mb-6",
                ),
                rx.el.h1(
                    rx.el.span(
                        LanguageState.hero_title_highlight,
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    LanguageState.hero_title_suffix,
                    class_name="text-4xl md:text-5xl lg:text-6xl font-semibold tracking-tight text-white leading-[1.1] mb-6 max-w-2xl",
                ),
                rx.el.p(
                    LanguageState.hero_desc,
                    class_name="text-lg text-gray-400 mb-8 max-w-xl",
                ),
                rx.el.div(
                    _feature_check(LanguageState.hero_feature1),
                    _feature_check(LanguageState.hero_feature2),
                    _feature_check(LanguageState.hero_feature3),
                    class_name="flex flex-wrap items-center gap-6 mb-10",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            LanguageState.hero_btn_overview,
                            class_name="bg-gradient-to-b from-blue-500 to-blue-600 hover:from-blue-400 hover:to-blue-500 text-white px-6 py-3 rounded-lg font-medium shadow-lg shadow-blue-500/30 transition-all cursor-pointer",
                        ),
                        href="#products",
                    ),
                    rx.el.button(
                        LanguageState.hero_btn_telegram,
                        class_name="border border-white/10 hover:border-white/20 hover:bg-white/5 text-white px-6 py-3 rounded-lg font-medium transition-all cursor-pointer",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex-1 relative z-10",
            ),
            rx.el.div(
                _floating_card(),
                class_name="hidden lg:flex flex-1 items-center justify-center relative",
            ),
            class_name="max-w-7xl mx-auto px-6 pt-40 pb-24 flex flex-col lg:flex-row items-center gap-12",
        ),
        rx.el.div(
            class_name="absolute inset-0 bg-[radial-gradient(ellipse_80%_60%_at_50%_-10%,rgba(59,130,246,0.15),transparent)] pointer-events-none",
        ),
        rx.el.div(
            class_name="absolute -left-20 top-1/3 w-96 h-96 rounded-full bg-purple-500/10 blur-[120px] pointer-events-none",
        ),
        rx.el.div(
            class_name="absolute right-0 bottom-0 w-96 h-96 rounded-full bg-blue-500/10 blur-[120px] pointer-events-none",
        ),
        id="hero",
        class_name="relative overflow-hidden",
    )