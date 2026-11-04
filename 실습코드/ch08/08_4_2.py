# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.4 클래스 연습하기 — 예제 2

# 상속으로 이자 기능이 있는 적금 계좌 만들기
class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.03):
        super().__init__(owner, balance)
        self.rate = rate
    def add_interest(self):
        interest = int(self.balance * self.rate)
        self.deposit(interest)
        print(f"이자 {interest:,}원 지급")

s = SavingAccount("이코딩", 100000)
s.add_interest()
print(s)
