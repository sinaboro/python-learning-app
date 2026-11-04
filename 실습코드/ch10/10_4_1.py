# 10장 오류 읽고 예외 처리하기
# 10.4 raise 로 직접 예외 발생시키기 — 예제 1

def set_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")   # 예외를 직접 발생
    print(f"나이를 {age}살로 설정했어요")

try:
    set_age(20)
    set_age(-5)
except ValueError as e:
    print("오류:", e)
