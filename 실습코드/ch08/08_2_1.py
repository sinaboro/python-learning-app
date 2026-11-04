# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.2 상속과 다형성 — 예제 1

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: ...")

class Dog(Animal):                   # Animal 을 물려받는다
    def speak(self):                 # 같은 이름으로 다시 정의 (오버라이딩)
        print(f"{self.name}: 멍멍!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 야옹~")

for pet in [Dog("바둑이"), Cat("나비"), Animal("거북이")]:
    pet.speak()                      # 같은 명령, 다른 동작 → 다형성
