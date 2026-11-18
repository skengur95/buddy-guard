"""buddy-guard 진입점.

    python main.py                         # 실제 하드웨어 (라즈베리파이)
    python main.py --sim <시나리오.yaml>    # 하드웨어 없이 시뮬레이션
"""
import argparse
import sys
import time

import yaml

from core import bus
from core.clock import to_kst_str
from core.events import Event


def load_config(path: str = "config.yaml") -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_sim(scenario_path: str) -> None:
    """시나리오 파일의 이벤트를 시간 순서대로 bus에 넣는다.
    지금은 출력만 한다. logic/state_machine.py가 완성되면 여기에 연결."""
    with open(scenario_path, encoding="utf-8") as f:
        sc = yaml.safe_load(f)
    print(f"[SIM] {sc.get('name', scenario_path)}")
    start = time.time()
    for e in sorted(sc["events"], key=lambda x: x["t"]):
        wait = start + e["t"] - time.time()
        if wait > 0:
            time.sleep(wait)
        bus.put(Event(e["source"], e["type"], e.get("data", {})))
        ev = bus.get()
        print(f"  t={e['t']:>4}s  {to_kst_str(ev.ts)}  {ev.source:<13} {ev.type:<11} {ev.data}")
    print("[SIM] 끝")


def run_hw(cfg: dict) -> None:
    print("[HW] 아직 모듈이 연결되지 않았어요. sensors/, vision/ 등이 완성되면 여기서 스레드를 시작합니다.")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sim", metavar="SCENARIO", help="시뮬레이션 시나리오 YAML 경로")
    p.add_argument("--config", default="config.yaml")
    args = p.parse_args()

    cfg = load_config(args.config)
    print(f"설정 로드 완료: 감시인 부재 {cfg['guard']['absent_seconds']}초, "
          f"교대 유예 {cfg['guard']['handover_grace_seconds']}초")

    if args.sim:
        run_sim(args.sim)
    else:
        run_hw(cfg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
