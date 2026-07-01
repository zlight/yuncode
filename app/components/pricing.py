import reflex as rx
from app.states.pricing_state import PricingState


PLANS: list[dict[str, str | float | bool]] = [
    {
        "id": "starter",
        "name": "Starter",
        "tag": "",
        "desc": "For side projects and personal tunnels.",
        "price": 5.99,
        "vcpu": "1 vCPU",
        "ram": "1 GB RAM",
        "disk": "20 GB NVMe",
        "bandwidth": "500 Mbps",
        "traffic": "500 GB / mo",
        "features": "Native IP · IPv6 · Snapshot · Streaming Unlock",
        "highlight": False,
    },
    {
        "id": "standard",
        "name": "Standard",
        "tag": "Most Popular",
        "desc": "Balanced VPS for websites and small apps.",
        "price": 12.99,
        "vcpu": "2 vCPU",
        "ram": "4 GB RAM",
        "disk": "60 GB NVMe",
        "bandwidth": "1 Gbps",
        "traffic": "2 TB / mo",
        "features": "Native IP · Streaming Unlock · Daily Backup · DDoS 20 Gbps",
        "highlight": True,
    },
    {
        "id": "pro",
        "name": "Professional",
        "tag": "Recommended",
        "desc": "Production-grade compute with premium routes.",
        "price": 29.99,
        "vcpu": "4 vCPU",
        "ram": "8 GB RAM",
        "disk": "120 GB NVMe",
        "bandwidth": "2 Gbps",
        "traffic": "5 TB / mo",
        "features": "CN2 GIA · Native IP · Priority Support · DDoS 50 Gbps",
        "highlight": False,
    },
    {
        "id": "business",
        "name": "Business",
        "tag": "High Perf",
        "desc": "Dedicated cores for enterprise workloads.",
        "price": 69.99,
        "vcpu": "8 vCPU",
        "ram": "16 GB RAM",
        "disk": "240 GB NVMe",
        "bandwidth": "5 Gbps",
        "traffic": "10 TB / mo",
        "features": "Dedicated CPU · Private Net · 24/7 Support · DDoS 100 Gbps",
        "highlight": False,
    },
]


def _cycle_button(label: str, value: str, badge: str = "") -> rx.Component:
    return rx.el.button(
        label,
        rx.cond(
            badge != "",
            rx.el.span(
                badge,
                class_name="ml-1.5 text-[9px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-semibold",
            ),
            rx.fragment(),
        ),
        on_click=lambda: PricingState.set_cycle(value),
        class_name=rx.cond(
            PricingState.billing_cycle == value,
            "flex items-center px-4 py-1.5 rounded-md text-sm font-medium bg-white/10 text-white shadow-inner border border-white/10 transition-all",
            "flex items-center px-4 py-1.5 rounded-md text-sm font-medium text-gray-400 hover:text-white transition-all",
        ),
    )


def _feature_line(text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(
            "check", size=12, class_name="text-emerald-400 shrink-0 mt-0.5"
        ),
        rx.el.span(text, class_name="text-sm text-gray-400"),
        class_name="flex items-start gap-2",
    )


