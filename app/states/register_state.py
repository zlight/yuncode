import reflex as rx
import asyncio
import logging
from app.services import user_store


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

        username = str(form_data.get("username", "")).strip()
        email = str(form_data.get("email", "")).strip()
        captcha = str(form_data.get("captcha", "")).strip()
        password = str(form_data.get("password", "")).strip()
        confirm_password = str(form_data.get("confirm_password", "")).strip()
        invitation_code = str(form_data.get("invitation_code", "")).strip()

        # 1. Username check
        if not username:
            self.validation_error_en = "Username is required."
            self.validation_error_zh = "用户名为必填项。"
        elif len(username) < 3 or len(username) > 20:
            self.validation_error_en = (
                "Username must be between 3 and 20 characters."
            )
            self.validation_error_zh = "用户名长度必须在 3 到 20 位之间。"
        elif not all(c.isalnum() or c == "_" for c in username):
            self.validation_error_en = (
                "Username can only contain letters, numbers, and underscores."
            )
            self.validation_error_zh = "用户名只能包含字母、数字和下划线。"
        # 2. Email check
        elif not email:
            self.validation_error_en = "Email is required."
            self.validation_error_zh = "电子邮箱为必填项。"
        elif "@" not in email or "." not in email:
            self.validation_error_en = "Please enter a valid email address."
            self.validation_error_zh = "请输入有效的电子邮箱地址。"
        # 3. Captcha check
        elif not captcha:
            self.validation_error_en = "Verification code is required."
            self.validation_error_zh = "验证码为必填项。"
        # 4. Password check
        elif not password:
            self.validation_error_en = "Password is required."
            self.validation_error_zh = "密码为必填项。"
        elif len(password) < 6:
            self.validation_error_en = "Password must be at least 6 characters."
            self.validation_error_zh = "密码长度不能少于 6 位。"
        elif password != confirm_password:
            self.validation_error_en = "Passwords do not match."
            self.validation_error_zh = "两次输入的密码不一致。"

        if self.validation_error_en:
            self.is_submitting = False
            yield rx.toast(
                title="Registration Failed / 注册失败",
                description=self.validation_error_zh,
                duration=4000,
                close_button=True,
            )
            return

        await asyncio.sleep(0.5)

        from app.services import backend

        try:
            env = await backend.register(
                email=email,
                username=username,
                password=password,
                invitation_code=invitation_code,
            )
        except Exception as e:
            logging.exception(f"Backend register exception: {e}")
            env = {"ok": False, "code": "internal_error"}

        self.is_submitting = False

        if not env.get("ok"):
            code = env.get("code", "")
            if code == "email_exists":
                self.validation_error_en = "This email is already registered."
                self.validation_error_zh = "该电子邮箱已被注册。"
            elif code == "username_exists":
                self.validation_error_en = "This username is already taken."
                self.validation_error_zh = "该用户名已被使用。"
            elif code == "rate_limited":
                self.validation_error_en = (
                    "Too many registration attempts. Please try again later."
                )
                self.validation_error_zh = "尝试注册次数过多，请稍后再试。"
            else:
                err_obj = env.get("error", {})
                msg_obj = err_obj.get("message", {})
                self.validation_error_en = msg_obj.get(
                    "en", "Registration failed. Please try again."
                )
                self.validation_error_zh = msg_obj.get(
                    "zh", "注册失败，请稍后重试。"
                )

            yield rx.toast(
                title="Registration Error / 注册失败",
                description=self.validation_error_zh,
                duration=5000,
                close_button=True,
            )
            return

        yield rx.toast(
            title="Registration Successful! / 注册成功!",
            description=f"Welcome to AiarksCloud, {username}!",
            duration=3500,
            close_button=True,
        )
        yield rx.redirect("/login")
