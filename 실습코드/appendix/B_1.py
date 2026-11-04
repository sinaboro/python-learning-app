# 부록 — 파이썬 실력을 완성하는 바로 쓰는 알찬 부록
# B 자주 쓰는 내장 함수 25가지 — 예제 1

words = ["banana", "Apple", "cherry"]
print(sorted(words, key=str.lower))              # 대소문자 무시하고 정렬
print(list(map(len, words)))
print(any(w.startswith("A") for w in words), all(len(w) > 3 for w in words))
print(divmod(17, 5), pow(2, 5), chr(65), ord("A"))   # 덤: 몫과 나머지, 거듭제곱, 문자↔코드