def _plan_card(p: dict) -> rx.Component:
    return rx.el.div(
        rx.cond(
            p["highlight"],
            rx.el.div(
                class_name="absolute -inset-px rounded-2xl bg-gradient-to-b from-blue-500/50 via-blue-500/20 to-transparent -z-10",
            ),
            rx.fragment(),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    p["name"].to(str),
                    class_name="text-white text-lg font-semibold",
                ),
                rx.cond(
                    p["tag"].to(str) != "",
                    rx.el.span(
                        p["tag"].to(str),
                        class_name=rx.cond(
                            p["highlight"],
                            "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-blue-500/20 text-blue-300 border border-blue-500/30",
                            "text-[10px] font-semibold px-2 py-0.5 rounded-md bg-white/5 text-gray-400 border border-white/10",
                        ),
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-start justify-between mb-2",
            ),
            rx.el.p(
                p["desc"].to(str),
                class_name="text-sm text-gray-500 mb-6 min-h-[2.5rem]",
            ),
            rx.el.div(
                rx.el.span(
                    "$",
                    class_name="text-2xl text-gray-400 font-semibold align-top",
                ),
                rx.el.span(
                    (
                        p["price"].to(float) * PricingState.cycle_multiplier
                    ).to_string(),
                    class_name="text-5xl text-white font-semibold tracking-tight",
                ),
                rx.el.span(
                    PricingState.cycle_label,
                    class_name="text-sm text-gray-500 ml-1",
                ),
                class_name="flex items-baseline mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("cpu", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        p["vcpu"].to(str), class_name="text-sm text-gray-300"
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon(
                        "memory-stick", size=14, class_name="text-blue-400"
                    ),
                    rx.el.span(
                        p["ram"].to(str), class_name="text-sm text-gray-300"
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("hard-drive", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        p["disk"].to(str), class_name="text-sm text-gray-300"
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("gauge", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        p["bandwidth"].to(str),
                        class_name="text-sm text-gray-300",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.icon("activity", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        p["traffic"].to(str), class_name="text-sm text-gray-300"
                    ),
                    class_name="flex items-center gap-2",
                ),
                class_name="flex flex-col gap-3 mb-6 pb-6 border-b border-white/5",
            ),
            _feature_line(p["features"].to(str)),
            rx.el.button(
                rx.cond(
                    p["highlight"],
                    "Buy Now",
                    "Get Started",
                ),
                rx.icon("arrow-right", size=14, class_name="ml-1.5"),
                class_name=rx.cond(
                    p["highlight"],
                    "mt-6 w-full flex items-center justify-center gap-1 py-3 rounded-lg bg-gradient-to-b from-blue-500 to-blue-600 hover:from-blue-400 hover:to-blue-500 text-white font-medium text-sm shadow-lg shadow-blue-500/30 transition-all",
                    "mt-6 w-full flex items-center justify-center gap-1 py-3 rounded-lg bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 text-white font-medium text-sm transition-all",
                ),
            ),
            rx.cond(
                PricingState.compare_mode,
                rx.el.button(
                    rx.cond(
                        PricingState.compared_plans.contains(p["id"].to(str)),
                        rx.el.span(
                            rx.icon("check", size=12, class_name="mr-1"),
                            "Selected for compare",
                            class_name="flex items-center justify-center text-xs text-blue-400",
                        ),
                        rx.el.span(
                            "Add to compare",
                            class_name="text-xs text-gray-500 hover:text-gray-300",
                        ),
                    ),
                    on_click=lambda: PricingState.toggle_plan_compare(
                        p["id"].to(str)
                    ),
                    class_name="mt-3 w-full py-2 rounded-md border border-dashed border-white/10 hover:border-blue-500/40 transition-colors",
                ),
                rx.fragment(),
            ),
            class_name="relative",
        ),
        class_name=rx.cond(
            p["highlight"],
            "relative rounded-2xl bg-gradient-to-b from-blue-500/[0.08] to-white/[0.02] border border-blue-500/30 p-7 backdrop-blur-sm hover:-translate-y-1 transition-all duration-300 shadow-2xl shadow-blue-500/10",
            "relative rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-7 backdrop-blur-sm hover:border-white/20 hover:-translate-y-1 transition-all duration-300",
        ),
    )


def pricing_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("tag", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        "Pricing",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Simple pricing, ",
                    rx.el.span(
                        "scale as you grow",
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "All plans include native IP, streaming unlock, DDoS protection and 24/7 monitoring.",
                    class_name="text-gray-400 max-w-2xl mx-auto mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        _cycle_button("Monthly", "monthly"),
                        _cycle_button("Quarterly", "quarterly", "-5%"),
                        _cycle_button("Yearly", "yearly", "-17%"),
                        class_name="inline-flex items-center gap-1 p-1 rounded-lg bg-white/[0.03] border border-white/10",
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
                            "Exit compare",
                            "Compare plans",
                        ),
                        on_click=PricingState.toggle_compare,
                        class_name="inline-flex items-center px-4 py-2 rounded-lg bg-white/[0.03] border border-white/10 text-sm text-gray-300 hover:text-white hover:border-white/20 transition-all",
                    ),
                    class_name="flex flex-wrap items-center justify-center gap-3",
                ),
                class_name="text-center mb-14",
            ),
            rx.cond(
                PricingState.is_loading,
                rx.el.div(
                    rx.foreach(
                        [1, 2, 3, 4],
                        lambda _: rx.el.div(
                            class_name="h-96 rounded-2xl bg-white/[0.03] border border-white/10 animate-pulse",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5",
                ),
                rx.el.div(
                    rx.foreach(PLANS, _plan_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5",
                ),
            ),
            rx.cond(
                PricingState.compare_mode
                & (PricingState.compared_plans.length() > 0),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "git-compare", size=16, class_name="text-blue-400"
                        ),
                        rx.el.span(
                            f"{PricingState.compared_plans.length()} plan(s) selected",
                            class_name="text-sm text-white font-medium",
                        ),
                        rx.el.span(
                            PricingState.compared_plans.join(", "),
                            class_name="text-xs text-gray-400 ml-2",
                        ),
                        rx.el.button(
                            "Compare now",
                            rx.icon("arrow-right", size=14, class_name="ml-1"),
                            class_name="ml-auto flex items-center gap-1 px-4 py-2 rounded-md bg-blue-500 hover:bg-blue-400 text-white text-sm font-medium transition-colors",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="fixed bottom-6 left-1/2 -translate-x-1/2 z-40 rounded-xl bg-[#141824]/95 backdrop-blur-xl border border-white/10 px-5 py-3 shadow-2xl",
                ),
                rx.fragment(),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("info", size=14, class_name="text-gray-500"),
                    rx.el.span(
                        "All prices in USD. Custom enterprise plans available on request.",
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.a(
                    "Contact sales",
                    rx.icon("arrow-right", size=12, class_name="ml-1"),
                    href="#",
                    class_name="flex items-center text-xs text-blue-400 hover:text-blue-300",
                ),
                class_name="flex flex-wrap items-center justify-between mt-10 pt-6 border-t border-white/5",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="pricing",
        class_name="relative py-24 border-t border-white/5",
    )