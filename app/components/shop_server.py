import reflex as rx
from app.states.shop_state import ShopState
from app.states.language_state import LanguageState
from app.states.session_state import SessionState
from app.states.ui_state import UIState


_ACTIVE_PILL = "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-indigo-50 border border-indigo-500 text-indigo-700 font-semibold text-sm shadow-xs transition-all cursor-pointer"
_INACTIVE_PILL = "flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-indigo-600 hover:border-indigo-300 hover:bg-indigo-50/30 font-medium text-sm transition-all cursor-pointer shadow-xs"


def _machine_type_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.machine_type == item["id"]
    return rx.el.button(
        rx.icon(item["icon"], size=16),
        rx.el.span(item["label"], class_name="text-sm font-semibold"),
        on_click=lambda: ShopState.set_machine_type(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-indigo-50 border border-indigo-500 text-indigo-700 shadow-sm transition-all cursor-pointer",
            "flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-white border border-slate-200 text-slate-600 hover:text-indigo-600 hover:border-indigo-300 hover:bg-indigo-50/30 transition-all cursor-pointer shadow-xs",
        ),
    )


def _region_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_region == item["id"]
    return rx.el.button(
        rx.el.span(item["flag"], class_name="text-lg"),
        rx.el.span(item["name"], class_name="text-sm font-semibold"),
        on_click=lambda: ShopState.set_region(item["id"].to(str)),
        class_name=rx.cond(is_active, _ACTIVE_PILL, _INACTIVE_PILL),
    )


def _node_button(node: rx.Var) -> rx.Component:
    is_active = ShopState.selected_node == node
    return rx.el.button(
        rx.icon("network", size=14, class_name="text-indigo-500"),
        rx.el.span(node, class_name="text-sm font-semibold"),
        on_click=lambda: ShopState.set_node(node.to(str)),
        class_name=rx.cond(is_active, _ACTIVE_PILL, _INACTIVE_PILL),
    )


def _system_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_system == item["id"]
    return rx.el.button(
        rx.icon(item["icon"], size=14, class_name="text-indigo-500"),
        rx.el.span(item["label"], class_name="text-sm font-semibold"),
        on_click=lambda: ShopState.set_system(item["id"].to(str)),
        class_name=rx.cond(is_active, _ACTIVE_PILL, _INACTIVE_PILL),
    )


def _cycle_button(item: rx.Var) -> rx.Component:
    is_active = ShopState.selected_cycle == item["id"]
    return rx.el.button(
        rx.el.span(item["label"], class_name="text-sm font-semibold"),
        on_click=lambda: ShopState.set_cycle(item["id"].to(str)),
        class_name=rx.cond(
            is_active,
            "px-4 py-2 rounded-lg bg-indigo-50 border border-indigo-500 text-indigo-700 font-semibold text-sm transition-all cursor-pointer shadow-xs",
            "px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-indigo-600 hover:border-indigo-300 font-medium text-sm transition-all cursor-pointer shadow-xs",
        ),
    )


def _stock_badge(stock: rx.Var) -> rx.Component:
    return rx.cond(
        stock == 0,
        rx.el.span(
            rx.el.span(
                class_name="w-1.5 h-1.5 rounded-full bg-rose-500 mr-1.5"
            ),
            LanguageState.shop_sold_out,
            class_name="inline-flex items-center text-[10px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-full border border-rose-200 w-fit",
        ),
        rx.cond(
            stock < 10,
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-amber-500 mr-1.5 animate-pulse"
                ),
                LanguageState.shop_stock_low,
                " · ",
                stock.to_string(),
                class_name="inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200 w-fit",
            ),
            rx.el.span(
                rx.el.span(
                    class_name="w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1.5"
                ),
                LanguageState.shop_stock_available,
                " · ",
                stock.to_string(),
                class_name="inline-flex items-center text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200 w-fit",
            ),
        ),
    )


