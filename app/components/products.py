import reflex as rx
from app.states.language_state import LanguageState


def _tag(text: str, color: str) -> rx.Component:
    return rx.el.span(
        text,
        class_name=rx.match(
            color,
            (
                "blue",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-blue-500/15 text-blue-400 border border-blue-500/20",
            ),
            (
                "emerald",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-emerald-500/15 text-emerald-400 border border-emerald-500/20",
            ),
            (
                "purple",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-purple-500/15 text-purple-400 border border-purple-500/20",
            ),
            (
                "amber",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-amber-500/15 text-amber-400 border border-amber-500/20",
            ),
            (
                "rose",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-rose-500/15 text-rose-400 border border-rose-500/20",
            ),
            (
                "cyan",
                "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-cyan-500/15 text-cyan-400 border border-cyan-500/20",
            ),
            "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-gray-500/15 text-gray-400",
        ),
    )


def _spec_row(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=14, class_name="text-blue-400 shrink-0"),
        rx.el.span(text, class_name="text-sm text-gray-400"),
        class_name="flex items-center gap-2",
    )


def _product_card(p) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.icon(p["icon"], size=20, class_name="text-blue-400"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/20 flex items-center justify-center",
            ),
            _tag(p["tag"], p["tag_color"]),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            p["title"],
            class_name="text-white text-lg font-semibold mb-2 min-h-[1.75rem]",
        ),
        rx.el.p(
            p["desc"],
            class_name="text-sm text-gray-400 leading-relaxed mb-5 min-h-[3.5rem]",
        ),
        rx.el.div(
            _spec_row("cpu", p["spec1"]),
            _spec_row("gauge", p["spec2"]),
            _spec_row("shield", p["spec3"]),
            class_name="flex flex-col gap-2 mb-6 pb-6 border-b border-white/5",
        ),
        rx.el.div(
            rx.el.button(
                p["cta"],
                rx.icon(
                    "arrow-right",
                    size=14,
                    class_name="ml-1 group-hover/btn:translate-x-0.5 transition-transform",
                ),
                class_name="group/btn flex items-center text-sm text-white font-medium hover:text-blue-400 transition-colors",
            ),
            rx.el.span(
                LanguageState.products_cta_details,
                class_name="text-xs text-gray-500 group-hover:text-gray-300 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        href="/shop/server",
        class_name="group relative rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 hover:border-blue-500/30 hover:bg-white/[0.06] transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl hover:shadow-blue-500/10 backdrop-blur-sm flex flex-col",
    )


def products_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layers", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        LanguageState.products_badge,
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    LanguageState.products_title_prefix,
                    rx.el.span(
                        LanguageState.products_title_highlight,
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.products_desc,
                    class_name="text-gray-400 max-w-2xl mx-auto",
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
        class_name="relative py-24",
    )