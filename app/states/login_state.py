import reflex as rx
import asyncio
import logging
from app.services import user_store


class LoginState(rx.State):
    show_password: bool = False
    remember_me: bool = False
    is_submitting: bool = False
    validation_error_en: str = ""
    validation_error_zh: str = ""
    email_input: str = ""
    show_suggestions: bool = False
    common_suffixes: list[str] = [
        "gmail.com",
        "qq.com",
        "outlook.com",
        "hotmail.com",
        "icloud.com",
        "yahoo.com",
        "163.com",
        "126.com",
        "proton.me",
    ]

    @rx.event
    def set_email_input(self, val: str):
        self.email_input = val
        if val.strip() != "":
            self.show_suggestions = True
        else:
            self.show_suggestions = False

    @rx.event
    def select_full_email(self, full_email: str):
        self.email_input = full_email
        self.show_suggestions = False

    @rx.event
    def hide_suggestions(self):
        self.show_suggestions = False

    @rx.var
    def email_suggestions(self) -> list[str]:
        val = self.email_input.strip()
        if not val:
            return []
        parts = val.split("@")
        prefix = parts[0]
        if not prefix:
            return []
        typed_suffix = parts[1] if len(parts) > 1 else ""
        results: list[str] = []
        for s in self.common_suffixes:
            if not typed_suffix:
                results.append(f"{prefix}@{s}")
            elif s.startswith(typed_suffix) and s != typed_suffix:
                results.append(f"{prefix}@{s}")
        return results

    @rx.event
    def toggle_password_visibility(self):
        self.show_password = not self.show_password

    @rx.event
    def toggle_remember_me(self):
        self.remember_me = not self.remember_me

    @rx.var
    def current_error(self) -> str:
        return (
            self.validation_error_zh
            if self.validation_error_zh != ""
            else self.validation_error_en
        )

    @rx.event
    async def handle_login(self, form_data: dict):
        self.validation_error_en = ""
        self.validation_error_zh = ""
        self.is_submitting = True
        yield

        email = str(form_data.get("email", "")).strip()
        password = str(form_data.get("password", "")).strip()

        # 1. Email check
        if not email:
            self.validation_error_en = "Email is required."
            self.validation_error_zh = "电子邮箱为必填项。"
        elif "@" not in email or "." not in email:
            self.validation_error_en = "Please enter a valid email address."
            self.validation_error_zh = "请输入有效的电子邮箱地址。"
        # 2. Password check
        elif not password:
            self.validation_error_en = "Password is required."
            self.validation_error_zh = "密码为必填项。"
        elif len(password) < 6:
            self.validation_error_en = "Password must be at least 6 characters."
            self.validation_error_zh = "密码长度不能少于 6 位。"

        if self.validation_error_en:
            self.is_submitting = False
            yield rx.toast(
                title="Login Failed / 登录失败",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        await asyncio.sleep(0.5)

        from app.services import backend

        try:
            env = await backend.login(email, password)
        except Exception as e:
            logging.exception(f"Backend login exception: {e}")
            env = {"ok": False, "code": "internal_error"}

        self.is_submitting = False

        if not env.get("ok"):
            code = env.get("code", "")
            if code == "not_found":
                self.validation_error_en = (
                    "Account not found. Please check your email or register."
                )
                self.validation_error_zh = "账户不存在，请检查邮箱或先注册。"
            elif code in ("invalid_credentials", "wrong_password"):
                self.validation_error_en = (
                    "Incorrect password. Please try again."
                )
                self.validation_error_zh = "密码错误，请重试。"
            elif code == "rate_limited":
                self.validation_error_en = (
                    "Too many requests. Please try again later."
                )
                self.validation_error_zh = "请求过于频繁，请稍后再试。"
            else:
                err_obj = env.get("error", {})
                msg_obj = err_obj.get("message", {})
                self.validation_error_en = msg_obj.get(
                    "en", "Server error occurred. Please contact support."
                )
                self.validation_error_zh = msg_obj.get(
                    "zh", "发生服务器错误，请联系技术支持。"
                )

            yield rx.toast(
                title="Authentication Failed / 认证失败",
                description=self.validation_error_zh,
                duration=5000,
                close_button=True,
            )
            return

        profile = env["data"].get("profile", {}) or {}
        username = profile.get("username") or email.split("@")[0].capitalize()

        from app.states.session_state import SessionState

        session = await self.get_state(SessionState)
        await session.login_user(email, username)

        yield rx.toast(
            title="Welcome Back! / 欢迎回来!",
            description=f"Successfully authenticated as {email}",
            duration=3500,
            close_button=True,
        )
        yield rx.redirect("/")
