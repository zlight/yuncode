"""Firewall rules service (local JSON, keyed by instance)."""

from __future__ import annotations

import asyncio
import json
import logging
import secrets
from pathlib import Path
from typing import TypedDict


class FirewallRule(TypedDict):
    id: str
    action: str
    protocol: str
    port: str
    source: str
    desc: str
    enabled: bool


_LOCK = asyncio.Lock()
_DATA_DIR = Path(__file__).resolve().parent.parent / "_data"
_FW_FILE = _DATA_DIR / "firewall.json"


_SEED_RULES: list[FirewallRule] = [
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
        "action": "DENY",
        "protocol": "TCP",
        "port": "23",
        "source": "0.0.0.0/0",
        "desc": "Block Telnet",
        "enabled": True,
    },
    {
        "id": "fw-05",
        "action": "ALLOW",
        "protocol": "ICMP",
        "port": "*",
        "source": "0.0.0.0/0",
        "desc": "Ping (ICMP)",
        "enabled": True,
    },
]


def _read() -> dict:
    try:
        if not _FW_FILE.exists():
            return {}
        with _FW_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.exception(f"Error reading firewall store: {e}")
        return {}


def _write(data: dict) -> None:
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        tmp = _FW_FILE.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        tmp.replace(_FW_FILE)
    except Exception as e:
        logging.exception(f"Error writing firewall store: {e}")


def _seed_key(store: dict, key: str) -> None:
    if key not in store:
        store[key] = list(_SEED_RULES)


async def list_rules(instance_id: str = "default") -> list[FirewallRule]:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        _write(store)
        return list(store.get(instance_id, []))


async def add_rule(instance_id: str, rule: dict) -> FirewallRule:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        r: FirewallRule = {
            "id": "fw-" + secrets.token_hex(3),
            "action": str(rule.get("action", "ALLOW")).upper(),
            "protocol": str(rule.get("protocol", "TCP")).upper(),
            "port": str(rule.get("port", "*")),
            "source": str(rule.get("source", "0.0.0.0/0")),
            "desc": str(rule.get("desc", "")),
            "enabled": bool(rule.get("enabled", True)),
        }
        store[instance_id].append(r)
        _write(store)
        return r


async def toggle_rule(instance_id: str, rule_id: str) -> FirewallRule | None:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        rules = store.get(instance_id, [])
        for i, r in enumerate(rules):
            if r["id"] == rule_id:
                r["enabled"] = not bool(r.get("enabled", True))
                rules[i] = r
                store[instance_id] = rules
                _write(store)
                return r
        return None


async def delete_rule(instance_id: str, rule_id: str) -> bool:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        rules = store.get(instance_id, [])
        new_rules = [r for r in rules if r["id"] != rule_id]
        if len(new_rules) == len(rules):
            return False
        store[instance_id] = new_rules
        _write(store)
        return True


__all__ = [
    "FirewallRule",
    "list_rules",
    "add_rule",
    "toggle_rule",
    "delete_rule",
]
