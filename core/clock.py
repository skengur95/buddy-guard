"""시간은 모두 한국시간(KST) 기준으로 표기한다."""
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9), "KST")


def now_kst() -> datetime:
    return datetime.now(KST)


def to_kst_str(epoch: float) -> str:
    return datetime.fromtimestamp(epoch, KST).strftime("%Y-%m-%d %H:%M:%S KST")
