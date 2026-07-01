import reflex as rx


NODES: list[dict[str, str]] = [
    {
        "flag": "🇺🇸",
        "region": "Los Angeles",
        "code": "USBGP",
        "bandwidth": "10 Gbps",
        "latency": "142 ms",
        "line": "CN2 GIA · 4837",
        "load": "62",
    },
    {
        "flag": "🇯🇵",
        "region": "Tokyo",
        "code": "JPBGP",
        "bandwidth": "10 Gbps",
        "latency": "48 ms",
        "line": "IIJ · SoftBank BGP",
        "load": "71",
    },
    {
        "flag": "🇭🇰",
        "region": "Hong Kong",
        "code": "HKBGP",
        "bandwidth": "5 Gbps",
        "latency": "28 ms",
        "line": "HKIX · CN2 GIA",
        "load": "55",
    },
    {
        "flag": "🇸🇬",
        "region": "Singapore",
        "code": "SGBGP",
        "bandwidth": "5 Gbps",
        "latency": "62 ms",
        "line": "NTT · Telstra",
        "load": "44",
    },
    {
        "flag": "🇩🇪",
        "region": "Frankfurt",
        "code": "DEBGP",
        "bandwidth": "10 Gbps",
        "latency": "182 ms",
        "line": "DE-CIX · Cogent",
        "load": "38",
    },
    {
        "flag": "🇬🇧",
        "region": "London",
        "code": "UKBGP",
        "bandwidth": "5 Gbps",
        "latency": "195 ms",
        "line": "LINX · Level3",
        "load": "41",
    },
    {
        "flag": "🇰🇷",
        "region": "Seoul",
        "code": "KRBGP",
        "bandwidth": "3 Gbps",
        "latency": "52 ms",
        "line": "KT · LG U+",
        "load": "48",
    },
    {
        "flag": "🇹🇼",
        "region": "Taipei",
        "code": "TWBGP",
        "bandwidth": "3 Gbps",
        "latency": "55 ms",
        "line": "HINET · TWGATE",
        "load": "50",
    },
]


NETWORK_STATS: list[dict[str, str]] = [
    {"icon": "globe", "value": "100+", "label": "Global PoPs"},
    {"icon": "activity", "value": "10 Gbps", "label": "Peak per Node"},
    {"icon": "zap", "value": "< 30 ms", "label": "Intra-Asia Latency"},
    {"icon": "shield", "value": "200 Gbps", "label": "DDoS Mitigation"},
]


def _stat_card(s: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(s["icon"], size=16, class_name="text-blue-400"),
            class_name="w-10 h-10 rounded-lg bg-blue-500/10 border border-blue-500/20 flex items-center justify-center mb-3",
        ),
        rx.el.p(s["value"], class_name="text-2xl font-semibold text-white"),
        rx.el.p(
            s["label"],
            class_name="text-xs text-gray-500 uppercase tracking-wider",
        ),
        class_name="rounded-xl bg-white/[0.03] border border-white/10 p-5 backdrop-blur-sm hover:bg-white/[0.06] transition-colors",
    )


def _node_row(n: dict[str, str]) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.span(n["flag"], class_name="text-xl"),
                rx.el.div(
                    rx.el.p(
                        n["region"], class_name="text-white text-sm font-medium"
                    ),
                    rx.el.p(
                        n["code"],
                        class_name="text-[10px] text-gray-500 tracking-wider",
                    ),
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.icon("gauge", size=12, class_name="text-blue-400"),
                rx.el.span(
                    n["bandwidth"], class_name="text-sm text-gray-300 font-mono"
                ),
                class_name="flex items-center gap-1.5",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                n["latency"], class_name="text-sm text-emerald-400 font-mono"
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(n["line"], class_name="text-sm text-gray-400"),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        class_name="h-full bg-gradient-to-r from-blue-500 to-cyan-400 rounded-full",
                        style={"width": f"{n['load']}%"},
                    ),
                    class_name="w-24 h-1.5 bg-white/5 rounded-full overflow-hidden",
                ),
                rx.el.span(
                    f"{n['load']}%",
                    class_name="text-xs text-gray-400 font-mono",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5 animate-pulse"
                ),
                "Online",
                class_name="inline-flex items-center text-[10px] font-medium text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20",
            ),
            class_name="px-6 py-4",
        ),
        class_name="border-b border-white/5 hover:bg-white/[0.03] transition-colors",
    )


def nodes_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("globe", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        "Global Network",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Global backbone with ",
                    rx.el.span(
                        "BGP-optimized routes",
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "Distributed nodes across Asia, Europe and North America — direct peering, premium transit, low latency.",
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(NETWORK_STATS, _stat_card),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                class_name="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"
                            ),
                            rx.el.span(
                                "Live network status",
                                class_name="text-xs text-gray-300 font-medium",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.span(
                            "Updated 5s ago", class_name="text-xs text-gray-500"
                        ),
                        class_name="flex items-center justify-between px-6 py-4 border-b border-white/5",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Region",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        "Bandwidth",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        "Latency",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        "Line",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        "Load",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                    rx.el.th(
                                        "Status",
                                        class_name="text-left text-[10px] font-semibold text-gray-500 uppercase tracking-wider px-6 py-3",
                                    ),
                                ),
                                class_name="bg-white/[0.02]",
                            ),
                            rx.el.tbody(
                                rx.foreach(NODES, _node_row),
                            ),
                            class_name="table-auto w-full",
                        ),
                        class_name="overflow-x-auto",
                    ),
                    class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 backdrop-blur-sm overflow-hidden",
                ),
                class_name="",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="nodes",
        class_name="relative py-24 border-t border-white/5",
    )