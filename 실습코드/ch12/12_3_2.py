# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.3 반복의 정체, 이터러블과 제너레이터 — 예제 2

def countdown(n):
    while n > 0:
        yield n                  # 값을 하나 내주고 여기서 잠시 멈춘다
        n -= 1

gen = countdown(3)
print(next(gen))
for value in gen:                # 남은 값을 이어서 꺼낸다
    print(value)
