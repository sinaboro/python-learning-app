# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.3 반복의 정체, 이터러블과 제너레이터 — 예제 3

# 리스트 vs 제너레이터 표현식: 메모리 크기 비교
import sys
big_list = [n * n for n in range(100_000)]
big_gen = (n * n for n in range(100_000))      # 대괄호 대신 소괄호
print("리스트:", sys.getsizeof(big_list), "바이트")
print("제너레이터:", sys.getsizeof(big_gen), "바이트")
print("합계는 같다:", sum(big_gen) == sum(big_list))
