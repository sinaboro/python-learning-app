# 06장 반복을 만드는 제어문, 반복문
# 06.3 리스트와 반복문 — 예제 5

prices = {"커피": 4500, "라떼": 5000, "케이크": 6500}
for menu, price in prices.items():
    print(f"{menu}: {price:,}원")      # :, → 천 단위 쉼표
