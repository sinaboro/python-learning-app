# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.2 표준 라이브러리 활용하기 — 예제 3

import os, time
print("지금 폴더에 있는 .txt 파일 수:", len([f for f in os.listdir(".") if f.endswith(".txt")]))
start = time.time()
total = sum(range(1_000_000))
print("백만까지 더하는 데 1초도 안 걸렸나요?", time.time() - start < 1)
