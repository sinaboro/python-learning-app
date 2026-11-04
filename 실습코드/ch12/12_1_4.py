# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.1 값을 복사한다는 것은 무엇일까? — 예제 4

def add_item(cart, item):
    cart.append(item)            # 넘겨받은 리스트를 직접 바꾼다

my_cart = ["우유"]
add_item(my_cart, "빵")
print(my_cart)                   # 함수 밖의 리스트도 바뀐다
