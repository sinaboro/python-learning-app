# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.2 함수와 반환 알아보기 — 예제 1

def add(a, b):
    return a + b            # 결과를 돌려주고 함수를 끝낸다

result = add(3, 4)
print(result)
print(add(10, 20) * 2)      # 반환값을 바로 계산에 쓰기
