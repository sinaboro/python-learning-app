# 09장 입력과 출력
# 09.2 파일 출력 이해하기 — 예제 1

f = open("hello.txt", "w", encoding="utf-8")   # 한글은 encoding="utf-8" 을 꼭!
f.write("안녕하세요\n")                          # write 는 줄바꿈을 자동으로 넣지 않는다
f.write("파일에 저장된 두 번째 줄\n")
f.close()                                       # 다 쓰면 닫기
print("hello.txt 저장 완료")
