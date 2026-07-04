import reflex as rx
from app.states.language_state import LanguageState
from app.states.api_demo_state import ApiDemoState
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.ui_styles import (
    style_container,
    style_card,
    style_badge,
    style_btn_gradient,
)


def _example_btn(
    key: str, label_en: str, label_zh: str, kind: str
) -> rx.Component:
    active = ApiDemoState.active_example == key
    label = rx.cond(LanguageState.is_zh, label_zh, label_en)
    color_map = {
        "success": "emerald",
        "error": "rose",
        "list": "cyan",
    }
    accent = color_map.get(kind, "cyan")
    return rx.el.button(
        rx.el.span(
            class_name=rx.cond(
                active,
                f"w-1.5 h-1.5 rounded-full bg-{accent}-400 mr-2 shadow-lg shadow-{accent}-400/50",
                f"w-1.5 h-1.5 rounded-full bg-{accent}-500/40 mr-2",
            ),
        ),
        rx.el.span(label, class_name="text-xs font-semibold"),
        on_click=lambda: ApiDemoState.set_example(key),
        class_name=rx.cond(
            active,
            "w-full flex items-center px-3 py-2 rounded-lg bg-cyan-500/10 border border-cyan-500/40 text-cyan-100 shadow-lg shadow-cyan-500/5 transition-all cursor-pointer text-left",
            "w-full flex items-center px-3 py-2 rounded-lg bg-white/[0.02] border border-transparent hover:border-white/10 hover:bg-white/5 text-slate-300 hover:text-white transition-all cursor-pointer text-left",
        ),
    )


def _envelope_field(
    name: str, desc_en: str, desc_zh: str, tag: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.code(
                name,
                class_name="text-xs text-cyan-300 font-mono font-bold",
            ),
            style_badge(tag, color="cyan"),
            class_name="flex items-center justify-between mb-1",
        ),
        rx.el.p(
            rx.cond(LanguageState.is_zh, desc_zh, desc_en),
            class_name="text-[11px] text-slate-400 font-medium leading-relaxed",
        ),
        class_name="p-3 rounded-lg bg-white/[0.02] border border-white/5",
    )


def _biz_code_row(
    code: str, http: str, desc_en: str, desc_zh: str
) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.code(
                code, class_name="text-xs text-cyan-300 font-mono font-bold"
            ),
            class_name="px-4 py-2.5 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(
                http,
                class_name="text-xs text-slate-200 font-mono font-semibold",
            ),
            class_name="px-4 py-2.5 border-b border-white/5",
        ),
        rx.el.td(
            rx.el.span(
                rx.cond(LanguageState.is_zh, desc_zh, desc_en),
                class_name="text-xs text-slate-300 font-medium",
            ),
            class_name="px-4 py-2.5 border-b border-white/5",
        ),
    )


def _th(label) -> rx.Component:
    return rx.el.th(
        label,
        class_name="text-left text-[10px] font-bold text-slate-400 uppercase tracking-wider px-4 py-2.5",
    )


def _ui_showcase() -> rx.Component:
    body = rx.el.div(
        rx.el.div(
            rx.el.p(
                rx.cond(LanguageState.is_zh, "状态徽章", "Status Badges"),
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold mb-2",
            ),
            rx.el.div(
                style_badge(
                    rx.cond(LanguageState.is_zh, "运行中", "Running"),
                    color="emerald",
                ),
                style_badge(
                    rx.cond(LanguageState.is_zh, "预警", "Warning"),
                    color="amber",
                ),
                style_badge(
                    rx.cond(LanguageState.is_zh, "错误", "Error"), color="rose"
                ),
                style_badge(
                    rx.cond(LanguageState.is_zh, "信息", "Info"), color="cyan"
                ),
                class_name="flex flex-wrap gap-2",
            ),
            class_name="mb-5",
        ),
        rx.el.div(
            rx.el.p(
                rx.cond(LanguageState.is_zh, "按钮", "Buttons"),
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold mb-2",
            ),
            rx.el.div(
                style_btn_gradient(
                    label=rx.cond(
                        LanguageState.is_zh, "主要操作", "Primary Action"
                    ),
                    icon="rocket",
                ),
                rx.el.button(
                    rx.icon("refresh-cw", size=14, class_name="mr-1.5"),
                    rx.el.span(
                        rx.cond(LanguageState.is_zh, "次要", "Secondary"),
                    ),
                    class_name="flex items-center px-4 py-2 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 text-slate-100 text-xs font-bold transition-all cursor-pointer",
                ),
                rx.el.button(
                    rx.icon("trash-2", size=14, class_name="mr-1.5"),
                    rx.el.span(rx.cond(LanguageState.is_zh, "危险", "Danger")),
                    class_name="flex items-center px-4 py-2 rounded-lg bg-rose-500/10 border border-rose-500/30 hover:bg-rose-500/20 text-rose-300 text-xs font-bold transition-all cursor-pointer",
                ),
                class_name="flex flex-wrap gap-2",
            ),
            class_name="mb-5",
        ),
        rx.el.div(
            rx.el.p(
                rx.cond(LanguageState.is_zh, "输入框", "Inputs"),
                class_name="text-[10px] text-slate-500 uppercase tracking-widest font-bold mb-2",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    size=14,
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 pointer-events-none",
                ),
                rx.el.input(
                    placeholder=rx.cond(
                        LanguageState.is_zh,
                        "示例输入...",
                        "Sample input...",
                    ),
                    class_name="w-full pl-9 pr-4 py-2 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden text-sm",
                ),
                class_name="relative",
            ),
        ),
    )
    return style_card(
        title=rx.cond(
            LanguageState.is_zh, "UI 组件预览", "UI Component Preview"
        ),
        icon="palette",
        body=body,
        accent_color="cyan",
    )


