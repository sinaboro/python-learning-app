# 09장 입력과 출력
# 09.2 파일 출력 이해하기 — 예제 2

with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("11월 4일: 파이썬 파일 저장을 배웠다.\n")
with open("diary.txt", "a", encoding="utf-8") as f:   # a: 이어 쓰기
    f.write("11월 5일: 파일 읽기를 배울 예정.\n")
    print("print 로도 파일에 쓸 수 있다", file=f)
print("diary.txt 에 3줄 저장")
