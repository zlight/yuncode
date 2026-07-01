import reflex as rx
from app.states.shop_state import ShopState
from app.states.language_state import LanguageState


def _machine_type_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.machine_type == item["id"]
    return rx.el.button(
        rx.icon(item["icon"], size=16),
        rx.el.span(item["label"], class_name="text-sm font-medium"),
        on_click=lambda: ShopState.set_machine_type(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-gradient-to-b from-blue-500/25 to-blue-500/10 border border-blue-500/50 text-white shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
            "flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-white/[0.03] border border-white/10 text-gray-300 hover:bg-white/[0.06] hover:border-white/20 hover:text-white transition-all cursor-pointer",
        ),
    )


def _region_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_region == item["id"]
    return rx.el.button(
        rx.el.span(item["flag"], class_name="text-lg"),
        rx.el.span(item["name"], class_name="text-sm font-medium"),
        on_click=lambda: ShopState.set_region(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-gradient-to-b from-blue-500/25 to-blue-500/10 border border-blue-500/50 text-white shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white/[0.03] border border-white/10 text-gray-300 hover:bg-white/[0.06] hover:border-white/20 hover:text-white transition-all cursor-pointer",
        ),
    )


def _node_button(node: rx.Var) -> rx.Component:
    is_active = ShopState.selected_node == node
    return rx.el.button(
        rx.el.span("🇲🇴", class_name="text-base"),
        rx.el.span(node, class_name="text-sm font-medium"),
        on_click=lambda: ShopState.set_node(node.to(str)),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-gradient-to-b from-blue-500/25 to-blue-500/10 border border-blue-500/50 text-white shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white/[0.03] border border-white/10 text-gray-300 hover:bg-white/[0.06] hover:border-white/20 hover:text-white transition-all cursor-pointer",
        ),
    )


def _system_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_system == item["id"]
    return rx.el.button(
        rx.icon(item["icon"], size=14, class_name="text-blue-400"),
        rx.el.span(item["label"], class_name="text-sm font-medium"),
        on_click=lambda: ShopState.set_system(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-gradient-to-b from-blue-500/25 to-blue-500/10 border border-blue-500/50 text-white shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
            "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white/[0.03] border border-white/10 text-gray-300 hover:bg-white/[0.06] hover:border-white/20 hover:text-white transition-all cursor-pointer",
        ),
    )


def _cycle_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_cycle == item["id"]
    return rx.el.button(
        rx.el.span(item["label"], class_name="text-sm font-medium"),
        on_click=lambda: ShopState.set_cycle(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "px-4 py-2 rounded-lg bg-gradient-to-b from-blue-500/25 to-blue-500/10 border border-blue-500/50 text-white shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
            "px-4 py-2 rounded-lg bg-white/[0.03] border border-white/10 text-gray-300 hover:bg-white/[0.06] hover:border-white/20 hover:text-white transition-all cursor-pointer",
        ),
    )


def _stock_badge(stock: rx.Var) -> rx.Component:
    return rx.cond(
        stock == 0,
        rx.el.span(
            rx.el.span(
                class_name="w-1.5 h-1.5 rounded-full bg-rose-400 mr-1.5"
            ),
            LanguageState.shop_sold_out,
            class_name="inline-flex items-center text-[10px] font-medium text-rose-400 bg-rose-500/10 px-2 py-0.5 rounded-full border border-rose-500/20",
        ),
        rx.cond(
            stock < 10,
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-amber-400 mr-1.5 animate-pulse"
                ),
                LanguageState.shop_stock_low,
                " · ",
                stock.to_string(),
                class_name="inline-flex items-center text-[10px] font-medium text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-full border border-amber-500/20",
            ),
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1.5"
                ),
                LanguageState.shop_stock_available,
                " · ",
                stock.to_string(),
                class_name="inline-flex items-center text-[10px] font-medium text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20",
            ),
        ),
    )


