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


def index() -> rx.Component:
    return rx.el.main(
        _ambient_bg(),
        navbar(),
        hero(),
        products_section(),
        nodes_section(),
        workflow_section(),
        capability_matrix_section(),
        metrics_section(),
        faq_section(),
        cta_section(),
        footer(),
        class_name="font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap",
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
