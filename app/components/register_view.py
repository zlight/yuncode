import reflex as rx
from app.states.language_state import LanguageState
from app.states.register_state import RegisterState


def register_page() -> rx.Component:
    return rx.el.div(
        # Grid background simulation matching index/login page
        rx.el.div(
            class_name="fixed inset-0 pointer-events-none opacity-[0.15] [background-image:linear-gradient(rgba(255,255,255,0.06)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.06)_1px,transparent_1px)] [background-size:56px_56px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_30%,black_40%,transparent_100%)]",
        ),
        # Top branding header
        rx.el.header(
            rx.el.div(
                # Left Brand
                rx.el.a(
                    rx.el.div(
                        rx.icon("box", size=18, class_name="text-blue-400"),
                        class_name="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500/20 to-blue-500/5 border border-blue-500/30 flex items-center justify-center",
                    ),
                    rx.el.span(
                        "AiarksCloud",
                        class_name="text-white font-semibold text-base tracking-tight",
                    ),
                    href="/",
                    class_name="flex items-center gap-2",
                ),
                # Right Language switch
                rx.el.button(
                    rx.icon(
                        "languages", size=16, class_name="text-blue-400 mr-1.5"
                    ),
                    rx.el.span(
                        LanguageState.lang_toggle_label,
                        class_name="text-xs text-gray-300 font-semibold",
                    ),
                    on_click=LanguageState.toggle_language,
                    class_name="flex items-center px-3 py-1.5 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
                ),
                class_name="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between",
            ),
            class_name="fixed top-0 left-0 right-0 z-50 bg-transparent",
        ),
        # Centered narrow form card container
        rx.el.div(
            rx.el.div(
                # Form Heading
                rx.el.div(
                    rx.el.h1(
                        LanguageState.register_title,
                        class_name="text-2xl font-semibold text-white text-center tracking-tight mb-2",
                    ),
                    rx.el.p(
                        LanguageState.register_subtitle,
                        class_name="text-sm text-gray-500 text-center mb-8",
                    ),
                ),
                # The Form itself
                rx.el.form(
                    rx.el.div(
                        # Username Input Group
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "user", size=16, class_name="text-gray-500"
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type="text",
                                name="username",
                                placeholder=LanguageState.register_placeholder_username,
                                required=True,
                                class_name="w-full pl-10 pr-4 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Email Input Group
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "mail", size=16, class_name="text-gray-500"
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type="email",
                                name="email",
                                placeholder=LanguageState.register_placeholder_email,
                                required=True,
                                class_name="w-full pl-10 pr-4 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Captcha & Verification Code
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "shield-alert",
                                        size=16,
                                        class_name="text-gray-500",
                                    ),
                                    class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                                ),
                                rx.el.input(
                                    type="text",
                                    name="captcha",
                                    placeholder=LanguageState.register_placeholder_captcha,
                                    required=True,
                                    class_name="w-full pl-10 pr-4 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                                ),
                                class_name="relative flex-1",
                            ),
                            rx.el.button(
                                RegisterState.captcha_btn_text,
                                type="button",
                                on_click=RegisterState.send_captcha,
                                disabled=RegisterState.captcha_countdown > 0,
                                class_name="px-4 py-2.5 bg-[#141824]/50 border border-white/5 hover:bg-[#141824]/80 disabled:opacity-50 text-gray-300 text-sm font-medium rounded-lg transition-all cursor-pointer whitespace-nowrap",
                            ),
                            class_name="flex items-center gap-2 mb-4",
                        ),
                        # Password Input Group
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "lock", size=16, class_name="text-gray-500"
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
                                class_name="w-full pl-10 pr-10 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        RegisterState.show_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-gray-500 hover:text-gray-300",
                                ),
                                type="button",
                                on_click=RegisterState.toggle_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Repeat Password Input Group
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "lock", size=16, class_name="text-gray-500"
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
                                class_name="w-full pl-10 pr-10 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                            ),
                            rx.el.button(
                                rx.icon(
                                    rx.cond(
                                        RegisterState.show_confirm_password,
                                        "eye-off",
                                        "eye",
                                    ),
                                    size=16,
                                    class_name="text-gray-500 hover:text-gray-300",
                                ),
                                type="button",
                                on_click=RegisterState.toggle_confirm_password_visibility,
                                class_name="absolute right-3 top-1/2 -translate-y-1/2 flex items-center",
                            ),
                            class_name="relative mb-4",
                        ),
                        # Invitation Code Input Group (Optional)
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "ticket",
                                    size=16,
                                    class_name="text-gray-500",
                                ),
                                class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
                            ),
                            rx.el.input(
                                type="text",
                                name="invitation_code",
                                placeholder=LanguageState.register_placeholder_invitation,
                                required=False,
                                class_name="w-full pl-10 pr-4 py-2.5 bg-[#141824]/50 text-white placeholder-gray-600 rounded-lg border border-white/5 focus:border-blue-500/50 focus:outline-hidden transition-all text-sm",
                            ),
                            class_name="relative mb-6",
                        ),
                        # Dynamic Validation error display
                        rx.cond(
                            RegisterState.current_error != "",
                            rx.el.div(
                                rx.icon(
                                    "circle_alert",
                                    size=14,
                                    class_name="text-rose-500 shrink-0",
                                ),
                                rx.el.p(
                                    rx.cond(
                                        LanguageState.is_zh,
                                        RegisterState.validation_error_zh,
                                        RegisterState.validation_error_en,
                                    ),
                                    class_name="text-rose-400 text-xs font-medium",
                                ),
                                class_name="flex items-center gap-2 px-3 py-2 rounded-lg bg-rose-500/10 border border-rose-500/20 mb-4",
                            ),
                            rx.fragment(),
                        ),
                        # Submit Button
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
                            class_name="w-full py-2.5 bg-blue-600 hover:bg-blue-500 disabled:bg-blue-600/50 text-white font-medium text-sm rounded-lg shadow-lg shadow-blue-500/20 transition-all cursor-pointer",
                        ),
                        # Footer back to login link
                        rx.el.div(
                            rx.el.a(
                                LanguageState.register_has_account,
                                href="/login",
                                class_name="text-xs text-gray-500 hover:text-gray-300 transition-colors",
                            ),
                            class_name="text-center mt-6",
                        ),
                    ),
                    on_submit=RegisterState.handle_register,
                    reset_on_submit=True,
                ),
                class_name="w-full max-w-sm px-6 py-8 md:px-8",
            ),
            class_name="flex-1 flex items-center justify-center relative z-10",
        ),
        # Bottom Copyright Footer
        rx.el.footer(
            rx.el.p(
                "Copyright © 2023-2026 Akile LTD.",
                class_name="text-xs text-gray-600 text-center",
            ),
            class_name="py-6 bg-transparent relative z-10",
        ),
        class_name="font-['Inter'] bg-[#0a0d14] min-h-screen flex flex-col relative overflow-hidden text-white antialiased",
    )
