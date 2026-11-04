# 04장 컬렉션 자료형과 불리언
# 04.3 딕셔너리 — 예제 2

student = {"name": "김파이", "age": 20}
print(student.get("phone"))            # 없는 키 → None (오류 없음)
print(student.get("phone", "없음"))     # 없을 때 대신 쓸 값
print(student.keys())
print(student.values())
print(student.items())
print("name" in student)
