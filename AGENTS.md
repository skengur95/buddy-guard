# buddy-guard — AI 코딩 도구 공통 작업 규칙 (AGENTS.md)

> 이 파일이 규칙의 **원본(single source of truth)** 이다. Claude Code · Codex · Gemini 등 어떤 AI 코딩 도구를 쓰든 이 파일을 따른다.
> 규칙을 바꿀 때는 이 파일만 고친다. (CLAUDE.md, .gemini/settings.json은 이 파일을 가리키기만 한다)
>
> **작업을 시작하기 전에 `docs/project-context.md`를 먼저 읽을 것.** 프로젝트 배경·결정 사항·이슈·다음 작업을 할 때의 기준이 있다.

## 한 줄 요약
밀폐공간(탱크·맨홀) 2인 1조 작업을 라즈베리파이 4 한 대로 지켜보는 온디바이스 AI 안전 모니터링 시스템.
감시인 부재·쓰러짐·가스/온도 이상·불꽃을 감지해 안쪽 작업자와 바깥 감시인에게 경보한다.

## 코드 규칙
- 언어: Python 3 (라즈베리파이 OS 64-bit, 노트북은 Windows + Git Bash)
- 기준값·핀 번호·해상도 등 **숫자는 코드에 직접 쓰지 않고 `config.yaml`에서 읽는다.**
- 모듈 간 데이터는 `core/events.py`의 `Event(source, type, data, ts)` 하나로만 주고받는다. 형식은 `docs/interface.md`가 기준.
- 비전 공통 형식(v2): 좌표 픽셀 · 원점 왼쪽 위 · 아래로 y 증가 · bbox `(x1, y1, x2, y2)` · 관절 COCO 17개(항상 전부 존재, 안 보이면 conf=0) · 사람 없으면 `[]` · 카메라 출력 BGR 640×480 · 신뢰도 기준 `vision.person_conf_min=0.5`, `vision.kp_conf_min=0.3`
- 시간은 내부적으로 epoch 초, 기록·표시는 한국시간(KST).
- 하드웨어 없이도 개발할 수 있게 `FakeDetector`, `python main.py --sim <시나리오.yaml>`을 유지한다.
- 모델 파일(`models/`), 실행 데이터(`data/`), 영상(`*.mp4`)은 Git에 올리지 않는다.

## 폴더 담당
| 폴더 | 담당 |
|---|---|
| `vision/outer/` | 원석 (감시 카메라) |
| `vision/inner/` | 두혁 (작업자 카메라) |
| `vision/common/` | 모두 — 고치기 전에 상대에게 먼저 알린다. `fall.py` 관리는 두혁 |
| `core/`, `sim/`, `docs/` | 두혁 (통합·문서) |
| `sensors/`, `io_devices/` | 미정 |
| `logic/`, `alerts/` | 미정 |
| `storage/` | 미정 |

## Git 규칙
- 기본 브랜치 `dev`(모든 PR 대상, Squash and merge) / `main`은 시연 가능한 버전만(dev→main은 Merge commit) — merge 전 버튼이 "Squash and merge"인지 확인
- 브랜치 이름: `<종류>/<이슈번호>-<담당쪽>-<기능>` 예) `feat/6-common-fall-rule` (영어 소문자, `-` 연결)
- 커밋 메시지: `<종류>(<범위>): <한 줄 설명>` — 종류 `feat fix docs test chore exp refactor`, 범위 `sensor io vision logic alerts sim config docs github core`
- `dev`, `main`에 직접 push 금지. `git push --force` 금지. 동기화는 rebase 대신 `git merge dev`.
- merge 후 브랜치는 삭제한다 (PR 화면 Delete branch, 로컬은 `git branch -d <브랜치>`)
- PR 본문에 `closes #번호`, 실행 결과(캡처·로그) 첨부.
- PR 체크: Event 형식 준수 / config에서 값 읽기 / 핀 변경 시 `docs/wiring.md` 수정 / 실기기 또는 `--sim` 실행 확인
