import asyncio
import hashlib
import json
import logging
import secrets
from pathlib import Path
from typing import TypedDict


class UserRecord(TypedDict):
    email: str
    username: str
    password_hash: str
    salt: str
    is_vip: bool
    balance: float
    ak_coins: int
    total_spending: float
    referral_earnings: float
    invitation_code: str
    referred_by: str
    created_at: str
    last_login_at: str


class SessionRecord(TypedDict):
    token: str
    email: str
    created_at: str


_LOCK = asyncio.Lock()
_DATA_DIR = Path(__file__).resolve().parent.parent / "_data"
_USERS_FILE = _DATA_DIR / "users.json"
_SESSIONS_FILE = _DATA_DIR / "sessions.json"
_ORDERS_FILE = _DATA_DIR / "orders.json"
_INSTANCES_FILE = _DATA_DIR / "instances.json"
_STOCK_FILE = _DATA_DIR / "stock.json"


def _hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()


def _now_iso() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _ensure_dir() -> None:
    try:
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logging.exception(f"Error creating data dir: {e}")


def _read_json(path: Path, default):
    try:
        if not path.exists():
            return default
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.exception(f"Error reading {path}: {e}")
        return default


def _write_json(path: Path, data) -> None:
    try:
        _ensure_dir()
        tmp = path.with_suffix(path.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        tmp.replace(path)
    except Exception as e:
        logging.exception(f"Error writing {path}: {e}")


def _seed_if_empty() -> None:
    _ensure_dir()
    if not _USERS_FILE.exists():
        salt_admin = secrets.token_hex(8)
        salt_demo = secrets.token_hex(8)
        salt_vip = secrets.token_hex(8)
        seed = {
            "admin@aiarks.com": {
                "email": "admin@aiarks.com",
                "username": "Admin",
                "password_hash": _hash_password("admin123", salt_admin),
                "salt": salt_admin,
                "is_vip": True,
                "balance": 888.88,
                "ak_coins": 5000,
                "total_spending": 3200.00,
                "referral_earnings": 240.00,
                "invitation_code": "AIARKS-ADMIN",
                "referred_by": "",
                "created_at": _now_iso(),
                "last_login_at": "",
            },
            "demo@aiarks.com": {
                "email": "demo@aiarks.com",
                "username": "Demo",
                "password_hash": _hash_password("demo1234", salt_demo),
                "salt": salt_demo,
                "is_vip": False,
                "balance": 128.50,
                "ak_coins": 2480,
                "total_spending": 1210.00,
                "referral_earnings": 86.40,
                "invitation_code": "AIARKS-DEMO",
                "referred_by": "",
                "created_at": _now_iso(),
                "last_login_at": "",
            },
            "vip@aiarks.com": {
                "email": "vip@aiarks.com",
                "username": "VipUser",
                "password_hash": _hash_password("vip12345", salt_vip),
                "salt": salt_vip,
                "is_vip": True,
                "balance": 512.00,
                "ak_coins": 8800,
                "total_spending": 5600.00,
                "referral_earnings": 420.00,
                "invitation_code": "AIARKS-VIP",
                "referred_by": "",
                "created_at": _now_iso(),
                "last_login_at": "",
            },
        }
        _write_json(_USERS_FILE, seed)
    if not _SESSIONS_FILE.exists():
        _write_json(_SESSIONS_FILE, {})


async def get_user_by_email(email: str) -> UserRecord | None:
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        return users.get(email.lower().strip())


async def username_exists(username: str) -> bool:
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        u = username.strip().lower()
        for rec in users.values():
            if rec.get("username", "").strip().lower() == u:
                return True
        return False


async def create_user(
    email: str,
    username: str,
    password: str,
    invitation_code: str = "",
) -> tuple[bool, str, UserRecord | None]:
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        key = email.lower().strip()
        if key in users:
            return False, "email_exists", None
        u_lower = username.strip().lower()
        for rec in users.values():
            if rec.get("username", "").strip().lower() == u_lower:
                return False, "username_exists", None
        salt = secrets.token_hex(8)
        new_code = "AIARKS-" + secrets.token_hex(3).upper()
        rec: UserRecord = {
            "email": key,
            "username": username.strip(),
            "password_hash": _hash_password(password, salt),
            "salt": salt,
            "is_vip": False,
            "balance": 10.00,
            "ak_coins": 100,
            "total_spending": 0.0,
            "referral_earnings": 0.0,
            "invitation_code": new_code,
            "referred_by": invitation_code.strip(),
            "created_at": _now_iso(),
            "last_login_at": "",
        }
        users[key] = rec
        _write_json(_USERS_FILE, users)
        return True, "ok", rec


async def verify_password(
    email: str, password: str
) -> tuple[bool, str, UserRecord | None]:
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        key = email.lower().strip()
        rec = users.get(key)
        if rec is None:
            return False, "not_found", None
        expected = _hash_password(password, rec.get("salt", ""))
        if expected != rec.get("password_hash"):
            return False, "wrong_password", None
        rec["last_login_at"] = _now_iso()
        users[key] = rec
        _write_json(_USERS_FILE, users)
        return True, "ok", rec


async def create_session(email: str) -> str:
    async with _LOCK:
        _seed_if_empty()
        sessions = _read_json(_SESSIONS_FILE, {})
        token = secrets.token_urlsafe(24)
        sessions[token] = {
            "token": token,
            "email": email.lower().strip(),
            "created_at": _now_iso(),
        }
        _write_json(_SESSIONS_FILE, sessions)
        return token


async def get_session(token: str) -> SessionRecord | None:
    if not token:
        return None
    async with _LOCK:
        _seed_if_empty()
        sessions = _read_json(_SESSIONS_FILE, {})
        return sessions.get(token)


async def destroy_session(token: str) -> None:
    if not token:
        return
    async with _LOCK:
        sessions = _read_json(_SESSIONS_FILE, {})
        if token in sessions:
            del sessions[token]
            _write_json(_SESSIONS_FILE, sessions)


async def upgrade_vip(email: str) -> None:
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        key = email.lower().strip()
        if key in users:
            users[key]["is_vip"] = True
            _write_json(_USERS_FILE, users)


async def get_public_profile(email: str) -> dict[str, str | float | int | bool]:
    rec = await get_user_by_email(email)
    if rec is None:
        return {}
    return {
        "email": rec.get("email", ""),
        "username": rec.get("username", ""),
        "is_vip": bool(rec.get("is_vip", False)),
        "balance": float(rec.get("balance", 0.0)),
        "ak_coins": int(rec.get("ak_coins", 0)),
        "total_spending": float(rec.get("total_spending", 0.0)),
        "referral_earnings": float(rec.get("referral_earnings", 0.0)),
        "invitation_code": rec.get("invitation_code", ""),
        "created_at": rec.get("created_at", ""),
    }


# ==================== Stock Management ====================
async def get_stock_overrides() -> dict[str, int]:
    async with _LOCK:
        _ensure_dir()
        return _read_json(_STOCK_FILE, {})


async def apply_stock_delta(
    plan_id: str, current_stock: int, delta: int
) -> int:
    """Apply delta to stock and persist. Returns new stock value."""
    async with _LOCK:
        _ensure_dir()
        overrides = _read_json(_STOCK_FILE, {})
        base = overrides.get(plan_id, current_stock)
        new_val = max(0, int(base) + int(delta))
        overrides[plan_id] = new_val
        _write_json(_STOCK_FILE, overrides)
        return new_val


# ==================== Orders & Instances ====================
async def create_order(
    email: str,
    order_data: dict,
) -> str:
    async with _LOCK:
        _ensure_dir()
        orders = _read_json(_ORDERS_FILE, {})
        key = email.lower().strip()
        user_orders = orders.get(key, [])
        order_id = "AC-" + secrets.token_hex(6).upper()
        record = {
            "id": order_id,
            "email": key,
            "created_at": _now_iso(),
            **order_data,
        }
        user_orders.append(record)
        orders[key] = user_orders
        _write_json(_ORDERS_FILE, orders)
        return order_id


async def get_user_orders(email: str) -> list[dict]:
    async with _LOCK:
        _ensure_dir()
        orders = _read_json(_ORDERS_FILE, {})
        return orders.get(email.lower().strip(), [])


async def create_instance(
    email: str,
    instance_data: dict,
) -> str:
    async with _LOCK:
        _ensure_dir()
        instances = _read_json(_INSTANCES_FILE, {})
        key = email.lower().strip()
        user_instances = instances.get(key, [])
        instance_id = instance_data.get("id") or (
            (instance_data.get("node", "srv").lower())
            + "s1-"
            + secrets.token_hex(8)
        )
        record = {
            "id": instance_id,
            "email": key,
            "created_at": _now_iso(),
            **instance_data,
        }
        user_instances.append(record)
        instances[key] = user_instances
        _write_json(_INSTANCES_FILE, instances)
        return instance_id


async def get_user_instances(email: str) -> list[dict]:
    async with _LOCK:
        _ensure_dir()
        instances = _read_json(_INSTANCES_FILE, {})
        return instances.get(email.lower().strip(), [])


async def update_instance(email: str, instance_id: str, updates: dict) -> bool:
    async with _LOCK:
        _ensure_dir()
        instances = _read_json(_INSTANCES_FILE, {})
        key = email.lower().strip()
        user_instances = instances.get(key, [])
        changed = False
        for i, inst in enumerate(user_instances):
            if inst.get("id") == instance_id:
                merged = {**inst, **updates}
                user_instances[i] = merged
                changed = True
                break
        if changed:
            instances[key] = user_instances
            _write_json(_INSTANCES_FILE, instances)
        return changed


async def deduct_balance_and_charge(
    email: str, amount: float
) -> tuple[bool, str, float]:
    """Deduct amount from balance, add to total_spending. Returns (ok, code, new_balance)."""
    async with _LOCK:
        _seed_if_empty()
        users = _read_json(_USERS_FILE, {})
        key = email.lower().strip()
        rec = users.get(key)
        if rec is None:
            return False, "not_found", 0.0
        current = float(rec.get("balance", 0.0))
        if current < amount:
            return False, "insufficient_balance", current
        rec["balance"] = round(current - amount, 2)
        rec["total_spending"] = round(
            float(rec.get("total_spending", 0.0)) + amount, 2
        )
        rec["is_vip"] = True
        users[key] = rec
        _write_json(_USERS_FILE, users)
        return True, "ok", float(rec["balance"])
