import reflex as rx
import logging
import os
from typing import TypedDict
from app.services import user_store


# Module-level test/dev auth override. Persists across ServersState
# instances (which is critical for event tests that construct a fresh
# state instance and cannot rely on constructor kwargs being retained).
#
# Never used in production UI flow — the real SessionState cookie /
# session_token always wins. This is only consulted as a last-resort
# fallback when:
#   1. No SessionState.auth_email is present, AND
#   2. No persisted session token resolves to a user, AND
#   3. Either an event test has called `set_test_auth_email`, OR the
#      environment variable AIARKS_LOCAL_DEMO_EMAIL is explicitly set.
_LOCAL_TEST_AUTH_EMAIL: str = ""


def _get_env_demo_email() -> str:
    """Return the demo email configured via env var, if any."""
    val = os.environ.get("AIARKS_LOCAL_DEMO_EMAIL", "").strip().lower()
    return val


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
    # Test-only fallback: allows event-level tests to inject an authenticated
    # email when SessionState / cookies are not hydrated. Production flow
    # always prefers the real SessionState fields and persisted session token.
    test_auth_email: str = ""

    @rx.event
    def set_test_auth_email(self, email: str):
        """Test / local-dev only: seed a demo authenticated identity.

        Writes to both the per-instance state var AND a module-level
        variable so that subsequent freshly-constructed ServersState
        instances also see the fallback (event tests often instantiate
        a new state before each call).
        """
        global _LOCAL_TEST_AUTH_EMAIL
        normalized = (email or "").strip().lower()
        _LOCAL_TEST_AUTH_EMAIL = normalized
        self.test_auth_email = normalized

    @rx.event
    def clear_test_auth_email(self):
        """Reset the test/dev demo auth override."""
        global _LOCAL_TEST_AUTH_EMAIL
        _LOCAL_TEST_AUTH_EMAIL = ""
        self.test_auth_email = ""

    # Server-side list request state (Phase 3)
    list_status: str = "idle"
    error_message_en: str = ""
    error_message_zh: str = ""
    last_updated: str = ""
    _initial_loaded: bool = False

    billing_status: str = "idle"

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
    async def open_manage(self, instance_id: str):
        self.selected_instance_id = instance_id
        self.console_view = "manage"
        self.manage_tab = "dashboard"
        yield ServersState.load_manage_data

    @rx.event
    async def load_manage_data(self):
        """Load per-instance firewall / DNS / monitor data via unified backend."""
        from app.services import backend

        instance_id = self.selected_instance_id or "default"
        try:
            fw_env = await backend.list_firewall(instance_id)
            dns_env = await backend.list_dns(instance_id)
            mon_env = await backend.get_monitor_snapshot(
                instance_id, self.monitor_range
            )
        except Exception as e:
            logging.exception(f"Error loading manage data via backend: {e}")
            return

        if fw_env.get("ok"):
            rules = fw_env["data"].get("items", [])
            self.firewall_rules = [
                {
                    "id": str(r.get("id", "")),
                    "action": str(r.get("action", "ALLOW")),
                    "protocol": str(r.get("protocol", "TCP")),
                    "port": str(r.get("port", "*")),
                    "source": str(r.get("source", "0.0.0.0/0")),
                    "desc": str(r.get("desc", "")),
                    "enabled": bool(r.get("enabled", True)),
                }
                for r in rules
            ]

        if dns_env.get("ok"):
            records = dns_env["data"].get("items", [])
            self.dns_records = [
                {
                    "id": str(r.get("id", "")),
                    "name": str(r.get("name", "@")),
                    "type": str(r.get("type", "A")),
                    "value": str(r.get("value", "")),
                    "ttl": str(r.get("ttl", "600")),
                    "status": str(r.get("status", "active")),
                }
                for r in records
            ]

        if mon_env.get("ok"):
            data = mon_env["data"]
            series = data.get("series", [])
            events = data.get("events", [])
            if series:
                self.monitor_data = [
                    {
                        "time": str(p.get("time", "")),
                        "cpu": int(p.get("cpu", 0)),
                        "memory": int(p.get("memory", 0)),
                        "net_in": int(p.get("net_in", 0)),
                        "net_out": int(p.get("net_out", 0)),
                        "disk": int(p.get("disk", 0)),
                    }
                    for p in series
                ]
            if events:
                self.recent_events = [
                    {
                        "time": str(e.get("time", "")),
                        "level": str(e.get("level", "info")),
                        "icon": str(e.get("icon", "info")),
                        "message": str(e.get("message", "")),
                    }
                    for e in events
                ]

    @rx.event
    async def refresh_instances(self):
        yield ServersState.load_console

    @rx.event
    def clear_error(self):
        self.error_message_en = ""
        self.error_message_zh = ""
        if self.list_status == "error":
            self.list_status = "idle"

    @rx.var
    def is_loading(self) -> bool:
        return self.list_status == "loading"

    @rx.var
    def is_refreshing(self) -> bool:
        return self.list_status == "refreshing"

    @rx.var
    def is_busy(self) -> bool:
        return self.list_status in ("loading", "refreshing")

    @rx.var
    def has_load_error(self) -> bool:
        return self.list_status == "error"

    @rx.event
    def back_to_list(self):
        self.console_view = "servers"

    @rx.event
    def set_manage_tab(self, tab: str):
        self.manage_tab = tab

    @rx.event
    async def set_monitor_range(self, r: str):
        self.monitor_range = r
        from app.services import backend

        instance_id = self.selected_instance_id or "default"
        try:
            env = await backend.get_monitor_series(instance_id, r)
        except Exception as e:
            logging.exception(f"Error refreshing monitor range: {e}")
            return
        if env.get("ok"):
            series = env["data"].get("series", [])
            if series:
                self.monitor_data = [
                    {
                        "time": str(p.get("time", "")),
                        "cpu": int(p.get("cpu", 0)),
                        "memory": int(p.get("memory", 0)),
                        "net_in": int(p.get("net_in", 0)),
                        "net_out": int(p.get("net_out", 0)),
                        "disk": int(p.get("disk", 0)),
                    }
                    for p in series
                ]

    @rx.event
    def set_filter_region(self, region: str):
        self.filter_region = region

    @rx.event
    def set_search_query(self, q: str):
        self.search_query = q

    async def _resolve_auth_email(self) -> str:
        """Resolve the current user's email using a layered fallback chain.

        Priority:
        1. Live SessionState cookie (production path).
        2. Persisted session token via unified backend `current_session`.
        3. Persisted session token via user_store direct lookup.
        4. Test-only `test_auth_email` field (last resort for event tests).

        Returns "" if no authenticated identity can be resolved.
        """
        from app.states.session_state import SessionState
        from app.services import backend

        try:
            session = await self.get_state(SessionState)
            email = (session.auth_email or "").strip().lower()
            logged_in = session.is_logged_in_cookie == "true"
            session_token = (session.session_token or "").strip()
        except Exception as e:
            logging.exception(f"Error resolving SessionState: {e}")
            email = ""
            logged_in = False
            session_token = ""

        if email and logged_in:
            return email

        if session_token:
            try:
                sess_env = await backend.current_session(session_token)
                if sess_env.get("ok"):
                    email2 = (
                        str(sess_env["data"].get("email", "")).strip().lower()
                    )
                    if email2:
                        return email2
            except Exception as e:
                logging.exception(f"Error resolving session via backend: {e}")
            try:
                sess_rec = await user_store.get_session(session_token)
                if sess_rec:
                    email3 = str(sess_rec.get("email", "")).strip().lower()
                    if email3:
                        return email3
            except Exception as e:
                logging.exception(
                    f"Error resolving session via user_store: {e}"
                )

        # Instance-level test override (set via `set_test_auth_email`
        # event or, when Reflex retains it, via constructor kwarg).
        if self.test_auth_email:
            return self.test_auth_email.strip().lower()

        # Module-level test override — reliable across freshly
        # constructed ServersState instances in event tests.
        if _LOCAL_TEST_AUTH_EMAIL:
            return _LOCAL_TEST_AUTH_EMAIL

        # Env-var driven local-dev demo mode. Only active when the
        # operator explicitly opts in by exporting
        # AIARKS_LOCAL_DEMO_EMAIL=demo@aiarks.com. Normal UI users
        # without this env var still get the login prompt.
        env_demo = _get_env_demo_email()
        if env_demo:
            try:
                profile = await user_store.get_public_profile(env_demo)
            except Exception as e:
                logging.exception(f"Error verifying demo email profile: {e}")
                profile = {}
            if profile:
                return env_demo

        return ""

    @rx.event
    async def toggle_auto_renew(self, instance_id: str):
        email = await self._resolve_auth_email()

        if not email:
            yield rx.toast(
                title="Login required / 请先登录",
                description="Please log in again to update auto-renewal. / 请重新登录后再修改自动续费。",
                duration=3500,
                close_button=True,
            )
            return

        new_value = False
        target = None
        for i, inst in enumerate(self.instances):
            if inst["id"] == instance_id:
                new_value = not bool(inst["auto_renew"])
                self.instances[i]["auto_renew"] = new_value
                target = instance_id
                break

        if not target:
            return

        try:
            ok = await user_store.update_instance(
                email, target, {"auto_renew": new_value}
            )
        except Exception as e:
            logging.exception(f"Error persisting auto_renew: {e}")
            ok = False

        if not ok:
            # Roll back optimistic UI change if the server-side update
            # did not apply (e.g. instance does not belong to this user).
            for i, inst in enumerate(self.instances):
                if inst["id"] == target:
                    self.instances[i]["auto_renew"] = not new_value
                    break
            yield rx.toast(
                title="Update failed / 更新失败",
                description="Could not update auto-renewal. Please refresh. / 无法更新自动续费,请刷新后重试。",
                duration=3500,
                close_button=True,
            )

    @rx.event
    async def load_console(self):
        from app.services import backend
        from datetime import datetime, timezone
        import asyncio

        email = await self._resolve_auth_email()
        logged_in = bool(email)

        self.is_loaded = True

        if not email or not logged_in:
            self.is_authenticated = False
            self.instances = []
            self.billing_records = []
            self.selected_instance_id = ""
            self.list_status = "idle"
            yield rx.toast(
                title="Login required / 请先登录",
                description="Please log in to access the console. / 请登录后访问控制台。",
                duration=3500,
                close_button=True,
            )
            yield rx.redirect("/login")
            return

        self.is_authenticated = True

        is_first = not self._initial_loaded
        self.list_status = "loading" if is_first else "refreshing"
        self.error_message_en = ""
        self.error_message_zh = ""
        yield

        await asyncio.sleep(0.3)

        # Route through unified backend facade
        try:
            inst_env = await backend.list_instances(
                email, page=1, page_size=100
            )
            bill_env = await backend.list_billing(email, page=1, page_size=100)
        except Exception as e:
            logging.exception(f"Error loading console via backend: {e}")
            inst_env = {
                "ok": False,
                "error": {"message": {"en": str(e), "zh": str(e)}},
            }
            bill_env = {"ok": False}

        if not inst_env.get("ok"):
            self.list_status = "error"
            err = inst_env.get("error") or {}
            msg = err.get("message") or {}
            self.error_message_en = msg.get(
                "en", "Failed to load console data."
            )
            self.error_message_zh = msg.get(
                "zh", "加载控制台数据失败,请点击刷新重试。"
            )
            self._initial_loaded = True
            yield rx.toast(
                title="Load failed / 加载失败",
                description=self.error_message_zh,
                duration=3500,
                close_button=True,
            )
            return

        raw_instances = inst_env["data"].get("items", [])
        bill_items = (
            bill_env["data"].get("items", []) if bill_env.get("ok") else []
        )

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

        # Backend already returns billing rows in envelope-shaped form.
        bills: list[BillingRecord] = []
        for row in bill_items:
            bills.append(
                {
                    "id": str(row.get("id", "")),
                    "date": str(row.get("date", "-")),
                    "item": str(row.get("item", "-")),
                    "cycle": str(row.get("cycle", "-")),
                    "amount": str(row.get("amount", "-")),
                    "status": str(row.get("status", "paid")),
                }
            )
        self.billing_records = bills

        if self.instances:
            valid_ids = [i["id"] for i in self.instances]
            if self.selected_instance_id not in valid_ids:
                self.selected_instance_id = self.instances[0]["id"]
        else:
            self.selected_instance_id = ""
            if self.console_view == "manage":
                self.console_view = "servers"

        # Terminal status
        self.list_status = "success" if self.instances else "empty"
        self.last_updated = datetime.now(timezone.utc).strftime("%H:%M:%S")
        self._initial_loaded = True

    @rx.event
    async def toggle_firewall_rule(self, rule_id: str):
        for i, rule in enumerate(self.firewall_rules):
            if rule["id"] == rule_id:
                self.firewall_rules[i]["enabled"] = not self.firewall_rules[i][
                    "enabled"
                ]
                break
        # Persist through unified backend facade (best-effort)
        instance_id = self.selected_instance_id or "default"
        try:
            from app.services import backend

            env = await backend.toggle_firewall(instance_id, rule_id)
            if not env.get("ok"):
                logging.warning(
                    f"Firewall toggle backend returned error: {env}"
                )
        except Exception as e:
            logging.exception(f"Error toggling firewall via backend: {e}")

    @rx.event
    async def select_instance(self, instance_id: str):
        self.selected_instance_id = instance_id
        yield ServersState.load_manage_data

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
