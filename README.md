# buddy-guard

밀폐공간(탱크·맨홀) **2인 1조 작업 안전 모니터링** — Raspberry Pi 4 온디바이스 AI

- 바깥 감시인이 감시 구역을 벗어나면 → 안쪽 작업자에게 경보
- 감시인이든 작업자든 쓰러지면 → 유예 없이 즉시 경보
- 감시인 교대 사인 → 60초 유예, 작업자에게 알림
- 안쪽 가스·온도가 기준을 넘거나 불꽃이 감지되면 → 경보

> ⚠️ 교육용 시제품입니다. 인증된 가스 측정기를 대신할 수 없습니다.

---

## 1. 실행 방법

```bash
# 라즈베리파이 (실제 하드웨어)
source .venv/bin/activate
python main.py

# 노트북 (하드웨어 없이 시뮬레이션)
python main.py --sim sim/scenarios/s3_handover_ok.yaml
```

## 2. 폴더 구조

| 폴더 | 내용 | 담당 역할 |
|---|---|---|
| `core/` | 이벤트 형식, 큐, KST 시간 | 통합·문서 |
| `sensors/` | MQ-2, MQ-7(ADS1115), BME280, 불꽃 | HW |
| `io_devices/` | 부저, LED, 릴레이, 버튼, RFID | HW |
| `vision/` | 카메라, 사람 검출, 감시 구역, 쓰러짐 | SW/AI |
| `common` | 공통 반환 형식 합의 / 카메라 모듈 | SW |
| `outer` | 감시자 쪽 카메라 기능 구현 | SW |
| `inner` | 내부 작업자 쪽 카메라 기능 구현 | SW |
| `logic/` | 상태 머신, 판정 규칙 | SW/AI |
| `alerts/` | 경보 등급 → 출력 패턴 | SW/AI |
| `storage/` | 이벤트 기록 (events.db) | SW/AI |
| `sim/` | 시뮬레이터 시나리오 | 통합·문서 |
| `tools/` | 단독 테스트·보정 스크립트 | 전원 |
| `docs/` | 모든 문서·회의록·예산·사진 | 통합·문서 |
| `models/` | AI 모델 파일 (**Git에 올리지 않음**) | SW/AI |

## 3. 브랜치 규칙

- `main` — 시연 가능한 버전만. `dev`에서 통합의 날에 합침
- `dev` — 통합 브랜치. **PR로만** 합침
- `feat/역할-기능` — 예: `feat/hw-gas-sensor`, `feat/sw-fall-rule`, `docs/interface-v2`

## 4. 커밋 메시지 규칙

```
<종류>(<범위>): <무엇을 했는지 한 줄>
```

| 종류 | 언제 |
|---|---|
| `feat` | 기능 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 |
| `test` | 테스트 |
| `chore` | 설정·환경·잡일 |
| `exp` | 실험(스파이크) |
| `refactor` | 동작 변화 없는 구조 정리 |

범위: `sensor`, `io`, `vision`, `logic`, `alerts`, `sim`, `config`, `docs` …

예) `feat(vision): 감시 구역 다각형 판정 추가`

## 5. PR 전 체크

- [ ] `docs/interface.md`의 Event 형식을 지켰다
- [ ] 숫자(기준값·핀 번호)를 코드에 직접 쓰지 않고 `config.yaml`에서 읽는다
- [ ] 핀을 바꿨다면 `docs/wiring.md`도 고쳤다
- [ ] 라즈베리파이 또는 `--sim`으로 실행해 봤다 (PR 본문에 결과 첨부)

## 6. 역할

PM · HW · SW/AI · 통합·문서 (업무 묶음은 프로젝트 매뉴얼 3장 참고)
