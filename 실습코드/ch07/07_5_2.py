# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.5 함수와 스코프 — 예제 2

def make_number():
    secret = 42
make_number()
print(secret)                # 지역 변수는 밖에서 쓸 수 없다
