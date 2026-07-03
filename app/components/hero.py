import reflex as rx
from app.states.language_state import LanguageState


def _feature_check(text: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("check", size=12, class_name="text-emerald-600"),
            class_name="w-4 h-4 rounded-full bg-emerald-100 flex items-center justify-center",
        ),
        rx.el.span(text, class_name="text-sm text-slate-600 font-medium"),
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
                            class_name="text-[10px] text-slate-400 font-semibold tracking-widest",
                        ),
                        rx.el.p(
                            "USBGP",
                            class_name="text-slate-800 text-sm font-bold",
                        ),
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.span(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1.5 animate-pulse"
                    ),
                    "Online",
                    class_name="flex items-center text-[10px] font-semibold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full border border-emerald-200",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "VCPU",
                        class_name="text-[10px] text-slate-400 font-semibold",
                    ),
                    rx.el.p(
                        "8 Cores", class_name="text-slate-700 font-bold text-xs"
                    ),
                    class_name="bg-slate-50 border border-slate-100 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p(
                        "RAM",
                        class_name="text-[10px] text-slate-400 font-semibold",
                    ),
                    rx.el.p(
                        "16 GB", class_name="text-slate-700 font-bold text-xs"
                    ),
                    class_name="bg-slate-50 border border-slate-100 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p(
                        "NVME",
                        class_name="text-[10px] text-slate-400 font-semibold",
                    ),
                    rx.el.p(
                        "160 GB", class_name="text-slate-700 font-bold text-xs"
                    ),
                    class_name="bg-slate-50 border border-slate-100 rounded-md px-3 py-1.5",
                ),
                class_name="grid grid-cols-3 gap-2 mb-3",
            ),
            rx.el.div(
                rx.el.p(
                    "Bandwidth",
                    class_name="text-[10px] text-slate-400 font-semibold",
                ),
                rx.el.p(
                    "10 Gbps",
                    class_name="text-indigo-600 font-bold text-xs ml-auto",
                ),
                class_name="flex items-center justify-between mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full w-4/5 bg-gradient-to-r from-indigo-600 to-cyan-500 rounded-full"
                ),
                class_name="h-1 bg-slate-100 rounded-full mb-3 overflow-hidden",
            ),
            rx.el.div(
                rx.el.span(
                    "● 4.2 ms · Premium Routes",
                    class_name="text-[10px] text-emerald-600 font-medium",
                ),
                rx.el.span(
                    "99.99%",
                    class_name="text-[10px] text-indigo-600 font-bold ml-auto",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="w-72 rounded-2xl bg-white border border-slate-200/80 p-5 shadow-lg relative z-10",
        ),
        rx.el.div(
            rx.icon("play", size=14, class_name="text-white fill-white"),
            rx.el.span(
                LanguageState.hero_streaming,
                class_name="text-xs text-white font-semibold",
            ),
            class_name="absolute -top-4 -right-8 flex items-center gap-1.5 bg-gradient-to-r from-indigo-600 to-cyan-500 px-3 py-1.5 rounded-full shadow-md z-20",
        ),
        rx.el.div(
            rx.icon("globe", size=12, class_name="text-indigo-600"),
            rx.el.span(
                LanguageState.hero_pops,
                class_name="text-[10px] text-slate-600 font-semibold",
            ),
            class_name="absolute -bottom-4 left-8 flex items-center gap-1.5 bg-white border border-slate-200 px-3 py-1.5 rounded-full shadow-sm z-20",
        ),
        class_name="relative",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-2"
                    ),
                    rx.el.span(
                        LanguageState.hero_badge,
                        class_name="text-xs text-slate-600 font-semibold",
                    ),
                    rx.el.span("→", class_name="text-xs text-slate-400 ml-2"),
                    class_name="inline-flex items-center px-3 py-1 rounded-full bg-slate-50 border border-slate-200 backdrop-blur-sm mb-6",
                ),
                rx.el.h1(
                    rx.el.span(
                        LanguageState.hero_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                    ),
                    LanguageState.hero_title_suffix,
                    class_name="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-slate-900 leading-[1.15] mb-6 max-w-2xl",
                ),
                rx.el.p(
                    LanguageState.hero_desc,
                    class_name="text-lg text-slate-600 mb-8 max-w-xl leading-relaxed",
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
                            class_name="bg-indigo-600 hover:bg-indigo-500 text-white px-6 py-3 rounded-lg font-medium shadow-md hover:shadow-lg transition-all cursor-pointer",
                        ),
                        href="/shop/server",
                    ),
                    rx.el.button(
                        LanguageState.hero_btn_telegram,
                        class_name="border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 px-6 py-3 rounded-lg font-medium transition-all cursor-pointer shadow-xs",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex-1 relative z-10",
            ),
            rx.el.div(
                _floating_card(),
                class_name="hidden lg:flex flex-1 items-center justify-center relative",
            ),
            class_name="max-w-7xl mx-auto px-6 pt-32 pb-20 flex flex-col lg:flex-row items-center gap-12",
        ),
        rx.el.div(
            class_name="absolute -left-20 top-1/3 w-96 h-96 rounded-full bg-indigo-100/40 blur-[120px] pointer-events-none",
        ),
        rx.el.div(
            class_name="absolute right-0 bottom-0 w-96 h-96 rounded-full bg-cyan-100/40 blur-[120px] pointer-events-none",
        ),
        id="hero",
        class_name="relative overflow-hidden border-b border-slate-100 bg-white",
    )
