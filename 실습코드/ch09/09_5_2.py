# 09장 입력과 출력
# 09.5 파일을 한 줄씩 읽어 처리하기 — 예제 2

# 합격자만 골라 새 파일에 저장하기
with open("scores.csv", encoding="utf-8") as src, \
     open("passed.txt", "w", encoding="utf-8") as dst:
    for line in src:
        name, score = line.strip().split(",")
        if int(score) >= 70:
            dst.write(name + "\n")
print(open("passed.txt", encoding="utf-8").read())
