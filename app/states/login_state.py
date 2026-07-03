import reflex as rx
import asyncio


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
        from app.states.language_state import LanguageState

        # Access language preference to determine error message
        # In case language state is imported inside this module
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

        # Front-end / state validation
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

        await asyncio.sleep(1.5)  # Simulate API roundtrip latency

        self.is_submitting = False

        # Simulated authentication logic
        if email == "admin@aiarks.com" and password != "admin123":
            self.validation_error_en = "Incorrect password."
            self.validation_error_zh = "密码错误。"
            yield rx.toast(
                title="Authentication Failed / 认证失败",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
        else:
            # Setup language-specific success toast message
            success_title = (
                "Welcome Back!"
                if self.validation_error_en == ""
                else "欢迎回来!"
            )
            success_desc = (
                f"Successfully authenticated as {email}"
                if self.validation_error_en == ""
                else f"成功以 {email} 身份登录"
            )
            yield rx.toast(
                title=success_title,
                description=success_desc,
                duration=4000,
                close_button=True,
            )
            yield rx.redirect("/")
