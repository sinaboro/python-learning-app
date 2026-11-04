# 05장 흐름을 가르는 제어문, 조건문
# 05.3 try~except 문 — 예제 2
# 입력 예: 스물

text = input("나이를 숫자로 입력하세요: ")
try:
    age = int(text)
    print(f"내년에는 {age + 1}살")
except ValueError:
    print("숫자만 입력해 주세요.")
