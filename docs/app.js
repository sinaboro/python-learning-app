// 파이썬 첫걸음 — 화면 이동, 진도 저장, 코드 실행(Pyodide), 퀴즈, 실습장, 앱 설치
// 화면 주소(해시): #/ 홈 · #/c/장 · #/c/장/절 · #/q/장 퀴즈 · #/play 실습장 · #/help 사용법

const $ = s => document.querySelector(s);
const view = $('#view');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
let tt;
function toast(m) { const t = $('#toast'); t.textContent = m; t.hidden = false; clearTimeout(tt); tt = setTimeout(() => t.hidden = true, 2200); }

// ───────── 진도 저장 ─────────
// 절은 "장/절번호"(예: 03/03.4)로, 퀴즈는 "q/장"으로 저장 → 내용을 추가해도 기록이 유지된다
const STORE = 'py-learn-progress-v1';
let prog = {};
try { prog = JSON.parse(localStorage.getItem(STORE)) || {}; } catch (e) {}
const saveProg = () => { try { localStorage.setItem(STORE, JSON.stringify(prog)); } catch (e) {} };
const skey = (c, s) => `${c.no}/${s.no}`;
const chLabel = c => c.no === '부록' ? '부록' : `${c.no}장`;
const items = c => c.sections.length + (c.quiz.length ? 1 : 0);
const doneOf = c => c.sections.filter(s => prog[skey(c, s)]).length + (prog['q/' + c.no] ? 1 : 0);
const totalItems = CH.reduce((a, c) => a + items(c), 0);
function nextStep() {
  for (const c of CH) {
    for (const s of c.sections) if (!prog[skey(c, s)]) return { c, s };
    if (c.quiz.length && !prog['q/' + c.no]) return { c, quiz: true };
  }
  return null;
}