def _plan_card(plan: rx.Var) -> rx.Component:
    is_selected = ShopState.selected_plan_id == plan["id"]
    is_sold_out = plan["stock"] == 0
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.icon("box", size=14, class_name="text-blue-400"),
                rx.el.p(
                    plan["name"].to(str),
                    class_name="text-white font-semibold text-sm",
                ),
                rx.cond(
                    plan["highlight"],
                    rx.el.span(
                        LanguageState.shop_recommended_tag,
                        class_name="ml-auto text-[9px] font-semibold px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-center gap-2 mb-2",
            ),
            rx.el.span(
                plan["tag"].to(str),
                class_name="inline-block text-[10px] font-medium px-2 py-0.5 rounded bg-amber-500/15 text-amber-300 border border-amber-500/20 mb-3",
            ),
            rx.el.div(
                rx.el.p(
                    "CPU ",
                    rx.el.span(plan["cpu"].to(str), class_name="text-gray-300"),
                    " │ Mem ",
                    rx.el.span(plan["ram"].to(str), class_name="text-gray-300"),
                    class_name="text-[11px] text-gray-500 font-mono",
                ),
                rx.el.p(
                    "Disk ",
                    rx.el.span(
                        plan["disk"].to(str), class_name="text-gray-300"
                    ),
                    " │ Bandwidth ",
                    rx.el.span(
                        plan["bandwidth"].to(str),
                        class_name="text-gray-300",
                    ),
                    class_name="text-[11px] text-gray-500 font-mono",
                ),
                rx.el.p(
                    "Traffic ",
                    rx.el.span(
                        plan["traffic"].to(str),
                        class_name="text-gray-300",
                    ),
                    class_name="text-[11px] text-gray-500 font-mono",
                ),
                rx.el.p(
                    "Reset Traffic ",
                    rx.el.span(
                        plan["reset_traffic"].to(str),
                        class_name="text-gray-300",
                    ),
                    class_name="text-[11px] text-gray-500 font-mono",
                ),
                rx.el.p(
                    "IPv4 ",
                    rx.el.span(
                        plan["ipv4"].to(str), class_name="text-gray-300"
                    ),
                    " │ IPv6 ",
                    rx.el.span(
                        plan["ipv6"].to(str), class_name="text-gray-300"
                    ),
                    class_name="text-[11px] text-gray-500 font-mono",
                ),
                class_name="flex flex-col gap-1 mb-3",
            ),
            _stock_badge(plan["stock"]),
            rx.el.div(
                rx.el.span(
                    "¥",
                    class_name="text-base text-gray-400 font-semibold",
                ),
                rx.el.span(
                    (
                        plan["price"].to(float) * ShopState.cycle_multiplier
                    ).to_string(),
                    class_name="text-2xl text-white font-semibold tracking-tight",
                ),
                rx.el.span(
                    "/Month",
                    class_name="text-xs text-gray-500 ml-1",
                ),
                class_name="flex items-baseline mt-3 pt-3 border-t border-white/5",
            ),
            class_name="text-left w-full",
        ),
        on_click=lambda: ShopState.select_plan(plan["id"].to(str)),
        disabled=is_sold_out,
        class_name=rx.cond(
            is_selected,
            "relative rounded-xl bg-gradient-to-b from-blue-500/[0.15] to-blue-500/[0.03] border border-blue-500/50 p-4 shadow-lg shadow-blue-500/20 text-left transition-all cursor-pointer",
            rx.cond(
                is_sold_out,
                "relative rounded-xl bg-white/[0.02] border border-white/10 p-4 opacity-60 text-left cursor-not-allowed",
                "relative rounded-xl bg-white/[0.03] border border-white/10 p-4 hover:border-blue-500/30 hover:bg-white/[0.06] text-left transition-all cursor-pointer",
            ),
        ),
    )


