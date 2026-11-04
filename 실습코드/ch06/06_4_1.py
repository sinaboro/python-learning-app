# 06장 반복을 만드는 제어문, 반복문
# 06.4 중첩 반복문 — 예제 1

for dan in range(2, 4):            # 2단, 3단
    for i in range(1, 10):         # 1 ~ 9
        print(f"{dan}×{i}={dan * i:2}", end="  ")
    print()                        # 한 단이 끝나면 줄바꿈
