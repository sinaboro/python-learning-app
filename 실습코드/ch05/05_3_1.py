# 05장 흐름을 가르는 제어문, 조건문
# 05.3 try~except 문 — 예제 1

try:
    result = 10 / 0          # 0 으로 나누면 오류가 난다
    print(result)
except ZeroDivisionError:
    print("0 으로는 나눌 수 없어요.")
print("프로그램은 계속 실행돼요")
