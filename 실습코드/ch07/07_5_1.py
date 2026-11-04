# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.5 함수와 스코프 — 예제 1

message = "전역"             # 전역 변수

def func():
    message = "지역"         # 같은 이름이지만 함수 안의 새 변수
    print("함수 안:", message)

func()
print("함수 밖:", message)   # 전역 변수는 그대로
