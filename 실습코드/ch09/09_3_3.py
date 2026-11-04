# 09장 입력과 출력
# 09.3 입력이란 무엇일까? — 예제 3
# 입력 예: 3 5 8

nums = input("숫자 여러 개 (띄어쓰기로): ").split()   # ['3', '5', '8']
nums = [int(n) for n in nums]                       # 모두 정수로
print("합계:", sum(nums), "평균:", sum(nums) / len(nums))