def _envelope_reference() -> rx.Component:
    body = rx.el.div(
        _envelope_field("ok", "Boolean success flag", "布尔成功标志", "bool"),
        _envelope_field(
            "http_status", "HTTP-style status code", "HTTP 状态码", "int"
        ),
        _envelope_field(
            "code", "Business code (BizCode)", "业务状态码 (BizCode)", "str"
        ),
        _envelope_field(
            "message",
            "Bilingual { en, zh } human message",
            "双语 { en, zh } 可读消息",
            "obj",
        ),
        _envelope_field(
            "data",
            "Success payload (null on error)",
            "成功数据 (错误时为 null)",
            "any",
        ),
        _envelope_field(
            "error",
            "Error object with code, field, details, message",
            "错误对象包含 code / field / details / message",
            "obj?",
        ),
        _envelope_field(
            "meta",
            "request_id, timestamp, trace_id, duration_ms, pagination",
            "request_id、timestamp、trace_id、duration_ms、pagination",
            "obj",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-3",
    )
    return style_card(
        title=rx.cond(
            LanguageState.is_zh, "响应信封字段", "Response Envelope Fields"
        ),
        icon="package-2",
        body=body,
        accent_color="cyan",
    )


def _biz_codes_table() -> rx.Component:
    body = rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    _th(rx.cond(LanguageState.is_zh, "业务码", "BizCode")),
                    _th("HTTP"),
                    _th(rx.cond(LanguageState.is_zh, "含义", "Meaning")),
                ),
                class_name="bg-white/[0.02] border-b border-white/10",
            ),
            rx.el.tbody(
                _biz_code_row("ok", "200", "Success", "成功"),
                _biz_code_row(
                    "created", "201", "Resource created", "资源已创建"
                ),
                _biz_code_row(
                    "validation_error",
                    "422",
                    "Field validation failed",
                    "字段校验失败",
                ),
                _biz_code_row(
                    "unauthenticated", "401", "Login required", "需要登录"
                ),
                _biz_code_row(
                    "forbidden", "403", "Permission denied", "无访问权限"
                ),
                _biz_code_row(
                    "not_found", "404", "Resource missing", "资源不存在"
                ),
                _biz_code_row(
                    "email_exists",
                    "409",
                    "Email already registered",
                    "邮箱已注册",
                ),
                _biz_code_row(
                    "insufficient_balance",
                    "422",
                    "Balance too low",
                    "账户余额不足",
                ),
                _biz_code_row(
                    "out_of_stock", "409", "Plan sold out", "套餐已售罄"
                ),
                _biz_code_row(
                    "rate_limited", "429", "Too many requests", "请求过于频繁"
                ),
                _biz_code_row(
                    "internal_error", "500", "Server error", "服务器内部错误"
                ),
            ),
            class_name="table-auto w-full",
        ),
        class_name="overflow-x-auto -mx-5",
    )
    return style_card(
        title=rx.cond(
            LanguageState.is_zh, "业务状态码索引", "Business Code Index"
        ),
        icon="list-checks",
        body=body,
        accent_color="emerald",
    )


