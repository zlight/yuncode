import reflex as rx
from app.states.pricing_state import PricingState
from app.states.language_state import LanguageState


def _cycle_button(label, value: str, badge: str = "") -> rx.Component:
    return rx.el.button(
        label,
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-1.5 text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30",
            ),
            rx.fragment(),
        ),
        on_click=lambda: PricingState.set_cycle(value),
        class_name=rx.cond(
            PricingState.billing_cycle == value,
            "flex items-center px-4 py-1.5 rounded-md text-sm font-bold bg-gradient-to-r from-indigo-500 to-cyan-500 text-white shadow-lg shadow-indigo-500/30 transition-all cursor-pointer",
            "flex items-center px-4 py-1.5 rounded-md text-sm font-medium text-slate-300 hover:text-white transition-all cursor-pointer",
        ),
    )


def _feature_line(text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(
            "check", size=12, class_name="text-emerald-300 shrink-0 mt-0.5"
        ),
        rx.el.span(text, class_name="text-sm text-slate-300 font-medium"),
        class_name="flex items-start gap-2",
    )


def _plan_card(p: dict) -> rx.Component:
    return rx.el.div(
        rx.cond(
            p["highlight"],
            rx.el.div(
                class_name="absolute -inset-px rounded-2xl bg-gradient-to-b from-cyan-400/40 via-indigo-500/20 to-transparent -z-10 blur-sm",
            ),
            rx.fragment(),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    p["name"].to(str),
                    class_name="text-white text-lg font-bold",
                ),
                rx.cond(
                    p["tag"].to(str) != "",
                    rx.el.span(
                        p["tag"].to(str),
                        class_name=rx.cond(
                            p["highlight"],
                            "text-[10px] font-bold px-2 py-0.5 rounded-md bg-cyan-500/10 text-cyan-300 border border-cyan-500/30",
                            "text-[10px] font-bold px-2 py-0.5 rounded-md bg-white/5 text-slate-300 border border-white/10",
                        ),
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-start justify-between mb-2",
            ),
            rx.el.p(
                p["desc"].to(str),
                class_name="text-sm text-slate-500 mb-6 min-h-[2.5rem] font-medium",
            ),
            rx.el.div(
                rx.el.span(
                    "$",
                    class_name="text-2xl text-slate-500 font-bold align-top",
                ),
                rx.el.span(
                    (
                        p["price"].to(float) * PricingState.cycle_multiplier
                    ).to_string(),
                    class_name="text-5xl text-white font-extrabold tracking-tight",
                ),
                rx.el.span(
                    PricingState.cycle_label,
                    class_name="text-sm text-slate-500 font-bold ml-1",
                ),
                class_name="flex items-baseline mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("cpu", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        p["vcpu"].to(str),
                        class_name="text-sm text-slate-200 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon(
                        "memory-stick", size=14, class_name="text-cyan-300"
                    ),
                    rx.el.span(
                        p["ram"].to(str),
                        class_name="text-sm text-slate-200 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("hard-drive", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        p["disk"].to(str),
                        class_name="text-sm text-slate-200 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("gauge", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        p["bandwidth"].to(str),
                        class_name="text-sm text-slate-200 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("activity", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        p["traffic"].to(str),
                        class_name="text-sm text-slate-200 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col gap-3 mb-6 pb-6 border-b border-white/5",
            ),
            _feature_line(p["features"].to(str)),
            rx.el.a(
                rx.el.button(
                    rx.cond(
                        p["highlight"],
                        LanguageState.pricing_buy_now,
                        LanguageState.pricing_get_started,
                    ),
                    rx.icon("arrow-right", size=14, class_name="ml-1.5"),
                    class_name=rx.cond(
                        p["highlight"],
                        "flex items-center justify-center gap-1 py-3 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white font-bold text-sm shadow-lg shadow-indigo-500/30 transition-all cursor-pointer w-full",
                        "flex items-center justify-center gap-1 py-3 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 text-slate-100 font-bold text-sm transition-all cursor-pointer w-full",
                    ),
                ),
                href="/shop/server",
                class_name="mt-6 block",
            ),
            rx.cond(
                PricingState.compare_mode,
                rx.el.button(
                    rx.cond(
                        PricingState.compared_plans.contains(p["id"].to(str)),
                        rx.el.span(
                            rx.icon("check", size=12, class_name="mr-1"),
                            LanguageState.pricing_selected_compare,
                            class_name="flex items-center justify-center text-xs text-cyan-300 font-bold",
                        ),
                        rx.el.span(
                            LanguageState.pricing_add_compare,
                            class_name="text-xs text-slate-500 hover:text-slate-300 font-medium",
                        ),
                    ),
                    on_click=lambda: PricingState.toggle_plan_compare(
                        p["id"].to(str)
                    ),
                    class_name="mt-3 w-full py-2 rounded-md border border-dashed border-white/10 hover:border-cyan-500/50 hover:bg-cyan-500/5 transition-all cursor-pointer",
                ),
                rx.fragment(),
            ),
            class_name="relative",
        ),
        class_name=rx.cond(
            p["highlight"],
            "relative rounded-2xl bg-slate-900/70 backdrop-blur-xl border border-cyan-500/40 p-7 hover:-translate-y-1 transition-all duration-300 shadow-2xl shadow-cyan-500/20",
            "relative rounded-2xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-7 hover:border-white/20 hover:-translate-y-1 transition-all duration-300",
        ),
    )