// ───────── 화면 이동 ─────────
function route() {
  const p = location.hash.replace(/^#\/?/, '').split('/').filter(Boolean).map(decodeURIComponent);
  const tab = p[0] === 'play' ? 'play' : p[0] === 'help' ? 'help' : 'home';
  document.querySelectorAll('.tabs a').forEach(a => a.classList.toggle('on', a.dataset.tab === tab));
  const back = $('#back');
  back.hidden = !(p[0] === 'c' || p[0] === 'q');
  if (p[0] === 'c' || p[0] === 'q') {
    const c = CH.find(x => x.no === p[1]);
    if (!c) return go('#/');
    if (p[0] === 'q') { back.onclick = () => go(`#/c/${c.no}`); renderQuiz(c); }
    else if (p[2]) {
      const s = c.sections.find(x => x.no === p[2]);
      if (!s) return go(`#/c/${c.no}`);
      back.onclick = () => go(`#/c/${c.no}`); renderSection(c, s);
    } else { back.onclick = () => go('#/'); renderChapter(c); }
  } else if (tab === 'play') renderPlay();
  else if (tab === 'help') renderHelp();
  else renderHome();
  window.scrollTo(0, 0);
}
const go = h => { location.hash = h; };
addEventListener('hashchange', route);

// ───────── 홈 ─────────
function renderHome() {
  $('#title').textContent = '파이썬 첫걸음';
  const done = CH.reduce((a, c) => a + doneOf(c), 0), n = nextStep();
  view.innerHTML = `<div class="stack">
    <div class="hero"><h2>파이썬 첫걸음 🐍</h2>
      <p>코드를 폰에서 바로 고치고 실행하며 배워요. 장마다 총정리 퀴즈로 확인!</p>
      <div class="bar"><i style="width:${done / totalItems * 100}%"></i></div>
      <p style="margin-top:6px;font-size:13px">진도 ${done} / ${totalItems} (절 + 퀴즈)</p>
      <button class="cont" id="cont">${n ? `▶ ${done ? '이어서 학습하기' : '첫 장 시작하기'}<br><small style="font-weight:600">${chLabel(n.c)} · ${n.quiz ? '총정리 퀴즈' : n.s.no + ' ' + n.s.title}</small>` : '🎉 모두 완료! 처음부터 복습하기'}</button>
    </div>
    ${CH.map(c => `<button class="chap ${doneOf(c) === items(c) ? 'done' : ''}" data-c="${c.no}">
      <span class="no">${doneOf(c) === items(c) ? '✓' : c.no === '부록' ? '+' : c.no}</span>
      <span class="ct"><b>${c.no === '부록' ? '부록 ' : ''}${c.title}</b><small>${c.sections.length}개 절${c.quiz.length ? ` · 퀴즈 ${c.quiz.length}문제` : ''} · 진도 ${doneOf(c)}/${items(c)}</small>
      <span class="bar"><i style="width:${doneOf(c) / items(c) * 100}%"></i></span></span></button>`).join('')}
  </div>`;
  $('#cont').onclick = () => { const x = nextStep(); if (!x) return go(`#/c/01/${CH[0].sections[0].no}`); go(x.quiz ? `#/q/${x.c.no}` : `#/c/${x.c.no}/${x.s.no}`); };
  view.querySelectorAll('[data-c]').forEach(b => b.onclick = () => go(`#/c/${b.dataset.c}`));
}

// ───────── 장 ─────────
function renderChapter(c) {
  $('#title').textContent = `${chLabel(c)} ${c.title}`;
  view.innerHTML = `<div class="stack">
    <div class="lhead"><span class="k">${c.no === '부록' ? 'APPENDIX' : 'CHAPTER ' + c.no}</span><h2>${c.title}</h2></div>
    ${c.goals.length ? `<div class="goals"><h3>🎯 학습 목표</h3><ul>${c.goals.map(g => `<li>${g}</li>`).join('')}</ul></div>` : ''}
    ${c.sections.map(s => `<button class="sec" data-s="${s.no}"><span class="k">${s.no}</span><span class="t">${s.title}</span><span class="ck">${prog[skey(c, s)] ? '✓' : '›'}</span></button>`).join('')}
    ${c.quiz.length ? `<button class="qbtn" id="qb">📝 ${c.no === '부록' ? '종합 실력 점검' : '총정리 퀴즈'} ${c.quiz.length}문제 ${prog['q/' + c.no] ? '· 완료 ✓' : ''}</button>` : ''}
  </div>`;
  view.querySelectorAll('[data-s]').forEach(b => b.onclick = () => go(`#/c/${c.no}/${b.dataset.s}`));
  const qb = $('#qb'); if (qb) qb.onclick = () => go(`#/q/${c.no}`);
}

// ───────── 절 (본문 + 실행할 수 있는 코드) ─────────
function renderSection(c, s) {
  const i = c.sections.indexOf(s), prev = c.sections[i - 1], next = c.sections[i + 1];
  const ci = CH.indexOf(c), nextCh = CH[ci + 1];
  $('#title').textContent = `${s.no} ${s.title}`;
  view.innerHTML = `<div class="stack">
    <div class="lhead"><span class="k">${chLabel(c)} ${c.title} · ${i + 1} / ${c.sections.length}</span><h2>${s.no} ${s.title}</h2></div>
    <div class="card body">${s.html}</div>
    <div class="nav2">
      ${prev ? `<button data-go="#/c/${c.no}/${prev.no}">‹ 이전</button>` : `<button data-go="#/c/${c.no}">‹ 목차</button>`}
      ${next ? `<button class="pri" data-go="#/c/${c.no}/${next.no}">다음 ›</button>`
        : c.quiz.length ? `<button class="pri" data-go="#/q/${c.no}">📝 총정리 퀴즈 ›</button>`
        : nextCh ? `<button class="pri" data-go="#/c/${nextCh.no}">다음 장 ›</button>` : `<button class="pri" data-go="#/">홈</button>`}
    </div></div>`;
  view.querySelectorAll('[data-go]').forEach(b => b.onclick = () => go(b.dataset.go));
  view.querySelectorAll('.cb[data-c]').forEach(el => codeBox(el, CODE[+el.dataset.c]));
  if (!prog[skey(c, s)]) { prog[skey(c, s)] = Date.now(); saveProg(); }     // 열어 본 절은 읽음으로 기록
}

// 코드 상자: 고쳐서 ▶ 실행, ↺ 원래대로, 복사
function codeBox(el, ex, opts = {}) {
  const label = ex.file ? `📄 파일: ${ex.file}` : ex.norun ? '파이썬 (실행하면 오류·무한 반복이 나는 예시)' : '파이썬';
  el.innerHTML = `<div class="hd"><span>${label}</span>${ex.file ? '' : '<button class="run">▶ 실행</button>'}<button class="rs">↺</button><button class="cp">복사</button></div>
    <textarea spellcheck="false" autocapitalize="off" autocomplete="off"></textarea><pre class="out" hidden></pre>`;
  const ta = el.querySelector('textarea'), out = el.querySelector('.out');
  const fit = () => { ta.style.height = 'auto'; ta.style.height = ta.scrollHeight + 'px'; };
  ta.value = ex.code; requestAnimationFrame(fit);
  ta.addEventListener('input', () => { fit(); if (ex.file) FILES[ex.file] = ta.value; });
  ta.addEventListener('keydown', e => { if (e.key === 'Tab') { e.preventDefault(); document.execCommand('insertText', false, '    '); } });
  const showOut = (text, lb, err) => { out.hidden = false; out.className = 'out' + (err ? ' err' : ''); out.innerHTML = `<span class="lb">${lb}</span>${esc(text || '(출력 없음)')}`; };
  if (ex.out != null && !opts.blank) showOut(ex.out, '실행 결과 (예시)' + (ex.input ? ` · 입력값: ${ex.input.map(x => x || '(Enter)').join(', ')}` : ''));
  if (ex.file) FILES[ex.file] = ex.code;
  const run = el.querySelector('.run');
  if (run) run.onclick = async () => {
    run.disabled = true; run.textContent = '⏳';
    try {
      if (ex.input) toast('입력 창이 뜨면 값을 입력하세요');
      const r = await runPython(ta.value);
      showOut(r.out, r.err ? '오류가 났어요 (마지막 줄을 읽어 보세요)' : '실행 결과', r.err);
    } catch (e) { showOut(String(e.message || e), '실행 준비 실패', true); }
    run.disabled = false; run.textContent = '▶ 실행';
  };
  el.querySelector('.rs').onclick = () => { ta.value = ex.code; fit(); if (ex.file) FILES[ex.file] = ex.code; toast('원래 코드로 되돌렸어요'); };
  el.querySelector('.cp').onclick = async () => { try { await navigator.clipboard.writeText(ta.value); toast('코드를 복사했어요'); } catch (e) { ta.select(); toast('길게 눌러 복사하세요'); } };
}

// ───────── 파이썬 실행 (Pyodide: 브라우저 안의 파이썬) ─────────
// 처음 실행할 때 한 번 내려받고(약 10MB), 이후에는 폰에 저장된 것을 써서 인터넷 없이도 실행된다.
const PYODIDE = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/';
const FILES = {};                                     // 모듈 예제(calc.py 등): 실행 전에 가상 폴더에 저장
let pyReady = null;
function loadPy() {
  if (pyReady) return pyReady;
  pyReady = new Promise((res, rej) => {
    toast('파이썬 준비 중… 처음 한 번은 10초쯤 걸려요');
    const s = document.createElement('script'); s.src = PYODIDE + 'pyodide.js';
    s.onload = async () => {
      try {
        const py = await loadPyodide({ indexURL: PYODIDE });
        // input() → 입력 창, 오래 걸리는 코드(무한 반복)는 10초 뒤 멈춤
        py.runPython(`
import builtins, sys, time, js
_deadline = [0]
def _input(prompt=''):
    v = js.prompt(str(prompt) or '입력하세요')
    v = '' if v is None else str(v)
    print(str(prompt) + v)
    _deadline[0] = time.time() + 10
    return v
builtins.input = _input
def _tracer(frame, event, arg):
    if time.time() > _deadline[0]:
        raise TimeoutError('10초가 넘어 실행을 멈췄어요. 무한 반복인지 확인하세요.')
    return _tracer
`);
        res(py);
      } catch (e) { pyReady = null; rej(e); }
    };
    s.onerror = () => { pyReady = null; rej(new Error('파이썬을 내려받지 못했어요. 처음 한 번은 인터넷 연결이 필요해요.')); };
    document.head.appendChild(s);
  });
  return pyReady;
}
async function runPython(code) {
  const py = await loadPy();
  for (const [name, src] of Object.entries(FILES)) {           // 모듈 파일 저장 + 다시 읽게 하기
    py.FS.writeFile(name, src);
    py.runPython(`import sys; sys.modules.pop(${JSON.stringify(name.replace(/\.py$/, ''))}, None)`);
  }
  let out = '';
  py.setStdout({ batched: s => { out += s + '\n'; } });
  py.setStderr({ batched: s => { out += s + '\n'; } });
  py.globals.set('_user_code', code);
  try {
    await py.runPythonAsync(`
import sys, time
_deadline[0] = time.time() + 10
sys.settrace(_tracer)
try:
    exec(compile(_user_code, '<코드>', 'exec'), {'__name__': '__main__'})
finally:
    sys.settrace(None)
`);
    return { out: out.replace(/\n$/, '') };
  } catch (e) {
    // 파이썬 오류 메시지에서 앱 내부 줄은 빼고 학생 코드 부분만 보여 준다
    const lines = String(e.message).split('\n');
    const keep = []; let skip = false;
    for (const l of lines) {
      if (/^\s+File "/.test(l)) { skip = !l.includes('<코드>'); if (skip) continue; }
      else if (skip && /^\s{4}/.test(l)) continue;
      else skip = false;
      if (!/^\s*\^+\s*$/.test(l)) keep.push(l);
    }
    return { out: (out + keep.join('\n')).trim(), err: true };
  }
}

// ───────── 퀴즈 ─────────
function renderQuiz(c) {
  $('#title').textContent = `${chLabel(c)} ${c.no === '부록' ? '종합 실력 점검' : '총정리 퀴즈'}`;
  const picked = c.quiz.map(() => null);
  const ci = CH.indexOf(c), nextCh = CH[ci + 1];
  view.innerHTML = `<div class="stack"><div class="lhead"><span class="k">${chLabel(c)} ${c.title}</span><h2>📝 ${c.no === '부록' ? '종합 실력 점검' : '총정리 퀴즈'} ${c.quiz.length}문제</h2></div>
    <div class="card quiz" id="qz"></div>
    <div class="nav2"><button data-go="#/c/${c.no}">‹ 목차</button>${nextCh ? `<button class="pri" data-go="#/c/${nextCh.no}">다음 장 ›</button>` : '<button class="pri" data-go="#/">홈</button>'}</div></div>`;
  view.querySelectorAll('[data-go]').forEach(b => b.onclick = () => go(b.dataset.go));
  const box = $('#qz');
  const draw = () => {
    const answered = picked.every(p => p !== null), right = picked.filter((p, k) => p === c.quiz[k].a).length;
    box.innerHTML = c.quiz.map((q, k) => `<div class="qq"><p>Q${k + 1}. ${q.q}</p><div class="qo">${q.o.map((o, j) => {
      let cls = ''; if (picked[k] !== null) { if (j === q.a) cls = 'right'; else if (j === picked[k]) cls = 'wrong'; }
      return `<button data-q="${k}" data-o="${j}" class="${cls}" ${picked[k] !== null ? 'disabled' : ''}>${'①②③④⑤'[j]} ${o}</button>`;
    }).join('')}</div>${picked[k] !== null ? `<div class="qe ${picked[k] === q.a ? 'ok' : 'no'}">${picked[k] === q.a ? '⭕ 정답!' : '❌ 아쉬워요.'} ${q.e}</div>` : ''}</div>`).join('') +
      (answered ? `<div class="qres">${right === c.quiz.length ? '🎉 모두 맞혔어요! 진도에 기록했어요' : `${right} / ${c.quiz.length} 정답`}</div>
        ${right === c.quiz.length ? '' : '<div style="margin-top:8px"><button class="btnw" id="retry">↺ 틀린 문제 다시 풀기</button></div>'}` : '');
    box.querySelectorAll('[data-q]').forEach(b => b.onclick = () => {
      picked[+b.dataset.q] = +b.dataset.o; draw();
      if (picked.every((p, k) => p === c.quiz[k].a) && !prog['q/' + c.no]) { prog['q/' + c.no] = Date.now(); saveProg(); toast('🎉 퀴즈 완료!'); }
    });
    const r = $('#retry'); if (r) r.onclick = () => { picked.forEach((p, k) => { if (p !== c.quiz[k].a) picked[k] = null; }); draw(); };
  };
  draw();
}

// ───────── 실습장: 자유롭게 코드 쓰고 실행 ─────────
const PLAY_KEY = 'py-learn-playground';
function renderPlay() {
  $('#title').textContent = '실습장';
  let saved = '# 여기에 자유롭게 코드를 써 보세요\nname = input("이름: ")\nfor i in range(3):\n    print(f"{i + 1}. 안녕, {name}!")\n';
  try { saved = localStorage.getItem(PLAY_KEY) || saved; } catch (e) {}
  view.innerHTML = `<div class="stack">
    <p class="muted" style="margin:0;font-size:14px">배운 내용을 직접 써 보는 연습장이에요. 쓴 코드는 이 폰에 자동 저장돼요. <b>input()</b> 은 입력 창으로 받아요.</p>
    <div class="cb" id="pg"></div>
    <div class="status" id="pst"></div></div>`;
  const ex = { code: saved, out: null };
  codeBox($('#pg'), ex, { blank: true });
  const ta = $('#pg textarea');
  ta.addEventListener('input', () => { try { localStorage.setItem(PLAY_KEY, ta.value); } catch (e) {} });
  $('#pg .rs').onclick = () => { if (confirm('실습장을 처음 예제로 되돌릴까요?')) { try { localStorage.removeItem(PLAY_KEY); } catch (e) {} renderPlay(); } };
  $('#pst').textContent = pyReady ? '파이썬 준비 완료' : '처음 ▶ 실행을 누르면 파이썬을 준비해요 (한 번만 인터넷 필요)';
}

// ───────── 사용법 ─────────
function renderHelp() {
  $('#title').textContent = '사용법';
  const installed = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  const sec = (t, b) => `<div class="card help"><h3>${t}</h3>${b}</div>`;
  view.innerHTML = `<div class="stack">
    ${sec('📚 이렇게 공부해요', `<ol>
      <li><b>학습</b> 탭에서 1장부터 차례로 엽니다. 홈의 <b>▶ 이어서 학습하기</b>를 누르면 안 본 곳으로 바로 가요.</li>
      <li>절을 열면 <b>읽음(✓)</b>으로 기록돼요. 장 끝의 <b>총정리 퀴즈</b>를 모두 맞히면 그 장이 완료됩니다.</li>
      <li>마지막 <b>부록</b>에는 AI 활용법, 내장 함수·표준 라이브러리 표, <b>종합 실력 점검 20문제</b>가 있어요.</li></ol>`)}
    ${sec('▶ 코드 실행하기', `<ul>
      <li>검은 코드 상자는 <b>직접 고칠 수 있어요.</b> 숫자나 글자를 바꾸고 <b>▶ 실행</b>을 눌러 보세요.</li>
      <li>처음 실행할 때 브라우저 안에 파이썬을 준비해요 (약 10MB, 10초 정도). 그다음부터는 <b>인터넷 없이도</b> 실행돼요.</li>
      <li><b>↺</b> 는 원래 코드로 되돌리기, <b>복사</b>는 코드 복사예요.</li>
      <li><code>input()</code> 이 있는 코드는 <b>입력 창</b>이 떠요. 처음 보이는 '실행 결과 (예시)'는 교안과 같은 입력값으로 실행한 결과예요.</li>
      <li>무한 반복은 <b>10초</b> 뒤 자동으로 멈춰요.</li>
      <li>9~11장의 파일 예제는 앱 안의 임시 폴더에 저장돼요. 앞 예제부터 차례로 실행하세요. (앱을 다시 열면 초기화)</li>
      <li>📄 <b>파일</b> 상자(calc.py 등)는 실행 대신 모듈로 저장돼서, 같은 장의 다른 예제에서 <code>import</code> 할 수 있어요.</li></ul>`)}
    ${sec('🐍 실습장', '<ul><li>아래 <b>실습장</b> 탭에서 아무 코드나 써서 실행해 보세요. 쓴 코드는 자동 저장돼요.</li></ul>')}
    ${sec('📲 앱으로 설치 · 오프라인', `<ul>
      <li>${installed ? '✅ 지금 <b>앱으로 실행 중</b>이에요.' : 'Chrome: 위쪽 <b>[설치]</b> 안내 또는 <b>⋮ → 앱 설치</b> · 아이폰 Safari: <b>공유 → 홈 화면에 추가</b>'}</li>
      <li>카카오톡에서 링크를 열면 자동으로 Chrome(아이폰은 Safari)으로 넘어가요.</li>
      <li>새 내용이 추가되면 인터넷이 될 때 앱을 열면 <b>자동으로 업데이트</b>돼요. 진도는 그대로 남아요.</li></ul>`)}
    ${sec('💾 진도 기록', `<ul><li>진도는 <b>이 폰의 이 브라우저</b>에만 저장돼요.</li></ul>
      <div style="margin-top:10px"><button class="btnw" id="reset">진도 기록 지우기</button></div>`)}
    <p class="muted" style="text-align:center;font-size:13px">${CH.length - 1}개 장 + 부록 · 예제 ${CODE.length}개 · 퀴즈 ${CH.reduce((a, c) => a + c.quiz.length, 0)}문제<br>
      <a href="https://github.com/sinaboro/python-learning-app" target="_blank" rel="noopener">교안 PDF · 실습코드 (GitHub)</a></p>
  </div>`;
  $('#reset').onclick = () => { if (confirm('진도 기록을 모두 지울까요?')) { prog = {}; saveProg(); toast('진도 기록을 지웠어요'); } };
}

// ───────── 앱 설치 · 오프라인 ─────────
// 카카오톡 안에서 열면 바깥 브라우저로 넘기고, Chrome 은 [설치] 버튼, 아이폰은 홈 화면 추가 안내
if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
(() => {
  const bar = $('#inst'), msg = $('#instMsg'), btn = $('#instGo');
  const ua = navigator.userAgent;
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  const kakao = /KAKAOTALK/i.test(ua), android = /Android/i.test(ua);
  const ios = /iP(hone|ad|od)/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const inApp = kakao || /NAVER|Instagram|FBAN|FBAV|Line\//i.test(ua);
  const DISMISS = 'py-learn-install-dismissed';
  const show = (text, label, onGo) => { msg.innerHTML = text; btn.hidden = !label; btn.textContent = label || ''; btn.onclick = onGo || null; bar.hidden = false; };
  const dismissed = () => { try { return localStorage.getItem(DISMISS) === '1'; } catch (e) { return false; } };
  $('#instX').onclick = () => { bar.hidden = true; try { localStorage.setItem(DISMISS, '1'); } catch (e) {} };
  if (standalone) return;
  const openOutside = () => {
    const url = location.href.split('#')[0];
    if (kakao) location.href = 'kakaotalk://web/openExternal?url=' + encodeURIComponent(url);
    else if (android) location.href = `intent://${location.host}${location.pathname}#Intent;scheme=https;package=com.android.chrome;end`;
  };
  if (inApp) {
    show(ios ? '📲 앱으로 설치하려면 <b>Safari</b>에서 열어야 해요.' : '📲 앱으로 설치하려면 <b>Chrome</b>에서 열어야 해요.', ios ? 'Safari로 열기' : 'Chrome으로 열기', openOutside);
    let jumped = false;
    try { jumped = sessionStorage.getItem('kakaoJump') === '1'; sessionStorage.setItem('kakaoJump', '1'); } catch (e) {}
    if (kakao && !jumped) setTimeout(openOutside, 300);
    return;
  }
  let deferred = null;
  addEventListener('beforeinstallprompt', e => {
    e.preventDefault(); deferred = e;
    if (dismissed()) return;
    show('📲 홈 화면에 <b>앱으로 설치</b>하면 인터넷 없이도 공부할 수 있어요.', '설치', async () => {
      deferred.prompt();
      const r = await deferred.userChoice.catch(() => ({}));
      deferred = null; bar.hidden = true;
      if (r.outcome === 'accepted') toast('설치했어요. 홈 화면의 파이썬 아이콘으로 여세요.');
    });
  });
  addEventListener('appinstalled', () => { bar.hidden = true; });
  if (ios && !dismissed()) show('📲 아래 <b>공유 버튼</b> → <b>홈 화면에 추가</b>를 누르면 앱처럼 쓸 수 있어요.');
})();

route();
