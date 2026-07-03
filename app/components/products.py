import reflex as rx
from app.states.language_state import LanguageState


def _tag(text: str, color: str) -> rx.Component:
    return rx.el.span(
        text,
        class_name=rx.match(
            color,
            (
                "blue",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-indigo-500/10 text-indigo-300 border border-indigo-500/30",
            ),
            (
                "emerald",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-500/10 text-emerald-300 border border-emerald-500/30",
            ),
            (
                "purple",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-violet-500/10 text-violet-300 border border-violet-500/30",
            ),
            (
                "amber",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-amber-500/10 text-amber-300 border border-amber-500/30",
            ),
            (
                "rose",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-rose-500/10 text-rose-300 border border-rose-500/30",
            ),
            (
                "cyan",
                "text-[10px] font-bold px-2 py-0.5 rounded-md bg-cyan-500/10 text-cyan-300 border border-cyan-500/30",
            ),
            "text-[10px] font-bold px-2 py-0.5 rounded-md bg-white/5 text-slate-300",
        ),
    )


def _spec_row(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=14, class_name="text-cyan-300 shrink-0"),
        rx.el.span(text, class_name="text-sm text-slate-300 font-medium"),
        class_name="flex items-center gap-2",
    )


def _product_card(p) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            class_name="absolute inset-0 rounded-2xl bg-gradient-to-br from-indigo-500/0 via-transparent to-cyan-500/0 group-hover:from-indigo-500/10 group-hover:to-cyan-500/10 transition-all duration-500 pointer-events-none",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(p["icon"], size=20, class_name="text-white"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center shadow-lg shadow-indigo-500/10",
            ),
            _tag(p["tag"], p["tag_color"]),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            p["title"],
            class_name="text-white text-lg font-bold mb-2 min-h-[1.75rem]",
        ),
        rx.el.p(
            p["desc"],
            class_name="text-sm text-slate-400 leading-relaxed mb-5 min-h-[3.5rem]",
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
                    class_name="ml-1 group-hover:translate-x-0.5 transition-transform",
                ),
                class_name="flex items-center text-sm text-cyan-300 font-bold hover:text-cyan-200 transition-colors cursor-pointer",
            ),
            rx.el.span(
                LanguageState.products_cta_details,
                class_name="text-xs text-slate-500 group-hover:text-slate-300 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        href="/shop/server",
        class_name="group relative rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-6 hover:border-cyan-500/40 hover:shadow-2xl hover:shadow-cyan-500/10 transition-all duration-300 hover:-translate-y-1 flex flex-col overflow-hidden",
    )


def products_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layers", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        LanguageState.products_badge,
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    LanguageState.products_title_prefix,
                    rx.el.span(
                        LanguageState.products_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.products_desc,
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(LanguageState.products_list, _product_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="products",
        class_name="relative py-24",
    )
