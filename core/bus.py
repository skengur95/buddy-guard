"""스레드 간 이벤트 통로. 모든 모듈은 bus.put(Event(...))로 보낸다."""
from __future__ import annotations

import queue

from core.events import Event

_q: "queue.Queue[Event]" = queue.Queue()


def put(ev: Event) -> None:
    _q.put(ev)


def get(timeout: float = 0.1) -> Event | None:
    try:
        return _q.get(timeout=timeout)
    except queue.Empty:
        return None
