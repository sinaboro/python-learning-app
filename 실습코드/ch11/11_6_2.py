# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.6 모듈과 라이브러리 연습하기 — 예제 2

import json                                          # 파이썬 자료 ↔ 문자열(JSON)
profile = {"name": "김파이", "skills": ["python", "git"], "age": 20}
text = json.dumps(profile, ensure_ascii=False)       # 딕셔너리 → JSON 문자열
print(text)
back = json.loads(text)                              # JSON 문자열 → 딕셔너리
print(back["skills"][0])
