# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.7 알아두면 좋은 파이썬 내장 함수 6가지 — 예제 1

data = [-3, 8, 1, -9, 5]
print(abs(-3), round(2.675, 1), sum(data))
print(max(data), min(data), max(data, key=abs))   # key: 기준을 정할 수 있다
print(sorted(data, reverse=True))
for i, (a, b) in enumerate(zip("가나", "AB")):
    print(i, a, b)
