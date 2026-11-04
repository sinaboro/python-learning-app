# 05장 흐름을 가르는 제어문, 조건문
# 05.2 비교 연산자, 논리 연산자 — 예제 1

age = 16
has_ticket = True
if age >= 13 and has_ticket:
    print("입장 가능")
day = "일"
if day == "토" or day == "일":
    print("주말이에요")
print(not has_ticket)
