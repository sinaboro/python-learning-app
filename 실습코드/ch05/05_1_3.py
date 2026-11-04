# 05장 흐름을 가르는 제어문, 조건문
# 05.1 if 문 — 예제 3

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:          # 위 조건이 거짓일 때 다음 조건 검사
    grade = "B"
elif score >= 70:
    grade = "C"
else:                      # 모든 조건이 거짓일 때
    grade = "F"
print(f"{score}점은 {grade}학점")
