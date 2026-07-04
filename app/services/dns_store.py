"""DNS records service (local JSON, keyed by instance)."""

from __future__ import annotations

import asyncio
import json
import logging
import secrets
from pathlib import Path
from typing import TypedDict


class DnsRecord(TypedDict):
    id: str
    name: str
    type: str
    value: str
    ttl: str
    status: str


_LOCK = asyncio.Lock()
_DATA_DIR = Path(__file__).resolve().parent.parent / "_data"
_DNS_FILE = _DATA_DIR / "dns.json"


_SEED_RECORDS: list[DnsRecord] = [
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
]


def _read() -> dict:
    try:
        if not _DNS_FILE.exists():
            return {}
        with _DNS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.exception(f"Error reading dns store: {e}")
        return {}


def _write(data: dict) -> None:
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        tmp = _DNS_FILE.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        tmp.replace(_DNS_FILE)
    except Exception as e:
        logging.exception(f"Error writing dns store: {e}")


def _seed_key(store: dict, key: str) -> None:
    if key not in store:
        store[key] = list(_SEED_RECORDS)


async def list_records(instance_id: str = "default") -> list[DnsRecord]:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        _write(store)
        return list(store.get(instance_id, []))


async def add_record(instance_id: str, record: dict) -> DnsRecord:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        rec: DnsRecord = {
            "id": "dns-" + secrets.token_hex(3),
            "name": str(record.get("name", "@")),
            "type": str(record.get("type", "A")),
            "value": str(record.get("value", "")),
            "ttl": str(record.get("ttl", "600")),
            "status": str(record.get("status", "pending")),
        }
        store[instance_id].append(rec)
        _write(store)
        return rec


async def update_record(
    instance_id: str, record_id: str, updates: dict
) -> DnsRecord | None:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        records = store.get(instance_id, [])
        for i, r in enumerate(records):
            if r["id"] == record_id:
                merged = {**r, **{k: str(v) for k, v in updates.items()}}
                records[i] = merged
                store[instance_id] = records
                _write(store)
                return merged  # type: ignore
        return None


async def delete_record(instance_id: str, record_id: str) -> bool:
    async with _LOCK:
        store = _read()
        _seed_key(store, instance_id)
        records = store.get(instance_id, [])
        new_records = [r for r in records if r["id"] != record_id]
        if len(new_records) == len(records):
            return False
        store[instance_id] = new_records
        _write(store)
        return True


__all__ = [
    "DnsRecord",
    "list_records",
    "add_record",
    "update_record",
    "delete_record",
]
