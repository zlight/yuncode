import reflex as rx
from app.states.language_state import LanguageState
from app.states.login_state import LoginState


def _email_suggestion_item(sug: rx.Var) -> rx.Component:
    return rx.el.button(
        rx.icon("mail", size=12, class_name="text-indigo-500 shrink-0"),
        rx.el.span(sug, class_name="text-sm text-slate-700 truncate"),
        type="button",
        on_click=lambda: LoginState.select_full_email(sug.to(str)),
        class_name="w-full flex items-center gap-2 px-3 py-2 hover:bg-indigo-50/50 text-left transition-colors",
    )


def _auth_navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("box", size=18, class_name="text-indigo-600"),
                    class_name="w-8 h-8 rounded-lg bg-indigo-50 border border-indigo-100 flex items-center justify-center",
                ),
                rx.el.span(
                    "AiarksCloud",
                    class_name="text-slate-900 font-bold text-base tracking-tight",
                ),
                href="/",
                class_name="flex items-center gap-2",
            ),
            rx.el.button(
                rx.icon(
                    "languages",
                    size=16,
                    class_name="text-indigo-600 mr-1.5",
                ),
                rx.el.span(
                    LanguageState.lang_toggle_label,
                    class_name="text-xs text-slate-600 font-semibold",
                ),
                on_click=LanguageState.toggle_language,
                class_name="flex items-center px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 hover:bg-slate-100 hover:border-slate-300 transition-all cursor-pointer",
            ),
            class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
        ),
        class_name="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-white/85 border-b border-slate-200/60",
    )


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none opacity-100 [background-image:linear-gradient(to_right,rgba(99,102,241,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.03)_1px,transparent_1px)] [background-size:24px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,black_70%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="fixed -left-20 top-1/3 w-96 h-96 rounded-full bg-indigo-100/40 blur-[120px] pointer-events-none",
        ),
        rx.el.div(
            class_name="fixed right-0 bottom-0 w-96 h-96 rounded-full bg-cyan-100/40 blur-[120px] pointer-events-none",
        ),
        _auth_navbar(),
        rx.el.div(
            rx.el.div(
                # Card
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "log-in",
                                size=18,
                                class_name="text-indigo-600",
                            ),
                            class_name="w-11 h-11 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center mx-auto mb-4",
                        ),
                        rx.el.h1(
                            LanguageState.login_title,
                            class_name="text-2xl font-bold text-slate-900 text-center tracking-tight mb-2",
                        ),
                        rx.el.p(
                            LanguageState.login_subtitle,
                            class_name="text-sm text-slate-500 text-center font-medium mb-8",
                        ),
                    ),
                    rx.el.form(
                        # Email
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "user",
                                    size=16,
                                    class_name="text-slate-400",
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
                                class_name="w-full pl-10 pr-4 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                            ),
                            rx.cond(
                                LoginState.show_suggestions
                                & (LoginState.email_suggestions.length() > 0),
                                rx.el.div(
                                    rx.foreach(
                                        LoginState.email_suggestions,
                                        _email_suggestion_item,
                                    ),
                                    class_name="absolute top-full left-0 right-0 mt-1 rounded-lg bg-white border border-slate-200 shadow-lg z-20 overflow-hidden max-h-56 overflow-y-auto",
                                ),
                                rx.fragment(),
                            ),
                            class_name="relative mb-4",
                        ),
                        # Password
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "lock",
                                    size=16,
                                    class_name="text-slate-400",
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
                                class_name="w-full pl-10 pr-10 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        LoginState.show_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-slate-400 hover:text-slate-600",
                                ),
                                type="button",
                                on_click=LoginState.toggle_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Options
                        rx.el.div(
                            rx.el.label(
                                rx.el.input(
                                    type="checkbox",
                                    name="remember_me",
                                    default_checked=LoginState.remember_me,
                                    class_name="rounded border-slate-300 bg-white text-indigo-600 focus:ring-indigo-200 mr-2 size-3.5",
                                ),
                                LanguageState.login_remember,
                                class_name="flex items-center text-xs text-slate-600 select-none cursor-pointer hover:text-slate-800 font-medium",
                            ),
                            rx.el.a(
                                LanguageState.login_forgot,
                                href="#",
                                class_name="text-xs text-indigo-600 hover:text-indigo-700 font-semibold",
                            ),
                            class_name="flex items-center justify-between mb-4",
                        ),
                        # Error
                        rx.cond(
                            LoginState.current_error != "",
                            rx.el.div(
                                rx.icon(
                                    "circle_alert",
                                    size=14,
                                    class_name="text-rose-600 shrink-0",
                                ),
                                rx.el.p(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        LoginState.validation_error_zh,
                                        LoginState.validation_error_en,
                                    ),
                                    class_name="text-rose-600 text-xs font-semibold",
                                ),
                                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-rose-50 border border-rose-200 mb-4",
                            ),
                            rx.fragment(),
                        ),
                        # Submit
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
                            class_name="w-full py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:bg-indigo-300 text-white font-bold text-sm rounded-lg shadow-md hover:shadow-lg transition-all cursor-pointer",
                        ),
                        # Divider
                        rx.el.div(
                            rx.el.div(class_name="h-px bg-slate-200 flex-1"),
                            rx.el.span(
                                LanguageState.login_or,
                                class_name="text-[10px] text-slate-400 px-3 uppercase tracking-wider font-bold",
                            ),
                            rx.el.div(class_name="h-px bg-slate-200 flex-1"),
                            class_name="flex items-center my-6",
                        ),
                        # Telegram
                        rx.el.button(
                            rx.icon(
                                "send",
                                size=14,
                                class_name="text-indigo-600",
                            ),
                            LanguageState.login_telegram,
                            type="button",
                            class_name="w-full py-2.5 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 font-semibold text-sm rounded-lg flex items-center justify-center gap-2 transition-all cursor-pointer shadow-xs",
                        ),
                        # Signup
                        rx.el.div(
                            rx.el.a(
                                LanguageState.login_no_account,
                                href="/register",
                                class_name="text-xs text-slate-500 hover:text-indigo-600 transition-colors font-medium",
                            ),
                            class_name="text-center mt-6",
                        ),
                        on_submit=LoginState.handle_login,
                        reset_on_submit=True,
                    ),
                    class_name="w-full max-w-md rounded-2xl bg-white border border-slate-200 shadow-sm p-8",
                ),
                class_name="w-full max-w-md",
            ),
            class_name="flex-1 flex items-center justify-center relative z-10 pt-24 pb-12 px-6",
        ),
        rx.el.footer(
            rx.el.p(
                "© 2025 AiarksCloud Technology Ltd. All rights reserved.",
                class_name="text-xs text-slate-400 text-center font-medium",
            ),
            class_name="py-6 bg-transparent relative z-10",
        ),
        class_name="font-['Inter'] bg-[#f8fafc] min-h-screen flex flex-col relative overflow-hidden text-slate-800 antialiased",
    )
