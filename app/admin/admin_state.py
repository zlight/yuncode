import reflex as rx
from typing import TypedDict


class AdminStat(TypedDict):
    title: str
    value: str
    icon: str
    trend: str
    color: str


class AdminUser(TypedDict):
    id: int
    name: str
    email: str
    role: str
    status: str


class AdminState(rx.State):
    current_tab: str = "overview"
    search_query: str = ""

    # Edit dialog state
    edit_dialog_open: bool = False
    edit_user_id: int = 0
    edit_name: str = ""
    edit_email: str = ""

    stats: list[AdminStat] = [
        {
            "title": "Total Users",
            "value": "1,482",
            "icon": "users",
            "trend": "+12.5% this month",
            "color": "indigo",
        },
        {
            "title": "Active Servers",
            "value": "314",
            "icon": "server",
            "trend": "+5.2% this week",
            "color": "cyan",
        },
        {
            "title": "Monthly Revenue",
            "value": "$14,240",
            "icon": "wallet",
            "trend": "+8.4% vs last month",
            "color": "emerald",
        },
        {
            "title": "Pending Tickets",
            "value": "18",
            "icon": "life-buoy",
            "trend": "-2.1% load decrease",
            "color": "amber",
        },
    ]

    users_list: list[AdminUser] = [
        {
            "id": 101,
            "name": "Alex Mercer",
            "email": "alex.m@aiarks.com",
            "role": "Super Administrator",
            "status": "Active",
        },
        {
            "id": 102,
            "name": "Sarah Connor",
            "email": "sarah.c@aiarks.com",
            "role": "Support Agent",
            "status": "Active",
        },
        {
            "id": 103,
            "name": "John Doe",
            "email": "john.doe@gmail.com",
            "role": "Customer (VIP)",
            "status": "Active",
        },
        {
            "id": 104,
            "name": "Jane Smith",
            "email": "jane.s@outlook.com",
            "role": "Customer",
            "status": "Suspended",
        },
        {
            "id": 105,
            "name": "Bruce Wayne",
            "email": "bruce@wayne.co",
            "role": "Customer (VIP)",
            "status": "Active",
        },
    ]

    @rx.event
    def set_tab(self, tab: str):
        self.current_tab = tab

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def open_edit_dialog(self, user_id: int):
        for u in self.users_list:
            if u["id"] == user_id:
                self.edit_user_id = user_id
                self.edit_name = u["name"]
                self.edit_email = u["email"]
                self.edit_dialog_open = True
                return

    @rx.event
    def close_edit_dialog(self):
        self.edit_dialog_open = False
        self.edit_user_id = 0
        self.edit_name = ""
        self.edit_email = ""

    @rx.event
    def set_edit_dialog_open(self, is_open: bool):
        if not is_open:
            self.edit_user_id = 0
            self.edit_name = ""
            self.edit_email = ""
        self.edit_dialog_open = is_open

    @rx.event
    def set_edit_name(self, val: str):
        self.edit_name = val

    @rx.event
    def set_edit_email(self, val: str):
        self.edit_email = val

    @rx.event
    def submit_edit_user(self, form_data: dict):
        new_name = str(form_data.get("name", "")).strip()
        new_email = str(form_data.get("email", "")).strip()
        if not new_name or not new_email:
            return rx.toast(
                "Name and email are required. / 姓名与邮箱不能为空。",
                duration=3500,
                close_button=True,
            )
        for i, u in enumerate(self.users_list):
            if u["id"] == self.edit_user_id:
                self.users_list[i]["name"] = new_name
                self.users_list[i]["email"] = new_email
                break
        target_id = self.edit_user_id
        self.edit_dialog_open = False
        self.edit_user_id = 0
        self.edit_name = ""
        self.edit_email = ""
        return rx.toast(
            f"User #{target_id} updated. / 已更新用户 #{target_id}。",
            duration=3000,
            close_button=True,
        )

    @rx.var
    def filtered_users(self) -> list[AdminUser]:
        if not self.search_query:
            return self.users_list
        q = self.search_query.lower()
        return [
            u
            for u in self.users_list
            if q in u["name"].lower()
            or q in u["email"].lower()
            or q in u["role"].lower()
        ]