def pricing_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("tag", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        LanguageState.pricing_badge,
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    LanguageState.pricing_title_prefix,
                    rx.el.span(
                        LanguageState.pricing_title_highlight,
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    LanguageState.pricing_desc,
                    class_name="text-slate-400 max-w-2xl mx-auto mb-8 font-medium",
                ),
                rx.el.div(
                    rx.el.div(
                        _cycle_button(
                            LanguageState.pricing_cycle_monthly, "monthly"
                        ),
                        _cycle_button(
                            LanguageState.pricing_cycle_quarterly,
                            "quarterly",
                            "-5%",
                        ),
                        _cycle_button(
                            LanguageState.pricing_cycle_yearly, "yearly", "-17%"
                        ),
                        class_name="inline-flex items-center gap-1 p-1 rounded-lg bg-slate-900/60 backdrop-blur-xl border border-white/10",
                    ),
                    rx.el.button(
                        rx.icon(
                            rx.cond(
                                PricingState.compare_mode, "x", "git-compare"
                            ),
                            size=14,
                            class_name="mr-1.5",
                        ),
                        rx.cond(
                            PricingState.compare_mode,
                            LanguageState.pricing_exit_compare,
                            LanguageState.pricing_compare,
                        ),
                        on_click=PricingState.toggle_compare,
                        class_name="inline-flex items-center px-4 py-2 rounded-lg bg-slate-900/60 backdrop-blur-xl border border-white/10 text-sm font-semibold text-slate-200 hover:text-white hover:bg-white/5 transition-all cursor-pointer",
                    ),
                    class_name="flex flex-wrap items-center justify-center gap-3",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(LanguageState.pricing_plans, _plan_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5",
            ),
            rx.cond(
                PricingState.compare_mode
                & (PricingState.compared_plans.length() > 0),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "git-compare", size=16, class_name="text-cyan-300"
                        ),
                        rx.el.span(
                            f"{PricingState.compared_plans.length()} ",
                            LanguageState.pricing_plans_selected,
                            class_name="text-sm text-white font-bold",
                        ),
                        rx.el.span(
                            PricingState.compared_plans.join(", "),
                            class_name="text-xs text-slate-400 ml-2 font-medium",
                        ),
                        rx.el.button(
                            LanguageState.pricing_compare_now,
                            rx.icon("arrow-right", size=14, class_name="ml-1"),
                            class_name="ml-auto flex items-center gap-1 px-4 py-2 rounded-md bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-sm font-bold cursor-pointer",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 rounded-xl bg-slate-950/90 backdrop-blur-xl border border-white/10 px-5 py-3 shadow-2xl w-[90vw] max-w-lg",
                ),
                rx.fragment(),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("info", size=14, class_name="text-slate-500"),
                    rx.el.span(
                        LanguageState.pricing_footer_note,
                        class_name="text-xs text-slate-500 font-semibold",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.a(
                    LanguageState.pricing_contact_sales,
                    rx.icon("arrow-right", size=12, class_name="ml-1"),
                    href="#",
                    class_name="flex items-center text-xs text-cyan-300 hover:text-cyan-200 font-bold",
                ),
                class_name="flex flex-wrap items-center justify-between mt-10 pt-6 border-t border-white/5",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="pricing",
        class_name="relative py-24",
    )
