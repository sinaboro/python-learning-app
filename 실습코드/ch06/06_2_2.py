# 06장 반복을 만드는 제어문, 반복문
# 06.2 for 문과 순회 — 예제 2

for i in range(1, 6):
    print(i, end=" ")
print()
total = 0
for i in range(1, 101):
    total += i
print("1부터 100까지의 합:", total)
