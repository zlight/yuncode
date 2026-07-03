import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.products import products_section
from app.components.nodes import nodes_section
from app.components.pricing import pricing_section
from app.components.metrics import metrics_section
from app.components.faq import faq_section
from app.components.cta import cta_section
from app.components.footer import footer
from app.components.login_view import login_page
from app.components.register_view import register_page
from app.components.shop_server import shop_server_page
from app.states.shop_state import ShopState


def _grid_bg() -> rx.Component:
    return rx.el.div(
        class_name="fixed inset-0 pointer-events-none opacity-[0.15] [background-image:linear-gradient(rgba(255,255,255,0.06)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.06)_1px,transparent_1px)] [background-size:56px_56px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_30%,black_40%,transparent_100%)]",
    )


def index() -> rx.Component:
    return rx.el.main(
        _grid_bg(),
        navbar(),
        hero(),
        products_section(),
        nodes_section(),
        pricing_section(),
        metrics_section(),
        faq_section(),
        cta_section(),
        footer(),
        class_name="font-['Inter'] bg-[#0a0d14] min-h-screen relative overflow-x-hidden text-white antialiased scroll-smooth",
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
