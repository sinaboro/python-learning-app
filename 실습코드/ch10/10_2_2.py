# 10장 오류 읽고 예외 처리하기
# 10.2 필요한 예외만 골라 처리하기 — 예제 2

data = {"a": 1}
for key in ["a", "b"]:
    try:
        print(key, "→", 10 / (data[key] - 1))
    except (KeyError, ZeroDivisionError) as e:   # 괄호로 묶어 여러 개
        print(f"{key}: {type(e).__name__} 발생 ({e})")
