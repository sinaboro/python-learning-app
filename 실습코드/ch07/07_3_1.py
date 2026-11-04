# 07장 코드를 묶어 재사용할 수 있는 함수
# 07.3 매개변수 좀 더 깊게 알아보기 — 예제 1

def order(menu, size="보통", count=1):    # 기본값이 있는 매개변수는 뒤에
    print(f"{menu} {size} {count}개 주문")

order("라면")                              # 기본값 사용
order("짜장면", "곱빼기")
order("커피", count=3)                     # 이름=값 으로 원하는 것만 지정
