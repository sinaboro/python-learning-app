# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.3 모듈 만들고 사용해보기 — 예제 2

import calc                       # calc.py 를 가져온다 (.py 는 쓰지 않음)
print(calc.add(10, 5))
print(round(calc.circle_area(3), 2))
from calc import PI
print(PI)
