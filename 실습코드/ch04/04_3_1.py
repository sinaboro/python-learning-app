# 04장 컬렉션 자료형과 불리언
# 04.3 딕셔너리 — 예제 1

student = {"name": "김파이", "age": 20, "major": "컴퓨터"}
print(student["name"])
student["age"] = 21              # 값 바꾸기
student["email"] = "pi@ex.com"   # 새 키 추가
del student["major"]             # 삭제
print(student)
