import reflex as rx


METRICS: list[dict[str, str]] = [
    {
        "icon": "trending-up",
        "value": "99.99%",
        "label": "SLA Uptime",
        "desc": "Guaranteed monthly availability with financial-backed SLA.",
    },
    {
        "icon": "users",
        "value": "50,000+",
        "label": "Active Customers",
        "desc": "Trusted by developers, streamers and enterprises worldwide.",
    },
    {
        "icon": "server",
        "value": "20,000+",
        "label": "Deployed Servers",
        "desc": "Running production workloads across our global backbone.",
    },
    {
        "icon": "clock",
        "value": "< 60s",
        "label": "Provisioning Time",
        "desc": "Instant deployment from checkout to fully-booted OS.",
    },
    {
        "icon": "headphones",
        "value": "24/7",
        "label": "Expert Support",
        "desc": "Bilingual engineers on-call for every plan tier.",
    },
    {
        "icon": "shield",
        "value": "200 Gbps",
        "label": "DDoS Mitigation",
        "desc": "Enterprise-grade protection with L3/L4/L7 filtering.",
    },
]


GUARANTEES: list[dict[str, str]] = [
    {
        "icon": "shield-check",
        "title": "SLA-Backed Uptime",
        "desc": "99.99% availability guarantee with automatic credit compensation for any downtime beyond commitment.",
        "tag": "Reliability",
    },
    {
        "icon": "refresh-ccw",
        "title": "7-Day Money Back",
        "desc": "Try any plan risk-free. Full refund within 7 days, no questions asked, no hidden fees.",
        "tag": "Guarantee",
    },
    {
        "icon": "lock",
        "title": "Data Sovereignty",
        "desc": "Your data stays in your chosen region. Encrypted at rest with AES-256 and in transit with TLS 1.3.",
        "tag": "Privacy",
    },
    {
        "icon": "life-buoy",
        "title": "24/7 Expert Support",
        "desc": "Direct access to senior engineers via ticket, chat and Telegram — average first response under 5 minutes.",
        "tag": "Support",
    },
    {
        "icon": "activity",
        "title": "Real-time Monitoring",
        "desc": "Live dashboard with CPU, network, disk metrics, alerts and historical graphs at every layer.",
        "tag": "Observability",
    },
    {
        "icon": "git-branch",
        "title": "One-click Snapshots",
        "desc": "Instant snapshots and automated daily backups. Roll back in seconds without service interruption.",
        "tag": "Backup",
    },
]


def _metric_card(m: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(m["icon"], size=18, class_name="text-blue-400"),
            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/20 flex items-center justify-center mb-4",
        ),
        rx.el.p(
            m["value"],
            class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-1",
        ),
        rx.el.p(
            m["label"],
            class_name="text-xs text-blue-400 uppercase tracking-wider font-semibold mb-3",
        ),
        rx.el.p(
            m["desc"],
            class_name="text-sm text-gray-400 leading-relaxed",
        ),
        class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 backdrop-blur-sm hover:border-blue-500/30 hover:-translate-y-1 transition-all duration-300",
    )


def _guarantee_card(g: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(g["icon"], size=18, class_name="text-emerald-400"),
                class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-emerald-500/20 to-emerald-500/5 border border-emerald-500/20 flex items-center justify-center",
            ),
            rx.el.span(
                g["tag"],
                class_name="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-white/5 text-gray-400 border border-white/10 uppercase tracking-wider",
            ),
            class_name="flex items-center justify-between mb-4",
        ),
        rx.el.h3(
            g["title"],
            class_name="text-white text-base font-semibold mb-2",
        ),
        rx.el.p(
            g["desc"],
            class_name="text-sm text-gray-400 leading-relaxed",
        ),
        class_name="rounded-2xl bg-gradient-to-b from-white/[0.04] to-white/[0.01] border border-white/10 p-6 backdrop-blur-sm hover:border-emerald-500/30 transition-all duration-300",
    )


def metrics_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("bar-chart-3", size=14, class_name="text-blue-400"),
                    rx.el.span(
                        "Trusted at Scale",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Numbers that ",
                    rx.el.span(
                        "speak for themselves",
                        class_name="bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "Proven performance and reliability, backed by real customers and real infrastructure.",
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(METRICS, _metric_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-20",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "shield-check", size=14, class_name="text-emerald-400"
                    ),
                    rx.el.span(
                        "Service Guarantees",
                        class_name="text-xs text-gray-300 font-medium tracking-wide uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 mb-4",
                ),
                rx.el.h2(
                    "Enterprise-grade ",
                    rx.el.span(
                        "guarantees",
                        class_name="bg-gradient-to-r from-emerald-400 to-cyan-300 bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-semibold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    "Every plan includes the operational guarantees typically reserved for premium enterprise contracts.",
                    class_name="text-gray-400 max-w-2xl mx-auto",
                ),
                class_name="text-center mb-14",
            ),
            rx.el.div(
                rx.foreach(GUARANTEES, _guarantee_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5",
            ),
            class_name="max-w-7xl mx-auto px-6",
        ),
        id="trust",
        class_name="relative py-24 border-t border-white/5",
    )