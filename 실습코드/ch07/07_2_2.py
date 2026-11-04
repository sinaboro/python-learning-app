# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.2 함수와 반환 알아보기 — 예제 2

def show_double(x):
    print(x * 2)            # 화면에 보여 주기만 한다

def get_double(x):
    return x * 2            # 값을 돌려준다

a = show_double(5)          # 10 이 출력되지만
b = get_double(5)
print("a =", a)             # a 에는 아무 값도 없다 (None)
print("b =", b)
