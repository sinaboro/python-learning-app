# 10장 오류 읽고 예외 처리하기
# 10.4 raise 로 직접 예외 발생시키기 — 예제 2

class NotEnoughMoney(Exception):          # Exception 을 상속해서 만든다
    pass

def pay(balance, price):
    if price > balance:
        raise NotEnoughMoney(f"{price - balance:,}원이 부족해요")
    return balance - price

try:
    print(pay(10000, 3000))
    print(pay(10000, 15000))
except NotEnoughMoney as e:
    print("결제 실패:", e)
