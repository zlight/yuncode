import reflex as rx


class ThemeState(rx.State):
    theme_mode: str = rx.LocalStorage("dark", name="theme_mode_key", sync=True)

    @rx.event
    def toggle_theme(self):
        self.theme_mode = "light" if self.theme_mode == "dark" else "dark"

    @rx.var
    def is_dark(self) -> bool:
        return self.theme_mode == "dark"

    @rx.var
    def bg_class(self) -> str:
        return (
            "bg-[#04060f] text-slate-100"
            if self.is_dark
            else "bg-neutral-50 text-neutral-900"
        )

    @rx.var
    def card_class(self) -> str:
        return (
            "bg-slate-900/60 backdrop-blur-xl border border-white/5"
            if self.is_dark
            else "bg-white border border-neutral-200 shadow-sm"
        )

    @rx.var
    def text_primary(self) -> str:
        return "text-white" if self.is_dark else "text-neutral-900"

    @rx.var
    def text_secondary(self) -> str:
        return "text-slate-400" if self.is_dark else "text-neutral-500"

    @rx.var
    def border_class(self) -> str:
        return "border-white/10" if self.is_dark else "border-neutral-200"

    @rx.var
    def accent_text(self) -> str:
        return "text-cyan-300" if self.is_dark else "text-neutral-900 font-bold"

    @rx.var
    def primary_btn_class(self) -> str:
        return (
            "bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white shadow-lg shadow-indigo-500/30"
            if self.is_dark
            else "bg-neutral-900 hover:bg-neutral-800 text-white"
        )

    @rx.var
    def secondary_btn_class(self) -> str:
        return (
            "bg-white/5 border border-white/10 text-slate-100 hover:bg-white/10"
            if self.is_dark
            else "bg-neutral-100 border border-neutral-200 text-neutral-800 hover:bg-neutral-200"
        )

    @rx.var
    def input_class(self) -> str:
        return (
            "bg-slate-900/60 text-white placeholder-slate-500 border border-white/10 focus:border-cyan-500/50"
            if self.is_dark
            else "bg-white text-neutral-900 placeholder-neutral-400 border border-neutral-300 focus:border-neutral-900 focus:ring-neutral-200"
        )
