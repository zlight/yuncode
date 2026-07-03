import reflex as rx
from typing import TypedDict


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
    selected_instance_id: str = "hks1-20260701204720ff9b5c"
    filter_region: str = "all"
    search_query: str = ""
    manage_tab: str = "dashboard"
    monitor_range: str = "24h"

    instances: list[ServerInstance] = [
        {
            "id": "hks1-20260701204720ff9b5c",
            "name": "hks1-20260701204720ff9b5c",
            "status": "running",
            "ip": "103.28.201.42",
            "region": "中国香港",
            "region_flag": "🇭🇰",
            "node": "HKS",
            "plan": "HKS-Standard",
            "cpu": "1核",
            "ram": "1024M",
            "disk": "10GB",
            "bandwidth": "1200M",
            "traffic_used": "377.06MB",
            "traffic_total": "1500G/月",
            "traffic_percent": 3,
            "reset_price": "¥20.00",
            "price": "¥42.49/月",
            "expires": "2026-08-01 20:48:15",
            "auto_renew": True,
            "health": "healthy",
            "os": "Debian 12",
            "created": "2025-07-01 20:47:20",
        },
        {
            "id": "jps1-20250815103012aa2b1c",
            "name": "jps1-20250815103012aa2b1c",
            "status": "running",
            "ip": "45.32.108.221",
            "region": "日本东京",
            "region_flag": "🇯🇵",
            "node": "JPS",
            "plan": "JPS-Pro",
            "cpu": "2核",
            "ram": "4096M",
            "disk": "60GB",
            "bandwidth": "2000M",
            "traffic_used": "1.2GB",
            "traffic_total": "5000G/月",
            "traffic_percent": 12,
            "reset_price": "¥50.00",
            "price": "¥69.99/月",
            "expires": "2025-11-02 10:30:12",
            "auto_renew": False,
            "health": "healthy",
            "os": "Ubuntu 22.04",
            "created": "2025-08-15 10:30:12",
        },
        {
            "id": "uss1-20250620145533bc9e3f",
            "name": "uss1-20250620145533bc9e3f",
            "status": "running",
            "ip": "199.180.55.14",
            "region": "美国洛杉矶",
            "region_flag": "🇺🇸",
            "node": "USS",
            "plan": "USS-Business",
            "cpu": "4核",
            "ram": "8192M",
            "disk": "160GB",
            "bandwidth": "10000M",
            "traffic_used": "845MB",
            "traffic_total": "20000G/月",
            "traffic_percent": 1,
            "reset_price": "¥60.00",
            "price": "¥89.99/月",
            "expires": "2026-03-01 14:55:33",
            "auto_renew": True,
            "health": "healthy",
            "os": "Debian 11",
            "created": "2025-06-20 14:55:33",
        },
    ]

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

    billing_records: list[BillingRecord] = [
        {
            "id": "#AC-20250912",
            "date": "2025-09-12",
            "item": "HKS-Standard · 续费",
            "cycle": "1 个月",
            "amount": "¥42.49",
            "status": "paid",
        },
        {
            "id": "#AC-20250812",
            "date": "2025-08-12",
            "item": "HKS-Standard · 续费",
            "cycle": "1 个月",
            "amount": "¥42.49",
            "status": "paid",
        },
        {
            "id": "#AC-20250712",
            "date": "2025-07-12",
            "item": "HKS-Standard · 开通",
            "cycle": "1 个月",
            "amount": "¥42.49",
            "status": "paid",
        },
        {
            "id": "#AC-20250625",
            "date": "2025-06-25",
            "item": "流量包 · 500GB",
            "cycle": "一次性",
            "amount": "¥20.00",
            "status": "paid",
        },
        {
            "id": "#AC-20250601",
            "date": "2025-06-01",
            "item": "快照存储",
            "cycle": "1 个月",
            "amount": "¥5.00",
            "status": "paid",
        },
        {
            "id": "#AC-20250510",
            "date": "2025-05-10",
            "item": "带宽升级",
            "cycle": "一次性",
            "amount": "¥15.00",
            "status": "refunded",
        },
    ]

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
    def toggle_auto_renew(self, instance_id: str):
        for i, inst in enumerate(self.instances):
            if inst["id"] == instance_id:
                self.instances[i]["auto_renew"] = not self.instances[i][
                    "auto_renew"
                ]
                break

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
        return self.instances[0]
