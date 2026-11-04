# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.1 값을 복사한다는 것은 무엇일까? — 예제 3

import copy
original = [1, [10, 20]]
shallow = original.copy()          # 얕은 복사 (= list(original), original[:])
deep = copy.deepcopy(original)     # 깊은 복사: 안쪽 리스트까지 새로

original[0] = 99                   # 바깥 값 변경
original[1].append(30)             # 안쪽 리스트 변경
print("원본:", original)
print("얕은:", shallow)            # 안쪽 리스트는 함께 바뀜!
print("깊은:", deep)               # 완전히 독립
