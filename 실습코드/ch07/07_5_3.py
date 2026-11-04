# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.5 함수와 스코프 — 예제 3

count = 0
def increase():
    global count             # 전역 변수 count 를 쓰겠다는 선언
    count += 1
increase(); increase()
print(count)
