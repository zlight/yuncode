import reflex as rx
import logging
from app.services import user_store


class SessionState(rx.State):
    session_token: str = rx.Cookie(name="aiarks_session", path="/")
    auth_email: str = rx.Cookie(name="auth_email", path="/")
    auth_username: str = rx.Cookie(name="auth_username", path="/")
    is_logged_in_cookie: str = rx.Cookie(name="is_logged_in_cookie", path="/")
    vip_cookie: str = rx.Cookie(name="vip_cookie", path="/")

    balance: float = 0.0
    ak_coins: int = 0
    total_spending: float = 0.0
    referral_earnings: float = 0.0
    invitation_code: str = ""

    @rx.var
    def is_logged_in(self) -> bool:
        return self.is_logged_in_cookie == "true"

    @rx.var
    def is_vip(self) -> bool:
        return self.vip_cookie == "true"

    @rx.var
    def avatar_initial(self) -> str:
        name = self.auth_username.strip()
        if name:
            return name[0].upper()
        email = self.auth_email.strip()
        if email:
            return email[0].upper()
        return "U"

    @rx.event
    async def login_user(self, email: str, username: str):
        try:
            token = await user_store.create_session(email)
            profile = await user_store.get_public_profile(email)
        except Exception as e:
            logging.exception(f"Error during login_user session creation: {e}")
            token = ""
            profile = {}
        self.session_token = token
        self.auth_email = email
        self.auth_username = username or str(profile.get("username", ""))
        self.is_logged_in_cookie = "true"
        if profile.get("is_vip"):
            self.vip_cookie = "true"
        else:
            self.vip_cookie = ""
        self.balance = float(profile.get("balance", 0.0))
        self.ak_coins = int(profile.get("ak_coins", 0))
        self.total_spending = float(profile.get("total_spending", 0.0))
        self.referral_earnings = float(profile.get("referral_earnings", 0.0))
        self.invitation_code = str(profile.get("invitation_code", ""))

    @rx.event
    async def refresh_profile(self):
        if not self.auth_email:
            return
        try:
            profile = await user_store.get_public_profile(self.auth_email)
        except Exception as e:
            logging.exception(f"Error refreshing profile: {e}")
            profile = {}
        if not profile:
            return
        self.auth_username = str(profile.get("username", self.auth_username))
        if profile.get("is_vip"):
            self.vip_cookie = "true"
        self.balance = float(profile.get("balance", 0.0))
        self.ak_coins = int(profile.get("ak_coins", 0))
        self.total_spending = float(profile.get("total_spending", 0.0))
        self.referral_earnings = float(profile.get("referral_earnings", 0.0))
        self.invitation_code = str(profile.get("invitation_code", ""))

    @rx.event
    async def upgrade_to_vip(self):
        if not self.auth_email:
            return
        try:
            await user_store.upgrade_vip(self.auth_email)
        except Exception as e:
            logging.exception(f"Error upgrading VIP: {e}")
        self.vip_cookie = "true"

    @rx.event
    async def logout_user(self):
        try:
            await user_store.destroy_session(self.session_token)
        except Exception as e:
            logging.exception(f"Error destroying session: {e}")
        self.session_token = ""
        self.auth_email = ""
        self.auth_username = ""
        self.is_logged_in_cookie = ""
        self.vip_cookie = ""
        self.balance = 0.0
        self.ak_coins = 0
        self.total_spending = 0.0
        self.referral_earnings = 0.0
        self.invitation_code = ""
        yield rx.remove_cookie("aiarks_session")
        yield rx.remove_cookie("auth_email")
        yield rx.remove_cookie("auth_username")
        yield rx.remove_cookie("is_logged_in_cookie")
        yield rx.remove_cookie("vip_cookie")
        yield rx.redirect("/")
