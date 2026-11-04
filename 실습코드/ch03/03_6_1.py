# 03장 기본 자료형
# 03.6 문자열 다양하게 다뤄보기 — 예제 1

text = "  Hello Python  "
print(text.strip())
print(text.strip().upper())
print("사과,배,포도".split(","))
print(" / ".join(["월", "화", "수"]))
print("banana".count("a"), "banana".find("n"))
print("I like Java".replace("Java", "Python"))