def _plan_card(plan: rx.Var) -> rx.Component:
    is_selected = ShopState.selected_plan_id == plan["id"]
    is_sold_out = plan["stock"] == 0
    return rx.el.button(
        rx.el.div(
            rx.el.div(
                rx.icon("box", size=14, class_name="text-indigo-600"),
                rx.el.p(
                    plan["name"].to(str),
                    class_name="text-slate-900 font-bold text-sm",
                ),
                rx.cond(
                    plan["highlight"],
                    rx.el.span(
                        LanguageState.shop_recommended_tag,
                        class_name="ml-auto text-[9px] font-bold px-1.5 py-0.5 rounded bg-indigo-50 text-indigo-600 border border-indigo-100",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-center gap-2 mb-2",
            ),
            rx.el.span(
                plan["tag"].to(str),
                class_name="inline-block text-[10px] font-bold px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-100 mb-3 w-fit",
            ),
            rx.el.div(
                rx.el.p(
                    "CPU ",
                    rx.el.span(
                        plan["cpu"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    " │ Mem ",
                    rx.el.span(
                        plan["ram"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    class_name="text-[11px] text-slate-500 font-mono",
                ),
                rx.el.p(
                    "Disk ",
                    rx.el.span(
                        plan["disk"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    " │ BW ",
                    rx.el.span(
                        plan["bandwidth"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    class_name="text-[11px] text-slate-500 font-mono",
                ),
                rx.el.p(
                    "Traffic ",
                    rx.el.span(
                        plan["traffic"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    class_name="text-[11px] text-slate-500 font-mono",
                ),
                rx.el.p(
                    "Reset ",
                    rx.el.span(
                        plan["reset_traffic"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    class_name="text-[11px] text-slate-500 font-mono",
                ),
                rx.el.p(
                    "IPv4 ",
                    rx.el.span(
                        plan["ipv4"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    " │ IPv6 ",
                    rx.el.span(
                        plan["ipv6"].to(str),
                        class_name="text-slate-700 font-semibold",
                    ),
                    class_name="text-[11px] text-slate-500 font-mono",
                ),
                class_name="flex flex-col gap-1 mb-3",
            ),
            _stock_badge(plan["stock"]),
            rx.el.div(
                rx.el.span(
                    "¥",
                    class_name="text-base text-slate-400 font-bold",
                ),
                rx.el.span(
                    (
                        plan["price"].to(float) * ShopState.cycle_multiplier
                    ).to_string(),
                    class_name="text-2xl text-slate-900 font-extrabold tracking-tight",
                ),
                rx.el.span(
                    "/mo",
                    class_name="text-xs text-slate-400 ml-1 font-semibold",
                ),
                class_name="flex items-baseline mt-3 pt-3 border-t border-slate-100",
            ),
            class_name="text-left w-full",
        ),
        on_click=lambda: ShopState.select_plan(plan["id"].to(str)),
        disabled=is_sold_out,
        class_name=rx.cond(
            is_selected,
            "relative rounded-xl bg-white border border-indigo-500 p-4 shadow-md ring-2 ring-indigo-100 text-left transition-all cursor-pointer",
            rx.cond(
                is_sold_out,
                "relative rounded-xl bg-slate-50 border border-slate-200 p-4 opacity-60 text-left cursor-not-allowed",
                "relative rounded-xl bg-white border border-slate-200 p-4 hover:border-indigo-300 hover:shadow-md hover:-translate-y-0.5 text-left transition-all cursor-pointer shadow-xs",
            ),
        ),
    )


def _custom_config_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("settings-2", size=14, class_name="text-indigo-600"),
            rx.el.p(
                "Custom higher configuration",
                class_name="text-slate-900 font-bold text-sm",
            ),
            class_name="flex items-center gap-2 mb-3",
        ),
        rx.el.div(
            rx.el.p(
                "CPU XX cores",
                class_name="text-[11px] text-slate-500 font-mono",
            ),
            rx.el.p(
                "Disk XXG", class_name="text-[11px] text-slate-500 font-mono"
            ),
            rx.el.p(
                "Traffic XXG/month",
                class_name="text-[11px] text-slate-500 font-mono",
            ),
            rx.el.p(
                "Traffic reset ¥XX",
                class_name="text-[11px] text-slate-500 font-mono",
            ),
            rx.el.p(
                "IPv4 XX", class_name="text-[11px] text-slate-500 font-mono"
            ),
            class_name="flex flex-col gap-1 mb-4",
        ),
        rx.el.p(
            "Open a ticket or contact support for a custom quote",
            class_name="text-[11px] text-slate-500 mb-3",
        ),
        rx.el.button(
            "Get quote",
            class_name="px-4 py-1.5 rounded-md bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition-all cursor-pointer shadow-xs",
        ),
        class_name="rounded-xl bg-white border border-dashed border-slate-300 p-4",
    )


def _detail_row(label: rx.Var, value: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.span(label, class_name="text-xs text-slate-500 font-medium"),
        rx.el.span(
            value,
            class_name="text-xs text-slate-800 font-semibold text-right",
        ),
        class_name="flex items-center justify-between gap-2",
    )


def _order_details_sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        LanguageState.shop_order_details,
                        class_name="text-slate-900 font-bold text-base",
                    ),
                    rx.cond(
                        SessionState.is_logged_in,
                        rx.cond(
                            SessionState.is_vip,
                            rx.el.span(
                                rx.icon("crown", size=10, class_name="mr-1"),
                                "VIP",
                                class_name="inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200",
                            ),
                            rx.el.span(
                                rx.cond(
                                    LanguageState.is_zh,
                                    "普通用户",
                                    "Free",
                                ),
                                class_name="text-[10px] font-bold text-slate-500 bg-slate-50 px-2 py-0.5 rounded-md border border-slate-200",
                            ),
                        ),
                        rx.fragment(),
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.button(
                    rx.icon("percent", size=12, class_name="mr-1"),
                    "AFF",
                    class_name="flex items-center px-2 py-1 rounded-md bg-slate-50 border border-slate-200 hover:border-indigo-500 hover:text-indigo-600 text-xs text-slate-600 font-semibold transition-all cursor-pointer",
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
                class_name="flex flex-col gap-2 mb-4 pb-4 border-b border-slate-100",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    default_checked=ShopState.agree_terms,
                    on_change=ShopState.toggle_agree_terms,
                    class_name="mt-0.5 rounded border-slate-300 bg-white text-indigo-600 focus:ring-indigo-200 shrink-0",
                ),
                rx.el.span(
                    LanguageState.shop_agree_terms,
                    class_name="text-[11px] text-slate-600 leading-relaxed font-medium",
                ),
                class_name="flex items-start gap-2 mb-2 cursor-pointer",
            ),
            rx.el.label(
                rx.el.input(
                    type="checkbox",
                    default_checked=ShopState.agree_broadcast,
                    on_change=ShopState.toggle_agree_broadcast,
                    class_name="mt-0.5 rounded border-slate-300 bg-white text-indigo-600 focus:ring-indigo-200 shrink-0",
                ),
                rx.el.span(
                    LanguageState.shop_agree_broadcast,
                    class_name="text-[11px] text-slate-600 leading-relaxed font-medium",
                ),
                class_name="flex items-start gap-2 mb-4 cursor-pointer",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "¥",
                        class_name="text-base text-slate-400 font-bold",
                    ),
                    rx.el.span(
                        f"{ShopState.selected_plan_price:.2f}",
                        class_name="text-2xl text-slate-900 font-extrabold tracking-tight",
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
                        "px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-bold shadow-md hover:shadow-lg transition-all cursor-pointer",
                        "px-5 py-2 rounded-lg bg-slate-100 border border-slate-200 text-slate-400 text-sm font-bold cursor-not-allowed",
                    ),
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="rounded-2xl bg-white border border-slate-200 p-5 shadow-sm",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("headphones", size=14, class_name="text-indigo-600"),
                rx.el.span(
                    LanguageState.shop_help_title,
                    class_name="text-slate-900 text-sm font-bold",
                ),
                class_name="flex items-center gap-2 mb-2",
            ),
            rx.el.p(
                LanguageState.shop_help_desc,
                class_name="text-xs text-slate-500 mb-3 leading-relaxed font-medium",
            ),
            rx.el.button(
                LanguageState.shop_contact_sales,
                rx.icon("arrow-right", size=12, class_name="ml-1"),
                class_name="w-full flex items-center justify-center gap-1 py-2 rounded-lg bg-white border border-slate-200 hover:border-indigo-500 hover:text-indigo-600 text-slate-700 text-xs font-bold transition-all cursor-pointer shadow-xs",
            ),
            class_name="mt-4 p-4 rounded-xl bg-indigo-50/40 border border-indigo-100",
        ),
        class_name="w-80 shrink-0 hidden xl:block sticky top-24 self-start",
    )


def _section(title: rx.Var, body: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            title,
            class_name="text-lg font-bold text-slate-900 mb-4",
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
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none",
                ),
                rx.el.input(
                    placeholder=LanguageState.shop_search_placeholder,
                    default_value=ShopState.search_query,
                    on_change=ShopState.set_search.debounce(300),
                    class_name="w-full pl-9 pr-4 py-2 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden text-sm shadow-xs",
                ),
                class_name="relative flex-1 min-w-0",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option(
                        LanguageState.shop_sort_recommended, value="recommended"
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
                    class_name="appearance-none pl-3 pr-9 py-2 bg-white text-slate-800 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden text-sm cursor-pointer shadow-xs",
                ),
                rx.icon(
                    "chevron-down",
                    size=14,
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none",
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.el.span(
                    LanguageState.shop_price_range,
                    class_name="text-xs text-slate-500 mr-2 font-semibold",
                ),
                rx.el.input(
                    type="number",
                    default_value=ShopState.price_min.to_string(),
                    on_change=ShopState.set_price_min.debounce(400),
                    class_name="w-20 px-2 py-1.5 bg-white text-slate-800 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden text-xs shadow-xs",
                ),
                rx.el.span("—", class_name="text-slate-400 text-xs"),
                rx.el.input(
                    type="number",
                    default_value=ShopState.price_max.to_string(),
                    on_change=ShopState.set_price_max.debounce(400),
                    class_name="w-20 px-2 py-1.5 bg-white text-slate-800 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden text-xs shadow-xs",
                ),
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon("rotate-ccw", size=12, class_name="mr-1"),
                LanguageState.shop_reset,
                on_click=ShopState.reset_filters,
                class_name="flex items-center px-3 py-2 rounded-lg bg-white border border-slate-200 text-xs text-slate-600 hover:text-indigo-600 hover:border-indigo-300 font-semibold transition-all cursor-pointer shadow-xs",
            ),
            class_name="flex flex-wrap items-center gap-3",
        ),
        class_name="mb-6",
    )


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search-x", size=32, class_name="text-slate-400"),
            class_name="w-16 h-16 rounded-2xl bg-slate-50 border border-slate-200 flex items-center justify-center mx-auto mb-4",
        ),
        rx.el.h3(
            LanguageState.shop_no_results_title,
            class_name="text-slate-900 font-bold text-base mb-1",
        ),
        rx.el.p(
            LanguageState.shop_no_results_desc,
            class_name="text-sm text-slate-500 mb-4 font-medium",
        ),
        rx.el.button(
            rx.icon("rotate-ccw", size=12, class_name="mr-1"),
            LanguageState.shop_reset,
            on_click=ShopState.reset_filters,
            class_name="inline-flex items-center px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition-all cursor-pointer shadow-xs",
        ),
        class_name="text-center py-16 rounded-2xl bg-white border border-dashed border-slate-200",
    )


def _shop_navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-indigo-600"),
                    class_name="w-8 h-8 rounded-lg bg-indigo-50 border border-indigo-100 flex items-center justify-center",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-slate-900 font-bold text-base tracking-tight",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.nav(
                rx.el.a(
                    LanguageState.nav_home,
                    href="/",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_products,
                    href="/#products",
                    class_name="text-sm text-indigo-600 font-semibold",
                ),
                rx.el.a(
                    LanguageState.nav_pricing,
                    href="/#pricing",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_network,
                    href="/#nodes",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                rx.el.a(
                    LanguageState.nav_faq,
                    href="/#faq",
                    class_name="text-sm text-slate-600 hover:text-indigo-600 font-medium transition-colors",
                ),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        "languages",
                        size=16,
                        class_name="text-indigo-600 mr-1.5",
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-slate-600 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 hover:bg-slate-100 hover:border-slate-300 transition-all cursor-pointer",
                ),
                rx.cond(
                    SessionState.is_logged_in,
                    rx.fragment(
                        rx.el.a(
                            rx.el.button(
                                rx.cond(
                                    LanguageState.is_zh, "控制台", "Console"
                                ),
                                class_name="text-sm bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-xs hover:shadow-md cursor-pointer",
                            ),
                            href="/console",
                        ),
                        rx.cond(
                            SessionState.is_vip,
                            rx.el.span(
                                rx.icon("crown", size=12, class_name="mr-1"),
                                "VIP",
                                class_name="hidden sm:inline-flex items-center text-[10px] font-bold text-amber-700 bg-amber-50 px-2 py-1 rounded-md border border-amber-200",
                            ),
                            rx.fragment(),
                        ),
                        rx.el.div(
                            rx.el.button(
                                SessionState.avatar_initial,
                                class_name="size-8 rounded-full bg-indigo-50 text-indigo-700 font-bold text-xs flex items-center justify-center border border-indigo-200 hover:bg-indigo-100 transition-colors shadow-xs cursor-pointer",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.p(
                                        SessionState.auth_username,
                                        class_name="text-sm font-bold text-slate-800",
                                    ),
                                    rx.el.p(
                                        SessionState.auth_email,
                                        class_name="text-xs text-slate-500 truncate",
                                    ),
                                    class_name="px-4 py-3 border-b border-slate-100",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        "退出登录",
                                        "Sign Out",
                                    ),
                                    on_click=SessionState.logout_user,
                                    class_name="w-full text-left text-sm text-rose-600 hover:bg-rose-50 px-4 py-2.5 transition-colors cursor-pointer",
                                ),
                                class_name="invisible opacity-0 translate-y-1 group-hover/avatar:visible group-hover/avatar:opacity-100 group-hover/avatar:translate-y-0 absolute right-0 mt-2 w-48 rounded-xl bg-white border border-slate-200 shadow-lg transition-all duration-200 z-50 overflow-hidden",
                            ),
                            class_name="group/avatar relative",
                        ),
                    ),
                    rx.fragment(
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_login,
                                class_name="text-sm text-slate-600 hover:text-indigo-600 px-3 py-1.5 font-medium transition-colors cursor-pointer",
                            ),
                            href="/login",
                        ),
                        rx.el.a(
                            rx.el.button(
                                LanguageState.nav_signup,
                                class_name="text-sm bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-1.5 rounded-md font-medium transition-colors shadow-xs hover:shadow-md cursor-pointer",
                            ),
                            href="/register",
                        ),
                    ),
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-[1400px] mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-white/85 border-b border-slate-200/60",
    )


def shop_server_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none opacity-100 [background-image:linear-gradient(to_right,rgba(99,102,241,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.03)_1px,transparent_1px)] [background-size:24px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,black_70%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -left-40 top-40 w-[500px] h-[500px] rounded-full bg-indigo-100/40 blur-[140px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed right-0 bottom-0 w-[400px] h-[400px] rounded-full bg-cyan-100/40 blur-[140px] pointer-events-none",
        ),
        _shop_navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    LanguageState.shop_breadcrumb_home,
                    href="/",
                    class_name="text-xs text-slate-500 hover:text-indigo-600 font-medium",
                ),
                rx.icon("chevron-right", size=12, class_name="text-slate-300"),
                rx.el.span(
                    LanguageState.shop_breadcrumb_shop,
                    class_name="text-xs text-slate-500 font-medium",
                ),
                rx.icon("chevron-right", size=12, class_name="text-slate-300"),
                rx.el.span(
                    LanguageState.shop_breadcrumb_server,
                    class_name="text-xs text-slate-800 font-semibold",
                ),
                class_name="flex items-center gap-1.5 mb-6",
            ),
            rx.el.div(
                rx.el.div(
                    _section(
                        LanguageState.shop_select_machine,
                        rx.el.div(
                            rx.foreach(
                                ShopState.machine_types, _machine_type_button
                            ),
                            class_name="grid grid-cols-2 md:grid-cols-3 gap-3",
                        ),
                    ),
                    _section(
                        LanguageState.shop_select_region,
                        rx.el.div(
                            rx.foreach(ShopState.regions, _region_button),
                            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3",
                        ),
                    ),
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
                                    class_name="text-indigo-600 shrink-0",
                                ),
                                rx.el.span(
                                    "澳门广播IP 机器位置在HK",
                                    class_name="text-xs text-slate-600 font-medium",
                                ),
                                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-indigo-50/40 border border-indigo-100",
                            ),
                        ),
                    ),
                    _filter_bar(),
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
                    _section(
                        LanguageState.shop_select_system,
                        rx.el.div(
                            rx.foreach(ShopState.systems_data, _system_button),
                            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3",
                        ),
                    ),
                    _section(
                        LanguageState.shop_select_cycle,
                        rx.el.div(
                            rx.el.div(
                                rx.el.p(
                                    LanguageState.shop_purchase_time,
                                    class_name="text-xs text-slate-500 mb-2 font-semibold",
                                ),
                                rx.el.div(
                                    rx.foreach(ShopState.cycles, _cycle_button),
                                    class_name="flex flex-wrap gap-2 mb-4",
                                ),
                                rx.el.p(
                                    LanguageState.shop_coupon,
                                    class_name="text-xs text-slate-500 mb-2 font-semibold",
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
                                        class_name="appearance-none w-full pl-3 pr-9 py-2 bg-white text-slate-800 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden text-sm cursor-pointer shadow-xs",
                                    ),
                                    rx.icon(
                                        "chevron-down",
                                        size=14,
                                        class_name="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none",
                                    ),
                                    class_name="relative mb-2",
                                ),
                                rx.el.p(
                                    LanguageState.shop_coupon_note,
                                    class_name="text-[11px] text-slate-500 font-medium",
                                ),
                                class_name="p-5 rounded-2xl bg-white border border-slate-200 shadow-xs",
                            ),
                        ),
                    ),
                    rx.el.div(
                        rx.icon("info", size=12, class_name="text-slate-400"),
                        rx.el.span(
                            LanguageState.shop_info_note,
                            class_name="text-xs text-slate-500 font-medium",
                        ),
                        class_name="flex items-center gap-2 pt-6 border-t border-slate-100",
                    ),
                    class_name="flex-1 min-w-0",
                ),
                _order_details_sidebar(),
                class_name="flex gap-8",
            ),
            class_name="max-w-[1400px] mx-auto px-6 pt-24 pb-16 relative z-10",
        ),
        class_name="font-['Inter'] bg-[#f8fafc] min-h-screen relative overflow-x-hidden text-slate-800 antialiased",
    )
