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

        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()

        if not email:
            self.validation_error_en = "Email is required."
            self.validation_error_zh = "电子邮箱为必填项。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        if "@" not in email:
            self.validation_error_en = "Please enter a valid email address."
            self.validation_error_zh = "请输入有效的电子邮箱地址。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        if not password:
            self.validation_error_en = "Password is required."
            self.validation_error_zh = "密码为必填项。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        if len(password) < 6:
            self.validation_error_en = "Password must be at least 6 characters."
            self.validation_error_zh = "密码长度不能少于 6 位。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        await asyncio.sleep(0.6)

        try:
            ok, code, rec = await user_store.verify_password(email, password)
        except Exception as e:
            logging.exception(f"Error verifying password: {e}")
            ok, code, rec = False, "error", None

        self.is_submitting = False

        if not ok:
            if code == "not_found":
                self.validation_error_en = (
                    "Account not found. Please register first."
                )
                self.validation_error_zh = "账户不存在，请先注册。"
            elif code == "wrong_password":
                self.validation_error_en = "Incorrect password."
                self.validation_error_zh = "密码错误。"
            else:
                self.validation_error_en = (
                    "Authentication failed. Please try again."
                )
                self.validation_error_zh = "认证失败，请稍后重试。"
            yield rx.toast(
                title="Authentication Failed / 认证失败",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        username = (
            rec.get("username", email.split("@")[0].capitalize())
            if rec
            else email.split("@")[0].capitalize()
        )
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
