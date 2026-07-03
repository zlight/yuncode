import reflex as rx
from app.states.language_state import LanguageState


def _footer_link(item) -> rx.Component:
    return rx.el.a(
        item["label"],
        href=item["href"],
        class_name="block text-sm text-gray-400 hover:text-white transition-colors py-1",
    )


def _footer_col(title, items) -> rx.Component:
    return rx.el.div(
        rx.el.h4(
            title,
            class_name="text-white text-xs font-semibold mb-4 uppercase tracking-wider",
        ),
        rx.el.div(
            rx.foreach(items, _footer_link),
            class_name="flex flex-col",
        ),
    )


def _social_link(icon: str, label: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, size=16),
        href="#",
        aria_label=label,
        class_name="w-9 h-9 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center text-gray-400 hover:text-white hover:border-white/20 transition-all",
    )


def _contact_row(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, size=14, class_name="text-blue-400 shrink-0"),
        rx.el.span(text, class_name="text-sm text-gray-400"),
        class_name="flex items-center gap-2",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon("box", size=18, class_name="text-blue-400"),
                            class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/30 flex items-center justify-center",
                        ),
                        rx.el.span(
                            "AiarksCloud",
                            class_name="text-white font-semibold text-base",
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        LanguageState.footer_desc,
                        class_name="text-sm text-gray-400 mb-6 max-w-xs leading-relaxed",
                    ),
                    rx.el.div(
                        _contact_row("mail", "support@aiarkscloud.com"),
                        _contact_row("send", "@AiarksCloud on Telegram"),
                        rx.el.div(
                            rx.icon(
                                "map-pin",
                                size=14,
                                class_name="text-blue-400 shrink-0",
                            ),
                            rx.el.span(
                                LanguageState.footer_addr,
                                class_name="text-sm text-gray-400",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        class_name="flex flex-col gap-2 mb-6",
                    ),
                    rx.el.div(
                        _social_link("send", "Telegram"),
                        _social_link("git_fork", "GitHub"),
                        _social_link("wifi", "Twitter"),
                        _social_link("video", "YouTube"),
                        _social_link("rss", "RSS"),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="lg:col-span-2",
                ),
                _footer_col(
                    LanguageState.footer_col_products,
                    LanguageState.footer_products_links,
                ),
                _footer_col(
                    LanguageState.footer_col_network,
                    LanguageState.footer_network_links,
                ),
                _footer_col(
                    LanguageState.footer_col_resources,
                    LanguageState.footer_resources_links,
                ),
                _footer_col(
                    LanguageState.footer_col_company,
                    LanguageState.footer_company_links,
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 pb-10 border-b border-white/5",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                class_name="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"
                            ),
                            rx.el.span(
                                LanguageState.footer_all_operational,
                                class_name="text-xs text-gray-300 font-medium",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.a(
                            LanguageState.footer_status_page,
                            rx.icon(
                                "arrow-up-right", size=12, class_name="ml-1"
                            ),
                            href="#",
                            class_name="flex items-center text-xs text-blue-400 hover:text-blue-300",
                        ),
                        class_name="flex items-center gap-4",
                    ),
                    rx.el.div(
                        rx.el.span(
                            LanguageState.footer_payments_accepted,
                            class_name="text-xs text-gray-500",
                        ),
                        rx.el.div(
                            rx.el.span(
                                "Visa",
                                class_name="text-[10px] text-gray-400 px-2 py-0.5 rounded bg-white/5 border border-white/10",
                            ),
                            rx.el.span(
                                "Mastercard",
                                class_name="text-[10px] text-gray-400 px-2 py-0.5 rounded bg-white/5 border border-white/10",
                            ),
                            rx.el.span(
                                "PayPal",
                                class_name="text-[10px] text-gray-400 px-2 py-0.5 rounded bg-white/5 border border-white/10",
                            ),
                            rx.el.span(
                                "Alipay",
                                class_name="text-[10px] text-gray-400 px-2 py-0.5 rounded bg-white/5 border border-white/10",
                            ),
                            rx.el.span(
                                "USDT",
                                class_name="text-[10px] text-gray-400 px-2 py-0.5 rounded bg-white/5 border border-white/10",
                            ),
                            class_name="flex flex-wrap items-center gap-1.5",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 py-6 border-b border-white/5",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            LanguageState.footer_copy,
                            class_name="text-xs text-gray-500",
                        ),
                        rx.el.div(
                            rx.el.a(
                                LanguageState.footer_legal_privacy,
                                href="#",
                                class_name="text-xs text-gray-500 hover:text-white transition-colors",
                            ),
                            rx.el.a(
                                LanguageState.footer_legal_terms,
                                href="#",
                                class_name="text-xs text-gray-500 hover:text-white transition-colors",
                            ),
                            rx.el.a(
                                "SLA",
                                href="#",
                                class_name="text-xs text-gray-500 hover:text-white transition-colors",
                            ),
                            rx.el.a(
                                LanguageState.footer_legal_cookies,
                                href="#",
                                class_name="text-xs text-gray-500 hover:text-white transition-colors",
                            ),
                            rx.el.a(
                                LanguageState.footer_legal_aup,
                                href="#",
                                class_name="text-xs text-gray-500 hover:text-white transition-colors",
                            ),
                            class_name="flex flex-wrap items-center gap-6",
                        ),
                        class_name="flex flex-col md:flex-row items-center justify-between gap-4 pt-6",
                    ),
                ),
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="footer",
        class_name="relative py-16 border-t border-white/5",
    )
