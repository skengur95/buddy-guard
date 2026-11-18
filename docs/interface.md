# 인터페이스 정의서 v1

모든 모듈은 `core/events.py`의 `Event(source, type, data, ts)` 하나로만 메인 루프와 이야기한다.
바뀌면 버전을 올리고 팀 채팅에 공지한다.

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

## 변경 이력
| 버전 | 날짜(KST) | 내용 | 확인 |
|---|---|---|---|
| v1 | | 최초 작성 | |
