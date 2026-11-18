"""L1 단독 테스트: 교대 버튼을 누르면 바깥 빨간 LED 토글 + 부저 2회.
라즈베리파이에서만 실행. 핀 번호는 config.yaml에서 읽는다."""
from signal import pause

import yaml
from gpiozero import LED, Button, Buzzer

with open("config.yaml", encoding="utf-8") as f:
    pins = yaml.safe_load(f)["pins"]

red = LED(pins["led_outer"]["red"])
buzz = Buzzer(pins["buzzer_outer"])  # Low 트리거 모듈이면 active_high=False
btn = Button(pins["btn_handover"], pull_up=True, bounce_time=0.05)


def on_press():
    red.toggle()
    buzz.beep(on_time=0.1, off_time=0.1, n=2)


btn.when_pressed = on_press
print("교대 버튼을 눌러 보세요 (Ctrl+C로 종료)")
pause()
