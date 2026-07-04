"""Monitoring metrics and event log service (local, deterministic)."""

from __future__ import annotations

import random
from typing import TypedDict


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


_BASE_24H: list[MonitorPoint] = [
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


_BASE_EVENTS: list[RecentEvent] = [
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


async def get_series(
    instance_id: str = "", range_key: str = "24h"
) -> list[MonitorPoint]:
    """Return synthetic monitoring series for a given instance and range."""
    seed_str = f"{instance_id}-{range_key}"
    rng = random.Random(sum(ord(c) for c in seed_str) or 42)

    if range_key == "1h":
        base = _BASE_24H[-6:]
    elif range_key == "6h":
        base = _BASE_24H[-6:]
    elif range_key == "7d":
        base = _BASE_24H
    elif range_key == "30d":
        base = _BASE_24H
    else:
        base = _BASE_24H

    result: list[MonitorPoint] = []
    for p in base:
        jitter = rng.randint(-4, 4)
        result.append(
            {
                "time": p["time"],
                "cpu": max(0, min(100, p["cpu"] + jitter)),
                "memory": max(0, min(100, p["memory"] + jitter)),
                "net_in": max(0, p["net_in"] + jitter * 8),
                "net_out": max(0, p["net_out"] + jitter * 8),
                "disk": max(0, min(100, p["disk"] + (jitter // 2))),
            }
        )
    return result


async def get_peaks(instance_id: str = "", range_key: str = "24h") -> dict:
    series = await get_series(instance_id, range_key)
    if not series:
        return {}

    def _peak(key: str) -> tuple[int, str]:
        best = series[0]
        for p in series:
            if p[key] > best[key]:
                best = p
        return int(best[key]), str(best["time"])

    cpu_v, cpu_t = _peak("cpu")
    mem_v, mem_t = _peak("memory")
    net_v, net_t = _peak("net_in")
    disk_v, disk_t = _peak("disk")
    return {
        "cpu": {"value": cpu_v, "at": cpu_t},
        "memory": {"value": mem_v, "at": mem_t},
        "network": {"value": net_v, "unit": "KB/s", "at": net_t},
        "disk": {"value": disk_v, "at": disk_t},
    }


async def get_events(
    instance_id: str = "", limit: int = 20
) -> list[RecentEvent]:
    return _BASE_EVENTS[: max(1, int(limit))]


async def get_snapshot(instance_id: str = "", range_key: str = "24h") -> dict:
    return {
        "range": range_key,
        "series": await get_series(instance_id, range_key),
        "peaks": await get_peaks(instance_id, range_key),
        "events": await get_events(instance_id),
    }


__all__ = [
    "MonitorPoint",
    "RecentEvent",
    "get_series",
    "get_peaks",
    "get_events",
    "get_snapshot",
]