def _custom_config_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("settings-2", size=14, class_name="text-blue-400"),
            rx.el.p(
                "Custom higher configuration",
                class_name="text-white font-semibold text-sm",
            ),
            class_name="flex items-center gap-2 mb-3",
        ),
        rx.el.div(
            rx.el.p(
                "CPU XX cores",
                class_name="text-[11px] text-gray-500 font-mono",
            ),
            rx.el.p(
                "Disk XXG",
                class_name="text-[11px] text-gray-500 font-mono",
            ),
            rx.el.p(
                "Traffic XXG/month",
                class_name="text-[11px] text-gray-500 font-mono",
            ),
            rx.el.p(
                "Traffic reset ¥XX",
                class_name="text-[11px] text-gray-500 font-mono",
            ),
            rx.el.p(
                "IPv4 XX",
                class_name="text-[11px] text-gray-500 font-mono",
            ),
            class_name="flex flex-col gap-1 mb-4",
        ),
        rx.el.p(
            "Open a ticket or contact support for a custom quote",
            class_name="text-[11px] text-gray-500 mb-3",
        ),
        rx.el.button(
            "Get quote",
            class_name="px-4 py-1.5 rounded-md bg-blue-600 hover:bg-blue-500 text-white text-xs font-medium transition-all cursor-pointer",
        ),
        class_name="rounded-xl bg-white/[0.03] border border-dashed border-white/15 p-4",
    )


def _order_details_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    LanguageState.shop_order_details,
                    class_name="text-white font-semibold text-base",
                ),
                rx.el.button(
                    rx.icon("percent", size=12, class_name="mr-1"),
                    "AFF",
                    class_name="flex items-center px-2 py-1 rounded-md bg-white/5 border border-white/10 hover:border-blue-500/40 text-xs text-gray-300 transition-all cursor-pointer",
                ),
                class_name="flex items-center justify-between mb-4",
            ),
            rx.el.div(
                _detail_row(
                    LanguageState.shop_type, ShopState.selected_machine_label
                ),
                _detail_row(
                    LanguageState.shop_region, ShopState.selected_region_name
                ),
                _detail_row(LanguageState.shop_node, ShopState.selected_node),
                _detail_row(
                    LanguageState.shop_plan, ShopState.selected_plan_name
                ),
                _detail_row(
                    LanguageState.shop_cpu, ShopState.selected_plan_cpu
                ),
                _detail_row(
                    LanguageState.shop_memory, ShopState.selected_plan_ram
                ),
                _detail_row(
                    LanguageState.shop_disk, ShopState.selected_plan_disk
                ),
                _detail_row(
                    LanguageState.shop_bandwidth,
                    ShopState.selected_plan_bandwidth,
                ),
                _detail_row(
                    LanguageState.shop_traffic, ShopState.selected_plan_traffic
                ),
                _detail_row(
                    LanguageState.shop_system, ShopState.selected_system_label
                ),
                _detail_row(
                    LanguageState.shop_cycle, ShopState.selected_cycle_label
                ),
                class_name="flex flex-col gap-2 mb-4 pb-4 border-b border-white/5",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    default_checked=ShopState.agree_terms,
                    on_change=ShopState.toggle_agree_terms,
                    class_name="mt-0.5 rounded border-white/10 bg-[#141824]/60 text-blue-500 shrink-0",
                ),
                rx.el.span(
                    LanguageState.shop_agree_terms,
                    class_name="text-[11px] text-gray-400 leading-relaxed",
                ),
                class_name="flex items-start gap-2 mb-2 cursor-pointer",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    default_checked=ShopState.agree_broadcast,
                    on_change=ShopState.toggle_agree_broadcast,
                    class_name="mt-0.5 rounded border-white/10 bg-[#141824]/60 text-blue-500 shrink-0",
                ),
                rx.el.span(
                    LanguageState.shop_agree_broadcast,
                    class_name="text-[11px] text-gray-400 leading-relaxed",
                ),
                class_name="flex items-start gap-2 mb-4 cursor-pointer",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "¥",
                        class_name="text-base text-gray-400 font-semibold",
                    ),
                    rx.el.span(
                        f"{ShopState.selected_plan_price:.2f}",
                        class_name="text-2xl text-white font-semibold tracking-tight",
                    ),
                    class_name="flex items-baseline",
                ),
                rx.el.button(
                    rx.cond(
                        ShopState.selected_plan_available,
                        LanguageState.shop_buy_now,
                        LanguageState.shop_sold_out,
                    ),
                    on_click=ShopState.handle_purchase,
                    disabled=~ShopState.selected_plan_available,
                    class_name=rx.cond(
                        ShopState.selected_plan_available,
                        "px-5 py-2 rounded-lg bg-gradient-to-b from-blue-500 to-blue-600 hover:from-blue-400 hover:to-blue-500 text-white text-sm font-semibold shadow-lg shadow-blue-500/30 transition-all cursor-pointer",
                        "px-5 py-2 rounded-lg bg-white/5 border border-white/10 text-gray-500 text-sm font-semibold cursor-not-allowed",
                    ),
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="rounded-2xl bg-gradient-to-b from-white/[0.05] to-white/[0.01] border border-white/10 p-5 backdrop-blur-sm",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("headphones", size=14, class_name="text-blue-400"),
                rx.el.span(
                    LanguageState.shop_help_title,
                    class_name="text-white text-sm font-semibold",
                ),
                class_name="flex items-center gap-2 mb-2",
            ),
            rx.el.p(
                LanguageState.shop_help_desc,
                class_name="text-xs text-gray-500 mb-3 leading-relaxed",
            ),
            rx.el.button(
                LanguageState.shop_contact_sales,
                rx.icon("arrow-right", size=12, class_name="ml-1"),
                class_name="w-full flex items-center justify-center gap-1 py-2 rounded-lg bg-white/5 border border-white/10 hover:border-blue-500/40 text-white text-xs font-medium transition-all cursor-pointer",
            ),
            class_name="mt-4 p-4 rounded-xl bg-gradient-to-b from-blue-500/[0.06] to-white/[0.01] border border-white/10",
        ),
        class_name="w-80 shrink-0 hidden xl:block sticky top-24 self-start",
    )


