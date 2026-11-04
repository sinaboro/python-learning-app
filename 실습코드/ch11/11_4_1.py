# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.4 패키지와 외부 라이브러리 알아보기 — 예제 1
# 실행하지 않는 예시 (일부러 오류가 나거나 끝나지 않는 코드)

import requests                                   # pip install requests 필요
res = requests.get("https://api.github.com")
print(res.status_code)                            # 200 이면 성공
