import reflex as rx
from typing import TypedDict


class ListStatus:
    """Standard status codes for any server-backed list."""

    IDLE = "idle"
    LOADING = "loading"
    REFRESHING = "refreshing"
    SUCCESS = "success"
    EMPTY = "empty"
    ERROR = "error"


class ListRequestMeta(TypedDict):
    status: str
    total: int
    page: int
    page_size: int
    error_code: str
    error_message_en: str
    error_message_zh: str
    last_updated: str


def make_default_meta(page_size: int = 20) -> ListRequestMeta:
    return {
        "status": ListStatus.IDLE,
        "total": 0,
        "page": 1,
        "page_size": page_size,
        "error_code": "",
        "error_message_en": "",
        "error_message_zh": "",
        "last_updated": "",
    }


class BaseListState(rx.State):
    """
    Shared list-request state fields and events.

    Subclass this in feature-specific states (server catalog, console
    instance list, billing list) so that every list-shaped surface has the
    same status vocabulary: loading / refreshing / empty / error / success,
    plus search, filter, sort and pagination.

    Concrete lists should override `_do_fetch` to hit their real backend
    (services / SQL / HTTP). This base class only wires state; it does not
    force a specific transport.
    """

    _list_status: str = ListStatus.IDLE
    _list_error_code: str = ""
    _list_error_en: str = ""
    _list_error_zh: str = ""
    _list_total: int = 0
    _list_page: int = 1
    _list_page_size: int = 20
    _list_last_updated: str = ""

    search_query: str = ""
    sort_by: str = "recommended"
    filter_key: str = "all"

    @rx.event
    def set_search_query(self, q: str):
        self.search_query = q
        self._list_page = 1

    @rx.event
    def set_sort_by(self, key: str):
        self.sort_by = key

    @rx.event
    def set_filter_key(self, key: str):
        self.filter_key = key
        self._list_page = 1

    @rx.event
    def set_page(self, page: int):
        try:
            self._list_page = max(1, int(page))
        except (TypeError, ValueError):
            self._list_page = 1

    @rx.event
    def next_page(self):
        if self._list_page * self._list_page_size < self._list_total:
            self._list_page += 1

    @rx.event
    def prev_page(self):
        if self._list_page > 1:
            self._list_page -= 1

    @rx.event
    def clear_error(self):
        self._list_error_code = ""
        self._list_error_en = ""
        self._list_error_zh = ""
        if self._list_status == ListStatus.ERROR:
            self._list_status = ListStatus.IDLE

    @rx.event
    def reset_list_filters(self):
        self.search_query = ""
        self.sort_by = "recommended"
        self.filter_key = "all"
        self._list_page = 1

    @rx.var
    def is_loading(self) -> bool:
        return self._list_status == ListStatus.LOADING

    @rx.var
    def is_refreshing(self) -> bool:
        return self._list_status == ListStatus.REFRESHING

    @rx.var
    def is_busy(self) -> bool:
        return self._list_status in (ListStatus.LOADING, ListStatus.REFRESHING)

    @rx.var
    def is_empty(self) -> bool:
        return self._list_status == ListStatus.EMPTY

    @rx.var
    def has_error(self) -> bool:
        return self._list_status == ListStatus.ERROR

    @rx.var
    def total_pages(self) -> int:
        if self._list_page_size <= 0:
            return 1
        return max(1, -(-self._list_total // self._list_page_size))
