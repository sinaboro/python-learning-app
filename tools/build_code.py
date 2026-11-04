"""
실습코드 만들기: guide/*.md 의 예제를 장별 폴더의 .py 파일로 꺼낸다 → 실습코드/chNN/

사용법 (저장소 맨 위 폴더에서):  python tools/build_code.py
파일 이름: 절번호_예제순서.py (예: 03_4_2.py = 3장 4절의 두 번째 예제)
모듈 예제(file=)는 원래 이름(calc.py 등)으로 저장한다.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide_lib import ROOT, load_all  # noqa: E402

OUT = os.path.join(ROOT, '실습코드')


def main():
    sys.stdout.reconfigure(errors='replace')
    chs = load_all(run=False)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    index = ['# 실습코드', '', '교안(`Python_기초_학습교안.pdf`)과 학습 앱의 예제를 장별로 모은 폴더입니다.',
             '각 파일은 `python 파일이름.py` 로 따로 실행할 수 있어요. (VS Code 에서는 ▷ 버튼)', '',
             '- 파일 이름 `03_4_2.py` = 3장 4절의 두 번째 예제', '- `# 입력 예:` 가 있는 파일은 실행하면 키보드 입력을 기다려요.',
             '- `# 실행하지 않는 예시` 는 일부러 오류가 나거나 끝나지 않는 코드예요. 읽고 확인만 하세요.',
             '- 9~11장은 파일을 만들고 읽어요. **같은 폴더에서 순서대로** 실행하세요. (11장은 `calc.py`, `memo_store.py` 가 같은 폴더에 있어야 해요)', '']
    total = 0
    for ch in chs:
        folder = 'appendix' if ch['no'] == '부록' else f'ch{ch["no"]}'
        d = os.path.join(OUT, folder)
        os.makedirs(d, exist_ok=True)
        index.append(f'## {folder} — {ch["title"]}')
        for sec in ch['sections']:
            k = 0
            for b in sec['blocks']:
                if b['t'] != 'code' or b['lang'] != 'python':
                    continue
                k += 1
                name = b.get('file') or f'{sec["no"].replace(".", "_")}_{k}.py'
                head = [f'# {ch["no"]}장 {ch["title"]}' if ch['no'] != '부록' else f'# 부록 — {ch["title"]}',
                        f'# {sec["no"]} {sec["title"]} — 예제 {k}']
                if b.get('input'):
                    head.append('# 입력 예: ' + ' / '.join(x or '(그냥 Enter)' for x in b['input']))
                if b.get('norun') and not b.get('file'):
                    head.append('# 실행하지 않는 예시 (일부러 오류가 나거나 끝나지 않는 코드)')
                open(os.path.join(d, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(head) + '\n\n' + b['code'] + '\n')
                index.append(f'- `{name}` — {sec["no"]} {sec["title"]}')
                total += 1
        index.append('')
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(index))
    print(f'실습코드: {total}개 파일 → 실습코드/')


if __name__ == '__main__':
    main()
