# 09장 입력과 출력
# 09.4 파일 입력 이해하기 — 예제 2

with open("diary.txt", encoding="utf-8") as f:   # 모드를 생략하면 "r"
    lines = f.readlines()
print(len(lines), "줄")
print(lines[0].strip())                          # strip() 으로 줄 끝의 \n 제거
