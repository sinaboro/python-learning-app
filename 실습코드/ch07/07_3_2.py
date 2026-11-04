# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.3 매개변수 좀 더 깊게 알아보기 — 예제 2

def total(*nums):           # 넘긴 값들이 튜플로 모인다
    return sum(nums)

print(total(1, 2), total(1, 2, 3, 4, 5))

def profile(**info):        # 이름=값 들이 딕셔너리로 모인다
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="김파이", age=20, city="서울")
