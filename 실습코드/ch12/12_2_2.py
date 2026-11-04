# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.2 함수를 값처럼 다루기 — 예제 2

def apply(func, values):
    return [func(v) for v in values]

print(apply(abs, [-1, -2, 3]))
print(apply(str.upper, ["a", "b"]))
print(apply(lambda x: x * x, [1, 2, 3]))
