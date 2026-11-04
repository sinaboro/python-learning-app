# 06장 반복을 만드는 제어문, 반복문
# 06.1 while 문과 반복문의 기초 — 예제 1

count = 1
while count <= 5:            # count 가 5 이하인 동안
    print(f"{count}번째 인사: 안녕!")
    count += 1               # 이 줄이 없으면 영원히 반복된다
print("반복 끝")
