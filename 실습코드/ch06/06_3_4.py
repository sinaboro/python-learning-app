# 06장 반복을 만드는 제어문, 반복문
# 06.3 리스트와 반복문 — 예제 4

scores = [88, 72, 95, 60]
passed = [s for s in scores if s >= 80]
squares = [n ** 2 for n in range(1, 6)]
print(passed, squares)
