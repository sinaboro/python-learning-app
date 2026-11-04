# 09장 입력과 출력
# 09.4 파일 입력 이해하기 — 예제 1

with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()                    # 전체를 문자열 하나로
print(content)
