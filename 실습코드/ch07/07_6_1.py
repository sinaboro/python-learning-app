# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.6 재귀 함수 알아보기 — 예제 1

def countdown(n):
    if n == 0:               # 종료 조건
        print("발사!")
        return
    print(n)
    countdown(n - 1)         # 더 작은 문제로 자기 자신 호출

countdown(3)
