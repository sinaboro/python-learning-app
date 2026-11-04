# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.5 메모장 프로그램을 모듈로 나누기 — 예제 2
# 입력 예: 1 / 모듈 공부 / 1 / 패키지 공부 / 2 / 3

# memo_app.py — 화면(입력·출력)만 담당, 저장은 memo_store 에게 맡긴다
import memo_store as store
store.clear()                                  # 실습을 위해 비우고 시작

while True:
    menu = input("[1]쓰기 [2]목록 [3]끝 > ")
    if menu == "1":
        store.add(input("메모: "))
    elif menu == "2":
        for i, m in enumerate(store.load(), 1):
            print(f"  {i}. {m}")
    elif menu == "3":
        break
