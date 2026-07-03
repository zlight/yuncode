import reflex as rx
from app.states.language_state import LanguageState


def _tag(text: str, color: str) -> rx.Component:
    return rx.el.span(
        text,
        class_name=rx.match(
            color,
            (
                "blue",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-600 border border-indigo-100",
            ),
            (
                "emerald",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-600 border border-emerald-100",
            ),
            (
                "purple",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-purple-50 text-purple-600 border border-purple-100",
            ),
            (
                "amber",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-amber-50 text-amber-600 border border-amber-100",
            ),
            (
                "rose",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-rose-50 text-rose-600 border border-rose-100",
            ),
            (
                "cyan",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-cyan-50 text-cyan-600 border border-cyan-100",
            ),
            "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-slate-100 text-slate-600",
        ),
    )


def _spec_row(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=14, class_name="text-indigo-600 shrink-0"),
        rx.el.span(text, class_name="text-sm text-slate-600 font-medium"),
        class_name="flex items-center gap-2",
    )


def _product_card(p) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.icon(p["icon"], size=20, class_name="text-indigo-600"),
                class_name="w-11 h-11 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center",
            ),
            _tag(p["tag"], p["tag_color"]),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            p["title"],
            class_name="text-slate-900 text-lg font-bold mb-2 min-h-[1.75rem]",
        ),
        rx.el.p(
            p["desc"],
            class_name="text-sm text-slate-500 leading-relaxed mb-5 min-h-[3.5rem]",
        ),
        rx.el.div(
            _spec_row("cpu", p["spec1"]),
            _spec_row("gauge", p["spec2"]),
            _spec_row("shield", p["spec3"]),
            class_name="flex flex-col gap-2 mb-6 pb-6 border-b border-slate-100",
        ),
        rx.el.div(
            rx.el.button(
                p["cta"],
                rx.icon(
                    "arrow-right",
                    size=14,
                    class_name="ml-1 group-hover/btn:translate-x-0.5 transition-transform",
                ),
                class_name="group/btn flex items-center text-sm text-indigo-600 font-bold hover:text-indigo-700 transition-colors cursor-pointer",
            ),
            rx.el.span(
                LanguageState.products_cta_details,
                class_name="text-xs text-slate-400 group-hover:text-slate-600 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        href="/shop/server",
        class_name="group relative rounded-2xl bg-white border border-slate-200/80 p-6 hover:border-indigo-500 hover:shadow-md transition-all duration-300 hover:-translate-y-1 backdrop-blur-xs flex flex-col shadow-xs",
    )


def products_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layers", size=14, class_name="text-indigo-600"),
                    rx.el.span(
                        LanguageState.products_badge,
                        class_name="text-xs text-indigo-600 font-bold tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-100 mb-4",
                ),
                rx.el.h2(
                    LanguageState.products_title_prefix,
                    rx.el.span(
                        LanguageState.products_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-bold text-slate-900 tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.products_desc,
                    class_name="text-slate-500 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(LanguageState.products_list, _product_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="products",
        class_name="relative py-24 bg-slate-50/50 border-b border-slate-100",
    )
