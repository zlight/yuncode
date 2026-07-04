import shutil
from pathlib import Path

# Clean up stale persisted lockfile directory to resolve sync conflicts with package.json
_lock_dir = Path(__file__).resolve().parent.parent / "reflex.lock"
if _lock_dir.exists():
    try:
        shutil.rmtree(_lock_dir)
    except Exception:
        logging.exception("Unexpected error")

import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.products import products_section
from app.components.faq import faq_section
from app.components.cta import cta_section
from app.components.footer import footer
from app.states.language_state import LanguageState
from app.components.login_view import login_page
from app.components.register_view import register_page
from app.components.shop_server import shop_server_page
from app.components.console import console_page
from app.states.shop_state import ShopState
from app.states.servers_state import ServersState
from app.states.theme_state import ThemeState


def _ambient_bg() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 [background-image:linear-gradient(to_right,rgba(99,102,241,0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.06)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_0%,black_50%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="absolute -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-indigo-600/20 blur-[160px]",
        ),
        rx.el.div(
            class_name="absolute top-[40%] -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/10 blur-[140px]",
        ),
        rx.el.div(
            class_name="absolute top-[70%] -right-40 w-[600px] h-[600px] rounded-full bg-violet-600/15 blur-[140px]",
        ),
        class_name="fixed inset-0 pointer-events-none overflow-hidden",
    )


def _metric_pill(icon: str, value: str, label) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-cyan-300"),
            class_name="w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mb-3",
        ),
        rx.el.p(
            value,
            class_name="text-2xl font-extrabold text-white tracking-tight",
        ),
        rx.el.p(
            label,
            class_name="text-[11px] text-cyan-300 uppercase tracking-wider font-bold mt-1",
        ),
        class_name="rounded-xl bg-slate-900/50 backdrop-blur-xl border border-white/5 p-5 hover:border-cyan-500/30 transition-colors",
    )


def _metrics_light() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    rx.cond(LanguageState.is_zh, "值得信赖的 ", "Trusted by "),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh, "全球规模", "global scale"
                        ),
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    rx.cond(
                        LanguageState.is_zh,
                        "由真实客户与全球骨干网验证的性能与可靠性。",
                        "Real performance backed by real infrastructure and customers worldwide.",
                    ),
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                _metric_pill(
                    "trending-up",
                    "99.99%",
                    rx.cond(LanguageState.is_zh, "SLA 可用性", "SLA Uptime"),
                ),
                _metric_pill(
                    "users",
                    "50,000+",
                    rx.cond(
                        LanguageState.is_zh, "活跃客户", "Active Customers"
                    ),
                ),
                _metric_pill(
                    "server",
                    "20,000+",
                    rx.cond(
                        LanguageState.is_zh, "已部署服务器", "Deployed Servers"
                    ),
                ),
                _metric_pill(
                    "clock",
                    "< 60s",
                    rx.cond(LanguageState.is_zh, "开通时间", "Provisioning"),
                ),
                _metric_pill(
                    "shield",
                    "200 Gbps",
                    rx.cond(
                        LanguageState.is_zh, "DDoS 防护", "DDoS Mitigation"
                    ),
                ),
                _metric_pill(
                    "globe",
                    "100+",
                    rx.cond(LanguageState.is_zh, "全球节点", "Global PoPs"),
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="trust",
        class_name="relative py-20",
    )


def _pricing_teaser() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("tag", size=14, class_name="text-cyan-300"),
                    rx.el.span(
                        rx.cond(LanguageState.is_zh, "定价", "Pricing"),
                        class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
                ),
                rx.el.h2(
                    rx.cond(
                        LanguageState.is_zh, "简明定价, ", "Simple pricing, "
                    ),
                    rx.el.span(
                        rx.cond(
                            LanguageState.is_zh,
                            "随业务成长",
                            "scale as you grow",
                        ),
                        class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
                    ),
                    class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
                ),
                rx.el.p(
                    rx.cond(
                        LanguageState.is_zh,
                        "12+ 地区,20+ 方案。原生 IP 流媒体解锁,60 秒内开通。",
                        "12+ regions, 20+ plans. Native IP streaming unlock, provisioned in under 60 seconds.",
                    ),
                    class_name="text-slate-400 max-w-2xl mx-auto font-medium mb-8",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.cond(
                            LanguageState.is_zh,
                            "查看全部方案",
                            "View all plans",
                        ),
                        rx.icon("arrow-right", size=16, class_name="ml-1.5"),
                        class_name="inline-flex items-center bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white px-6 py-3 rounded-lg font-bold shadow-xl shadow-indigo-500/30 transition-all cursor-pointer",
                    ),
                    href="/shop/server",
                ),
                class_name="text-center",
            ),
            class_name="max-w-7xl mx-auto px-6 relative z-10",
        ),
        id="pricing",
        class_name="relative py-20",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.cond(ThemeState.is_dark, _ambient_bg(), rx.fragment()),
        navbar(),
        hero(),
        products_section(),
        _metrics_light(),
        _pricing_teaser(),
        faq_section(),
        cta_section(),
        footer(),
        class_name=rx.cond(
            ThemeState.is_dark,
            "font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
            "font-['Inter'] bg-white min-h-screen relative overflow-x-hidden text-neutral-900 antialiased",
        ),
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
)
app.add_page(index, route="/")
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(
    shop_server_page, route="/shop/server", on_load=ShopState.load_from_query
)
app.add_page(
    shop_server_page, route="/servers", on_load=ShopState.load_from_query
)
app.add_page(shop_server_page, route="/shop", on_load=ShopState.load_from_query)
app.add_page(
    shop_server_page,
    route="/server-catalog",
    on_load=ShopState.load_from_query,
)
app.add_page(
    shop_server_page,
    route="/server-directory",
    on_load=ShopState.load_from_query,
)
app.add_page(console_page, route="/console", on_load=ServersState.load_console)
from app.components.style_demo_view import style_demo_page
from app.components.api_spec_view import api_spec_page
from app.admin.admin_layout import admin_dashboard_layout
import logging

app.add_page(style_demo_page, route="/style-guide")
app.add_page(api_spec_page, route="/api-spec")
app.add_page(admin_dashboard_layout, route="/admin")
