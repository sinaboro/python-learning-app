# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.4 함수를 한 줄로 정의할 수 있는 람다 — 예제 2

nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * 10, nums)))        # 모두에 적용
print(list(filter(lambda n: n % 2 == 0, nums))) # 조건에 맞는 것만
