# 06장 반복을 만드는 제어문, 반복문
# 06.4 중첩 반복문 — 예제 3

# 2차원 리스트(표) 돌기
table = [[1, 2, 3], [4, 5, 6]]
for row in table:
    for value in row:
        print(value, end=" ")
    print()
