import reflex as rx


class PricingState(rx.State):
    billing_cycle: str = "monthly"
    selected_region: str = "all"
    compare_mode: bool = False
    compared_plans: list[str] = []
    is_loading: bool = False

    @rx.event
    def set_cycle(self, cycle: str):
        self.billing_cycle = cycle

    @rx.event
    def set_region(self, region: str):
        self.selected_region = region

    @rx.event
    def toggle_compare(self):
        self.compare_mode = not self.compare_mode
        if not self.compare_mode:
            self.compared_plans = []

    @rx.event
    def toggle_plan_compare(self, plan: str):
        if plan in self.compared_plans:
            self.compared_plans.remove(plan)
        else:
            if len(self.compared_plans) < 3:
                self.compared_plans.append(plan)

    @rx.var
    def cycle_multiplier(self) -> float:
        if self.billing_cycle == "yearly":
            return 10.0
        if self.billing_cycle == "quarterly":
            return 2.85
        return 1.0

    @rx.var
    def cycle_label(self) -> str:
        if self.billing_cycle == "yearly":
            return "/yr"
        if self.billing_cycle == "quarterly":
            return "/qtr"
        return "/mo"