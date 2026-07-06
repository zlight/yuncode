import reflex as rx
from app.states.language_state import LanguageState


def error_banner(
    message_en: rx.Var,
    message_zh: rx.Var,
    on_dismiss: rx.event.EventType | None = None,
    on_retry: rx.event.EventType | None = None,
    retry_label_en: str = "Retry",
    retry_label_zh: str = "重试",
    icon: str = "circle_alert",
) -> rx.Component:
    """Reusable rose-toned persistent error banner.

    Displays a bilingual error message in a fixed-styled rose card with an
    optional dismiss (X) button and an optional retry action button.
    """
    dismiss_btn = rx.cond(
        on_dismiss != None,
        rx.el.button(
            rx.icon("x", size=14, class_name="text-rose-300 hover:text-white"),
            on_click=on_dismiss,
            type="button",
            class_name="ml-2 shrink-0 w-7 h-7 rounded-md hover:bg-rose-500/20 flex items-center justify-center cursor-pointer transition-all",
        ),
        rx.fragment(),
    )
    retry_btn = rx.cond(
        on_retry != None,
        rx.el.button(
            rx.icon("refresh-cw", size=12, class_name="mr-1.5"),
            rx.el.span(
                rx.cond(LanguageState.is_zh, retry_label_zh, retry_label_en),
                class_name="text-xs font-bold",
            ),
            on_click=on_retry,
            type="button",
            class_name="mt-3 inline-flex items-center px-3 py-1.5 rounded-md bg-rose-500/20 hover:bg-rose-500/30 border border-rose-500/40 text-rose-100 transition-all cursor-pointer",
        ),
        rx.fragment(),
    )
    return rx.el.div(
        rx.el.div(
            rx.icon(
                icon,
                size=14,
                class_name="text-rose-300 shrink-0 mt-0.5",
            ),
            rx.el.div(
                rx.el.p(
                    rx.cond(LanguageState.is_zh, message_zh, message_en),
                    class_name="text-xs text-rose-100 font-semibold leading-relaxed",
                ),
                retry_btn,
                class_name="flex-1 min-w-0",
            ),
            dismiss_btn,
            class_name="flex items-start gap-2",
        ),
        class_name="rounded-lg bg-rose-500/10 border border-rose-500/40 shadow-lg shadow-rose-500/10 px-3 py-2.5 backdrop-blur-sm animate-fadeIn",
    )
