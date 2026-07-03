import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.products import products_section
from app.components.nodes import nodes_section
from app.components.workflow import workflow_section
from app.components.capability_matrix import capability_matrix_section
from app.components.pricing import pricing_section
from app.components.metrics import metrics_section
from app.components.faq import faq_section
from app.components.cta import cta_section
from app.components.footer import footer
from app.components.login_view import login_page
from app.components.register_view import register_page
from app.components.shop_server import shop_server_page
from app.components.console import console_page
from app.states.shop_state import ShopState


def _grid_bg() -> rx.Component:
    return rx.el.div(
        class_name="fixed inset-0 pointer-events-none opacity-100 [background-image:linear-gradient(to_right,rgba(99,102,241,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.03)_1px,transparent_1px)] [background-size:24px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,black_70%,transparent_100%)]",
    )


def index() -> rx.Component:
    return rx.el.main(
        _grid_bg(),
        navbar(),
        hero(),
        products_section(),
        nodes_section(),
        workflow_section(),
        capability_matrix_section(),
        pricing_section(),
        metrics_section(),
        faq_section(),
        cta_section(),
        footer(),
        class_name="font-['Inter'] bg-[#f8fafc] min-h-screen relative overflow-x-hidden text-slate-800 antialiased scroll-smooth",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")
app.add_page(login_page, route="/login")
app.add_page(register_page, route="/register")
app.add_page(
    shop_server_page, route="/shop/server", on_load=ShopState.load_from_query
)
app.add_page(console_page, route="/console")
