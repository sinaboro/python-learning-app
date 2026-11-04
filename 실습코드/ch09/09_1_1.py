# 09장 입력과 출력
# 09.1 출력이란 무엇일까? — 예제 1

name, score = "김파이", 92.456
print("이름:", name, "점수:", score)            # 쉼표: 띄어쓰기로 연결
print("이름: " + name)                           # +: 문자열끼리만
print(f"이름: {name}, 점수: {score:.1f}")         # f-문자열 (가장 추천)
print("이름: {}, 점수: {:.1f}".format(name, score))  # format() 메서드
