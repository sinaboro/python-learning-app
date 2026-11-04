# 06장 반복을 만드는 제어문, 반복문
# 06.1 while 문과 반복문의 기초 — 예제 3
# 입력 예: 3 / 7 / 0

# 0 을 입력할 때까지 숫자를 더하는 계산기
total = 0
while True:
    num = int(input("숫자 (0=끝): "))
    if num == 0:
        break
    total += num
print("합계:", total)
