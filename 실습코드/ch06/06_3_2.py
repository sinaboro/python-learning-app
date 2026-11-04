# 06장 반복을 만드는 제어문, 반복문
# 06.3 리스트와 반복문 — 예제 2

names = ["김파이", "이코딩", "박자바"]
for i, name in enumerate(names, start=1):
    print(f"{i}번: {name}")
scores = [90, 85, 77]
for name, score in zip(names, scores):
    print(name, score)
