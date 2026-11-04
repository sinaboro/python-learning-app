# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.4 함수를 한 줄로 정의할 수 있는 람다 — 예제 1

square = lambda x: x ** 2
print(square(5))

students = [("김파이", 85), ("이코딩", 92), ("박자바", 78)]
students.sort(key=lambda s: s[1], reverse=True)    # 점수(1번 값)로 정렬
print(students)
