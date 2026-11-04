# 04장 컬렉션 자료형과 불리언
# 04.1 리스트 — 예제 3

scores = [70, 95, 82, 60]
scores.sort()                     # 오름차순으로 제자리 정렬
print(scores)
scores.sort(reverse=True)         # 내림차순
print(scores)
print(max(scores), min(scores), sum(scores))
print(sorted([3, 1, 2]))          # 원본은 두고 정렬된 새 리스트
print(82 in scores, scores.index(82))
