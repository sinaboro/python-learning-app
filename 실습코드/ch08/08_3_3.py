# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.3 클래스 변수와 메서드 — 예제 3

class Book:
    def __init__(self, title, price):
        self.title, self.price = title, price
    def __str__(self):
        return f"『{self.title}』 {self.price:,}원"

print(Book("파이썬 첫걸음", 18000))
