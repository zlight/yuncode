import reflex as rx


class UIState(rx.State):
    open_faq: str = "faq-1"
    mobile_menu_open: bool = False

    @rx.event
    def toggle_faq(self, faq_id: str):
        if self.open_faq == faq_id:
            self.open_faq = ""
        else:
            self.open_faq = faq_id

    @rx.event
    def toggle_mobile_menu(self):
        self.mobile_menu_open = not self.mobile_menu_open

    @rx.event
    def close_mobile_menu(self):
        self.mobile_menu_open = False