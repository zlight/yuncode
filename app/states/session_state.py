import reflex as rx


class SessionState(rx.State):
    auth_email: str = rx.Cookie(name="auth_email", path="/")
    auth_username: str = rx.Cookie(name="auth_username", path="/")
    is_logged_in_cookie: str = rx.Cookie(name="is_logged_in_cookie", path="/")
    vip_cookie: str = rx.Cookie(name="vip_cookie", path="/")

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
    def login_user(self, email: str, username: str):
        self.auth_email = email
        self.auth_username = username
        self.is_logged_in_cookie = "true"

    @rx.event
    def upgrade_to_vip(self):
        self.vip_cookie = "true"

    @rx.event
    def logout_user(self):
        self.auth_email = ""
        self.auth_username = ""
        self.is_logged_in_cookie = ""
        self.vip_cookie = ""
        yield rx.remove_cookie("auth_email")
        yield rx.remove_cookie("auth_username")
        yield rx.remove_cookie("is_logged_in_cookie")
        yield rx.remove_cookie("vip_cookie")
        yield rx.redirect("/")
