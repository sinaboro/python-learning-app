# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.2 표준 라이브러리 활용하기 — 예제 1

import random                      # ① 모듈 전체
from math import ceil, floor       # ② 필요한 기능만 → 이름만으로 사용
import datetime as dt              # ③ 별명 붙이기

print(random.randint(1, 6))        # 1~6 주사위 (실행할 때마다 다름)
print(ceil(3.2), floor(3.8))       # 올림, 내림
print(dt.date(2026, 12, 25) - dt.date(2026, 11, 4))   # 날짜 빼기