def _example_selector() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            rx.cond(LanguageState.is_zh, "成功响应", "Success Responses"),
            class_name="px-3 mb-2 text-[10px] uppercase tracking-widest font-bold text-emerald-300/70",
        ),
        rx.el.div(
            _example_btn("user_profile", "User Profile", "用户资料", "success"),
            _example_btn(
                "plans_catalog",
                "Plans Catalog (Paginated)",
                "套餐列表 (分页)",
                "list",
            ),
            _example_btn(
                "order_created",
                "Order Created (201)",
                "订单创建 (201)",
                "success",
            ),
            _example_btn("orders_list", "Orders List", "订单列表", "list"),
            _example_btn("monitor", "Monitor Snapshot", "监控快照", "success"),
            class_name="flex flex-col gap-1 mb-4",
        ),
        rx.el.p(
            rx.cond(LanguageState.is_zh, "错误响应", "Error Responses"),
            class_name="px-3 mb-2 text-[10px] uppercase tracking-widest font-bold text-rose-300/70",
        ),
        rx.el.div(
            _example_btn(
                "not_found", "Not Found (404)", "资源不存在 (404)", "error"
            ),
            _example_btn(
                "validation_error",
                "Validation Error (422)",
                "参数校验错误 (422)",
                "error",
            ),
            _example_btn(
                "insufficient_balance",
                "Insufficient Balance",
                "余额不足",
                "error",
            ),
            _example_btn(
                "rate_limited", "Rate Limited (429)", "限流 (429)", "error"
            ),
            class_name="flex flex-col gap-1",
        ),
        class_name="p-2",
    )


def _json_viewer() -> rx.Component:
    body = rx.el.div(
        rx.el.pre(
            rx.el.code(
                ApiDemoState.current_json,
                class_name="text-[11px] text-slate-100 font-mono leading-relaxed whitespace-pre",
            ),
            class_name="p-4 bg-slate-950/70 rounded-lg overflow-auto max-h-[560px]",
        ),
    )
    return style_card(
        title=rx.cond(
            LanguageState.is_zh, "JSON 响应预览", "JSON Response Preview"
        ),
        icon="braces",
        body=body,
        accent_color="cyan",
    )


def api_spec_page() -> rx.Component:
    header = rx.el.div(
        rx.el.div(
            rx.icon("book-open", size=14, class_name="text-cyan-300"),
            rx.el.span(
                rx.cond(LanguageState.is_zh, "接口规范", "API Specification"),
                class_name="text-xs text-cyan-300 font-bold tracking-wider uppercase",
            ),
            class_name="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 mb-4",
        ),
        rx.el.h1(
            rx.cond(LanguageState.is_zh, "统一 ", "Unified "),
            rx.el.span(
                rx.cond(
                    LanguageState.is_zh,
                    "接口与 UI 规范",
                    "API & UI Standards",
                ),
                class_name="bg-gradient-to-r from-indigo-300 via-cyan-300 to-white bg-clip-text text-transparent",
            ),
            class_name="text-3xl md:text-4xl font-extrabold text-white tracking-tight mb-3",
        ),
        rx.el.p(
            rx.cond(
                LanguageState.is_zh,
                "本页面展示 AiarksCloud 全站统一的复用 UI 组件与后端响应信封格式,包括成功、错误、分页列表响应,及双语 message、meta、error 对象。所有前端页面均基于同一套深色云平台视觉与青蓝强调色。",
                "This page showcases AiarksCloud's unified reusable UI components and backend response envelope format — including success, error, paginated list responses, plus bilingual messages, meta, and error objects. All pages share the same dark cloud-platform visual language and cyan accents.",
            ),
            class_name="text-sm text-slate-400 max-w-3xl font-medium mb-6",
        ),
        class_name="mb-6",
    )

    top_row = rx.el.div(
        _ui_showcase(),
        _envelope_reference(),
        class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-4",
    )

    example_row = rx.el.div(
        rx.el.aside(
            style_card(
                title=rx.cond(
                    LanguageState.is_zh, "示例响应", "Example Responses"
                ),
                icon="layers",
                body=_example_selector(),
                accent_color="cyan",
            ),
            class_name="lg:col-span-1",
        ),
        rx.el.div(_json_viewer(), class_name="lg:col-span-2"),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-4",
    )

    return rx.el.div(
        navbar(),
        style_container(
            [
                header,
                top_row,
                _request_flow_showcase(),
                example_row,
                _biz_codes_table(),
            ]
        ),
        footer(),
    )


