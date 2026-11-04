# 08장 자료와 함수를 묶어 관리하는 클래스
# 08.3 클래스 변수와 메서드 — 예제 1

class Member:
    count = 0                        # 클래스 변수: 모든 회원이 함께 쓰는 값

    def __init__(self, name):
        self.name = name             # 인스턴스 변수
        Member.count += 1            # 회원이 생길 때마다 1 증가

Member("김파이"); Member("이코딩"); m = Member("박자바")
print("전체 회원 수:", Member.count, "/", m.count)
