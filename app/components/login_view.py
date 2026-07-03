import reflex as rx
from app.states.language_state import LanguageState
from app.states.login_state import LoginState


def _email_suggestion_item(sug: rx.Var) -> rx.Component:
    return rx.el.button(
        rx.icon("mail", size=12, class_name="text-cyan-300 shrink-0"),
        rx.el.span(sug, class_name="text-sm text-slate-200 truncate"),
        type="button",
        on_click=lambda: LoginState.select_full_email(sug.to(str)),
        class_name="w-full flex items-center gap-2 px-3 py-2 hover:bg-white/5 text-left transition-colors",
    )


def _auth_navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-white"),
                    class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-indigo-500/30",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-white font-bold text-base tracking-tight",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon(
                    "languages",
                    size=16,
                    class_name="text-cyan-300 mr-1.5",
                ),
                rx.el.span(
                    LanguageState.lang_toggle_label,
                    class_name="text-xs text-slate-200 font-semibold",
                ),
                on_click=LanguageState.toggle_language,
                class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
            ),
            class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-slate-950/70 border-b border-white/5",
    )


def _ambient_bg() -> rx.Component:
    return rx.fragment(
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none [background-image:linear-gradient(to_right,rgba(99,102,241,0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.06)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_0%,black_50%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-indigo-600/20 blur-[160px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed top-[40%] -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/10 blur-[140px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed top-[70%] -right-40 w-[600px] h-[600px] rounded-full bg-violet-600/15 blur-[140px] pointer-events-none",
        ),
    )


def login_page() -> rx.Component:
    return rx.el.div(
        _ambient_bg(),
        _auth_navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="absolute -inset-px rounded-2xl bg-gradient-to-b from-cyan-400/30 via-indigo-500/20 to-transparent blur-sm -z-10",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "log-in",
                                size=18,
                                class_name="text-cyan-300",
                            ),
                            class_name="w-11 h-11 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center mx-auto mb-4 shadow-lg shadow-indigo-500/10",
                        ),
                        rx.el.h1(
                            LanguageState.login_title,
                            class_name="text-2xl font-extrabold text-white text-center tracking-tight mb-2",
                        ),
                        rx.el.p(
                            LanguageState.login_subtitle,
                            class_name="text-sm text-slate-400 text-center font-medium mb-8",
                        ),
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "user",
                                    size=16,
                                    class_name="text-slate-500",
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type="email",
                                name="email",
                                placeholder=LanguageState.login_placeholder_email,
                                default_value=LoginState.email_input,
                                key=LoginState.email_input,
                                required=True,
                                auto_complete="off",
                                class_name="w-full pl-10 pr-4 py-2.5 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden transition-all text-sm",
                            ),
                            rx.cond(
                                LoginState.show_suggestions
                                & (LoginState.email_suggestions.length() > 0),
                                rx.el.div(
                                    rx.foreach(
                                        LoginState.email_suggestions,
                                        _email_suggestion_item,
                                    ),
                                    class_name="absolute top-full left-0 right-0 mt-1 rounded-lg bg-slate-950/95 backdrop-blur-xl border border-white/10 shadow-2xl z-20 overflow-hidden max-h-56 overflow-y-auto",
                                ),
                                rx.fragment(),
                            ),
                            class_name="relative mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "lock",
                                    size=16,
                                    class_name="text-slate-500",
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type=rx.cond(
                                    LoginState.show_password,
                                    "text",
                                    "password",
                                ),
                                name="password",
                                placeholder=LanguageState.login_placeholder_password,
                                required=True,
                                class_name="w-full pl-10 pr-10 py-2.5 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden transition-all text-sm",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        LoginState.show_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-slate-500 hover:text-cyan-300",
                                ),
                                type="button",
                                on_click=LoginState.toggle_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center cursor-pointer",
                            ),
                            class_name="relative mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                rx.el.input(
                                    type="checkbox",
                                    name="remember_me",
                                    default_checked=LoginState.remember_me,
                                    class_name="rounded border-white/20 bg-slate-900 text-cyan-500 focus:ring-cyan-500/30 mr-2 size-3.5",
                                ),
                                LanguageState.login_remember,
                                class_name="flex items-center text-xs text-slate-400 select-none cursor-pointer hover:text-slate-200 font-medium",
                            ),
                            rx.el.a(
                                LanguageState.login_forgot,
                                href="#",
                                class_name="text-xs text-cyan-300 hover:text-cyan-200 font-semibold",
                            ),
                            class_name="flex items-center justify-between mb-4",
                        ),
                        rx.cond(
                            LoginState.current_error != "",
                            rx.el.div(
                                rx.icon(
                                    "circle_alert",
                                    size=14,
                                    class_name="text-rose-300 shrink-0",
                                ),
                                rx.el.p(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        LoginState.validation_error_zh,
                                        LoginState.validation_error_en,
                                    ),
                                    class_name="text-rose-300 text-xs font-semibold",
                                ),
                                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-rose-500/10 border border-rose-500/30 mb-4",
                            ),
                            rx.fragment(),
                        ),
                        rx.el.button(
                            rx.cond(
                                LoginState.is_submitting,
                                rx.el.span(
                                    LanguageState.login_btn_logging_in,
                                    class_name="flex items-center justify-center gap-2 animate-pulse",
                                ),
                                rx.el.span(LanguageState.login_btn_submit),
                            ),
                            type="submit",
                            disabled=LoginState.is_submitting,
                            class_name="w-full py-2.5 bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 disabled:opacity-50 disabled:cursor-not-allowed text-white font-bold text-sm rounded-lg shadow-xl shadow-indigo-500/30 transition-all cursor-pointer",
                        ),
                        rx.el.div(
                            rx.el.div(class_name="h-px bg-white/10 flex-1"),
                            rx.el.span(
                                LanguageState.login_or,
                                class_name="text-[10px] text-slate-500 px-3 uppercase tracking-wider font-bold",
                            ),
                            rx.el.div(class_name="h-px bg-white/10 flex-1"),
                            class_name="flex items-center my-6",
                        ),
                        rx.el.button(
                            rx.icon(
                                "send",
                                size=14,
                                class_name="text-cyan-300",
                            ),
                            LanguageState.login_telegram,
                            type="button",
                            class_name="w-full py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-white/20 text-slate-100 font-semibold text-sm rounded-lg flex items-center justify-center gap-2 transition-all cursor-pointer",
                        ),
                        rx.el.div(
                            rx.el.a(
                                LanguageState.login_no_account,
                                href="/register",
                                class_name="text-xs text-slate-400 hover:text-cyan-300 transition-colors font-medium",
                            ),
                            class_name="text-center mt-6",
                        ),
                        on_submit=LoginState.handle_login,
                        reset_on_submit=True,
                    ),
                    class_name="relative w-full max-w-md rounded-2xl bg-slate-900/70 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/50 p-8",
                ),
                class_name="relative w-full max-w-md",
            ),
            class_name="flex-1 flex items-center justify-center relative z-10 pt-24 pb-12 px-6",
        ),
        rx.el.footer(
            rx.el.p(
                "© 2025 AiarksCloud Technology Ltd. All rights reserved.",
                class_name="text-xs text-slate-500 text-center font-medium",
            ),
            class_name="py-6 bg-transparent relative z-10",
        ),
        class_name="font-['Inter'] bg-[#04060f] min-h-screen flex flex-col relative overflow-hidden text-slate-100 antialiased",
    )
