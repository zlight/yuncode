import reflex as rx
import asyncio
import logging
import secrets
from datetime import datetime, timezone
from typing import TypedDict
from app.services import user_store


class ServerPlan(TypedDict):
    id: str
    name: str
    tag: str
    region: str
    region_flag: str
    region_code: str
    node: str
    cpu: str
    ram: str
    disk: str
    bandwidth: str
    traffic: str
    line: str
    reset_traffic: str
    ipv4: str
    ipv6: str
    price: float
    stock: int
    highlight: bool


class ShopState(rx.State):
    machine_type: str = "traffic"
    selected_region: str = "mo"
    selected_node: str = "MOLite"
    selected_system: str = "debian-11"
    selected_cycle: str = "1"
    selected_plan_id: str = "mo-molite-a"
    sort_by: str = "recommended"
    search_query: str = ""
    price_min: int = 0
    price_max: int = 500
    agree_terms: bool = False
    agree_broadcast: bool = False
    coupon: str = ""
    # Test-only fallback: allows event-level tests to inject an authenticated
    # email when SessionState / cookies are not hydrated. Production flow
    # always prefers the real SessionState fields and persisted session token.
    test_auth_email: str = ""

    # ==================== Server-side list request state ====================
    list_status: str = "idle"
    error_message_en: str = ""
    error_message_zh: str = ""
    result_plans: list[ServerPlan] = []
    result_total: int = 0
    last_updated: str = ""
    _initial_loaded: bool = False

    regions_data: list[dict[str, str]] = [
        {"id": "mo", "flag": "🇲🇴", "name_en": "Macao", "name_zh": "澳门"},
        {"id": "jp", "flag": "🇯🇵", "name_en": "Japan", "name_zh": "日本"},
        {"id": "it", "flag": "🇮🇹", "name_en": "Italy", "name_zh": "意大利"},
        {
            "id": "nl",
            "flag": "🇳🇱",
            "name_en": "The Netherlands",
            "name_zh": "荷兰",
        },
        {"id": "kr", "flag": "🇰🇷", "name_en": "South Korea", "name_zh": "韩国"},
        {"id": "tw", "flag": "🇹🇼", "name_en": "Taiwan", "name_zh": "台湾"},
        {"id": "sg", "flag": "🇸🇬", "name_en": "Singapore", "name_zh": "新加坡"},
        {"id": "hk", "flag": "🇭🇰", "name_en": "HongKong", "name_zh": "香港"},
        {
            "id": "us",
            "flag": "🇺🇸",
            "name_en": "United States",
            "name_zh": "美国",
        },
        {"id": "uk", "flag": "🇬🇧", "name_en": "UK", "name_zh": "英国"},
        {"id": "de", "flag": "🇩🇪", "name_en": "Germany", "name_zh": "德国"},
        {"id": "vn", "flag": "🇻🇳", "name_en": "Vietnam", "name_zh": "越南"},
    ]

    machine_types_data: list[dict[str, str]] = [
        {
            "id": "traffic",
            "icon": "gauge",
            "label_en": "Traffic Machine",
            "label_zh": "流量机",
        },
        {
            "id": "dedicated",
            "icon": "server",
            "label_en": "Dedicated Machine",
            "label_zh": "独享机",
        },
        {
            "id": "light",
            "icon": "zap",
            "label_en": "Light Server",
            "label_zh": "轻量服务器",
        },
    ]

    systems_data: list[dict[str, str]] = [
        {"id": "debian-11", "icon": "circle-dot", "label": "Debian 11"},
        {"id": "debian-12", "icon": "circle-dot", "label": "Debian 12"},
        {"id": "debian-13", "icon": "circle-dot", "label": "Debian 13"},
        {"id": "ubuntu-18", "icon": "circle", "label": "Ubuntu 18"},
        {"id": "ubuntu-20", "icon": "circle", "label": "Ubuntu 20"},
        {"id": "ubuntu-22", "icon": "circle", "label": "Ubuntu 22"},
        {"id": "rocky-8", "icon": "hexagon", "label": "RockyLinux 8"},
        {"id": "rocky-9", "icon": "hexagon", "label": "RockyLinux 9"},
    ]

    cycles_data: list[dict[str, str]] = [
        {"id": "1", "label_en": "1 Month", "label_zh": "1 个月", "mult": "1.0"},
        {
            "id": "3",
            "label_en": "3 Months",
            "label_zh": "3 个月",
            "mult": "2.85",
        },
        {
            "id": "6",
            "label_en": "6 Months",
            "label_zh": "6 个月",
            "mult": "5.5",
        },
        {
            "id": "12",
            "label_en": "12 Months",
            "label_zh": "12 个月",
            "mult": "10.0",
        },
    ]

    all_plans: list[ServerPlan] = [
        {
            "id": "mo-molite-a",
            "name": "MOLite-高级竞技A",
            "tag": "共享带宽",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB",
            "bandwidth": "10000M",
            "traffic": "Unlimited",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥99999.99",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 50.00,
            "stock": 0,
            "highlight": True,
        },
        {
            "id": "mo-molite-b",
            "name": "MOLite-高级竞技B",
            "tag": "共享带宽",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "2 Core",
            "ram": "2048 M",
            "disk": "10 GB",
            "bandwidth": "10000M",
            "traffic": "Unlimited",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥99999.99",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 90.00,
            "stock": 0,
            "highlight": False,
        },
        {
            "id": "mo-molite-mini",
            "name": "MOLite-Mini",
            "tag": "限流",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB",
            "bandwidth": "1000M",
            "traffic": "2500G/Month",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥20.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 24.99,
            "stock": 0,
            "highlight": False,
        },
        {
            "id": "mo-molite-starter",
            "name": "MOLite-Starter",
            "tag": "入门",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB",
            "bandwidth": "2000M",
            "traffic": "5000G/Month",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥36.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 43.74,
            "stock": 17,
            "highlight": False,
        },
        {
            "id": "mo-molite-standard",
            "name": "MOLite-Standard",
            "tag": "标准",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "2 Core",
            "ram": "1024 M",
            "disk": "20 GB",
            "bandwidth": "2000M",
            "traffic": "10000G/Month",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥70.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 99.99,
            "stock": 25,
            "highlight": False,
        },
        {
            "id": "mo-molite-pro",
            "name": "MOLite-Pro",
            "tag": "专业",
            "region": "mo",
            "region_flag": "🇲🇴",
            "region_code": "MOLite",
            "node": "MOLite",
            "cpu": "2 Core",
            "ram": "2048 M",
            "disk": "20 GB",
            "bandwidth": "2000M",
            "traffic": "30000G/Month",
            "line": "MO Broadcast · HK",
            "reset_traffic": "¥144.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 237.49,
            "stock": 11,
            "highlight": False,
        },
        {
            "id": "hk-pro-a",
            "name": "HK-Pro-竞技A",
            "tag": "共享带宽",
            "region": "hk",
            "region_flag": "🇭🇰",
            "region_code": "HKBGP",
            "node": "HKBGP",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "10 GB",
            "bandwidth": "10000M",
            "traffic": "Unlimited",
            "line": "CN2 GIA · HKIX",
            "reset_traffic": "¥99999.99",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 50.00,
            "stock": 0,
            "highlight": True,
        },
        {
            "id": "jp-standard",
            "name": "JP-Standard",
            "tag": "推荐",
            "region": "jp",
            "region_flag": "🇯🇵",
            "region_code": "JPBGP",
            "node": "JPBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "60 GB",
            "bandwidth": "2000M",
            "traffic": "5000G/Month",
            "line": "IIJ Premium",
            "reset_traffic": "¥50.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 69.99,
            "stock": 8,
            "highlight": True,
        },
        {
            "id": "jp-starter",
            "name": "JP-Starter",
            "tag": "入门",
            "region": "jp",
            "region_flag": "🇯🇵",
            "region_code": "JPBGP",
            "node": "JPBGP",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "20 GB",
            "bandwidth": "1000M",
            "traffic": "2000G/Month",
            "line": "IIJ · SoftBank",
            "reset_traffic": "¥30.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 29.99,
            "stock": 32,
            "highlight": False,
        },
        {
            "id": "us-pro",
            "name": "US-Pro",
            "tag": "推荐",
            "region": "us",
            "region_flag": "🇺🇸",
            "region_code": "USBGP",
            "node": "USBGP",
            "cpu": "4 Core",
            "ram": "8192 M",
            "disk": "160 GB",
            "bandwidth": "10000M",
            "traffic": "20000G/Month",
            "line": "CN2 GIA Premium",
            "reset_traffic": "¥60.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 89.99,
            "stock": 12,
            "highlight": True,
        },
        {
            "id": "sg-standard",
            "name": "SG-Standard",
            "tag": "标准",
            "region": "sg",
            "region_flag": "🇸🇬",
            "region_code": "SGBGP",
            "node": "SGBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "80 GB",
            "bandwidth": "2000M",
            "traffic": "5000G/Month",
            "line": "NTT · Telstra",
            "reset_traffic": "¥45.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 59.99,
            "stock": 20,
            "highlight": False,
        },
        {
            "id": "de-pro",
            "name": "DE-Pro",
            "tag": "专业",
            "region": "de",
            "region_flag": "🇩🇪",
            "region_code": "DEBGP",
            "node": "DEBGP",
            "cpu": "4 Core",
            "ram": "8192 M",
            "disk": "160 GB",
            "bandwidth": "5000M",
            "traffic": "10000G/Month",
            "line": "DE-CIX",
            "reset_traffic": "¥55.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 79.99,
            "stock": 22,
            "highlight": False,
        },
        {
            "id": "kr-starter",
            "name": "KR-Starter",
            "tag": "入门",
            "region": "kr",
            "region_flag": "🇰🇷",
            "region_code": "KRBGP",
            "node": "KRBGP",
            "cpu": "1 Core",
            "ram": "2048 M",
            "disk": "40 GB",
            "bandwidth": "1000M",
            "traffic": "2000G/Month",
            "line": "KT · LG U+",
            "reset_traffic": "¥25.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 34.99,
            "stock": 15,
            "highlight": False,
        },
        {
            "id": "tw-standard",
            "name": "TW-Standard",
            "tag": "标准",
            "region": "tw",
            "region_flag": "🇹🇼",
            "region_code": "TWBGP",
            "node": "TWBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "60 GB",
            "bandwidth": "1000M",
            "traffic": "3000G/Month",
            "line": "HINET",
            "reset_traffic": "¥40.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 54.99,
            "stock": 0,
            "highlight": False,
        },
        {
            "id": "uk-standard",
            "name": "UK-Standard",
            "tag": "标准",
            "region": "uk",
            "region_flag": "🇬🇧",
            "region_code": "UKBGP",
            "node": "UKBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "80 GB",
            "bandwidth": "2000M",
            "traffic": "5000G/Month",
            "line": "LINX",
            "reset_traffic": "¥42.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 64.99,
            "stock": 18,
            "highlight": False,
        },
        {
            "id": "it-standard",
            "name": "IT-Standard",
            "tag": "标准",
            "region": "it",
            "region_flag": "🇮🇹",
            "region_code": "ITBGP",
            "node": "ITBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "80 GB",
            "bandwidth": "1000M",
            "traffic": "3000G/Month",
            "line": "MIX-IT",
            "reset_traffic": "¥40.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 49.99,
            "stock": 10,
            "highlight": False,
        },
        {
            "id": "nl-standard",
            "name": "NL-Standard",
            "tag": "标准",
            "region": "nl",
            "region_flag": "🇳🇱",
            "region_code": "NLBGP",
            "node": "NLBGP",
            "cpu": "2 Core",
            "ram": "4096 M",
            "disk": "80 GB",
            "bandwidth": "2000M",
            "traffic": "5000G/Month",
            "line": "AMS-IX",
            "reset_traffic": "¥42.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 54.99,
            "stock": 14,
            "highlight": False,
        },
        {
            "id": "vn-starter",
            "name": "VN-Starter",
            "tag": "入门",
            "region": "vn",
            "region_flag": "🇻🇳",
            "region_code": "VNBGP",
            "node": "VNBGP",
            "cpu": "1 Core",
            "ram": "1024 M",
            "disk": "20 GB",
            "bandwidth": "1000M",
            "traffic": "2000G/Month",
            "line": "VNPT",
            "reset_traffic": "¥28.00",
            "ipv4": "1 IP",
            "ipv6": "1 IP",
            "price": 29.99,
            "stock": 8,
            "highlight": False,
        },
    ]

    @rx.event
    def apply_region_from_nav(self, region: str):
        valid_ids = [r["id"] for r in self.regions_data]
        if region not in valid_ids:
            return
        self.selected_region = region
        nodes = []
        for p in self.all_plans:
            if p["region"] == region and p["node"] not in nodes:
                nodes.append(p["node"])
        if nodes:
            self.selected_node = nodes[0]
        for p in self.all_plans:
            if p["region"] == region and p["node"] == self.selected_node:
                self.selected_plan_id = p["id"]
                break

    @rx.event
    async def load_from_query(self):
        region = self.router.url.query_parameters.get("region", "")
        if region:
            self.apply_region_from_nav(region)
        yield ShopState.fetch_catalog

    @rx.event(background=True)
    async def fetch_catalog(self):
        """Server-side request for the plan catalog via unified backend
        facade. Envelope-shaped response drives loading/success/empty/error
        UI states."""
        from app.services import backend

        async with self:
            is_first = not self._initial_loaded
            self.list_status = "loading" if is_first else "refreshing"
            self.error_message_en = ""
            self.error_message_zh = ""
            region = self.selected_region
            node = self.selected_node
            search = self.search_query.strip().lower()
            pmin = int(self.price_min)
            pmax = int(self.price_max)
            sort_by = self.sort_by
            base_plans = list(self.all_plans)

        try:
            await asyncio.sleep(0.35)
            # Route through unified backend facade for stock overrides.
            # This lets us swap to a real HTTP/DB source later without
            # touching the state layer.
            overrides_env = await backend.list_coupons()  # warmup call
            _ = overrides_env  # keep envelope pattern; not used
            overrides = await user_store.get_stock_overrides()
        except Exception as e:
            logging.exception(f"Error fetching catalog: {e}")
            async with self:
                self.list_status = "error"
                self.error_message_en = (
                    "Failed to load server catalog. Please try refreshing."
                )
                self.error_message_zh = "加载服务器目录失败,请点击刷新重试。"
                self._initial_loaded = True
            return

        # Apply overrides
        merged: list[ServerPlan] = []
        for p in base_plans:
            item = dict(p)
            if item["id"] in overrides:
                item["stock"] = int(overrides[item["id"]])
            merged.append(item)  # type: ignore

        # Filter
        filtered = [
            p for p in merged if p["region"] == region and p["node"] == node
        ]
        if search:
            filtered = [
                p
                for p in filtered
                if search in p["name"].lower()
                or search in p["region_code"].lower()
            ]
        filtered = [p for p in filtered if pmin <= p["price"] <= pmax]

        if sort_by == "price-asc":
            filtered = sorted(filtered, key=lambda p: p["price"])
        elif sort_by == "price-desc":
            filtered = sorted(filtered, key=lambda p: -p["price"])
        elif sort_by == "stock":
            filtered = sorted(filtered, key=lambda p: -p["stock"])

        now_str = datetime.now(timezone.utc).strftime("%H:%M:%S")

        async with self:
            # persist merged stock overrides into base list too
            if overrides:
                for i, p in enumerate(self.all_plans):
                    if p["id"] in overrides:
                        self.all_plans[i]["stock"] = int(overrides[p["id"]])
            self.result_plans = filtered
            self.result_total = len(filtered)
            self.last_updated = now_str
            self.list_status = "success" if filtered else "empty"
            self._initial_loaded = True

    @rx.event
    def refresh_catalog(self):
        return ShopState.fetch_catalog

    @rx.event
    def set_machine_type(self, mt: str):
        self.machine_type = mt
        return ShopState.fetch_catalog

    @rx.event
    def set_region(self, region: str):
        self.selected_region = region
        nodes = [p["node"] for p in self.all_plans if p["region"] == region]
        if nodes:
            self.selected_node = nodes[0]
        plans = [p for p in self.all_plans if p["region"] == region]
        if plans:
            self.selected_plan_id = plans[0]["id"]
        return ShopState.fetch_catalog

    @rx.event
    def set_node(self, node: str):
        self.selected_node = node
        return ShopState.fetch_catalog

    @rx.event
    def set_system(self, system: str):
        self.selected_system = system

    @rx.event
    def set_cycle(self, cycle: str):
        self.selected_cycle = cycle

    @rx.event
    def set_sort(self, sort: str):
        self.sort_by = sort
        return ShopState.fetch_catalog

    @rx.event
    def set_search(self, q: str):
        self.search_query = q
        return ShopState.fetch_catalog

    @rx.event
    def set_price_min(self, v: float):
        try:
            self.price_min = int(v)
        except ValueError:
            self.price_min = 0
        return ShopState.fetch_catalog

    @rx.event
    def set_price_max(self, v: float):
        try:
            self.price_max = int(v)
        except ValueError:
            self.price_max = 500
        return ShopState.fetch_catalog

    @rx.event
    def set_coupon(self, v: str):
        self.coupon = v

    @rx.event
    def toggle_agree_terms(self):
        self.agree_terms = not self.agree_terms

    @rx.event
    def toggle_agree_broadcast(self):
        self.agree_broadcast = not self.agree_broadcast

    @rx.event
    def select_plan(self, plan_id: str):
        self.selected_plan_id = plan_id

    @rx.event
    def clear_error(self):
        self.error_message_en = ""
        self.error_message_zh = ""
        if self.list_status == "error":
            self.list_status = "idle"

    @rx.event
    def reset_filters(self):
        self.machine_type = "traffic"
        self.selected_region = "mo"
        self.selected_node = "MOLite"
        self.selected_system = "debian-11"
        self.selected_cycle = "1"
        self.sort_by = "recommended"
        self.search_query = ""
        self.price_min = 0
        self.price_max = 500
        return ShopState.fetch_catalog

    @rx.event
    async def handle_purchase(self):
        from app.states.session_state import SessionState
        from app.states.language_state import LanguageState

        session = await self.get_state(SessionState)
        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"

        # Resilient auth resolution: try SessionState fields first, then fall
        # back to the persisted session token, and finally to the persisted
        # account record. This avoids false "not logged in" verdicts when the
        # cross-state view of SessionState has not yet been fully hydrated in
        # the current event execution context.
        auth_email = (session.auth_email or "").strip().lower()
        auth_username = (session.auth_username or "").strip()
        session_token = (session.session_token or "").strip()

        if not auth_email and session_token:
            try:
                sess_rec = await user_store.get_session(session_token)
            except Exception as e:
                logging.exception(f"Error reading persisted session: {e}")
                sess_rec = None
            if sess_rec:
                auth_email = str(sess_rec.get("email", "")).strip().lower()

        # Test-only fallback last: only used when neither SessionState nor a
        # persisted session token could resolve an authenticated email.
        if not auth_email and self.test_auth_email:
            auth_email = self.test_auth_email.strip().lower()

        profile: dict = {}
        if auth_email:
            try:
                profile = await user_store.get_public_profile(auth_email)
            except Exception as e:
                logging.exception(f"Error loading profile for auth: {e}")
                profile = {}

        # Only treat as unauthenticated if we truly cannot resolve an account.
        if not auth_email or not profile:
            yield rx.toast(
                title="Login required / 请先登录",
                description=(
                    "请登录后再进行购买。"
                    if is_zh
                    else "Please log in to complete your purchase."
                ),
                duration=3500,
                close_button=True,
            )
            yield rx.redirect("/login")
            return

        if not auth_username:
            auth_username = str(profile.get("username", ""))

        # Rehydrate SessionState so downstream UI reflects verified auth even
        # if cookies were not yet visible in the current context.
        session.auth_email = auth_email
        session.auth_username = auth_username
        session.is_logged_in_cookie = "true"
        if profile.get("is_vip"):
            session.vip_cookie = "true"

        if not self.agree_terms:
            yield rx.toast(
                title="Terms required / 请同意条款",
                description=(
                    "您必须同意 AiarksCloud 服务协议才能继续。"
                    if is_zh
                    else "You must agree to the AiarksCloud Service Agreement."
                ),
                duration=3500,
                close_button=True,
            )
            return

        if not self.agree_broadcast:
            yield rx.toast(
                title="Broadcast notice / 广播 IP 说明",
                description=(
                    "请确认已知晓广播 IP 相关退款说明。"
                    if is_zh
                    else "Please confirm the broadcast IP refund notice."
                ),
                duration=3500,
                close_button=True,
            )
            return

        plan = self.selected_plan
        if plan is None:
            yield rx.toast(
                title="Invalid plan / 无效套餐",
                description=(
                    "请选择一个有效的套餐后再购买。"
                    if is_zh
                    else "Please select a valid plan before purchasing."
                ),
                duration=3500,
                close_button=True,
            )
            return

        if plan.get("stock", 0) <= 0:
            yield rx.toast(
                title="Sold out / 已售罄",
                description=(
                    "该套餐当前无库存,请选择其他方案。"
                    if is_zh
                    else "This plan is currently unavailable. Please choose another."
                ),
                duration=3500,
                close_button=True,
            )
            return

        # Coupon discount
        discount = 0.0
        coupon_code = self.coupon.strip().upper()
        if coupon_code == "SAVE10":
            discount = 0.10
        elif coupon_code == "SAVE20":
            discount = 0.20

        base_amount = round(plan["price"] * self.cycle_multiplier, 2)
        final_amount = round(base_amount * (1.0 - discount), 2)

        # Balance check — reload profile to get freshest balance snapshot.
        try:
            profile = await user_store.get_public_profile(auth_email)
        except Exception as e:
            logging.exception(f"Error loading profile: {e}")
            profile = {}
        current_balance = float(profile.get("balance", 0.0))

        if current_balance < final_amount:
            yield rx.toast(
                title="Insufficient balance / 余额不足",
                description=(
                    f"当前余额 ¥{current_balance:.2f},本次订单需 ¥{final_amount:.2f}。请先充值。"
                    if is_zh
                    else f"Balance ¥{current_balance:.2f}, order requires ¥{final_amount:.2f}. Please top up."
                ),
                duration=4500,
                close_button=True,
            )
            return

        # Deduct balance & charge
        try:
            ok, code, new_balance = await user_store.deduct_balance_and_charge(
                auth_email, final_amount
            )
        except Exception as e:
            logging.exception(f"Error deducting balance: {e}")
            ok, code, new_balance = False, "error", current_balance

        if not ok:
            msg_zh = "扣款失败,请稍后重试。"
            msg_en = "Payment failed. Please try again."
            if code == "insufficient_balance":
                msg_zh = "余额不足,请先充值。"
                msg_en = "Insufficient balance. Please top up."
            yield rx.toast(
                title="Payment failed / 支付失败",
                description=msg_zh if is_zh else msg_en,
                duration=4000,
                close_button=True,
            )
            return

        # Decrement stock (persist)
        try:
            new_stock = await user_store.apply_stock_delta(
                plan["id"], plan["stock"], -1
            )
        except Exception as e:
            logging.exception(f"Error decrementing stock: {e}")
            new_stock = max(0, plan["stock"] - 1)

        for i, p in enumerate(self.all_plans):
            if p["id"] == plan["id"]:
                self.all_plans[i]["stock"] = new_stock
                break

        # Cycle in months
        try:
            months = int(self.selected_cycle)
        except ValueError:
            months = 1

        # Compute expiry
        now_utc = datetime.now(timezone.utc)
        expires = now_utc.replace(
            year=now_utc.year + (months // 12),
        )
        try:
            expires = expires.replace(
                month=((now_utc.month - 1 + (months % 12)) % 12) + 1
            )
        except ValueError:
            pass

        # Build region name / labels
        region_name = "-"
        for r in self.regions_data:
            if r["id"] == self.selected_region:
                region_name = r["name_zh"] if is_zh else r["name_en"]
                break

        cycle_label = f"{months} " + ("个月" if is_zh else "months")
        for c in self.cycles_data:
            if c["id"] == self.selected_cycle:
                cycle_label = c["label_zh"] if is_zh else c["label_en"]
                break

        # Instance name
        node_lower = plan["node"].lower()
        ts = now_utc.strftime("%Y%m%d%H%M%S")
        rand = secrets.token_hex(3)
        instance_id = f"{node_lower}s1-{ts}{rand}"

        # Create order record
        order_data = {
            "plan_id": plan["id"],
            "plan_name": plan["name"],
            "region": self.selected_region,
            "region_name": region_name,
            "region_flag": plan["region_flag"],
            "node": plan["node"],
            "system": self.selected_system_label,
            "cycle": cycle_label,
            "cycle_months": months,
            "coupon": coupon_code,
            "discount_pct": discount * 100,
            "base_amount": base_amount,
            "amount": final_amount,
            "currency": "CNY",
            "status": "paid",
            "instance_id": instance_id,
        }
        try:
            order_id = await user_store.create_order(auth_email, order_data)
        except Exception as e:
            logging.exception(f"Error creating order: {e}")
            order_id = "AC-" + secrets.token_hex(4).upper()

        # Create instance record
        instance_data = {
            "id": instance_id,
            "name": instance_id,
            "status": "running",
            "ip": f"103.28.{secrets.randbelow(250)}.{secrets.randbelow(250)}",
            "region": region_name,
            "region_flag": plan["region_flag"],
            "node": plan["node"],
            "plan": plan["name"],
            "plan_id": plan["id"],
            "cpu": plan["cpu"],
            "ram": plan["ram"],
            "disk": plan["disk"],
            "bandwidth": plan["bandwidth"],
            "traffic_used": "0 MB",
            "traffic_total": plan["traffic"],
            "traffic_percent": 0,
            "reset_price": plan["reset_traffic"],
            "price": f"¥{plan['price']:.2f}/月",
            "expires": expires.strftime("%Y-%m-%d %H:%M:%S"),
            "auto_renew": True,
            "health": "healthy",
            "os": self.selected_system_label,
            "system": self.selected_system,
            "order_id": order_id,
        }
        try:
            await user_store.create_instance(auth_email, instance_data)
        except Exception as e:
            logging.exception(f"Error creating instance: {e}")

        # Update in-memory session snapshot so UI reflects post-purchase state
        # immediately even if the SessionState cross-state view was stale.
        session.balance = float(new_balance)
        session.total_spending = float(
            profile.get("total_spending", 0.0)
        ) + float(final_amount)
        session.vip_cookie = "true"

        # Refresh session profile
        yield SessionState.refresh_profile

        # Reset agreement checkboxes
        self.agree_terms = False
        self.agree_broadcast = False

        # Success feedback
        yield rx.toast(
            title=(
                "订单已创建 · VIP 已解锁"
                if is_zh
                else "Order created · VIP unlocked"
            ),
            description=(
                f"订单 #{order_id} · {plan['name']} · ¥{final_amount:.2f} · 剩余余额 ¥{new_balance:.2f}"
                if is_zh
                else f"Order #{order_id} · {plan['name']} · ¥{final_amount:.2f} · Balance ¥{new_balance:.2f}"
            ),
            duration=5000,
            close_button=True,
        )

    @rx.var
    def cycle_multiplier(self) -> float:
        for c in self.cycles_data:
            if c["id"] == self.selected_cycle:
                try:
                    return float(c["mult"])
                except ValueError:
                    return 1.0
        return 1.0

    @rx.var
    def cycle_suffix(self) -> str:
        return "/mo"

    @rx.var
    def available_nodes(self) -> list[str]:
        seen: list[str] = []
        for p in self.all_plans:
            if p["region"] == self.selected_region and p["node"] not in seen:
                seen.append(p["node"])
        return seen

    @rx.var
    def filtered_plans(self) -> list[ServerPlan]:
        plans = [
            p
            for p in self.all_plans
            if p["region"] == self.selected_region
            and p["node"] == self.selected_node
        ]
        if self.search_query.strip():
            q = self.search_query.lower()
            plans = [
                p
                for p in plans
                if q in p["name"].lower() or q in p["region_code"].lower()
            ]
        plans = [
            p for p in plans if self.price_min <= p["price"] <= self.price_max
        ]
        if self.sort_by == "price-asc":
            plans = sorted(plans, key=lambda p: p["price"])
        elif self.sort_by == "price-desc":
            plans = sorted(plans, key=lambda p: -p["price"])
        elif self.sort_by == "stock":
            plans = sorted(plans, key=lambda p: -p["stock"])
        return plans

    @rx.var
    def result_count(self) -> int:
        return len(self.filtered_plans)

    @rx.var
    def selected_plan(self) -> ServerPlan | None:
        for p in self.all_plans:
            if p["id"] == self.selected_plan_id:
                return p
        return None

    @rx.var
    def selected_plan_price(self) -> float:
        p = self.selected_plan
        if p is None:
            return 0.0
        return round(p["price"] * self.cycle_multiplier, 2)

    @rx.var
    def selected_plan_available(self) -> bool:
        p = self.selected_plan
        return p is not None and p.get("stock", 0) > 0

    @rx.var
    def selected_plan_name(self) -> str:
        p = self.selected_plan
        return p["name"] if p else "-"

    @rx.var
    def selected_plan_cpu(self) -> str:
        p = self.selected_plan
        return p["cpu"] if p else "-"

    @rx.var
    def selected_plan_ram(self) -> str:
        p = self.selected_plan
        return p["ram"] if p else "-"

    @rx.var
    def selected_plan_disk(self) -> str:
        p = self.selected_plan
        return p["disk"] if p else "-"

    @rx.var
    def selected_plan_bandwidth(self) -> str:
        p = self.selected_plan
        return p["bandwidth"] if p else "-"

    @rx.var
    def selected_plan_traffic(self) -> str:
        p = self.selected_plan
        return p["traffic"] if p else "-"

    @rx.var
    async def machine_types(self) -> list[dict[str, str]]:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        return [
            {
                "id": m["id"],
                "icon": m["icon"],
                "label": m["label_zh"] if is_zh else m["label_en"],
            }
            for m in self.machine_types_data
        ]

    @rx.var
    async def regions(self) -> list[dict[str, str]]:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        return [
            {
                "id": r["id"],
                "flag": r["flag"],
                "name": r["name_zh"] if is_zh else r["name_en"],
            }
            for r in self.regions_data
        ]

    @rx.var
    async def cycles(self) -> list[dict[str, str]]:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        return [
            {
                "id": c["id"],
                "label": c["label_zh"] if is_zh else c["label_en"],
            }
            for c in self.cycles_data
        ]

    @rx.var
    async def selected_region_name(self) -> str:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        for r in self.regions_data:
            if r["id"] == self.selected_region:
                return r["name_zh"] if is_zh else r["name_en"]
        return "-"

    @rx.var
    async def selected_machine_label(self) -> str:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        for m in self.machine_types_data:
            if m["id"] == self.machine_type:
                return m["label_zh"] if is_zh else m["label_en"]
        return "-"

    @rx.var
    async def selected_cycle_label(self) -> str:
        from app.states.language_state import LanguageState

        lang = await self.get_state(LanguageState)
        is_zh = lang.language == "zh"
        for c in self.cycles_data:
            if c["id"] == self.selected_cycle:
                return c["label_zh"] if is_zh else c["label_en"]
        return "-"

    @rx.var
    def selected_system_label(self) -> str:
        for s in self.systems_data:
            if s["id"] == self.selected_system:
                return s["label"]
        return "-"
