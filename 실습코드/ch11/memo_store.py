# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.5 메모장 프로그램을 모듈로 나누기 — 예제 1

# memo_store.py — 메모를 파일에 읽고 쓰는 일만 담당하는 모듈
FILE = "memo_mod.txt"

def load():
    """저장된 메모 목록을 돌려준다. 파일이 없으면 빈 리스트."""
    try:
        with open(FILE, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def add(text):
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def clear():
    open(FILE, "w", encoding="utf-8").close()
