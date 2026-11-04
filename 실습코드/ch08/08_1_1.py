# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.1 클래스와 인스턴스 — 예제 1

class Character:                     # 클래스 이름은 대문자로 시작 (PascalCase)
    def __init__(self, name, hp):    # 인스턴스를 만들 때 자동으로 실행
        self.name = name             # self.이름 = 인스턴스마다 따로 가지는 값(속성)
        self.hp = hp

    def attack(self, target):        # 메서드: 클래스 안의 함수
        print(f"{self.name}이(가) {target.name}을(를) 공격!")
        target.hp -= 10

hero = Character("아서", 100)         # 인스턴스 만들기
monster = Character("슬라임", 30)
hero.attack(monster)
print(monster.name, "남은 체력:", monster.hp)
