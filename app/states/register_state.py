import reflex as rx
import asyncio


class RegisterState(rx.State):
    show_password: bool = False
    show_confirm_password: bool = False
    is_submitting: bool = False
    captcha_countdown: int = 0
    validation_error_en: str = ""
    validation_error_zh: str = ""

    @rx.event
    def toggle_password_visibility(self):
        self.show_password = not self.show_password

    @rx.event
    def toggle_confirm_password_visibility(self):
        self.show_confirm_password = not self.show_confirm_password

    @rx.var
    def current_error(self) -> str:
        return (
            self.validation_error_zh
            if self.validation_error_zh != ""
            else self.validation_error_en
        )

    @rx.var
    async def captcha_btn_text(self) -> str:
        from app.states.language_state import LanguageState

        language_state = await self.get_state(LanguageState)
        return (
            f"{self.captcha_countdown}s"
            if self.captcha_countdown > 0
            else language_state.register_btn_captcha
        )

    @rx.event(background=True)
    async def send_captcha(self):
        async with self:
            if self.captcha_countdown > 0:
                return
            self.captcha_countdown = 60
            yield rx.toast(
                title="Captcha Sent / 验证码已发送",
                description="Please check your email inbox / 请查收您的邮箱",
                duration=3000,
                close_button=True,
            )

        while True:
            await asyncio.sleep(1.0)
            async with self:
                if self.captcha_countdown <= 0:
                    self.captcha_countdown = 0
                    break
                self.captcha_countdown -= 1

    @rx.event
    async def handle_register(self, form_data: dict):
        self.validation_error_en = ""
        self.validation_error_zh = ""
        self.is_submitting = True
        yield

        username = form_data.get("username", "").strip()
        email = form_data.get("email", "").strip()
        captcha = form_data.get("captcha", "").strip()
        password = form_data.get("password", "").strip()
        confirm_password = form_data.get("confirm_password", "").strip()

        if not username:
            self.validation_error_en = "Username is required."
            self.validation_error_zh = "用户名为必填项。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

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

        if not captcha:
            self.validation_error_en = "Captcha verification code is required."
            self.validation_error_zh = "验证码为必填项。"
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

        if password != confirm_password:
            self.validation_error_en = "Passwords do not match."
            self.validation_error_zh = "两次输入的密码不一致。"
            self.is_submitting = False
            yield rx.toast(
                title="Validation Error / 校验错误",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        await asyncio.sleep(1.5)
        self.is_submitting = False

        success_title = (
            "Registration Successful!"
            if self.validation_error_en == ""
            else "注册成功!"
        )
        success_desc = (
            f"Welcome to AkileCloud, {username}!"
            if self.validation_error_en == ""
            else f"欢迎来到 AkileCloud，{username}！"
        )

        yield rx.toast(
            title=success_title,
            description=success_desc,
            duration=4000,
            close_button=True,
        )
        yield rx.redirect("/login")