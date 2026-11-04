# 06장 반복을 만드는 제어문, 반복문
# 06.1 while 문과 반복문의 기초 — 예제 2

n = 0
while True:                  # 일부러 무한 반복을 만들고
    n += 1
    if n % 2 == 0:
        continue             # 짝수면 아래를 건너뛰고 다시 처음으로
    if n > 9:
        break                # 9 를 넘으면 반복 탈출
    print(n, end=" ")
