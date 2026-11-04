"""
앱 데이터 만들기: guide/*.md → docs/content.js

교안 PDF 와 같은 원고·같은 실행 결과를 앱에서 쓰도록 바꾼다.
사용법 (저장소 맨 위 폴더에서):  python tools/build_app.py
원고를 고친 뒤에는 docs/sw.js 의 VERSION 도 올려야 폰에 반영된다 (--bump).
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide_lib import ROOT, load_all, check  # noqa: E402

OUT = os.path.join(ROOT, 'docs', 'content.js')


def inline(t):
    t = html.escape(t, quote=False)
    codes = []                                   # `코드` 안의 ** 는 굵게로 바꾸지 않는다
    t = re.sub(r'`([^`]+)`', lambda m: codes.append(m.group(1)) or f'\x00{len(codes) - 1}\x00', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    return re.sub('\x00(\\d+)\x00', lambda m: f'<code>{codes[int(m.group(1))]}</code>', t)


def to_html(blocks, codes, ch_no):
    out = []
    for b in blocks:
        t = b['t']
        if t == 'p':
            out.append(f'<p>{inline(b["text"])}</p>')
        elif t == 'h3':
            out.append(f'<h3>{inline(b["text"])}</h3>')
        elif t in ('ul', 'ol'):
            out.append(f'<{t}>' + ''.join(f'<li>{inline(i)}</li>' for i in b['items']) + f'</{t}>')
        elif t == 'tip':
            out.append(f'<div class="tip">{inline(b["text"]).replace(chr(10), "<br>")}</div>')
        elif t == 'warn':
            out.append(f'<div class="warn">⚠️ {inline(b["text"])}</div>')
        elif t == 'table':
            rows = b['rows']
            out.append('<div class="tbw"><table class="tb">' + ''.join(
                '<tr>' + ''.join(f'<{"th" if i == 0 else "td"}>{inline(c)}</{"th" if i == 0 else "td"}>' for c in r) + '</tr>'
                for i, r in enumerate(rows)) + '</table></div>')
        elif t == 'code':
            if b['lang'] == 'python':
                codes.append({'ch': ch_no, 'code': b['code'], 'out': b.get('out'), 'input': b.get('input'),
                              'file': b.get('file'), 'norun': bool(b.get('norun'))})
                out.append(f'<div class="cb" data-c="{len(codes) - 1}"></div>')
            else:
                out.append(f'<pre class="scr">{html.escape(b["code"])}</pre>')
    return ''.join(out)


def main():
    sys.stdout.reconfigure(errors='replace')
    chs = load_all()
    errs = check(chs)
    if errs:
        sys.exit('원고 오류:\n' + '\n'.join(errs))
    codes, data = [], []
    for ch in chs:
        secs = []
        for s in ch['sections']:
            secs.append({'no': s['no'], 'title': s['title'], 'html': to_html(s['blocks'], codes, ch['no'])})
        data.append({'no': ch['no'], 'title': ch['title'], 'goals': [inline(g) for g in ch['goals']],
                     'sections': secs, 'quiz': [{'q': inline(q['q']), 'o': [inline(o) for o in q['o']], 'a': q['a'], 'e': inline(q['e'])} for q in ch['quiz']]})
    js = ('// 자동 생성 파일 — tools/build_app.py 가 guide/*.md 에서 만든다. 직접 고치지 마세요.\n'
          f'const CH = {json.dumps(data, ensure_ascii=False)};\n'
          f'const CODE = {json.dumps(codes, ensure_ascii=False)};\n')
    open(OUT, 'w', encoding='utf-8', newline='\n').write(js)
    print(f'저장: docs/content.js (장 {len(data)} · 예제 {len(codes)} · 퀴즈 {sum(len(c["quiz"]) for c in data)} · {len(js) // 1024}KB)')
    if '--bump' in sys.argv:
        p = os.path.join(ROOT, 'docs', 'sw.js')
        s = open(p, encoding='utf-8').read()
        m = re.search(r"const VERSION = '([^']*?)(\d+)';", s)
        new = m.group(1) + str(int(m.group(2)) + 1)
        open(p, 'w', encoding='utf-8', newline='\n').write(s.replace(m.group(0), f"const VERSION = '{new}';"))
        print('sw.js VERSION →', new)


if __name__ == '__main__':
    main()
