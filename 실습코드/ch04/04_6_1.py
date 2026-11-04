# 04장 컬렉션 자료형과 불리언
# 04.6 자료형 돌아보기 — 예제 1

# 상황에 맞는 자료형 고르기
shopping = ["우유", "빵", "우유"]          # 순서·중복 OK → 리스트
birthday = (2005, 3, 14)                  # 바뀌면 안 됨 → 튜플
phone_book = {"엄마": "010-1111-2222"}     # 이름으로 찾기 → 딕셔너리
visited = set(["서울", "부산", "서울"])     # 중복 없이 → 집합
print(shopping, birthday, phone_book, visited, sep="\n")
