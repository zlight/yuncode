import reflex as rx
from app.states.language_state import LanguageState
from app.states.register_state import RegisterState


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


def _light_input(icon: str, **props) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-slate-400"),
            class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
        ),
        rx.el.input(
            class_name="w-full pl-10 pr-4 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
            **props,
        ),
        class_name="relative mb-4",
    )


def register_page() -> rx.Component:
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
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "user-plus",
                            size=18,
                            class_name="text-indigo-600",
                        ),
                        class_name="w-11 h-11 rounded-xl bg-indigo-50 border border-indigo-100 flex items-center justify-center mx-auto mb-4",
                    ),
                    rx.el.h1(
                        LanguageState.register_title,
                        class_name="text-2xl font-bold text-slate-900 text-center tracking-tight mb-2",
                    ),
                    rx.el.p(
                        LanguageState.register_subtitle,
                        class_name="text-sm text-slate-500 text-center font-medium mb-8",
                    ),
                    rx.el.form(
                        _light_input(
                            "user",
                            type="text",
                            name="username",
                            placeholder=LanguageState.register_placeholder_username,
                            required=True,
                        ),
                        _light_input(
                            "mail",
                            type="email",
                            name="email",
                            placeholder=LanguageState.register_placeholder_email,
                            required=True,
                        ),
                        # Captcha row
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "shield-alert",
                                        size=16,
                                        class_name="text-slate-400",
                                    ),
                                    class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                                ),
                                rx.el.input(
                                    type="text",
                                    name="captcha",
                                    placeholder=LanguageState.register_placeholder_captcha,
                                    required=True,
                                    class_name="w-full pl-10 pr-4 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                                ),
                                class_name="relative flex-1",
                            ),
                            rx.el.button(
                                RegisterState.captcha_btn_text,
                                type="button",
                                on_click=RegisterState.send_captcha,
                                disabled=RegisterState.captcha_countdown > 0,
                                class_name="px-4 py-2.5 bg-white border border-slate-200 hover:border-indigo-500 hover:text-indigo-600 disabled:opacity-50 disabled:hover:border-slate-200 disabled:hover:text-slate-500 text-slate-700 text-xs font-bold rounded-lg transition-all cursor-pointer whitespace-nowrap shadow-xs",
                            ),
                            class_name="flex items-center gap-2 mb-4",
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
                                    RegisterState.show_password,
                                    "text",
                                    "password",
                                ),
                                name="password",
                                placeholder=LanguageState.register_placeholder_password,
                                required=True,
                                class_name="w-full pl-10 pr-10 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        RegisterState.show_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-slate-400 hover:text-slate-600",
                                ),
                                type="button",
                                on_click=RegisterState.toggle_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Confirm password
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
                                    RegisterState.show_confirm_password,
                                    "text",
                                    "password",
                                ),
                                name="confirm_password",
                                placeholder=LanguageState.register_placeholder_confirm,
                                required=True,
                                class_name="w-full pl-10 pr-10 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        RegisterState.show_confirm_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-slate-400 hover:text-slate-600",
                                ),
                                type="button",
                                on_click=RegisterState.toggle_confirm_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Invitation code
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "ticket",
                                    size=16,
                                    class_name="text-slate-400",
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type="text",
                                name="invitation_code",
                                placeholder=LanguageState.register_placeholder_invitation,
                                required=False,
                                class_name="w-full pl-10 pr-4 py-2.5 bg-white text-slate-800 placeholder-slate-400 rounded-lg border border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-100 focus:outline-hidden transition-all text-sm shadow-xs",
                            ),
                            class_name="relative mb-6",
                        ),
                        # Error
                        rx.cond(
                            RegisterState.current_error != "",
                            rx.el.div(
                                rx.icon(
                                    "circle_alert",
                                    size=14,
                                    class_name="text-rose-600 shrink-0",
                                ),
                                rx.el.p(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        RegisterState.validation_error_zh,
                                        RegisterState.validation_error_en,
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
                                RegisterState.is_submitting,
                                rx.el.span(
                                    LanguageState.register_btn_submitting,
                                    class_name="flex items-center justify-center gap-2 animate-pulse",
                                ),
                                rx.el.span(LanguageState.register_btn_submit),
                            ),
                            type="submit",
                            disabled=RegisterState.is_submitting,
                            class_name="w-full py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:bg-indigo-300 text-white font-bold text-sm rounded-lg shadow-md hover:shadow-lg transition-all cursor-pointer",
                        ),
                        rx.el.div(
                            rx.el.a(
                                LanguageState.register_has_account,
                                href="/login",
                                class_name="text-xs text-slate-500 hover:text-indigo-600 transition-colors font-medium",
                            ),
                            class_name="text-center mt-6",
                        ),
                        on_submit=RegisterState.handle_register,
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
