"""모듈 간에 주고받는 이벤트 형식 (docs/interface.md v1).

모든 모듈은 이 Event 하나로만 메인 루프와 대화한다.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

# source 값 목록 — 새 source를 추가하면 docs/interface.md도 함께 고칠 것
SOURCES = {
    "vision.outer", "vision.inner",
    "sensor.gas", "sensor.env", "sensor.flame",
    "input.button", "input.rfid",
    "system",
}


@dataclass
class Event:
    source: str
    type: str
    data: dict[str, Any] = field(default_factory=dict)
    ts: float = field(default_factory=time.time)  # epoch 초, 기록할 때 KST로 변환

    def __post_init__(self) -> None:
        if self.source not in SOURCES:
            raise ValueError(f"알 수 없는 source: {self.source}")