def _detail_row(label: rx.Var, value: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.span(label, class_name="text-xs text-gray-500"),
        rx.el.span(
            value, class_name="text-xs text-white font-medium text-right"
        ),
        class_name="flex items-center justify-between gap-2",
    )


def _section(title: rx.Var, body: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            title,
            class_name="text-lg font-semibold text-white mb-4",
        ),
        body,
        class_name="mb-8",
    )


def _filter_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    size=14,
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none",
                ),
                rx.el.input(
                    placeholder=LanguageState.shop_search_placeholder,
                    default_value=ShopState.search_query,
                    on_change=ShopState.set_search.debounce(300),
                    class_name="w-full pl-9 pr-4 py-2 bg-[#141824]/60 text-white placeholder-gray-600 rounded-lg border border-white/10 focus:border-blue-500/50 focus:outline-hidden text-sm",
                ),
                class_name="relative flex-1 min-w-0",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option(
                        LanguageState.shop_sort_recommended,
                        value="recommended",
                    ),
                    rx.el.option(
                        LanguageState.shop_sort_price_asc, value="price-asc"
                    ),
                    rx.el.option(
                        LanguageState.shop_sort_price_desc, value="price-desc"
                    ),
                    rx.el.option(LanguageState.shop_sort_stock, value="stock"),
                    default_value=ShopState.sort_by,
                    key=ShopState.sort_by,
                    on_change=ShopState.set_sort,
                    class_name="appearance-none pl-3 pr-9 py-2 bg-[#141824]/60 text-white rounded-lg border border-white/10 focus:border-blue-500/50 focus:outline-hidden text-sm cursor-pointer",
                ),
                rx.icon(
                    "chevron-down",
                    size=14,
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.el.span(
                    LanguageState.shop_price_range,
                    class_name="text-xs text-gray-500 mr-2",
                ),
                rx.el.input(
                    type="number",
                    default_value=ShopState.price_min.to_string(),
                    on_change=ShopState.set_price_min.debounce(400),
                    class_name="w-20 px-2 py-1.5 bg-[#141824]/60 text-white rounded-lg border border-white/10 focus:border-blue-500/50 focus:outline-hidden text-xs",
                ),
                rx.el.span("—", class_name="text-gray-500 text-xs"),
                rx.el.input(
                    type="number",
                    default_value=ShopState.price_max.to_string(),
                    on_change=ShopState.set_price_max.debounce(400),
                    class_name="w-20 px-2 py-1.5 bg-[#141824]/60 text-white rounded-lg border border-white/10 focus:border-blue-500/50 focus:outline-hidden text-xs",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon("rotate-ccw", size=12, class_name="mr-1"),
                LanguageState.shop_reset,
                on_click=ShopState.reset_filters,
                class_name="flex items-center px-3 py-2 rounded-lg bg-white/[0.03] border border-white/10 text-xs text-gray-300 hover:text-white hover:border-white/20 transition-all cursor-pointer",
            ),
            class_name="flex flex-wrap items-center gap-3",
        ),
        class_name="mb-6",
    )


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search-x", size=32, class_name="text-gray-600"),
            class_name="w-16 h-16 rounded-2xl bg-white/[0.03] border border-white/10 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            LanguageState.shop_no_results_title,
            class_name="text-white font-semibold text-base mb-1",
        ),
        rx.el.p(
            LanguageState.shop_no_results_desc,
            class_name="text-sm text-gray-500 mb-4",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", size=12, class_name="mr-1"),
            LanguageState.shop_reset,
            on_click=ShopState.reset_filters,
            class_name="inline-flex items-center px-4 py-2 rounded-lg bg-blue-500 hover:bg-blue-400 text-white text-xs font-medium transition-all cursor-pointer",
        ),
        class_name="text-center py-16 rounded-2xl bg-white/[0.02] border border-dashed border-white/10",
    )


