# 11장 코드를 나누고 가져오는 모듈과 라이브러리
# 11.3 모듈 만들고 사용해보기 — 예제 1

# calc.py — 계산 기능을 모아 둔 나만의 모듈
PI = 3.14159

def add(a, b):
    return a + b

def circle_area(r):
    return PI * r ** 2

if __name__ == "__main__":        # 이 파일을 직접 실행할 때만 아래가 실행된다
    print("calc.py 시험 실행:", add(1, 2))
