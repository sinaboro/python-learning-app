# 09장 입력과 출력
# 09.5 파일을 한 줄씩 읽어 처리하기 — 예제 1

# 성적 파일 만들기 (이름,점수)
with open("scores.csv", "w", encoding="utf-8") as f:
    f.write("김파이,88\n이코딩,95\n박자바,72\n최루비,64\n")

total, count = 0, 0
with open("scores.csv", encoding="utf-8") as f:
    for line in f:                          # 한 줄씩
        name, score = line.strip().split(",")
        score = int(score)
        mark = "합격" if score >= 70 else "불합격"
        print(f"{name}: {score}점 {mark}")
        total += score; count += 1
print(f"평균 {total / count:.1f}점")
