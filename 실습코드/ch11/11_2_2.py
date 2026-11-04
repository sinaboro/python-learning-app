# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.2 표준 라이브러리 활용하기 — 예제 2

import random
menu = ["김밥", "라면", "돈가스", "비빔밥"]
print("오늘 점심:", random.choice(menu))     # 하나 고르기
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)                        # 섞기
print(cards, random.sample(range(1, 46), 6)) # 겹치지 않게 6개 뽑기
