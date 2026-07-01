import reflex as rx


PRODUCTS: list[dict[str, str]] = [
    {
        "icon": "zap",
        "tag": "Popular",
        "tag_color": "blue",
        "title": "Light Cloud Server",
        "desc": "Entry-grade streaming-unlocked VPS for personal use, tunnels and light apps.",
        "spec1": "1-4 vCPU · 1-8 GB RAM",
        "spec2": "500 Mbps – 1 Gbps",
        "spec3": "Native IP · Streaming Unlock",
        "cta": "Explore",
    },
    {
        "icon": "server",
        "tag": "Recommended",
        "tag_color": "emerald",
        "title": "Business Cloud Server",
        "desc": "Balanced performance, BGP-optimized routes for production workloads.",
        "spec1": "4-16 vCPU · 8-32 GB RAM",
        "spec2": "2 Gbps – 5 Gbps",
        "spec3": "SSD NVMe · DDoS 20 Gbps",
        "cta": "Explore",
    },
    {
        "icon": "cpu",
        "tag": "High Performance",
        "tag_color": "purple",
        "title": "Enterprise Compute",
        "desc": "AMD EPYC dedicated cores for latency-sensitive services and clusters.",
        "spec1": "8-64 vCPU · 32-256 GB RAM",
        "spec2": "5 Gbps – 10 Gbps",
        "spec3": "Dedicated CPU · Private Net",
        "cta": "Explore",
    },
    {
        "icon": "hard-drive",
        "tag": "Bare Metal",
        "tag_color": "amber",
        "title": "Dedicated Servers",
        "desc": "Fully-managed physical machines with custom hardware configurations.",
        "spec1": "Xeon / EPYC · up to 1 TB RAM",
        "spec2": "10 Gbps unmetered options",
        "spec3": "IPMI · Custom OS · RAID",
        "cta": "Explore",
    },
    {
        "icon": "radio-tower",
        "tag": "Streaming",
        "tag_color": "rose",
        "title": "Streaming Unlock VPS",
        "desc": "Native IPs unlocking Netflix, Disney+, HBO, TikTok and more.",
        "spec1": "2-8 vCPU · 4-16 GB RAM",
        "spec2": "1 Gbps – 3 Gbps",
        "spec3": "Native IP · Full Region Unlock",
        "cta": "Explore",
    },
    {
        "icon": "shield-check",
        "tag": "Secure",
        "tag_color": "cyan",
        "title": "Anti-DDoS Cloud",
        "desc": "Enterprise DDoS protection up to 200 Gbps with L7 mitigation.",
        "spec1": "4-16 vCPU · 8-32 GB RAM",
        "spec2": "Protected 100-200 Gbps",
        "spec3": "L3/L4/L7 Mitigation · WAF",
        "cta": "Explore",
    },
]


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


def _product_card(p: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(p["icon"], size=20, class_name="text-blue-400"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/20 flex items-center justify-center",
            ),
            _tag(p["tag"], p["tag_color"]),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            p["title"], class_name="text-white text-lg font-semibold mb-2"
        ),
        rx.el.p(
            p["desc"],
            class_name="text-sm text-gray-400 leading-relaxed mb-5 min-h-[3rem]",
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
                "View details",
                class_name="text-xs text-gray-500 group-hover:text-gray-300 transition-colors",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="group relative rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 hover:border-blue-500/30 hover:bg-white/[0.06] transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl hover:shadow-blue-500/10 backdrop-blur-sm",
    )


def products_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("layers", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        "Products",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Cloud services for ",
                    rx.el.span(
                        "every scenario",
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "From streaming-unlocked light servers to enterprise-grade dedicated hardware — one platform, one console, one bill.",
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(PRODUCTS, _product_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="products",
        class_name="relative py-24",
    )