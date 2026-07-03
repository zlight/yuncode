import reflex as rx
from app.states.language_state import LanguageState


def _feature_check(text: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("check", size=12, class_name="text-cyan-300"),
            class_name="w-5 h-5 rounded-full bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center",
        ),
        rx.el.span(text, class_name="text-sm text-slate-300 font-medium"),
        class_name="flex items-center gap-2",
    )


def _floating_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute -inset-4 bg-gradient-to-br from-indigo-500/30 via-cyan-500/20 to-transparent rounded-3xl blur-2xl -z-10",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span("🇺🇸", class_name="text-xl"),
                    rx.el.div(
                        rx.el.p(
                            "LOS ANGELES",
                            class_name="text-[10px] text-slate-500 font-bold tracking-widest",
                        ),
                        rx.el.p(
                            "USBGP",
                            class_name="text-white text-sm font-bold",
                        ),
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.span(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse shadow-lg shadow-emerald-400/50"
                    ),
                    "Online",
                    class_name="flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/30",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "VCPU",
                        class_name="text-[10px] text-slate-500 font-bold",
                    ),
                    rx.el.p(
                        "8 Cores", class_name="text-slate-100 font-bold text-xs"
                    ),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p(
                        "RAM", class_name="text-[10px] text-slate-500 font-bold"
                    ),
                    rx.el.p(
                        "16 GB", class_name="text-slate-100 font-bold text-xs"
                    ),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                rx.el.div(
                    rx.el.p(
                        "NVME",
                        class_name="text-[10px] text-slate-500 font-bold",
                    ),
                    rx.el.p(
                        "160 GB", class_name="text-slate-100 font-bold text-xs"
                    ),
                    class_name="bg-white/5 border border-white/10 rounded-md px-3 py-1.5",
                ),
                class_name="grid grid-cols-3 gap-2 mb-3",
            ),
            rx.el.div(
                rx.el.p(
                    "Bandwidth",
                    class_name="text-[10px] text-slate-500 font-bold",
                ),
                rx.el.p(
                    "10 Gbps",
                    class_name="text-cyan-300 font-bold text-xs ml-auto",
                ),
                class_name="flex items-center justify-between mb-2",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full w-4/5 bg-gradient-to-r from-indigo-500 to-cyan-400 rounded-full shadow-lg shadow-cyan-500/50"
                ),
                class_name="h-1.5 bg-white/5 rounded-full mb-3 overflow-hidden",
            ),
            rx.el.div(
                rx.el.span(
                    "● 4.2 ms · Premium Routes",
                    class_name="text-[10px] text-emerald-300 font-medium",
                ),
                rx.el.span(
                    "99.99%",
                    class_name="text-[10px] text-cyan-300 font-bold ml-auto",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="w-72 rounded-2xl bg-slate-900/80 backdrop-blur-xl border border-white/10 p-5 shadow-2xl shadow-black/40 relative z-10",
        ),
        rx.el.div(
            rx.icon("play", size=14, class_name="text-white fill-white"),
            rx.el.span(
                LanguageState.hero_streaming,
                class_name="text-xs text-white font-semibold",
            ),
            class_name="absolute -top-4 -right-8 flex items-center gap-1.5 bg-gradient-to-r from-indigo-500 to-cyan-400 px-3 py-1.5 rounded-full shadow-xl shadow-indigo-500/40 z-20",
        ),
        rx.el.div(
            rx.icon("globe", size=12, class_name="text-cyan-300"),
            rx.el.span(
                LanguageState.hero_pops,
                class_name="text-[10px] text-slate-200 font-semibold",
            ),
            class_name="absolute -bottom-4 left-8 flex items-center gap-1.5 bg-slate-900/90 backdrop-blur-xl border border-white/10 px-3 py-1.5 rounded-full shadow-lg z-20",
        ),
        class_name="relative",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-2 shadow-lg shadow-emerald-400/50 animate-pulse"
                    ),
                    rx.el.span(
                        LanguageState.hero_badge,
                        class_name="text-xs text-slate-200 font-semibold",
                    ),
                    rx.el.span("→", class_name="text-xs text-slate-500 ml-2"),
                    class_name="inline-flex items-center px-3 py-1 rounded-full bg-white/5 border border-white/10 backdrop-blur-sm mb-6",
                ),
                rx.el.h1(
                    rx.el.span(
                        LanguageState.hero_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    LanguageState.hero_title_suffix,
                    class_name="text-4xl md:text-5xl lg:text-6xl font-extrabold tracking-tight text-white leading-[1.1] mb-6 max-w-2xl",
                ),
                rx.el.p(
                    LanguageState.hero_desc,
                    class_name="text-lg text-slate-400 mb-8 max-w-xl leading-relaxed",
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
                            rx.icon(
                                "arrow-right", size=16, class_name="ml-1.5"
                            ),
                            class_name="flex items-center bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white px-6 py-3 rounded-lg font-semibold shadow-xl shadow-indigo-500/30 transition-all cursor-pointer",
                        ),
                        href="/shop/server",
                    ),
                    rx.el.button(
                        rx.icon("send", size=15, class_name="mr-1.5"),
                        LanguageState.hero_btn_telegram,
                        class_name="flex items-center border border-white/10 bg-white/5 hover:bg-white/10 backdrop-blur-sm text-slate-100 px-6 py-3 rounded-lg font-semibold transition-all cursor-pointer",
                    ),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex-1 relative z-10",
            ),
            rx.el.div(
                _floating_card(),
                class_name="hidden lg:flex flex-1 items-center justify-center relative",
            ),
            class_name="max-w-7xl mx-auto px-6 pt-32 pb-24 flex flex-col lg:flex-row items-center gap-12 relative z-10",
        ),
        id="hero",
        class_name="relative overflow-hidden",
    )
