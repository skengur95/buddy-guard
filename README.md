# buddy-guard

밀폐공간(탱크·맨홀) **2인 1조 작업 안전 모니터링** — Raspberry Pi 4 온디바이스 AI

- 바깥 감시인이 감시 구역을 벗어나면 → 안쪽 작업자에게 경보
- 감시인이든 작업자든 쓰러지면 → 교대 유예 중에도 예외 없이 경보 (누운 자세 2초 확인 후)
- 감시인 교대 사인 → 60초 유예, 작업자에게 알림
- 안쪽 가스·온도가 기준을 넘거나 불꽃이 감지되면 → 경보

> ⚠️ 교육용 시제품입니다. 인증된 가스 측정기를 대신할 수 없습니다.

---

## 1. 시작하기

### 처음 설치
```bash
git clone https://github.com/skengur95/buddy-guard.git
cd buddy-guard              # 기본 브랜치 dev로 받아져요
python -m venv .venv        # 라즈베리파이: python3 -m venv --system-site-packages .venv
source .venv/Scripts/activate   # Windows Git Bash (라즈베리파이: source .venv/bin/activate)
pip install -r requirements.txt
```

### 실행
```bash
python main.py                                          # 라즈베리파이 (실제 하드웨어)
python main.py --sim sim/scenarios/s3_handover_ok.yaml  # 노트북 (하드웨어 없이)
```

## 2. 폴더 구조

| 폴더 | 내용 | 담당 역할 |
|---|---|---|
| `core/` | 이벤트 형식, 큐, KST 시간 | 통합·문서 |
| `sensors/` | MQ-2, MQ-7(ADS1115), BME280, 불꽃 | HW |
| `io_devices/` | 부저, LED, 릴레이, 버튼, RFID | HW |
| `vision/common/` | 카메라, 디텍터(Person 형식), 쓰러짐 규칙 | SW/AI |
| `vision/outer/` | 감시 구역 인원·감시인 부재 판정 | SW/AI |
| `vision/inner/` | 작업자 검출, 밝기 보정 | SW/AI |
| `tests/` | 자동 테스트 (pytest) | 전원 |
| `data/` | 실행 기록·녹화 (**Git에 올리지 않음**) | — |
| `config.yaml` | 모든 기준값·핀 번호 (코드에 숫자 직접 쓰지 않기) | 전원 |
| `AGENTS.md` · `CLAUDE.md` · `.gemini/` | AI 코딩 도구 공통 규칙 (원본: AGENTS.md) | 통합·문서 |
| `.github/` | 이슈·PR 템플릿 | 통합·문서 |
| `logic/` | 상태 머신, 판정 규칙 | SW/AI |
| `alerts/` | 경보 등급 → 출력 패턴 | SW/AI |
| `storage/` | 이벤트 기록 (events.db) | SW/AI |
| `sim/` | 시뮬레이터 시나리오 | 통합·문서 |
| `tools/` | 단독 테스트·보정 스크립트 | 전원 |
| `docs/` | 모든 문서·회의록·예산·사진 | 통합·문서 |
| `models/` | AI 모델 파일 (**Git에 올리지 않음**) | SW/AI |

> 사람별 담당은 [AGENTS.md](AGENTS.md) "폴더 담당"이 기준

## 3. Git 규칙 (요약)

> 전체 규칙의 원본은 [AGENTS.md](AGENTS.md)예요. 바꿀 때는 그 파일만 고쳐요.

- 기본 브랜치는 **`dev`**. 모든 PR은 dev로 → **Squash and merge**
- `main`은 시연 가능한 버전만. 통합의 날에 dev → main **Create a merge commit**
- 브랜치: `<종류>/<이슈번호>-<담당쪽>-<기능>` 예) `feat/6-common-fall-rule`
- 커밋: `<종류>(<범위>): <한 줄 설명>` 예) `feat(vision): 감시 구역 다각형 판정 추가`
- dev·main 직접 push 금지, `--force` 금지, 최신 dev 반영은 `git merge dev`

## 4. 이슈와 PR

- **New issue**에서 템플릿을 골라요: ✨ 기능(Type: Feature) · 🧩 작업(Task) · 📝 회의·결정(Task) · 🐞 버그(Bug)
- **Type** = 무슨 일 / **Labels** = 누가(`sw` `hw` `doc` `pm`)·어디(`common` `outer` `inner`)
- 이슈를 먼저 만들고 → 이슈 화면 **Development → Create a branch**로 브랜치를 따요
- PR을 열면 체크리스트가 자동으로 채워져요. 본문에 `closes #이슈번호`

## 5. 역할

PM · HW · SW/AI · 통합·문서 — 업무 분담과 담당은 [docs/project-context.md](docs/project-context.md) 4장 참고

## 6. 문서

| 문서 | 내용 |
|---|---|
| [docs/project-context.md](docs/project-context.md) | 프로젝트 배경·결정 사항·이슈 목록·다음 작업 순서 |
| [docs/interface.md](docs/interface.md) | 모듈 간 Event 형식, 비전 공통 형식 |
| `docs/meetings/` | 회의록·회의 자료 |
| `docs/budget/` | 예산·구매 내역 |
