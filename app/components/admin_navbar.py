import reflex as rx
from app.states.language_state import LanguageState
from app.states.session_state import SessionState


def admin_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            # Left: section identifier
            rx.el.div(
                rx.icon("shield-alert", size=18, class_name="text-orange-400"),
                rx.el.span(
                    "ADMIN PORTAL / 系统管理控制台",
                    class_name="text-xs font-bold text-orange-400 uppercase tracking-widest font-mono",
                ),
                class_name="flex items-center gap-2",
            ),
            # Right: quick user info & exit
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        SessionState.auth_username,
                        class_name="text-xs font-bold text-slate-200 truncate",
                    ),
                    rx.el.p(
                        SessionState.auth_email,
                        class_name="text-[10px] text-slate-500 truncate",
                    ),
                    class_name="text-right hidden sm:block",
                ),
                rx.el.a(
                    rx.el.button(
                        rx.icon("external-link", size=14, class_name="mr-1.5"),
                        rx.cond(LanguageState.is_zh, "返回前台", "User Portal"),
                        class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-xs text-slate-300 transition-all font-semibold cursor-pointer border border-white/5",
                    ),
                    href="/console",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="backdrop-blur-xl bg-slate-950/70 border-b border-white/5 sticky top-0 z-30",
    )
