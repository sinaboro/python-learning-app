# 06장 반복을 만드는 제어문, 반복문
# 06.3 리스트와 반복문 — 예제 1

scores = [88, 72, 95, 60]
total = 0
for s in scores:
    total += s
print("평균:", total / len(scores))