def _shop_navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-blue-400"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/30 flex items-center justify-center",
                ),
                rx.el.span(
                    "AkileCloud",
                    class_name="text-white font-semibold text-base",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.el.a(
                    LanguageState.nav_home,
                    href="/",
                    class_name="text-sm text-gray-400 hover:text-white transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_products,
                    href="/#products",
                    class_name="text-sm text-blue-400 font-medium",
                ),
                rx.el.a(
                    LanguageState.nav_pricing,
                    href="/#pricing",
                    class_name="text-sm text-gray-400 hover:text-white transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_network,
                    href="/#nodes",
                    class_name="text-sm text-gray-400 hover:text-white transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_faq,
                    href="/#faq",
                    class_name="text-sm text-gray-400 hover:text-white transition-colors",
                ),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages",
                        size=16,
                        class_name="text-blue-400 mr-1.5",
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-gray-300 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 transition-all cursor-pointer",
                ),
                rx.el.a(
                    rx.el.button(
                        LanguageState.nav_login,
                        class_name="text-sm text-gray-300 hover:text-white px-3 py-1.5 font-medium transition-colors cursor-pointer",
                    ),
                    href="/login",
                ),
                rx.el.a(
                    rx.el.button(
                        LanguageState.nav_signup,
                        class_name="text-sm bg-blue-500 hover:bg-blue-400 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-lg shadow-blue-500/20 cursor-pointer",
                    ),
                    href="/register",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-[1400px] mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-[#0a0d14]/70 border-b border-white/5",
    )


def shop_server_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none opacity-[0.15] [background-image:linear-gradient(rgba(255,255,255,0.06)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.06)_1px,transparent_1px)] [background-size:56px_56px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_30%,black_40%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -left-40 top-40 w-[500px] h-[500px] rounded-full bg-blue-500/10 blur-[140px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed right-0 bottom-0 w-[400px] h-[400px] rounded-full bg-purple-500/10 blur-[140px] pointer-events-none",
        ),
        _shop_navbar(),
        rx.el.div(
            # Breadcrumb
            rx.el.div(
                rx.el.a(
                    LanguageState.shop_breadcrumb_home,
                    href="/",
                    class_name="text-xs text-gray-500 hover:text-white",
                ),
                rx.icon("chevron-right", size=12, class_name="text-gray-600"),
                rx.el.span(
                    LanguageState.shop_breadcrumb_shop,
                    class_name="text-xs text-gray-500",
                ),
                rx.icon("chevron-right", size=12, class_name="text-gray-600"),
                rx.el.span(
                    LanguageState.shop_breadcrumb_server,
                    class_name="text-xs text-white font-medium",
                ),
                class_name="flex items-center gap-1.5 mb-6",
            ),
            rx.el.div(
                # Left: Main content
                rx.el.div(
                    # Machine Type Section
                    _section(
                        LanguageState.shop_select_machine,
                        rx.el.div(
                            rx.foreach(
                                ShopState.machine_types, _machine_type_button
                            ),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-3",
                        ),
                    ),
                    # Region Section
                    _section(
                        LanguageState.shop_select_region,
                        rx.el.div(
                            rx.foreach(ShopState.regions, _region_button),
                            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3",
                        ),
                    ),
                    # Node Section
                    _section(
                        LanguageState.shop_select_node,
                        rx.el.div(
                            rx.el.div(
                                rx.foreach(
                                    ShopState.available_nodes, _node_button
                                ),
                                class_name="flex flex-wrap gap-3 mb-3",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "info",
                                    size=12,
                                    class_name="text-blue-400 shrink-0",
                                ),
                                rx.el.span(
                                    "澳门广播IP 机器位置在HK",
                                    class_name="text-xs text-gray-400",
                                ),
                                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-blue-500/5 border border-blue-500/20",
                            ),
                        ),
                    ),
                    # Filter Bar
                    _filter_bar(),
                    # Plans Section
                    _section(
                        LanguageState.shop_select_plan,
                        rx.cond(
                            ShopState.result_count > 0,
                            rx.el.div(
                                rx.foreach(
                                    ShopState.filtered_plans, _plan_card
                                ),
                                _custom_config_card(),
                                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
                            ),
                            _empty_state(),
                        ),
                    ),
                    # System Section
                    _section(
                        LanguageState.shop_select_system,
                        rx.el.div(
                            rx.foreach(ShopState.systems_data, _system_button),
                            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3",
                        ),
                    ),
                    # Purchase Time Section
                    _section(
                        LanguageState.shop_select_cycle,
                        rx.el.div(
                            rx.el.div(
                                rx.el.p(
                                    LanguageState.shop_purchase_time,
                                    class_name="text-xs text-gray-500 mb-2",
                                ),
                                rx.el.div(
                                    rx.foreach(ShopState.cycles, _cycle_button),
                                    class_name="flex flex-wrap gap-2 mb-4",
                                ),
                                rx.el.p(
                                    LanguageState.shop_coupon,
                                    class_name="text-xs text-gray-500 mb-2",
                                ),
                                rx.el.div(
                                    rx.el.select(
                                        rx.el.option(
                                            LanguageState.shop_coupon_placeholder,
                                            value="",
                                        ),
                                        rx.el.option("SAVE10", value="SAVE10"),
                                        rx.el.option("SAVE20", value="SAVE20"),
                                        default_value=ShopState.coupon,
                                        on_change=ShopState.set_coupon,
                                        class_name="appearance-none w-full pl-3 pr-9 py-2 bg-[#141824]/60 text-white rounded-lg border border-white/10 focus:border-blue-500/50 focus:outline-hidden text-sm cursor-pointer",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        size=14,
                                        class_name="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none",
                                    ),
                                    class_name="relative mb-2",
                                ),
                                rx.el.p(
                                    LanguageState.shop_coupon_note,
                                    class_name="text-[11px] text-gray-500",
                                ),
                                class_name="p-5 rounded-2xl bg-white/[0.03] border border-white/10",
                            ),
                        ),
                    ),
                    rx.el.div(
                        rx.icon("info", size=12, class_name="text-gray-500"),
                        rx.el.span(
                            LanguageState.shop_info_note,
                            class_name="text-xs text-gray-500",
                        ),
                        class_name="flex items-center gap-2 pt-6 border-t border-white/5",
                    ),
                    class_name="flex-1 min-w-0",
                ),
                # Right: Order Details Sidebar
                _order_details_sidebar(),
                class_name="flex gap-8",
            ),
            class_name="max-w-[1400px] mx-auto px-6 pt-24 pb-16 relative z-10",
        ),
        class_name="font-['Inter'] bg-[#0a0d14] min-h-screen relative overflow-x-hidden text-white antialiased",
    )