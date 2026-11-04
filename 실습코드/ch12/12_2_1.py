# 12장 한 걸음 더 깊게 알아보는 파이썬
# 12.2 함수를 값처럼 다루기 — 예제 1

def shout(text):
    return text.upper() + "!"

speak = shout                    # 괄호 없이 쓰면 함수 자체를 가리킨다
print(speak("hello"))
print(type(shout))
