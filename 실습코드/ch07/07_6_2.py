# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.6 재귀 함수 알아보기 — 예제 2

def factorial(n):            # n! = n × (n-1)!
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))          # 5 × 4 × 3 × 2 × 1
