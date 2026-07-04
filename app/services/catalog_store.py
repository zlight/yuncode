"""
Local plan catalog data service.

Provides regions/nodes/systems/cycles configuration and the plan catalog,
with server-side filtering, sorting, pagination and stock overrides.

Persistence:
- Static config (regions/nodes/systems/cycles/plans) is defined in-code so
  the app has zero-config first-run behavior.
- Stock overrides live in `app/_data/stock.json` (via user_store).
"""

from __future__ import annotations

import logging
from typing import TypedDict

from app.services import user_store


class RegionConfig(TypedDict):
    id: str
    flag: str
    name_en: str
    name_zh: str


class MachineTypeConfig(TypedDict):
    id: str
    icon: str
    label_en: str
    label_zh: str


class SystemConfig(TypedDict):
    id: str
    icon: str
    label: str


class CycleConfig(TypedDict):
    id: str
    label_en: str
    label_zh: str
    mult: str


class PlanRecord(TypedDict):
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


REGIONS: list[RegionConfig] = [
    {"id": "mo", "flag": "🇲🇴", "name_en": "Macao", "name_zh": "澳门"},
    {"id": "jp", "flag": "🇯🇵", "name_en": "Japan", "name_zh": "日本"},
    {"id": "it", "flag": "🇮🇹", "name_en": "Italy", "name_zh": "意大利"},
    {"id": "nl", "flag": "🇳🇱", "name_en": "Netherlands", "name_zh": "荷兰"},
    {"id": "kr", "flag": "🇰🇷", "name_en": "South Korea", "name_zh": "韩国"},
    {"id": "tw", "flag": "🇹🇼", "name_en": "Taiwan", "name_zh": "台湾"},
    {"id": "sg", "flag": "🇸🇬", "name_en": "Singapore", "name_zh": "新加坡"},
    {"id": "hk", "flag": "🇭🇰", "name_en": "HongKong", "name_zh": "香港"},
    {"id": "us", "flag": "🇺🇸", "name_en": "United States", "name_zh": "美国"},
    {"id": "uk", "flag": "🇬🇧", "name_en": "UK", "name_zh": "英国"},
    {"id": "de", "flag": "🇩🇪", "name_en": "Germany", "name_zh": "德国"},
    {"id": "vn", "flag": "🇻🇳", "name_en": "Vietnam", "name_zh": "越南"},
]


MACHINE_TYPES: list[MachineTypeConfig] = [
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


SYSTEMS: list[SystemConfig] = [
    {"id": "debian-11", "icon": "circle-dot", "label": "Debian 11"},
    {"id": "debian-12", "icon": "circle-dot", "label": "Debian 12"},
    {"id": "debian-13", "icon": "circle-dot", "label": "Debian 13"},
    {"id": "ubuntu-18", "icon": "circle", "label": "Ubuntu 18"},
    {"id": "ubuntu-20", "icon": "circle", "label": "Ubuntu 20"},
    {"id": "ubuntu-22", "icon": "circle", "label": "Ubuntu 22"},
    {"id": "rocky-8", "icon": "hexagon", "label": "RockyLinux 8"},
    {"id": "rocky-9", "icon": "hexagon", "label": "RockyLinux 9"},
]


CYCLES: list[CycleConfig] = [
    {"id": "1", "label_en": "1 Month", "label_zh": "1 个月", "mult": "1.0"},
    {"id": "3", "label_en": "3 Months", "label_zh": "3 个月", "mult": "2.85"},
    {"id": "6", "label_en": "6 Months", "label_zh": "6 个月", "mult": "5.5"},
    {
        "id": "12",
        "label_en": "12 Months",
        "label_zh": "12 个月",
        "mult": "10.0",
    },
]


BASE_PLANS: list[PlanRecord] = [
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
        "stock": 5,
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
        "stock": 12,
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
]


async def get_regions() -> list[RegionConfig]:
    return list(REGIONS)


async def get_machine_types() -> list[MachineTypeConfig]:
    return list(MACHINE_TYPES)


async def get_systems() -> list[SystemConfig]:
    return list(SYSTEMS)


async def get_cycles() -> list[CycleConfig]:
    return list(CYCLES)


async def get_available_nodes(region: str) -> list[str]:
    seen: list[str] = []
    for p in BASE_PLANS:
        if p["region"] == region and p["node"] not in seen:
            seen.append(p["node"])
    return seen


async def _apply_stock_overrides(plans: list[PlanRecord]) -> list[PlanRecord]:
    try:
        overrides = await user_store.get_stock_overrides()
    except Exception as e:
        logging.exception(f"Error fetching stock overrides: {e}")
        overrides = {}
    result: list[PlanRecord] = []
    for p in plans:
        item = dict(p)
        if item["id"] in overrides:
            item["stock"] = int(overrides[item["id"]])
        result.append(item)  # type: ignore
    return result


async def get_all_plans() -> list[PlanRecord]:
    """Return all base plans with stock overrides applied."""
    return await _apply_stock_overrides(list(BASE_PLANS))


async def get_plan(plan_id: str) -> PlanRecord | None:
    plans = await get_all_plans()
    for p in plans:
        if p["id"] == plan_id:
            return p
    return None


async def query_plans(
    region: str = "",
    node: str = "",
    search: str = "",
    price_min: float | None = None,
    price_max: float | None = None,
    sort_by: str = "recommended",
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[PlanRecord], int]:
    """Filter, sort and paginate the plan catalog. Returns (page, total)."""
    plans = await get_all_plans()

    if region:
        plans = [p for p in plans if p["region"] == region]
    if node:
        plans = [p for p in plans if p["node"] == node]
    if search:
        s = search.strip().lower()
        plans = [
            p
            for p in plans
            if s in p["name"].lower() or s in p["region_code"].lower()
        ]
    if price_min is not None:
        plans = [p for p in plans if p["price"] >= float(price_min)]
    if price_max is not None:
        plans = [p for p in plans if p["price"] <= float(price_max)]

    if sort_by == "price-asc":
        plans = sorted(plans, key=lambda p: p["price"])
    elif sort_by == "price-desc":
        plans = sorted(plans, key=lambda p: -p["price"])
    elif sort_by == "stock":
        plans = sorted(plans, key=lambda p: -p["stock"])

    total = len(plans)
    page = max(1, int(page))
    page_size = max(1, int(page_size))
    start = (page - 1) * page_size
    end = start + page_size
    return plans[start:end], total


async def decrement_stock(plan_id: str) -> tuple[bool, int]:
    """Atomically decrement stock. Returns (ok, new_stock)."""
    plan = await get_plan(plan_id)
    if plan is None:
        return False, 0
    if plan["stock"] <= 0:
        return False, 0
    try:
        new_val = await user_store.apply_stock_delta(plan_id, plan["stock"], -1)
        return True, new_val
    except Exception as e:
        logging.exception(f"Error decrementing stock: {e}")
        return False, plan["stock"]


__all__ = [
    "RegionConfig",
    "MachineTypeConfig",
    "SystemConfig",
    "CycleConfig",
    "PlanRecord",
    "REGIONS",
    "MACHINE_TYPES",
    "SYSTEMS",
    "CYCLES",
    "BASE_PLANS",
    "get_regions",
    "get_machine_types",
    "get_systems",
    "get_cycles",
    "get_available_nodes",
    "get_all_plans",
    "get_plan",
    "query_plans",
    "decrement_stock",
]
