import reflex as rx
from app.states.language_state import LanguageState
from app.states.theme_state import ThemeState


def theme_toggle() -> rx.Component:
    """Reusable theme toggle button (dark <-> light)."""
    return rx.el.button(
        rx.icon(
            rx.cond(ThemeState.is_dark, "sun", "moon"),
            size=16,
            class_name=rx.cond(
                ThemeState.is_dark, "text-slate-200", "text-neutral-800"
            ),
        ),
        on_click=ThemeState.toggle_theme,
        title="Toggle theme",
        class_name=rx.cond(
            ThemeState.is_dark,
            "flex items-center justify-center w-9 h-9 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 transition-all cursor-pointer",
            "flex items-center justify-center w-9 h-9 rounded-lg bg-neutral-100 border border-neutral-200 hover:bg-neutral-200 transition-all cursor-pointer",
        ),
    )


def theme_root_class() -> rx.Var:
    """Root container class that switches between dark and light themes."""
    return rx.cond(
        ThemeState.is_dark,
        "font-['Inter'] bg-[#04060f] min-h-screen relative overflow-x-hidden text-slate-100 antialiased",
        "font-['Inter'] bg-white min-h-screen relative overflow-x-hidden text-neutral-900 antialiased",
    )


def theme_navbar_class() -> rx.Var:
    return rx.cond(
        ThemeState.is_dark,
        "fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-slate-950/70 border-b border-white/5",
        "fixed top-0 left-0 right-0 z-50 backdrop-blur-xl bg-white/85 border-b border-neutral-200",
    )


def style_bg() -> rx.Component:
    """Reusable ambient backdrop with glowing orbs and grids."""
    return rx.el.div(
        rx.el.div(
            class_name="absolute inset-0 [background-image:linear-gradient(to_right,rgba(99,102,241,0.06)_1px,transparent_1px),linear-gradient(to_bottom,rgba(99,102,241,0.06)_1px,transparent_1px)] [background-size:40px_40px] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_0%,black_50%,transparent_100%)]",
        ),
        rx.el.div(
            class_name="absolute -top-40 left-1/2 -translate-x-1/2 w-[900px] h-[900px] rounded-full bg-indigo-600/15 blur-[160px]",
        ),
        rx.el.div(
            class_name="absolute top-[40%] -left-40 w-[600px] h-[600px] rounded-full bg-cyan-500/8 blur-[140px]",
        ),
        class_name="fixed inset-0 pointer-events-none overflow-hidden -z-20",
    )


def style_card(
    body: rx.Component,
    title: rx.Var | None = None,
    icon: str | None = None,
    accent_color: str = "cyan",
) -> rx.Component:
    """Reusable standard glassmorphic dark-themed container."""
    header = rx.cond(
        title,
        rx.el.div(
            rx.el.div(
                rx.cond(
                    icon,
                    rx.icon(
                        icon, size=14, class_name=f"text-{accent_color}-300"
                    ),
                    rx.fragment(),
                ),
                rx.el.span(
                    title, class_name="text-xs text-white font-bold ml-1.5"
                ),
                class_name="flex items-center",
            ),
            class_name="flex items-center justify-between px-4 py-3 border-b border-white/5 bg-white/[0.02]",
        ),
        rx.fragment(),
    )
    return rx.el.div(
        header,
        rx.el.div(body, class_name="p-5"),
        class_name="rounded-xl bg-slate-900/60 backdrop-blur-xl border border-white/5 overflow-hidden transition-all duration-200 hover:border-white/10",
    )


def style_btn_gradient(
    label: rx.Var,
    icon: str | None = None,
    on_click: rx.event.EventType | None = None,
) -> rx.Component:
    """Standard CTA gradient button."""
    icon_comp = rx.cond(
        icon, rx.icon(icon, size=14, class_name="mr-1.5"), rx.fragment()
    )
    return rx.el.button(
        icon_comp,
        rx.el.span(label),
        on_click=on_click,
        class_name="flex items-center justify-center px-4 py-2 bg-gradient-to-r from-indigo-500 to-cyan-500 hover:brightness-110 text-white text-xs font-bold rounded-lg shadow-lg shadow-indigo-500/20 transition-all cursor-pointer",
    )


def style_badge(text: rx.Var, color: str = "cyan") -> rx.Component:
    """Standard badge for status labels."""
    return rx.el.span(
        text,
        class_name=rx.match(
            color,
            (
                "cyan",
                "inline-flex items-center text-[10px] font-bold text-cyan-300 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/30 w-fit",
            ),
            (
                "emerald",
                "inline-flex items-center text-[10px] font-bold text-emerald-300 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30 w-fit",
            ),
            (
                "rose",
                "inline-flex items-center text-[10px] font-bold text-rose-300 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30 w-fit",
            ),
            (
                "amber",
                "inline-flex items-center text-[10px] font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/30 w-fit",
            ),
            "inline-flex items-center text-[10px] font-bold text-slate-300 bg-white/5 px-2 py-0.5 rounded border border-white/10 w-fit",
        ),
    )


def style_input(icon: str, **props) -> rx.Component:
    """Standard input component with absolute icons."""
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=16, class_name="text-slate-500"),
            class_name="absolute left-3 top-1/2 -translate-y-1/2 flex items-center pointer-events-none",
        ),
        rx.el.input(
            class_name="w-full pl-10 pr-4 py-2.5 bg-slate-900/60 text-white placeholder-slate-500 rounded-lg border border-white/10 focus:border-cyan-500/50 focus:ring-2 focus:ring-cyan-500/20 focus:outline-hidden transition-all text-sm",
            **props,
        ),
        class_name="relative mb-4",
    )


def style_container(
    children: list[rx.Component], current_route: str = "/"
) -> rx.Component:
    """Uniform viewport wrapper with uniform padding and style backbone."""
    return rx.el.div(
        rx.cond(ThemeState.is_dark, style_bg(), rx.fragment()),
        rx.el.div(
            *children,
            class_name="max-w-7xl mx-auto px-6 pt-24 pb-16 relative z-10",
        ),
        class_name=theme_root_class(),
    )
