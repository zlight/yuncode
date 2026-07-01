import reflex as rx
from app.states.ui_state import UIState


FAQS: list[dict[str, str]] = [
    {
        "id": "faq-1",
        "q": "What does 'streaming unlock' actually mean?",
        "a": "Every AkileCloud VPS ships with a native residential-class IP for its region. This means services like Netflix, Disney+, HBO Max, TikTok, ChatGPT and BBC iPlayer detect the IP as a legitimate local user and serve full regional catalogs — no proxy blocks, no geo restrictions.",
    },
    {
        "id": "faq-2",
        "q": "How fast is provisioning after payment?",
        "a": "Automated. Once payment is confirmed, your VPS is provisioned, booted and ready via SSH/RDP in under 60 seconds. You'll receive credentials by email and in the console immediately.",
    },
    {
        "id": "faq-3",
        "q": "Can I upgrade or downgrade my plan later?",
        "a": "Yes. You can vertically scale (more vCPU / RAM / disk) at any time from the console with a simple reboot. Traffic and bandwidth caps can be increased instantly without downtime.",
    },
    {
        "id": "faq-4",
        "q": "Do you support custom ISO / operating systems?",
        "a": "Absolutely. We ship with Ubuntu, Debian, CentOS, Rocky, AlmaLinux, Windows Server 2019/2022 and FreeBSD. You can also upload your own ISO for full control.",
    },
    {
        "id": "faq-5",
        "q": "What is your refund policy?",
        "a": "We offer a 7-day money-back guarantee on all monthly plans. If you're not satisfied for any reason, open a ticket within 7 days of activation and receive a full refund — no questions asked.",
    },
    {
        "id": "faq-6",
        "q": "How does DDoS protection work?",
        "a": "All servers include free 20 Gbps mitigation. Business and Enterprise plans get 100–200 Gbps protection with automatic L3/L4 scrubbing and optional L7 WAF. Attacks are absorbed transparently — your service stays online.",
    },
    {
        "id": "faq-7",
        "q": "Which payment methods do you accept?",
        "a": "Credit / debit cards (Visa, Mastercard, Amex), PayPal, Alipay, WeChat Pay, USDT (TRC-20 / ERC-20) and bank wire for annual enterprise contracts.",
    },
    {
        "id": "faq-8",
        "q": "Is there an API for automation?",
        "a": "Yes. Our REST API and Terraform provider expose every console operation — create/destroy servers, snapshots, firewall rules, DNS. Perfect for CI/CD and infra-as-code workflows.",
    },
]


def _faq_item(f: dict[str, str]) -> rx.Component:
    is_open = UIState.open_faq == f["id"]
    return rx.el.div(
        rx.el.button(
            rx.el.div(
                rx.el.span(
                    f["q"],
                    class_name="text-white text-base font-medium text-left",
                ),
                rx.el.div(
                    rx.icon(
                        rx.cond(is_open, "minus", "plus"),
                        size=16,
                        class_name="text-blue-400",
                    ),
                    class_name=rx.cond(
                        is_open,
                        "w-8 h-8 rounded-lg bg-blue-500/20 border border-blue-500/30 flex items-center justify-center shrink-0 transition-all",
                        "w-8 h-8 rounded-lg bg-white/5 border border-white/10 flex items-center justify-center shrink-0 transition-all",
                    ),
                ),
                class_name="flex items-center justify-between gap-4 w-full",
            ),
            on_click=lambda: UIState.toggle_faq(f["id"]),
            class_name="w-full px-6 py-5 text-left hover:bg-white/[0.02] transition-colors",
            aria_expanded=is_open.to_string(),
        ),
        rx.cond(
            is_open,
            rx.el.div(
                rx.el.p(
                    f["a"],
                    class_name="text-sm text-gray-400 leading-relaxed",
                ),
                class_name="px-6 pb-5 -mt-1",
            ),
            rx.fragment(),
        ),
        class_name=rx.cond(
            is_open,
            "rounded-xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-blue-500/20 backdrop-blur-sm transition-all",
            "rounded-xl bg-white/[0.02] border border-white/10 hover:border-white/20 backdrop-blur-sm transition-all",
        ),
    )


def _support_channel(
    icon: str, title: str, desc: str, action: str
) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(icon, size=18, class_name="text-blue-400"),
            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/20 flex items-center justify-center mb-4",
        ),
        rx.el.h4(title, class_name="text-white font-semibold text-sm mb-1"),
        rx.el.p(desc, class_name="text-xs text-gray-500 mb-3"),
        rx.el.span(
            action,
            rx.icon("arrow-right", size=12, class_name="ml-1"),
            class_name="inline-flex items-center text-xs text-blue-400 font-medium hover:text-blue-300",
        ),
        href="#",
        class_name="block rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-5 hover:border-blue-500/30 hover:-translate-y-0.5 transition-all",
    )


def faq_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("circle_help", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        "FAQ",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Frequently asked ",
                    rx.el.span(
                        "questions",
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "Answers to the most common questions about our cloud services, network and support.",
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(FAQS, _faq_item),
                    class_name="flex flex-col gap-3",
                ),
                class_name="max-w-3xl mx-auto mb-16",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Still have questions?",
                        class_name="text-2xl font-semibold text-white mb-2",
                    ),
                    rx.el.p(
                        "Our team is here to help you 24/7. Choose your preferred channel.",
                        class_name="text-gray-400",
                    ),
                    class_name="text-center mb-8",
                ),
                rx.el.div(
                    _support_channel(
                        "message-circle",
                        "Live Chat",
                        "Avg. response < 2 min",
                        "Start chat",
                    ),
                    _support_channel(
                        "send",
                        "Telegram",
                        "Community & priority support",
                        "Join group",
                    ),
                    _support_channel(
                        "mail",
                        "Email",
                        "support@akilecloud.com",
                        "Send email",
                    ),
                    _support_channel(
                        "book-open",
                        "Documentation",
                        "Guides, API reference, tutorials",
                        "Read docs",
                    ),
                    class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="faq",
        class_name="relative py-24 border-t border-white/5",
    )