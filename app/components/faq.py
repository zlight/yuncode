import reflex as rx
from app.states.ui_state import UIState
from app.states.language_state import LanguageState


def _faq_item(f) -> rx.Component:
    is_open = UIState.open_faq == f["id"]
    return rx.el.div(
        rx.el.button(
            rx.el.div(
                rx.el.span(
                    f["q"],
                    class_name="text-white text-base font-semibold text-left",
                ),
                rx.el.div(
                    rx.icon(
                        rx.cond(is_open, "minus", "plus"),
                        size=16,
                        class_name="text-cyan-300",
                    ),
                    class_name=rx.cond(
                        is_open,
                        "w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/40 flex items-center justify-center shrink-0 transition-all",
                        "w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center shrink-0 transition-all",
                    ),
                ),
                class_name="flex items-center justify-between gap-4 w-full",
            ),
            on_click=lambda: UIState.toggle_faq(f["id"]),
            class_name="w-full px-6 py-5 text-left hover:bg-white/[0.02] transition-colors cursor-pointer",
        ),
        rx.cond(
            is_open,
            rx.el.div(
                rx.el.p(
                    f["a"],
                    class_name="text-sm text-slate-400 leading-relaxed font-medium",
                ),
                class_name="px-6 pb-5 -mt-1 border-t border-white/5 pt-4",
            ),
            rx.fragment(),
        ),
        class_name=rx.cond(
            is_open,
            "rounded-xl bg-slate-900/60 backdrop-blur-xl border border-cyan-500/30 shadow-lg shadow-cyan-500/10 transition-all",
            "rounded-xl bg-slate-900/40 backdrop-blur-xl border border-white/5 hover:border-white/15 transition-all",
        ),
    )


def _support_channel(c) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(c["icon"], size=18, class_name="text-cyan-300"),
            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mb-4",
        ),
        rx.el.h4(c["title"], class_name="text-white font-bold text-sm mb-1"),
        rx.el.p(
            c["desc"],
            class_name="text-xs text-slate-400 mb-3 min-h-[2.5rem] font-medium",
        ),
        rx.el.span(
            c["action"],
            rx.icon("arrow-right", size=12, class_name="ml-1"),
            class_name="inline-flex items-center text-xs text-cyan-300 font-bold hover:text-cyan-200",
        ),
        href="#",
        class_name="block rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/40 hover:-translate-y-0.5 transition-all",
    )


def faq_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("circle_help", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        LanguageState.faq_badge,
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    LanguageState.faq_title_prefix,
                    rx.el.span(
                        LanguageState.faq_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.faq_desc,
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(LanguageState.faq_list, _faq_item),
                    class_name="flex flex-col gap-3",
                ),
                class_name="max-w-3xl mx-auto mb-16",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        LanguageState.faq_still_questions,
                        class_name="text-2xl font-bold text-white mb-2",
                    ),
                    rx.el.p(
                        LanguageState.faq_help_desc,
                        class_name="text-slate-400 font-medium",
                    ),
                    class_name="text-center mb-8",
                ),
                rx.el.div(
                    rx.foreach(
                        LanguageState.support_channels, _support_channel
                    ),
                    class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="faq",
        class_name="relative py-24",
    )
