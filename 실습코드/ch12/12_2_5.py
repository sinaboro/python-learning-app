# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.2 함수를 값처럼 다루기 — 예제 5

def log(func):
    def wrapper(*args):
        print(f"[기록] {func.__name__}{args} 호출")
        return func(*args)
    return wrapper

@log                             # add = log(add) 와 같다
def add(a, b):
    return a + b

print(add(3, 4))
