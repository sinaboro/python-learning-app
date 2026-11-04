# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.6 모듈과 라이브러리 연습하기 — 예제 1

import random
from datetime import date

def lotto():
    return sorted(random.sample(range(1, 46), 6))   # 1~45 중 겹치지 않게 6개

def d_day(target):
    left = (target - date(2026, 11, 4)).days        # 오늘을 2026-11-04 로 가정
    return f"D-{left}" if left > 0 else ("D-Day" if left == 0 else f"D+{-left}")

for i in range(1, 4):
    print(f"{i}게임: {lotto()}")
print("크리스마스까지", d_day(date(2026, 12, 25)))
