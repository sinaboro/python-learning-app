# 부록 — 파이썬 실력을 완성하는 바로 쓰는 알찬 부록
# C 자주 쓰는 표준 라이브러리 12가지 — 예제 2

import csv
with open("members.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이"])
    writer.writerows([["김파이", 20], ["이코딩", 23]])
with open("members.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):              # 첫 줄을 키로 쓰는 딕셔너리
        print(row["이름"], int(row["나이"]) + 1)
