# 10장 오류 읽고 예외 처리하기
# 10.3 else 와 finally 로 실행 흐름 나누기 — 예제 1

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  → 0으로 나눌 수 없음")
    else:
        print("  → 성공:", result)
    finally:
        print("  → 계산 끝 (항상 실행)")

print("10 / 2"); divide(10, 2)
print("10 / 0"); divide(10, 0)
