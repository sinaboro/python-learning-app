# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.2 상속과 다형성 — 예제 2

class Student:
    def __init__(self, name):
        self.name = name

class Graduate(Student):
    def __init__(self, name, thesis):
        super().__init__(name)       # 부모의 __init__ 으로 name 설정
        self.thesis = thesis         # 자식만의 속성 추가

g = Graduate("김파이", "AI 연구")
print(g.name, "/", g.thesis)
print(isinstance(g, Student))        # 자식은 부모의 한 종류
