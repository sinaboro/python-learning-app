# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.2 함수와 반환 알아보기 — 예제 3

def min_max(numbers):
    return min(numbers), max(numbers)     # 튜플로 돌려준다

low, high = min_max([7, 2, 9, 4])
print(f"최솟값 {low}, 최댓값 {high}")
