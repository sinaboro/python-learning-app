# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.3 반복의 정체, 이터러블과 제너레이터 — 예제 1

nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it, "끝"))       # 기본값을 주면 오류 대신 그 값을 돌려준다
