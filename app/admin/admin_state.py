import reflex as rx
from datetime import datetime
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


class AdminServer(TypedDict):
    id: str
    name: str
    owner_email: str
    region: str
    region_flag: str
    node: str
    spec: str
    price: str
    price_num: float
    status: str
    expires: str
    days_left: int
    auto_renew: bool
    cpu: str
    ram: str
    disk: str
    bandwidth: str
    ip: str
    os: str
    created: str


class OperationLog(TypedDict):
    id: int
    action: str
    action_icon: str
    action_color: str
    instance_id: str
    instance_name: str
    operator: str
    timestamp: str
    result: str


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

    server_search: str = ""
    server_region_filter: str = "all"
    server_status_filter: str = "all"
    server_sort_by: str = "expires-asc"

    admin_servers: list[AdminServer] = [
        {
            "id": "hkbgps1-2025a8f",
            "name": "HK-Pro-01",
            "owner_email": "demo@aiarks.com",
            "region": "HongKong",
            "region_flag": "🇭🇰",
            "node": "HKBGP",
            "spec": "1C / 1024M / 10GB",
            "price": "¥50.00/mo",
            "price_num": 50.00,
            "status": "Running",
            "expires": "2025-12-14",
            "days_left": 45,
            "auto_renew": True,
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB NVMe",
            "bandwidth": "10 Gbps",
            "ip": "103.28.201.42",
            "os": "Debian 11",
            "created": "2025-06-14",
        },
        {
            "id": "jpbgps1-2025b9c",
            "name": "JP-Tokyo-Direct",
            "owner_email": "admin@aiarks.com",
            "region": "Japan",
            "region_flag": "🇯🇵",
            "node": "JPBGP",
            "spec": "2C / 4096M / 60GB",
            "price": "¥69.99/mo",
            "price_num": 69.99,
            "status": "Running",
            "expires": "2025-11-20",
            "days_left": 21,
            "auto_renew": True,
            "cpu": "2 Cores",
            "ram": "4096 M",
            "disk": "60 GB NVMe",
            "bandwidth": "5 Gbps",
            "ip": "185.19.22.14",
            "os": "Ubuntu 22",
            "created": "2025-05-20",
        },
        {
            "id": "usbgps1-2025c2d",
            "name": "US-LA-Backbone",
            "owner_email": "vip@aiarks.com",
            "region": "United States",
            "region_flag": "🇺🇸",
            "node": "USBGP",
            "spec": "4C / 8192M / 160GB",
            "price": "¥89.99/mo",
            "price_num": 89.99,
            "status": "Stopped",
            "expires": "2025-12-05",
            "days_left": 36,
            "auto_renew": False,
            "cpu": "4 Cores",
            "ram": "8192 M",
            "disk": "160 GB NVMe",
            "bandwidth": "10 Gbps",
            "ip": "142.171.88.9",
            "os": "Rocky Linux 9",
            "created": "2025-04-05",
        },
        {
            "id": "molites1-2025d1e",
            "name": "MO-Broadcast-IP",
            "owner_email": "demo@aiarks.com",
            "region": "Macao",
            "region_flag": "🇲🇴",
            "node": "MOLite",
            "spec": "1C / 1024M / 10GB",
            "price": "¥43.74/mo",
            "price_num": 43.74,
            "status": "Running",
            "expires": "2025-11-05",
            "days_left": 6,
            "auto_renew": True,
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB NVMe",
            "bandwidth": "2 Gbps",
            "ip": "154.31.202.7",
            "os": "Debian 12",
            "created": "2025-05-05",
        },
        {
            "id": "sgbgps1-2025e4f",
            "name": "SG-Standard-Prod",
            "owner_email": "vip@aiarks.com",
            "region": "Singapore",
            "region_flag": "🇸🇬",
            "node": "SGBGP",
            "spec": "2C / 4096M / 80GB",
            "price": "¥59.99/mo",
            "price_num": 59.99,
            "status": "Running",
            "expires": "2025-11-08",
            "days_left": 9,
            "auto_renew": True,
            "cpu": "2 Cores",
            "ram": "4096 M",
            "disk": "80 GB NVMe",
            "bandwidth": "2 Gbps",
            "ip": "103.75.180.55",
            "os": "Ubuntu 20",
            "created": "2025-05-08",
        },
        {
            "id": "debgps1-2025f7a",
            "name": "DE-Frankfurt-DC",
            "owner_email": "admin@aiarks.com",
            "region": "Germany",
            "region_flag": "🇩🇪",
            "node": "DEBGP",
            "spec": "4C / 8192M / 160GB",
            "price": "¥79.99/mo",
            "price_num": 79.99,
            "status": "Running",
            "expires": "2026-01-15",
            "days_left": 77,
            "auto_renew": True,
            "cpu": "4 Cores",
            "ram": "8192 M",
            "disk": "160 GB NVMe",
            "bandwidth": "5 Gbps",
            "ip": "89.44.211.30",
            "os": "Debian 12",
            "created": "2025-01-15",
        },
        {
            "id": "krbgps1-2025g8b",
            "name": "KR-Seoul-Gaming",
            "owner_email": "demo@aiarks.com",
            "region": "South Korea",
            "region_flag": "🇰🇷",
            "node": "KRBGP",
            "spec": "1C / 2048M / 40GB",
            "price": "¥34.99/mo",
            "price_num": 34.99,
            "status": "Suspended",
            "expires": "2025-12-01",
            "days_left": 32,
            "auto_renew": False,
            "cpu": "1 Core",
            "ram": "2048 M",
            "disk": "40 GB NVMe",
            "bandwidth": "1 Gbps",
            "ip": "121.166.12.88",
            "os": "Ubuntu 22",
            "created": "2025-06-01",
        },
        {
            "id": "twbgps1-2025h9c",
            "name": "TW-Taipei-Main",
            "owner_email": "vip@aiarks.com",
            "region": "Taiwan",
            "region_flag": "🇹🇼",
            "node": "TWBGP",
            "spec": "2C / 4096M / 60GB",
            "price": "¥54.99/mo",
            "price_num": 54.99,
            "status": "Running",
            "expires": "2025-11-11",
            "days_left": 12,
            "auto_renew": True,
            "cpu": "2 Cores",
            "ram": "4096 M",
            "disk": "60 GB NVMe",
            "bandwidth": "1 Gbps",
            "ip": "203.74.109.18",
            "os": "Debian 11",
            "created": "2025-05-11",
        },
        {
            "id": "jpbgps1-2025i0d",
            "name": "JP-Osaka-CDN",
            "owner_email": "demo@aiarks.com",
            "region": "Japan",
            "region_flag": "🇯🇵",
            "node": "JPBGP",
            "spec": "1C / 1024M / 20GB",
            "price": "¥29.99/mo",
            "price_num": 29.99,
            "status": "Stopped",
            "expires": "2025-10-30",
            "days_left": 0,
            "auto_renew": False,
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "20 GB NVMe",
            "bandwidth": "1 Gbps",
            "ip": "153.126.187.44",
            "os": "Ubuntu 20",
            "created": "2024-10-30",
        },
        {
            "id": "hkbgps1-2025j1e",
            "name": "HK-BGP-Gaming-2",
            "owner_email": "vip@aiarks.com",
            "region": "HongKong",
            "region_flag": "🇭🇰",
            "node": "HKBGP",
            "spec": "2C / 2048M / 20GB",
            "price": "¥90.00/mo",
            "price_num": 90.00,
            "status": "Running",
            "expires": "2026-02-20",
            "days_left": 113,
            "auto_renew": True,
            "cpu": "2 Cores",
            "ram": "2048 M",
            "disk": "20 GB NVMe",
            "bandwidth": "10 Gbps",
            "ip": "103.28.19.99",
            "os": "Rocky Linux 8",
            "created": "2025-02-20",
        },
        {
            "id": "ukbgps1-2025k2f",
            "name": "UK-London-Prod",
            "owner_email": "admin@aiarks.com",
            "region": "UK",
            "region_flag": "🇬🇧",
            "node": "UKBGP",
            "spec": "2C / 4096M / 80GB",
            "price": "¥64.99/mo",
            "price_num": 64.99,
            "status": "Running",
            "expires": "2025-12-25",
            "days_left": 56,
            "auto_renew": True,
            "cpu": "2 Cores",
            "ram": "4096 M",
            "disk": "80 GB NVMe",
            "bandwidth": "2 Gbps",
            "ip": "185.144.201.7",
            "os": "Ubuntu 22",
            "created": "2025-06-25",
        },
    ]

    # ==== Server Detail / Edit / Logs state ====
    detail_dialog_open: bool = False
    detail_server_id: str = ""

    edit_server_dialog_open: bool = False
    edit_server_id: str = ""
    edit_server_name: str = ""
    edit_server_owner: str = ""
    edit_server_status: str = "Running"
    edit_server_expires: str = ""
    edit_server_auto_renew: bool = True

    admin_operator: str = "Admin@AiarksCloud"

    operation_logs: list[OperationLog] = [
        {
            "id": 1,
            "action": "Server Started",
            "action_icon": "play",
            "action_color": "emerald",
            "instance_id": "hkbgps1-2025a8f",
            "instance_name": "HK-Pro-01",
            "operator": "Admin@AiarksCloud",
            "timestamp": "2025-10-30 14:22:03",
            "result": "success",
        },
        {
            "id": 2,
            "action": "Auto-Renew Enabled",
            "action_icon": "refresh-cw",
            "action_color": "cyan",
            "instance_id": "jpbgps1-2025b9c",
            "instance_name": "JP-Tokyo-Direct",
            "operator": "Admin@AiarksCloud",
            "timestamp": "2025-10-30 13:14:55",
            "result": "success",
        },
        {
            "id": 3,
            "action": "Server Suspended",
            "action_icon": "ban",
            "action_color": "rose",
            "instance_id": "krbgps1-2025g8b",
            "instance_name": "KR-Seoul-Gaming",
            "operator": "Admin@AiarksCloud",
            "timestamp": "2025-10-29 21:05:11",
            "result": "success",
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

    @rx.event
    def set_server_search(self, q: str):
        self.server_search = q

    @rx.event
    def set_server_region_filter(self, region: str):
        self.server_region_filter = region

    @rx.event
    def set_server_status_filter(self, status: str):
        self.server_status_filter = status

    @rx.event
    def set_server_sort(self, sort: str):
        self.server_sort_by = sort

    @rx.event
    def reset_server_filters(self):
        self.server_search = ""
        self.server_region_filter = "all"
        self.server_status_filter = "all"
        self.server_sort_by = "expires-asc"

    def _log(
        self,
        action: str,
        icon: str,
        color: str,
        instance_id: str,
        instance_name: str,
        result: str = "success",
    ):
        next_id = max((log["id"] for log in self.operation_logs), default=0) + 1
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operation_logs.insert(
            0,
            {
                "id": next_id,
                "action": action,
                "action_icon": icon,
                "action_color": color,
                "instance_id": instance_id,
                "instance_name": instance_name,
                "operator": self.admin_operator,
                "timestamp": ts,
                "result": result,
            },
        )

    def _find_server_index(self, server_id: str) -> int:
        for i, s in enumerate(self.admin_servers):
            if s["id"] == server_id:
                return i
        return -1

    @rx.event
    def toggle_server_status(self, server_id: str):
        for i, s in enumerate(self.admin_servers):
            if s["id"] == server_id:
                prev = s["status"]
                if s["status"] == "Running":
                    self.admin_servers[i]["status"] = "Stopped"
                    self._log(
                        "Server Stopped",
                        "power-off",
                        "amber",
                        s["id"],
                        s["name"],
                    )
                elif s["status"] == "Stopped":
                    self.admin_servers[i]["status"] = "Running"
                    self._log(
                        "Server Started",
                        "play",
                        "emerald",
                        s["id"],
                        s["name"],
                    )
                elif s["status"] == "Suspended":
                    self.admin_servers[i]["status"] = "Running"
                    self._log(
                        "Server Unlocked",
                        "unlock",
                        "emerald",
                        s["id"],
                        s["name"],
                    )
                new_status = self.admin_servers[i]["status"]
                return rx.toast(
                    f"Server {server_id} → {prev} → {new_status}",
                    duration=2500,
                    close_button=True,
                )

    @rx.event
    def suspend_server(self, server_id: str):
        for i, s in enumerate(self.admin_servers):
            if s["id"] == server_id:
                self.admin_servers[i]["status"] = "Suspended"
                self._log(
                    "Server Suspended",
                    "ban",
                    "rose",
                    s["id"],
                    s["name"],
                )
                return rx.toast(
                    f"Server {server_id} suspended / 服务器已封禁",
                    duration=2500,
                    close_button=True,
                )

    @rx.event
    def unsuspend_server(self, server_id: str):
        idx = self._find_server_index(server_id)
        if idx == -1:
            return
        self.admin_servers[idx]["status"] = "Running"
        s = self.admin_servers[idx]
        self._log("Server Unlocked", "unlock", "emerald", s["id"], s["name"])
        return rx.toast(
            f"Server {server_id} unlocked / 已解封",
            duration=2500,
            close_button=True,
        )

    @rx.event
    def restart_server(self, server_id: str):
        idx = self._find_server_index(server_id)
        if idx == -1:
            return
        self.admin_servers[idx]["status"] = "Running"
        s = self.admin_servers[idx]
        self._log(
            "Server Restarted",
            "rotate-cw",
            "cyan",
            s["id"],
            s["name"],
        )
        return rx.toast(
            f"Server {server_id} restarted / 已重启",
            duration=2500,
            close_button=True,
        )

    @rx.event
    def renew_server(self, server_id: str):
        idx = self._find_server_index(server_id)
        if idx == -1:
            return
        s = self.admin_servers[idx]
        self.admin_servers[idx]["days_left"] = int(s["days_left"]) + 30
        self._log(
            "Server Renewed (+30d)",
            "refresh-cw",
            "orange",
            s["id"],
            s["name"],
        )
        return rx.toast(
            f"Server {server_id} renewed +30 days / 已续费 30 天",
            duration=2500,
            close_button=True,
        )

    @rx.event
    def toggle_server_auto_renew(self, server_id: str):
        idx = self._find_server_index(server_id)
        if idx == -1:
            return
        cur = bool(self.admin_servers[idx].get("auto_renew", False))
        self.admin_servers[idx]["auto_renew"] = not cur
        s = self.admin_servers[idx]
        new_val = "Enabled" if not cur else "Disabled"
        self._log(
            f"Auto-Renew {new_val}",
            "refresh-cw",
            "cyan" if not cur else "amber",
            s["id"],
            s["name"],
        )
        return rx.toast(
            f"Auto-renew {new_val} / 自动续费已{'开启' if not cur else '关闭'}",
            duration=2500,
            close_button=True,
        )

    # ==== Details Dialog ====
    @rx.event
    def open_server_details(self, server_id: str):
        self.detail_server_id = server_id
        self.detail_dialog_open = True

    @rx.event
    def set_detail_dialog_open(self, is_open: bool):
        if not is_open:
            self.detail_server_id = ""
        self.detail_dialog_open = is_open

    @rx.event
    def close_server_details(self):
        self.detail_dialog_open = False
        self.detail_server_id = ""

    # ==== Edit Server Dialog ====
    @rx.event
    def open_edit_server(self, server_id: str):
        idx = self._find_server_index(server_id)
        if idx == -1:
            return
        s = self.admin_servers[idx]
        self.edit_server_id = server_id
        self.edit_server_name = s["name"]
        self.edit_server_owner = s["owner_email"]
        self.edit_server_status = s["status"]
        self.edit_server_expires = s["expires"]
        self.edit_server_auto_renew = bool(s.get("auto_renew", False))
        self.edit_server_dialog_open = True

    @rx.event
    def set_edit_server_dialog_open(self, is_open: bool):
        if not is_open:
            self.edit_server_id = ""
            self.edit_server_name = ""
            self.edit_server_owner = ""
            self.edit_server_status = "Running"
            self.edit_server_expires = ""
            self.edit_server_auto_renew = True
        self.edit_server_dialog_open = is_open

    @rx.event
    def close_edit_server(self):
        self.set_edit_server_dialog_open(False)

    @rx.event
    def set_edit_server_status(self, val: str):
        self.edit_server_status = val

    @rx.event
    def toggle_edit_server_auto_renew(self):
        self.edit_server_auto_renew = not self.edit_server_auto_renew

    @rx.event
    def submit_edit_server(self, form_data: dict):
        name = str(form_data.get("name", "")).strip()
        owner = str(form_data.get("owner_email", "")).strip()
        status = (
            str(form_data.get("status", "")).strip() or self.edit_server_status
        )
        expires = str(form_data.get("expires", "")).strip()
        auto_renew_val = form_data.get("auto_renew")
        auto_renew = (
            bool(auto_renew_val)
            if auto_renew_val is not None
            else self.edit_server_auto_renew
        )

        if not name or not owner or not expires:
            return rx.toast(
                "Name, owner and expires are required. / 名称、所属用户与到期时间为必填。",
                duration=3500,
                close_button=True,
            )

        idx = self._find_server_index(self.edit_server_id)
        if idx == -1:
            return
        prev = dict(self.admin_servers[idx])
        self.admin_servers[idx]["name"] = name
        self.admin_servers[idx]["owner_email"] = owner
        self.admin_servers[idx]["status"] = status
        self.admin_servers[idx]["expires"] = expires
        self.admin_servers[idx]["auto_renew"] = auto_renew
        self._log(
            "Server Edited",
            "pencil",
            "violet",
            self.admin_servers[idx]["id"],
            name,
        )
        target_id = self.edit_server_id
        self.edit_server_dialog_open = False
        self.edit_server_id = ""
        return rx.toast(
            f"Server {target_id} updated. / 已更新服务器 {target_id}。",
            duration=3000,
            close_button=True,
        )

    @rx.var
    def detail_server(self) -> AdminServer:
        for s in self.admin_servers:
            if s["id"] == self.detail_server_id:
                return s
        # fallback empty
        return {
            "id": "",
            "name": "-",
            "owner_email": "-",
            "region": "-",
            "region_flag": "🌐",
            "node": "-",
            "spec": "-",
            "price": "-",
            "price_num": 0.0,
            "status": "-",
            "expires": "-",
            "days_left": 0,
            "auto_renew": False,
            "cpu": "-",
            "ram": "-",
            "disk": "-",
            "bandwidth": "-",
            "ip": "-",
            "os": "-",
            "created": "-",
        }

    @rx.var
    def has_detail_selection(self) -> bool:
        return self.detail_server_id != ""

    @rx.var
    def recent_operation_logs(self) -> list[OperationLog]:
        return self.operation_logs[:20]

    @rx.var
    def server_region_options(self) -> list[str]:
        seen: list[str] = []
        for s in self.admin_servers:
            if s["region"] not in seen:
                seen.append(s["region"])
        return seen

    @rx.var
    def filtered_servers(self) -> list[AdminServer]:
        result = list(self.admin_servers)
        if self.server_search.strip():
            q = self.server_search.lower()
            result = [
                s
                for s in result
                if q in s["name"].lower()
                or q in s["id"].lower()
                or q in s["owner_email"].lower()
                or q in s["region"].lower()
                or q in s["node"].lower()
            ]
        if self.server_region_filter != "all":
            result = [
                s for s in result if s["region"] == self.server_region_filter
            ]
        if self.server_status_filter != "all":
            result = [
                s for s in result if s["status"] == self.server_status_filter
            ]
        if self.server_sort_by == "expires-asc":
            result = sorted(result, key=lambda s: s["days_left"])
        elif self.server_sort_by == "expires-desc":
            result = sorted(result, key=lambda s: -s["days_left"])
        elif self.server_sort_by == "price-asc":
            result = sorted(result, key=lambda s: s["price_num"])
        elif self.server_sort_by == "price-desc":
            result = sorted(result, key=lambda s: -s["price_num"])
        elif self.server_sort_by == "name":
            result = sorted(result, key=lambda s: s["name"].lower())
        return result

    @rx.var
    def running_count(self) -> int:
        return len([s for s in self.admin_servers if s["status"] == "Running"])

    @rx.var
    def stopped_count(self) -> int:
        return len(
            [
                s
                for s in self.admin_servers
                if s["status"] == "Stopped" or s["status"] == "Suspended"
            ]
        )

    @rx.var
    def expiring_count(self) -> int:
        return len(
            [
                s
                for s in self.admin_servers
                if s["days_left"] <= 15 and s["days_left"] >= 0
            ]
        )

    @rx.var
    def monthly_revenue(self) -> float:
        return sum(
            s["price_num"]
            for s in self.admin_servers
            if s["status"] == "Running"
        )

    @rx.var
    def monthly_revenue_display(self) -> str:
        return f"¥{self.monthly_revenue:,.2f}"

    @rx.var
    def total_servers(self) -> int:
        return len(self.admin_servers)

    @rx.var
    def filtered_servers_count(self) -> int:
        return len(self.filtered_servers)

    @rx.var
    def servers_has_active_filter(self) -> bool:
        return (
            self.server_search != ""
            or self.server_region_filter != "all"
            or self.server_status_filter != "all"
        )
