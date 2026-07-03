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
                    class_name="text-slate-800 text-base font-semibold text-left",
                ),
                rx.el.div(
                    rx.icon(
                        rx.cond(is_open, "minus", "plus"),
                        size=16,
                        class_name="text-indigo-600",
                    ),
                    class_name=rx.cond(
                        is_open,
                        "w-8 h-8 rounded-lg bg-indigo-50 border border-indigo-200 flex items-center justify-center shrink-0 transition-all",
                        "w-8 h-8 rounded-lg bg-slate-50 border border-slate-200 flex items-center justify-center shrink-0 transition-all",
                    ),
                ),
                class_name="flex items-center justify-between gap-4 w-full",
            ),
            on_click=lambda: UIState.toggle_faq(f["id"]),
            class_name="w-full px-6 py-5 text-left hover:bg-slate-50/50 transition-colors cursor-pointer",
            aria_expanded=is_open.to_string(),
        ),
        rx.cond(
            is_open,
            rx.el.div(
                rx.el.p(
                    f["a"],
                    class_name="text-sm text-slate-600 leading-relaxed font-medium",
                ),
                class_name="px-6 pb-5 -mt-1 border-t border-slate-100/50 pt-4",
            ),
            rx.fragment(),
        ),
        class_name=rx.cond(
            is_open,
            "rounded-xl bg-white border border-indigo-500/30 shadow-sm transition-all",
            "rounded-xl bg-white border border-slate-200/80 hover:border-slate-300 transition-all",
        ),
    )


def _support_channel(c) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(c["icon"], size=18, class_name="text-indigo-600"),
            class_name="w-11 h-11 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center mb-4",
        ),
        rx.el.h4(
            c["title"], class_name="text-slate-800 font-bold text-sm mb-1"
        ),
        rx.el.p(
            c["desc"],
            class_name="text-xs text-slate-500 mb-3 min-h-[2.5rem] font-medium",
        ),
        rx.el.span(
            c["action"],
            rx.icon("arrow-right", size=12, class_name="ml-1"),
            class_name="inline-flex items-center text-xs text-indigo-600 font-bold hover:text-indigo-700",
        ),
        href="#",
        class_name="block rounded-2xl bg-white border border-slate-200 p-5 hover:border-indigo-500 hover:-translate-y-0.5 transition-all shadow-xs",
    )


def faq_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "circle_help", size=14, class_name="text-indigo-600"
                    ),
                    rx.el.span(
                        LanguageState.faq_badge,
                        class_name="text-xs text-indigo-600 font-bold tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 mb-4",
                ),
                rx.el.h2(
                    LanguageState.faq_title_prefix,
                    rx.el.span(
                        LanguageState.faq_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.faq_desc,
                    class_name="text-slate-500 max-w-2xl mx-auto font-medium",
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
                        class_name="text-2xl font-bold text-slate-900 mb-2",
                    ),
                    rx.el.p(
                        LanguageState.faq_help_desc,
                        class_name="text-slate-500 font-medium",
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
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="faq",
        class_name="relative py-24 bg-slate-50/50 border-b border-slate-100",
    )
