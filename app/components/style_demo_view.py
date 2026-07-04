import reflex as rx
from app.states.language_state import LanguageState
from app.states.style_test_state import StyleTestState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.ui_styles import (
    style_container,
    style_card,
    style_btn_gradient,
    style_badge,
    style_input,
)


def _demo_record_card(rec: rx.Var) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                rec["name"], class_name="text-sm text-white font-bold font-mono"
            ),
            style_badge(
                rec["status"],
                color=rx.cond(rec["status"] == "active", "emerald", "amber"),
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.el.div(
            rx.el.p(
                f"IP: {rec['ip']}",
                class_name="text-xs text-slate-300 font-mono",
            ),
            rx.el.p(
                f"Route: {rec['type']}", class_name="text-xs text-slate-400"
            ),
            class_name="space-y-1",
        ),
        class_name="p-4 rounded-lg bg-white/5 border border-white/5 hover:border-cyan-500/20 transition-all",
    )


def style_demo_page() -> rx.Component:
    form_comp = rx.el.form(
        style_input(
            icon="user",
            name="name",
            placeholder="Server Name / 服务器名称",
            required=True,
        ),
        style_input(
            icon="mail",
            name="email",
            placeholder="Admin Email / 管理邮箱",
            required=True,
        ),
        style_btn_gradient(
            label=rx.cond(
                StyleTestState.is_submitting, "Deploying...", "Deploy Live Node"
            ),
            icon="plus",
        ),
        on_submit=StyleTestState.submit_demo,
        reset_on_submit=True,
        class_name="space-y-1",
    )

    main_content = rx.el.div(
        rx.el.div(
            rx.el.h1(
                rx.cond(
                    LanguageState.is_zh, "样式规范演示", "Style Guidelines Demo"
                ),
                class_name="text-3xl font-extrabold text-white tracking-tight mb-2",
            ),
            rx.el.p(
                rx.cond(
                    LanguageState.is_zh,
                    "本页面展示通过 app/components/ui_styles.py 实现的可复用深色云平台组件。",
                    "This page showcases the reusable dark-theme cloud platform components defined in app/components/ui_styles.py.",
                ),
                class_name="text-sm text-slate-400 max-w-2xl",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            style_card(
                title=rx.cond(
                    LanguageState.is_zh,
                    "新增模拟节点 (表单示例)",
                    "Add Mock Node (Form Example)",
                ),
                icon="server",
                body=form_comp,
                accent_color="cyan",
            ),
            style_card(
                title=rx.cond(
                    LanguageState.is_zh,
                    "实例列表 (复用卡片与徽章)",
                    "Instance List (Reused Cards & Badges)",
                ),
                icon="list",
                body=rx.el.div(
                    rx.foreach(StyleTestState.saved_records, _demo_record_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                ),
                accent_color="emerald",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        class_name="space-y-6",
    )

    return rx.el.div(navbar(), style_container([main_content]), footer())
