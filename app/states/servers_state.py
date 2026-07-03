import reflex as rx
import logging
from typing import TypedDict
from app.services import user_store


class ServerInstance(TypedDict):
    id: str
    name: str
    status: str
    ip: str
    region: str
    region_flag: str
    node: str
    plan: str
    cpu: str
    ram: str
    disk: str
    bandwidth: str
    traffic_used: str
    traffic_total: str
    traffic_percent: int
    reset_price: str
    price: str
    expires: str
    auto_renew: bool
    health: str
    os: str
    created: str


class FirewallRule(TypedDict):
    id: str
    action: str
    protocol: str
    port: str
    source: str
    desc: str
    enabled: bool


class DnsRecord(TypedDict):
    id: str
    name: str
    type: str
    value: str
    ttl: str
    status: str


class BillingRecord(TypedDict):
    id: str
    date: str
    item: str
    cycle: str
    amount: str
    status: str


class MonitorPoint(TypedDict):
    time: str
    cpu: int
    memory: int
    net_in: int
    net_out: int
    disk: int


class RecentEvent(TypedDict):
    time: str
    level: str
    icon: str
    message: str


class ServersState(rx.State):
    console_view: str = "overview"
    selected_instance_id: str = ""
    filter_region: str = "all"
    search_query: str = ""
    manage_tab: str = "dashboard"
    monitor_range: str = "24h"
    is_authenticated: bool = False
    is_loaded: bool = False

    instances: list[ServerInstance] = []

    firewall_rules: list[FirewallRule] = [
        {
            "id": "fw-01",
            "action": "ALLOW",
            "protocol": "TCP",
            "port": "22",
            "source": "0.0.0.0/0",
            "desc": "SSH access",
            "enabled": True,
        },
        {
            "id": "fw-02",
            "action": "ALLOW",
            "protocol": "TCP",
            "port": "80",
            "source": "0.0.0.0/0",
            "desc": "HTTP",
            "enabled": True,
        },
        {
            "id": "fw-03",
            "action": "ALLOW",
            "protocol": "TCP",
            "port": "443",
            "source": "0.0.0.0/0",
            "desc": "HTTPS",
            "enabled": True,
        },
        {
            "id": "fw-04",
            "action": "ALLOW",
            "protocol": "TCP",
            "port": "3306",
            "source": "10.0.0.0/8",
            "desc": "MySQL internal",
            "enabled": True,
        },
        {
            "id": "fw-05",
            "action": "DENY",
            "protocol": "TCP",
            "port": "23",
            "source": "0.0.0.0/0",
            "desc": "Block Telnet",
            "enabled": True,
        },
        {
            "id": "fw-06",
            "action": "ALLOW",
            "protocol": "UDP",
            "port": "51820",
            "source": "0.0.0.0/0",
            "desc": "WireGuard VPN",
            "enabled": False,
        },
        {
            "id": "fw-07",
            "action": "ALLOW",
            "protocol": "ICMP",
            "port": "*",
            "source": "0.0.0.0/0",
            "desc": "Ping (ICMP)",
            "enabled": True,
        },
    ]

    dns_records: list[DnsRecord] = [
        {
            "id": "dns-1",
            "name": "@",
            "type": "A",
            "value": "103.28.201.42",
            "ttl": "600",
            "status": "active",
        },
        {
            "id": "dns-2",
            "name": "www",
            "type": "A",
            "value": "103.28.201.42",
            "ttl": "600",
            "status": "active",
        },
        {
            "id": "dns-3",
            "name": "api",
            "type": "A",
            "value": "103.28.201.42",
            "ttl": "300",
            "status": "active",
        },
        {
            "id": "dns-4",
            "name": "@",
            "type": "AAAA",
            "value": "2001:db8::1",
            "ttl": "600",
            "status": "active",
        },
        {
            "id": "dns-5",
            "name": "mail",
            "type": "MX",
            "value": "10 mail.aiarks.com",
            "ttl": "3600",
            "status": "active",
        },
        {
            "id": "dns-6",
            "name": "cdn",
            "type": "CNAME",
            "value": "cdn.aiarks.net",
            "ttl": "600",
            "status": "active",
        },
        {
            "id": "dns-7",
            "name": "@",
            "type": "TXT",
            "value": "v=spf1 include:_spf.aiarks.com ~all",
            "ttl": "3600",
            "status": "active",
        },
        {
            "id": "dns-8",
            "name": "_dmarc",
            "type": "TXT",
            "value": "v=DMARC1; p=quarantine;",
            "ttl": "3600",
            "status": "pending",
        },
    ]

    billing_records: list[BillingRecord] = []

    monitor_data: list[MonitorPoint] = [
        {
            "time": "00:00",
            "cpu": 12,
            "memory": 42,
            "net_in": 120,
            "net_out": 80,
            "disk": 34,
        },
        {
            "time": "02:00",
            "cpu": 8,
            "memory": 40,
            "net_in": 90,
            "net_out": 60,
            "disk": 34,
        },
        {
            "time": "04:00",
            "cpu": 6,
            "memory": 39,
            "net_in": 70,
            "net_out": 45,
            "disk": 35,
        },
        {
            "time": "06:00",
            "cpu": 15,
            "memory": 44,
            "net_in": 210,
            "net_out": 130,
            "disk": 35,
        },
        {
            "time": "08:00",
            "cpu": 32,
            "memory": 52,
            "net_in": 480,
            "net_out": 320,
            "disk": 36,
        },
        {
            "time": "10:00",
            "cpu": 45,
            "memory": 61,
            "net_in": 720,
            "net_out": 510,
            "disk": 37,
        },
        {
            "time": "12:00",
            "cpu": 58,
            "memory": 68,
            "net_in": 890,
            "net_out": 640,
            "disk": 38,
        },
        {
            "time": "14:00",
            "cpu": 72,
            "memory": 74,
            "net_in": 1120,
            "net_out": 780,
            "disk": 39,
        },
        {
            "time": "16:00",
            "cpu": 66,
            "memory": 71,
            "net_in": 980,
            "net_out": 690,
            "disk": 40,
        },
        {
            "time": "18:00",
            "cpu": 54,
            "memory": 66,
            "net_in": 810,
            "net_out": 560,
            "disk": 41,
        },
        {
            "time": "20:00",
            "cpu": 41,
            "memory": 58,
            "net_in": 620,
            "net_out": 430,
            "disk": 42,
        },
        {
            "time": "22:00",
            "cpu": 28,
            "memory": 50,
            "net_in": 340,
            "net_out": 220,
            "disk": 42,
        },
    ]

    recent_events: list[RecentEvent] = [
        {
            "time": "10 min ago",
            "level": "info",
            "icon": "circle-check",
            "message": "Snapshot 'daily-backup' created successfully",
        },
        {
            "time": "1 hr ago",
            "level": "warn",
            "icon": "triangle-alert",
            "message": "CPU usage exceeded 70% for 3 minutes",
        },
        {
            "time": "3 hr ago",
            "level": "info",
            "icon": "rotate-cw",
            "message": "Auto-renewal payment of ¥42.49 successful",
        },
        {
            "time": "8 hr ago",
            "level": "info",
            "icon": "shield",
            "message": "Firewall rule fw-05 (Block Telnet) applied",
        },
        {
            "time": "1 day ago",
            "level": "critical",
            "icon": "circle_alert",
            "message": "DDoS attack mitigated · 2.4 Gbps peak",
        },
        {
            "time": "2 days ago",
            "level": "info",
            "icon": "package",
            "message": "System package updates installed (32 packages)",
        },
    ]

    @rx.event
    def set_view(self, view: str):
        self.console_view = view

    @rx.event
    def open_manage(self, instance_id: str):
        self.selected_instance_id = instance_id
        self.console_view = "manage"
        self.manage_tab = "dashboard"

    @rx.event
    async def refresh_instances(self):
        yield ServersState.load_console

    @rx.event
    def back_to_list(self):
        self.console_view = "servers"

    @rx.event
    def set_manage_tab(self, tab: str):
        self.manage_tab = tab

    @rx.event
    def set_monitor_range(self, r: str):
        self.monitor_range = r

    @rx.event
    def set_filter_region(self, region: str):
        self.filter_region = region

    @rx.event
    def set_search_query(self, q: str):
        self.search_query = q

    @rx.event
    async def toggle_auto_renew(self, instance_id: str):
        from app.states.session_state import SessionState

        session = await self.get_state(SessionState)
        email = (session.auth_email or "").strip().lower()
        new_value = False
        target = None
        for i, inst in enumerate(self.instances):
            if inst["id"] == instance_id:
                new_value = not bool(inst["auto_renew"])
                self.instances[i]["auto_renew"] = new_value
                target = instance_id
                break
        if target and email:
            try:
                await user_store.update_instance(
                    email, target, {"auto_renew": new_value}
                )
            except Exception as e:
                logging.exception(f"Error persisting auto_renew: {e}")

    @rx.event
    async def load_console(self):
        from app.states.session_state import SessionState

        session = await self.get_state(SessionState)
        email = (session.auth_email or "").strip().lower()
        logged_in = session.is_logged_in_cookie == "true"

        self.is_loaded = True

        if not email or not logged_in:
            self.is_authenticated = False
            self.instances = []
            self.billing_records = []
            self.selected_instance_id = ""
            yield rx.toast(
                title="Login required / 请先登录",
                description="Please log in to access the console. / 请登录后访问控制台。",
                duration=3500,
                close_button=True,
            )
            yield rx.redirect("/login")
            return

        self.is_authenticated = True

        try:
            raw_instances = await user_store.get_user_instances(email)
        except Exception as e:
            logging.exception(f"Error loading user instances: {e}")
            raw_instances = []

        try:
            raw_orders = await user_store.get_user_orders(email)
        except Exception as e:
            logging.exception(f"Error loading user orders: {e}")
            raw_orders = []

        normalized: list[ServerInstance] = []
        for inst in raw_instances:
            created_val = inst.get("created") or inst.get("created_at") or "-"
            normalized.append(
                {
                    "id": str(inst.get("id", "")),
                    "name": str(inst.get("name", "")),
                    "status": str(inst.get("status", "running")),
                    "ip": str(inst.get("ip", "-")),
                    "region": str(inst.get("region", "-")),
                    "region_flag": str(inst.get("region_flag", "🌐")),
                    "node": str(inst.get("node", "-")),
                    "plan": str(inst.get("plan", "-")),
                    "cpu": str(inst.get("cpu", "-")),
                    "ram": str(inst.get("ram", "-")),
                    "disk": str(inst.get("disk", "-")),
                    "bandwidth": str(inst.get("bandwidth", "-")),
                    "traffic_used": str(inst.get("traffic_used", "0 MB")),
                    "traffic_total": str(inst.get("traffic_total", "-")),
                    "traffic_percent": int(inst.get("traffic_percent", 0) or 0),
                    "reset_price": str(inst.get("reset_price", "-")),
                    "price": str(inst.get("price", "-")),
                    "expires": str(inst.get("expires", "-")),
                    "auto_renew": bool(inst.get("auto_renew", True)),
                    "health": str(inst.get("health", "healthy")),
                    "os": str(inst.get("os", "-")),
                    "created": str(created_val),
                }
            )
        self.instances = normalized

        bills: list[BillingRecord] = []
        for order in raw_orders:
            created_at = str(order.get("created_at", ""))
            if "T" in created_at:
                date_part = created_at.split("T")[0]
            else:
                date_part = created_at[:10] if created_at else "-"
            plan_name = str(order.get("plan_name", "-"))
            currency = str(order.get("currency", "CNY"))
            symbol = "¥" if currency.upper() == "CNY" else "$"
            try:
                amount_val = float(order.get("amount", 0))
            except (TypeError, ValueError):
                amount_val = 0.0
            bills.append(
                {
                    "id": "#" + str(order.get("id", "")),
                    "date": date_part,
                    "item": f"{plan_name} · 开通",
                    "cycle": str(order.get("cycle", "-")),
                    "amount": f"{symbol}{amount_val:.2f}",
                    "status": str(order.get("status", "paid")),
                }
            )
        bills.reverse()
        self.billing_records = bills

        if self.instances:
            valid_ids = [i["id"] for i in self.instances]
            if self.selected_instance_id not in valid_ids:
                self.selected_instance_id = self.instances[0]["id"]
        else:
            self.selected_instance_id = ""
            if self.console_view == "manage":
                self.console_view = "servers"

    @rx.event
    def toggle_firewall_rule(self, rule_id: str):
        for i, r in enumerate(self.firewall_rules):
            if r["id"] == rule_id:
                self.firewall_rules[i]["enabled"] = not self.firewall_rules[i][
                    "enabled"
                ]
                break

    @rx.event
    def select_instance(self, instance_id: str):
        self.selected_instance_id = instance_id

    @rx.var
    def filtered_instances(self) -> list[ServerInstance]:
        result = self.instances
        if self.filter_region != "all":
            result = [i for i in result if i["node"] == self.filter_region]
        if self.search_query.strip():
            q = self.search_query.lower()
            result = [
                i
                for i in result
                if q in i["name"].lower()
                or q in i["ip"].lower()
                or q in i["region"].lower()
            ]
        return result

    @rx.var
    def region_options(self) -> list[str]:
        seen: list[str] = []
        for i in self.instances:
            if i["node"] not in seen:
                seen.append(i["node"])
        return seen

    @rx.var
    def selected_instance(self) -> ServerInstance:
        for i in self.instances:
            if i["id"] == self.selected_instance_id:
                return i
        if self.instances:
            return self.instances[0]
        return {
            "id": "",
            "name": "-",
            "status": "-",
            "ip": "-",
            "region": "-",
            "region_flag": "🌐",
            "node": "-",
            "plan": "-",
            "cpu": "-",
            "ram": "-",
            "disk": "-",
            "bandwidth": "-",
            "traffic_used": "-",
            "traffic_total": "-",
            "traffic_percent": 0,
            "reset_price": "-",
            "price": "-",
            "expires": "-",
            "auto_renew": False,
            "health": "-",
            "os": "-",
            "created": "-",
        }

    @rx.var
    def has_instances(self) -> bool:
        return len(self.instances) > 0
