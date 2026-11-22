# 인터페이스 정의서 v2

모든 모듈은 `core/events.py`의 `Event(source, type, data, ts)` 하나로만 메인 루프와 소통한다.
(이 문서가 바뀌면 버전을 올리고 팀 채팅에 공지)

vision에서 주는 원본 데이터와 판별 후 Event에서 메인 루프에 전달하는 결론 데이터는 다르다.
이 문서의 약속은 두 층으로 되어있다.
- **1장 모듈 간 Event** : 모든 모듈이 메인 루프에 보내는 메시지 형식 (결론 보고 형식)
- **2장 비전 공통 형식** : vision 폴더 안에서 카메라 / 디텍터 결과를 주고받는 형식 (판정 전 원본 데이터)
- vision 코드는 2장의 결과(Detection)로 판정한 뒤, 1장의 Event로 바꿔서 메인 루프에 보낸다. Detection을 bus에 그대로 넣지 않는다.

## 1. 모듈 간 Event
| source | type | data 예시 | 주기 |
|---|---|---|---|
| vision.outer | zone_count | `{"persons_in_zone": 1, "fps": 6.2}` | 프레임마다 |
| vision.outer / vision.inner | pose | `{"lying": true, "torso_deg": 72, "conf": 0.81}` | 프레임마다 |
| sensor.gas | reading | `{"mq2_v": 0.92, "mq2_ratio": 1.08, "mq7_v": 0.61, "mq7_ratio": 1.02}` | 1초 |
| sensor.env | reading | `{"temp_c": 24.3, "hum": 41}` | 1초 |
| sensor.flame | detected | `{"value": true}` | 바뀔 때 |
| input.button | pressed | `{"name": "handover" \| "ack" \| "start"}` | 바뀔 때 |
| input.rfid | tag | `{"uid": "A1B2C3D4"}` | 바뀔 때 |
| system | device_error | `{"device": "cam_inner", "reason": "timeout"}` | 발생 시 |


## 2. 비전 공통 형식 (v2)
### 2.1 좌표 규칙
- 

### 2.2 관절

### 2.3 Person

### 2.4 Detection

### 2.5 카메라 출력

### 2.6 사용 방법


## 3. 바꾸는 법

## 변경 이력
| 버전 | 날짜(KST) | 내용 | 확인 |
|---|---|---|---|
| v1 | | 최초 작성, 모듈간 EVENT | |
| v1 | | 비전 공통 형식, 바꾸는 법 작성 | |