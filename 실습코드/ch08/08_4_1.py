# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.4 클래스 연습하기 — 예제 1

class BankAccount:
    bank = "파이은행"                    # 클래스 변수

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []                # 거래 기록

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"입금 {amount:,}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"잔액 부족! (잔액 {self.balance:,}원)")
            return False
        self.balance -= amount
        self.history.append(f"출금 {amount:,}")
        return True

    def __str__(self):
        return f"[{self.bank}] {self.owner} 님 잔액 {self.balance:,}원"

acc = BankAccount("김파이", 10000)
acc.deposit(5000)
acc.withdraw(30000)
acc.withdraw(3000)
print(acc)
print(acc.history)