def _flow_step(
    idx: str,
    title_en: str,
    title_zh: str,
    body_en: str,
    body_zh: str,
    icon: str,
    accent: str = "cyan",
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                idx,
                class_name=f"text-[10px] font-bold text-{accent}-300",
            ),
            class_name=f"w-8 h-8 rounded-lg bg-{accent}-500/10 border border-{accent}-500/30 flex items-center justify-center mb-3",
        ),
        rx.el.div(
            rx.icon(icon, size=16, class_name=f"text-{accent}-300"),
            rx.el.span(
                rx.cond(LanguageState.is_zh, title_zh, title_en),
                class_name="text-sm font-bold text-white ml-2",
            ),
            class_name="flex items-center mb-2",
        ),
        rx.el.p(
            rx.cond(LanguageState.is_zh, body_zh, body_en),
            class_name="text-[11px] text-slate-400 font-medium leading-relaxed",
        ),
        class_name="rounded-xl bg-white/[0.02] border border-white/5 p-4",
    )


def _flow_code_block(code: str) -> rx.Component:
    return rx.el.pre(
        rx.el.code(
            code,
            class_name="text-[11px] text-slate-100 font-mono leading-relaxed whitespace-pre",
        ),
        class_name="p-4 bg-slate-950/70 rounded-lg overflow-auto",
    )


def _request_flow_showcase() -> rx.Component:
    example_code = """# 1. Frontend event handler (Reflex state)
class ShopState(rx.State):
    @rx.event
    async def handle_purchase(self):
        from app.services import backend
        env = await backend.create_order(
            email=session.auth_email,
            plan_id=self.selected_plan_id,
            cycle_id=self.selected_cycle,
            system_id=self.selected_system,
            coupon_code=self.coupon,
        )
        if env["ok"]:
            yield rx.toast(f"Order {env['data']['order_id']} created")
        else:
            yield rx.toast(env["error"]["message"]["en"])

# 2. Unified backend facade (app/services/backend.py)
async def create_order(email, plan_id, cycle_id, ...) -> dict:
    plan = await catalog_store.get_plan(plan_id)
    if plan is None:
        return api_response.not_found(resource="plan")
    ok, code, new_balance = await user_store.deduct_balance_and_charge(
        email, final_amount)
    ...
    return api_response.created(data={
        "order_id": order_id,
        "instance_id": instance_id,
        "amount": final_amount,
    })

# 3. Unified response envelope (app/services/api_response.py)
{
    "ok": True,
    "http_status": 201,
    "code": "created",
    "message": {"en": "Created", "zh": "创建成功"},
    "data": {"order_id": "AC-...", "instance_id": "hkbgps1-...", ...},
    "error": null,
    "meta": {"request_id": "req_...", "timestamp": "..."}
}"""
    body = rx.el.div(
        rx.el.div(
            _flow_step(
                "01",
                "Page Event",
                "页面事件",
                "User clicks 'Buy Now'. Reflex state event handler is invoked with form data and current UI selection.",
                "用户点击「立即购买」。Reflex 状态事件处理器接收表单数据与当前 UI 选择。",
                "mouse-pointer-click",
                "cyan",
            ),
            _flow_step(
                "02",
                "Backend Facade",
                "后端 Facade",
                "Event handler calls app.services.backend function (e.g. backend.create_order). No direct SQL / HTTP.",
                "事件处理器调用 app.services.backend 中的函数（例如 backend.create_order）。无直接 SQL / HTTP。",
                "layers",
                "violet",
            ),
            _flow_step(
                "03",
                "Domain Services",
                "领域服务",
                "Facade orchestrates catalog_store, user_store, coupon_store etc. to validate, deduct balance, decrement stock, persist order.",
                "Facade 编排 catalog_store、user_store、coupon_store 等,完成校验、扣款、扣减库存、持久化订单。",
                "database",
                "emerald",
            ),
            _flow_step(
                "04",
                "Response Envelope",
                "统一响应",
                "Returns unified envelope: ok / code / message{en,zh} / data / error / meta. Same shape as future HTTP API.",
                "返回统一信封: ok / code / message{en,zh} / data / error / meta。与未来 HTTP 接口保持一致。",
                "package-2",
                "amber",
            ),
            _flow_step(
                "05",
                "Frontend State",
                "前端状态",
                "Handler inspects env['ok'], updates state vars, shows toast, chains follow-up events (redirect, refresh).",
                "处理器根据 env['ok'] 更新状态变量,显示 toast,链式触发后续事件(跳转、刷新)。",
                "refresh-cw",
                "rose",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3 mb-5",
        ),
        _flow_code_block(example_code),
    )
    return style_card(
        title=rx.cond(
            LanguageState.is_zh,
            "请求流示例: 页面事件 → Backend Facade → 响应信封 → 前端状态",
            "Request Flow: Page Event → Backend Facade → Envelope → Frontend State",
        ),
        icon="workflow",
        body=body,
        accent_color="violet",
    )
