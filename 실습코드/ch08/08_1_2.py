# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.1 클래스와 인스턴스 — 예제 2

class Counter:
    def __init__(self):
        self.value = 0
    def up(self):
        self.value += 1

a = Counter(); b = Counter()
a.up(); a.up(); b.up()
print(a.value, b.value)
