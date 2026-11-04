# 부록 — 파이썬 실력을 완성하는 바로 쓰는 알찬 부록
# C 자주 쓰는 표준 라이브러리 12가지 — 예제 1

import math, statistics, re
from collections import Counter
from datetime import date, timedelta

print(math.sqrt(2) ** 2 == 2, math.isclose(math.sqrt(2) ** 2, 2))   # 실수 비교는 isclose
print(statistics.mean([70, 80, 95]), statistics.median([3, 1, 2]))
print(Counter("hello world").most_common(2))                       # 가장 많이 나온 글자
print(re.findall(r"\d+", "주문 3개, 가격 4500원"))                  # 숫자만 뽑기
print(date(2026, 11, 4) + timedelta(days=100))                      # 100일 뒤
