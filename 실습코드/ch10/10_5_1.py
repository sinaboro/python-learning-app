# 10장 오류 읽고 예외 처리하기
# 10.5 오류에 대비한 메모장 프로그램 만들기 — 예제 1
# 입력 예: 2 / 1 / (그냥 Enter) / 1 / 장보기 / 1 / 운동하기 / 3 / 5 / 3 / 1 / 2 / 4

# memo_safe.py — 오류에 대비한 메모장
import os
FILE = "memo_safe.txt"
if os.path.exists(FILE):
    os.remove(FILE)                            # 실습을 위해 파일 없이 시작

def load():
    try:
        with open(FILE, encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:                  # 처음 실행하면 파일이 없다
        return []

def save(memos):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(memos) + ("\n" if memos else ""))

while True:
    menu = input("\n[1]쓰기 [2]목록 [3]삭제 [4]끝 > ")
    memos = load()
    if menu == "1":
        text = input("메모: ").strip()
        if not text:
            print("빈 메모는 저장하지 않아요.")
            continue
        memos.append(text); save(memos); print("저장!")
    elif menu == "2":
        if not memos:
            print("메모가 없어요.")
        for i, m in enumerate(memos, 1):
            print(f"{i}. {m}")
    elif menu == "3":
        try:
            n = int(input("지울 번호: "))
            removed = memos.pop(n - 1)         # 없는 번호면 IndexError
            save(memos); print(f"'{removed}' 삭제")
        except ValueError:
            print("번호는 숫자로 입력해 주세요.")
        except IndexError:
            print("그런 번호의 메모는 없어요.")
    elif menu == "4":
        print("종료합니다."); break
