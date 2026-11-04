# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.2 함수를 값처럼 다루기 — 예제 4

def make_multiplier(n):
    def multiply(x):
        return x * n             # 바깥 함수의 n 을 기억한다
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))
