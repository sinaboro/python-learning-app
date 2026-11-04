# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.3 클래스 변수와 메서드 — 예제 2

class MathTool:
    pi = 3.14159

    def __init__(self, r):
        self.r = r
    def area(self):                  # 인스턴스 메서드: self 사용
        return MathTool.pi * self.r ** 2

    @classmethod
    def info(cls):                   # 클래스 메서드: 클래스(cls) 사용
        return f"원주율 {cls.pi}"

    @staticmethod
    def add(a, b):                   # 정적 메서드: self·cls 없이 독립적인 기능
        return a + b

print(round(MathTool(2).area(), 2), MathTool.info(), MathTool.add(3, 4))
