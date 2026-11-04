# 09장 입력과 출력
# 09.6 메모장 프로그램 만들어보기 — 예제 1
# 입력 예: 1 / 우유 사기 / 1 / 파이썬 복습 / 2 / 3

# memo.py — 메모장 프로그램 (1: 쓰기, 2: 목록, 3: 끝)
FILE = "memo.txt"
open(FILE, "w", encoding="utf-8").close()     # 실습을 위해 빈 파일로 시작

while True:
    menu = input("\n[1] 메모 쓰기 [2] 목록 보기 [3] 끝내기 > ")
    if menu == "1":
        text = input("메모 내용: ")
        with open(FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print("저장했어요.")
    elif menu == "2":
        with open(FILE, encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                print(f"{i}. {line.strip()}")
    elif menu == "3":
        print("메모장을 종료합니다.")
        break
    else:
        print("1, 2, 3 중에서 골라 주세요.")
