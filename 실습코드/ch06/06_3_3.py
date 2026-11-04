# 06장 반복을 만드는 제어문, 반복문
# 06.3 리스트와 반복문 — 예제 3

scores = [88, 72, 95, 60]
passed = []
for s in scores:
    if s >= 80:
        passed.append(s)
print(passed)
