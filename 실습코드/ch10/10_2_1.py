# 10장 오류 읽고 예외 처리하기
# 10.2 필요한 예외만 골라 처리하기 — 예제 1
# 입력 예: 10 / 0

try:
    a = int(input("나눌 수: "))
    b = int(input("나누는 수: "))
    print("결과:", a / b)
except ValueError:
    print("숫자를 입력해 주세요.")
except ZeroDivisionError:
    print("0 으로 나눌 수 없어요.")
