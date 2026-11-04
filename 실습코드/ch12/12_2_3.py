# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.2 함수를 값처럼 다루기 — 예제 3

# 계산기: 기호와 함수를 딕셔너리에 담기
ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}
for sym in ops:
    print(f"8 {sym} 2 = {ops[sym](8, 2)}")
