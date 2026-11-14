"""ASHE - single-file desktop build (generated from the multi-file project).

Educational prototype, not a certified medical device.
"""

from __future__ import annotations

import os

import sys as _sys
if _sys.stdout is None:
    _sys.stdout = open(os.devnull, "w", encoding="utf-8")
if _sys.stderr is None:
    _sys.stderr = open(os.devnull, "w", encoding="utf-8")


# ---- embedded frontend (extracted to a temp dir at start) ----

FRONTEND = {
 'index.html': '''<!doctype html>
<html lang="en" data-theme="earth" data-tod="day">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ASHE</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header>
  <h1>ASHE</h1>
  <span class="pill" id="connPill">connecting…</span>
  <span class="pill" id="modePill">Demo mode</span>
  <span class="sp"></span>
  <button id="themeBtn">Space theme</button>
  <button id="langBtn">عربي / EN</button>
  <a href="/console" target="_blank"><button>Ground console</button></a>
</header>

<section class="welcome" id="welcome" aria-live="polite">
  <div class="w-line"><span class="w-hello" id="wHello">Welcome</span><span class="w-name" id="wName">Astronaut</span></div>
  <div class="w-greet"><span id="wGreetIcon">☀️</span> <span id="wGreet">Good Morning</span></div>
</section>

<main>
  <!-- ============ LEFT: profile + camera + companion ============ -->
  <div class="col">
    <!-- Profile hero card -->
    <div class="card hero" id="heroCard">
      <div class="avatar" id="avatar" aria-label="Astronaut">
        <svg viewBox="0 0 120 120" role="img" aria-hidden="true">
          <defs>
            <radialGradient id="avBg" cx="50%" cy="35%" r="75%"><stop offset="0" stop-color="var(--accent)" stop-opacity=".35"/><stop offset="1" stop-color="var(--accent2)" stop-opacity=".18"/></radialGradient>
            <linearGradient id="avVisor" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2b3f6b"/><stop offset=".55" stop-color="#10182e"/><stop offset="1" stop-color="#3a1f4a"/></linearGradient>
            <clipPath id="avClip"><circle cx="60" cy="60" r="58"/></clipPath>
          </defs>
          <g clip-path="url(#avClip)">
            <rect width="120" height="120" fill="url(#avBg)"/>
            <circle cx="22" cy="24" r="1.6" fill="#fff" opacity=".9"/><circle cx="98" cy="18" r="1.2" fill="#fff" opacity=".8"/><circle cx="104" cy="52" r="1.4" fill="#fff" opacity=".7"/><circle cx="14" cy="64" r="1" fill="#fff" opacity=".7"/><circle cx="86" cy="36" r="1" fill="#fff" opacity=".6"/>
            <!-- body -->
            <path d="M18 124 Q20 86 60 84 Q100 86 102 124Z" fill="#e9edf5"/>
            <path d="M30 124 Q32 96 60 94 Q88 96 90 124Z" fill="#cfd7e6"/>
            <rect x="46" y="100" width="28" height="16" rx="4" fill="#fff" stroke="#b7c2d8" stroke-width="1.5"/>
            <circle cx="53" cy="108" r="3" fill="#e0524a"/><circle cx="62" cy="108" r="3" fill="#4da3ff"/><rect x="67" y="106" width="4" height="4" rx="1" fill="#46d39a"/>
            <!-- neck ring -->
            <ellipse cx="60" cy="84" rx="25" ry="7" fill="#f4f6fb" stroke="#b7c2d8" stroke-width="2"/>
            <!-- helmet -->
            <circle cx="60" cy="50" r="33" fill="#f6f8fc" stroke="#b7c2d8" stroke-width="2.5"/>
            <rect x="35" y="36" width="50" height="34" rx="17" fill="url(#avVisor)" stroke="#8f9cb8" stroke-width="2"/>
            <path d="M42 44 Q52 38 66 41" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".55"/>
            <ellipse cx="73" cy="60" rx="7" ry="3" fill="#fff" opacity=".12"/>
            <!-- ear comms -->
            <rect x="24" y="44" width="7" height="14" rx="3.5" fill="#c3cde0" stroke="#8f9cb8" stroke-width="1.5"/>
            <rect x="89" y="44" width="7" height="14" rx="3.5" fill="#c3cde0" stroke="#8f9cb8" stroke-width="1.5"/>
          </g>
        </svg>
      </div>
      <div class="hero-name" id="heroName">Astronaut</div>
      <div class="hero-sub note" id="heroSub">Crew · Mission ASHE</div>
      <div class="hero-actions">
        <button class="rbtn" id="pfMute" title="Mute voice chat" aria-pressed="false">🔊</button>
        <button class="rbtn" id="pfWall" title="Wallpapers · الخلفيات">🖼</button>
        <button class="rbtn" id="pfEdit" title="Edit medical card · تعديل البطاقة">✎</button>
        <button class="rbtn" id="pfTheme" title="Switch theme · تغيير الثيم">🌓</button>
      </div>
      <div class="hero-actions wide">
        <button class="rect primary" id="pfMedBtn">🩺 Medical Card</button>
        <a href="/console" target="_blank" class="rect-a"><button class="rect">Ground console</button></a>
      </div>
    </div>

    <!-- Medical Card -->
    <div class="card" id="medCard">
      <h2>Medical Card · البطاقة الطبية</h2>
      <div id="medView">
        <dl class="med">
          <div><dt>Name · الاسم</dt><dd id="mName">–</dd></div>
          <div><dt>Medical conditions · الحالة الطبية / الأمراض</dt><dd id="mCond">–</dd></div>
          <div class="two">
            <div><dt>Height · الطول</dt><dd id="mH">–</dd></div>
            <div><dt>Weight · الوزن</dt><dd id="mW">–</dd></div>
          </div>
          <div id="mBmiRow" class="hidden"><dt>BMI (info only)</dt><dd id="mBmi">–</dd></div>
        </dl>
        <div class="row"><button class="rect primary" id="medEdit">✎ Edit card</button></div>
      </div>
      <form id="medForm" class="hidden" autocomplete="off">
        <label>Name · الاسم<input type="text" id="fName" maxlength="40" placeholder="e.g. Ahmed Hassan" dir="auto"></label>
        <label>Medical conditions / chronic diseases / past conditions · الحالة الطبية والأمراض المزمنة أو السابقة
          <textarea id="fCond" rows="3" maxlength="400" placeholder="e.g. Asthma (mild), penicillin allergy, previous knee surgery 2021 · or “None”" dir="auto"></textarea></label>
        <div class="two">
          <label>Height · الطول (cm)<input type="number" id="fH" min="50" max="260" step="0.5" inputmode="decimal" placeholder="175"></label>
          <label>Weight · الوزن (kg)<input type="number" id="fW" min="20" max="300" step="0.1" inputmode="decimal" placeholder="72"></label>
        </div>
        <div class="note" id="medErr"></div>
        <div class="row"><button type="submit" class="rect primary">Save · حفظ</button><button type="button" class="rect" id="medCancel">Cancel · إلغاء</button></div>
        <p class="note">Saved on this device only. It is not sent to Earth unless you share it with the flight surgeon.</p>
      </form>
    </div>

    <div class="card">
      <h2>Camera</h2>
      <div class="cam">
        <video id="video" playsinline muted></video>
        <canvas id="overlay"></canvas>
        <div class="ph" id="camPh">Press “Enable camera &amp; mic”.<br>Sit still with a neutral face for ~5 seconds so ASHE can learn your normal.</div>
      </div>
      <div class="row" style="margin-top:10px">
        <button class="primary" id="enableBtn">Enable camera &amp; mic</button>
        <span class="note" id="camStatus"></span>
      </div>
      <div class="vis-stats">
        <div class="stat"><b id="vBlink">–</b><span>blinks/min</span></div>
        <div class="stat"><b id="vPerclos">–</b><span>eye closure</span></div>
        <div class="stat"><b id="vYawn">–</b><span>yawns</span></div>
        <div class="stat"><b id="vHr">–</b><span>face pulse (est.)</span></div>
        <div class="stat"><b id="vPitch">–</b><span>voice pitch Hz</span></div>
        <div class="stat"><b id="vTone">–</b><span>voice tone</span></div>
      </div>
      <p class="note">Face pulse (rPPG) needs steady light and little movement. It is an estimate, not a medical measurement.</p>
    </div>

    <div class="card">
      <div class="row">
        <div class="orb off" id="orb"></div>
        <div>
          <h2 style="margin:0">Companion · voice chat (always on)</h2>
          <div class="note" id="orbStatus">Off</div>
        </div>
        <button class="rect mute-btn" id="muteBtn" aria-pressed="false" title="Mute voice chat">🔊 Voice on · الصوت شغال</button>
      </div>
      <div class="mute-note hidden" id="muteNote" role="alert"></div>
      <div class="chat" id="chat"></div>
      <div class="chat-in">
        <input type="text" id="chatIn" placeholder="Type instead of speaking…" dir="auto">
        <button id="chatSend">Send</button>
      </div>
    </div>
  </div>

  <!-- ============ CENTER: tabs ============ -->
  <div class="col">
    <div class="card">
      <div class="tabs">
        <button class="tab on" data-view="dash">Dashboard</button>
        <button class="tab" data-view="ex">Exercise &amp; medical</button>
        <button class="tab" data-view="games">Games</button>
        <button class="tab" data-view="sens">Sensors</button>
      </div>

      <!-- Dashboard -->
      <div class="view on" id="v-dash">
        <div class="score">
          <div class="ring" id="ring"><div id="wScore">–</div></div>
          <div class="bars">
            <div class="bar">Wellness <span id="wTxt"></span></div>
            <div class="bar">Fatigue<i><b id="fatBar"></b></i></div>
            <div class="bar">Stress<i><b id="strBar"></b></i></div>
            <div class="note" id="baseNote">Learning your baseline…</div>
          </div>
        </div>
        <div class="grid" id="metrics" style="margin-top:14px"></div>
        <h2 style="margin-top:16px">Demo scenarios (for the presentation)</h2>
        <div class="scen" id="scen"></div>
      </div>

      <!-- Exercise -->
      <div class="view" id="v-ex">
        <div class="row"><button class="primary" id="planBtn">Today’s workout plan</button></div>
        <div class="plan" id="plan" style="margin-top:10px"></div>
        <h2 style="margin-top:16px">Ask the knowledge base</h2>
        <div class="chat-in"><input type="text" id="kbIn" placeholder="e.g. my back hurts / ظهري بيوجعني / how to sleep better" dir="auto"><button id="kbBtn">Ask</button></div>
        <div id="kbOut"></div>
        <p class="note">Educational prototype. Answers come from a small sample knowledge base with cited sources. Entries are marked “not clinician-reviewed” until a doctor or physical therapist verifies them. Not a diagnosis.</p>
      </div>

      <!-- Games -->
      <div class="view" id="v-games">
        <div class="row">
          <button data-game="react">Reaction test</button>
          <button data-game="breath">Guided breathing</button>
          <button data-game="memory">Memory</button>
          <button data-game="sudoku">Sudoku</button>
        </div>
        <div class="note" style="margin-top:6px">Single-player games · ألعاب فردية</div>
        <div style="margin-top:12px" id="gameBox"><div class="game-stage">Pick a short game (2–5 min). The reaction test also helps estimate fatigue.</div></div>
        <div class="note" id="gameNote"></div>
      </div>

      <!-- Sensors -->
      <div class="view" id="v-sens">
        <div class="row">
          <label class="switch"><input type="checkbox" id="liveSw"> Live mode (use real sensor readings when available)</label>
        </div>
        <h2 style="margin-top:14px">What is shared with Earth</h2>
        <div class="row" id="consent"></div>
        <p class="note">Only summaries are sent, never audio or video. Psychological and genetic data are off until you consent.</p>
        <h2 style="margin-top:14px">Sensor connectors</h2>
        <div class="conn" id="conn"></div>
        <p class="note">Any device can post readings to <code>POST /api/sensor</code>. “planned” connectors show how they would attach; only the generic HTTP path is implemented in this prototype.</p>
      </div>
    </div>
  </div>

  <!-- ============ RIGHT: alerts + genetics ============ -->
  <div class="col">
    <div class="card"><h2>Alerts</h2><div id="alerts"><div class="note">No alerts.</div></div></div>
    <div class="card"><h2>Escalation to Earth</h2><div id="tickets"><div class="note">No open requests.</div></div></div>
    <div class="card">
      <h2>Genetic risk (sample genome)</h2>
      <div id="gen"></div>
      <p class="note">Probabilities, not a diagnosis. Sample data, adjusted by live readings.</p>
    </div>
  </div>
</main>

<script type="module" src="/app.js"></script>
<script src="/crew.js"></script>
<script src="/profile.js"></script>
<script src="/extras.js"></script>
</body>
</html>
''',
 'console.html': '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ASHE · Flight Surgeon Console</title>
<style>
:root{--bg:#0b0f14;--panel:#111821;--line:#1f2a38;--text:#d7e0ea;--muted:#7d8da1;--ok:#37c28a;--warn:#e0a030;--bad:#e5534b;--accent:#4aa3ff;--mono:ui-monospace,Consolas,"Courier New",monospace}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px system-ui,Segoe UI,sans-serif}
header{display:flex;gap:14px;align-items:center;padding:10px 16px;border-bottom:1px solid var(--line);background:#0e141c}
header h1{font-size:15px;margin:0;letter-spacing:1px;font-weight:600}
.sp{flex:1}.pill{font:12px var(--mono);padding:3px 9px;border:1px solid var(--line);border-radius:4px;color:var(--muted)}
.pill.ok{color:var(--ok);border-color:var(--ok)}.pill.bad{color:var(--bad);border-color:var(--bad)}
.banner{background:#16212e;border-bottom:1px solid var(--line);padding:6px 16px;font-size:12px;color:var(--muted)}
main{display:grid;grid-template-columns:1.2fr 1fr;gap:12px;padding:12px;max-width:1500px;margin:auto}
@media(max-width:1000px){main{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:12px}
.card h2{margin:0 0 10px;font-size:11px;text-transform:uppercase;letter-spacing:1.2px;color:var(--muted);font-weight:600}
table{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:13px}
td,th{padding:5px 6px;border-bottom:1px solid var(--line);text-align:left}th{color:var(--muted);font-weight:500}
td.crit{color:var(--bad)}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
button{background:#182231;border:1px solid var(--line);color:var(--text);padding:6px 11px;border-radius:4px;cursor:pointer}
button:hover{border-color:var(--accent)}button.primary{background:var(--accent);color:#04121f;border-color:transparent}
input[type=text],input[type=range]{background:#0c121a;border:1px solid var(--line);color:var(--text);border-radius:4px;padding:6px}
input[type=text]{flex:1;min-width:160px}
.ticket{border-left:3px solid var(--bad);background:#141c27;padding:8px 10px;margin-bottom:8px;border-radius:3px}
.ticket.acknowledged{border-color:var(--ok)}
.mono{font-family:var(--mono);font-size:12px;color:var(--muted)}
.w{font-size:34px;font-weight:700;font-family:var(--mono)}
.kv{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;font-family:var(--mono);font-size:13px}
.kv span:nth-child(odd){color:var(--muted)}
</style>
</head>
<body>
<header>
  <h1>FLIGHT SURGEON CONSOLE</h1>
  <span class="pill" id="conn">offline</span>
  <span class="pill" id="linkPill">link –</span>
  <span class="sp"></span>
  <span class="mono" id="clock"></span>
</header>
<div class="banner" id="policy">Advisory only. Read-only: no control over life-support or any ship system.</div>
<main>
  <div class="col">
    <div class="card">
      <h2>Crew telemetry (delayed copy)</h2>
      <div class="row" style="margin-bottom:10px"><span class="w" id="wScore">–</span><div class="mono" id="age">waiting for first packet…</div></div>
      <table><thead><tr><th>Metric</th><th>Value</th><th>Source</th></tr></thead><tbody id="vitals"></tbody></table>
      <h2 style="margin-top:14px">Crew-shared status</h2>
      <div class="kv" id="shared"></div>
    </div>
    <div class="card" style="margin-top:12px">
      <h2>Recent onboard alerts (as reported)</h2>
      <div id="alerts" class="mono">–</div>
    </div>
  </div>
  <div class="col">
    <div class="card">
      <h2>Escalations</h2>
      <div id="tickets"><div class="mono">None received.</div></div>
    </div>
    <div class="card" style="margin-top:12px">
      <h2>Message to crew (also delayed)</h2>
      <div class="row"><input type="text" id="msg" placeholder="Type a message to the astronaut…"><button class="primary" id="sendMsg">Send</button></div>
      <div class="mono" id="sent" style="margin-top:8px"></div>
    </div>
    <div class="card" style="margin-top:12px">
      <h2>Link simulation</h2>
      <div class="row">
        <span class="mono">Delay (demo-compressed)</span>
        <input type="range" id="delay" min="0" max="60" value="8"> <span class="mono" id="delayLbl">8 s</span>
      </div>
      <div class="mono" style="margin-top:6px">Real Earth–Mars one-way light time is roughly 4–24 minutes. The ship-side AI acts first; Earth sees the delayed copy.</div>
      <div class="mono" id="flight" style="margin-top:6px"></div>
    </div>
    <div class="card" style="margin-top:12px">
      <h2>Crew consent (set by the astronaut)</h2>
      <div class="kv" id="consent"></div>
    </div>
  </div>
</main>
<script>
const $=s=>document.querySelector(s);
const esc=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
let ws; const shownAck=new Set();
function send(o){ if(ws&&ws.readyState===1) ws.send(JSON.stringify(o)); }
function connect(){
  ws=new WebSocket(`${location.protocol==="https:"?"wss":"ws"}://${location.host}/ws/ground`);
  ws.onopen=()=>{$("#conn").textContent="connected";$("#conn").className="pill ok"};
  ws.onclose=()=>{$("#conn").textContent="offline";$("#conn").className="pill bad";setTimeout(connect,1500)};
  ws.onmessage=e=>{const m=JSON.parse(e.data); if(m.type==="ground") render(m)};
}
function render(g){
  $("#policy").textContent=g.policy;
  const lp=$("#linkPill"); lp.textContent=`link ${g.link.up?"UP":"DOWN"} · delay ${g.link.delay_s}s (≈${g.link.one_way_label_min} min real) · in flight ${g.link.in_flight}`; lp.className="pill "+(g.link.up?"ok":"bad");
  const L=g.latest;
  if(L){
    $("#wScore").textContent=L.wellness!=null?Math.round(L.wellness):"–";
    $("#age").textContent=`Data age: ${g.age_s.toFixed(0)} s (includes link delay)`;
    $("#vitals").innerHTML=L.vitals?Object.entries(L.vitals).map(([k,v])=>`<tr><td>${esc(k)}</td><td>${esc(v.value)} ${esc(v.unit)}</td><td>${esc(v.source)}</td></tr>`).join(""):'<tr><td colspan="3">Vitals not shared</td></tr>';
    const ps=L.psychological; $("#shared").innerHTML=
      `<span>Psychological</span><span>${typeof ps==="object"?`fatigue ${ps.fatigue.toFixed(0)} · stress ${ps.stress.toFixed(0)}`:esc(ps)}</span>`+
      `<span>Genetic</span><span>${typeof L.genetic==="object"?L.genetic.map(x=>esc(x.name)+" "+x.band).join("; "):esc(L.genetic)}</span>`;
    $("#alerts").innerHTML=(L.alerts&&L.alerts.length)?L.alerts.map(a=>"• "+esc(a)).join("<br>"):"None reported.";
  }
  $("#consent").innerHTML=Object.entries(g.consent).map(([k,v])=>`<span>${esc(k)}</span><span style="color:${v?"var(--ok)":"var(--bad)"}">${v?"shared":"withheld"}</span>`).join("");
  const t=$("#tickets"); const list=g.tickets.filter(x=>g.escalations.some(e=>e.id===x.id));
  t.innerHTML=list.length?"":'<div class="mono">None received.</div>';
  list.slice().reverse().forEach(x=>{
    const d=document.createElement("div"); d.className="ticket "+x.status;
    d.innerHTML=`<b>${esc(x.id)}</b> · ${esc(x.status)}<div class="mono">${esc(x.reason)}</div><div class="mono">wellness ${Math.round(x.brief.wellness)} · fatigue ${Math.round(x.brief.fatigue)} · stress ${esc(typeof x.brief.stress==="number"?Math.round(x.brief.stress):x.brief.stress)}</div><div class="mono">Suggested: ${esc(x.brief.suggested_contact)}</div>`;
    if(x.status==="open"){const b=document.createElement("button");b.textContent="Acknowledge";b.style.marginTop="6px";b.onclick=()=>send({type:"ack",id:x.id});d.appendChild(b);}
    t.appendChild(d);
  });
  $("#flight").textContent=g.downlink.length?`Last message sent ${new Date(g.downlink[g.downlink.length-1].sent_at*1000).toLocaleTimeString()}`:"";
}
$("#sendMsg").onclick=()=>{const v=$("#msg").value.trim();if(!v)return;send({type:"to_ship",text:v});$("#sent").textContent="Sent: "+v+" (arrives after the link delay)";$("#msg").value=""};
$("#delay").oninput=e=>{const s=+e.target.value;$("#delayLbl").textContent=s+" s";fetch("/api/ground/delay",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({seconds:s,label_minutes:Math.round(s/60*24)})})};
setInterval(()=>{$("#clock").textContent=new Date().toISOString().replace("T"," ").slice(0,19)+" UTC"},1000);
connect();
</script>
</body>
</html>
''',
 'app.js': '''// ASHE ship app: WebSocket state, camera (MediaPipe FaceLandmarker), voice, companion, games.
const $ = (s) => document.querySelector(s);
const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

let ws = null, lang = "ar", enabled = false, speaking = false, lastSpeechEnd = 0, speakStart = 0;
let calm = 0;

/* ------------------------------------------------------------------ socket */
function send(obj) { if (ws && ws.readyState === 1) ws.send(JSON.stringify(obj)); }
function connect() {
  ws = new WebSocket(`${location.protocol === "https:" ? "wss" : "ws"}://${location.host}/ws`);
  ws.onopen = () => { const p = $("#connPill"); p.textContent = "connected"; p.className = "pill live"; send({ type: "lang", lang }); };
  ws.onclose = () => { const p = $("#connPill"); p.textContent = "reconnecting…"; p.className = "pill bad"; setTimeout(connect, 1500); };
  ws.onmessage = (ev) => {
    let m; try { m = JSON.parse(ev.data); } catch { return; }
    if (m.type === "state") renderState(m);
    else if (m.type === "speak") { if (m.priority === "critical") emergencyUnmute(m.text); companionSays(m.text, m.priority); }
    else if (m.type === "ground_msg") { addMsg("Earth: " + m.text, "earth"); speak(m.text, "normal"); }
    else if (m.type === "kb") renderKb(m);
    else if (m.type === "action") runAction(m.name);
  };
}

/* ------------------------------------------------------------------- chat */
function addMsg(text, cls) {
  const c = $("#chat"); const d = el("div", "msg " + cls); d.textContent = text; d.dir = "auto";
  c.appendChild(d); c.scrollTop = c.scrollHeight;
  while (c.children.length > 60) c.removeChild(c.firstChild);
}
function companionSays(text, priority) { addMsg(text, "ai"); speak(text, priority); }
function userSays(text) { if (!text.trim()) return; addMsg(text, "me"); send({ type: "speech", text, lang }); }
$("#chatSend").onclick = () => { const i = $("#chatIn"); userSays(i.value); i.value = ""; };
$("#chatIn").addEventListener("keydown", (e) => { if (e.key === "Enter") $("#chatSend").click(); });

/* ------------------------------------------------- voice mute + alert override */
// The companion's always-on voice chat can be muted to avoid annoyance. SAFETY RULE: any danger /
// emergency alert force-unmutes immediately (and sounds an alarm tone even if no TTS voice exists).
let muted = false;
const seenAlerts = new Set(); let alertsPrimed = false; const prevCrit = {};
function paintMute(why) {
  const b = $("#muteBtn"), h = $("#pfMute"), o = $("#orb"), st = $("#orbStatus");
  [b, h].forEach((x) => { if (!x) return; x.classList.toggle("on", muted); x.setAttribute("aria-pressed", String(muted)); x.title = muted ? "Unmute voice chat · إلغاء الكتم" : "Mute voice chat · كتم الصوت"; });
  if (b) b.textContent = muted ? "🔇 Muted · مكتوم" : "🔊 Voice on · الصوت شغال";
  if (h) h.textContent = muted ? "🔇" : "🔊";
  if (o) o.classList.toggle("muted", muted);
  if (st) st.textContent = muted ? "Muted: alerts will unmute automatically · أي إنذار هيفتح الصوت" : (enabled ? "Listening" : "Off");
  const n = $("#muteNote"); if (n) { n.textContent = why || ""; n.classList.toggle("hidden", !why); }
}
function setMuted(v, why) {
  v = !!v; if (v === muted) { paintMute(why); return; }
  muted = v;
  if (muted) {
    try { speechSynthesis.cancel(); } catch {}
    speaking = false; lastSpeechEnd = Date.now(); $("#orb").classList.remove("speaking");
    recWanted = false; try { rec && rec.stop(); } catch {}          // stop listening too while muted
  } else if (enabled) { setTimeout(() => { if (!muted && enabled) startRecognition(); }, 350); }
  try { localStorage.setItem("ac-muted", muted ? "1" : "0"); } catch {}
  paintMute(why);
}
function alarmTone() {                                                // audible even when no speech voice is installed
  try {
    const ctx = audioCtx2();
    [0, 0.45, 0.9].forEach((t) => { tone(880, 0.2, "square", 0.12, t); tone(660, 0.2, "square", 0.12, t + 0.2); });
  } catch {}
}
function emergencyUnmute(text) {
  const was = muted;
  if (muted) setMuted(false, "⚠ Voice chat was unmuted automatically because of an emergency alert. · اتفتح الصوت تلقائيًا بسبب إنذار طارئ");
  if (was) alarmTone();
  document.dispatchEvent(new CustomEvent("ashe-emergency", { detail: { text, wasMuted: was } }));
}
$("#muteBtn").onclick = () => setMuted(!muted);
document.addEventListener("ashe-toggle-mute", () => setMuted(!muted));
try { if (localStorage.getItem("ac-muted") === "1") { muted = true; } } catch {}

/* -------------------------------------------------------------------- TTS */
function pickVoice() {
  const vs = speechSynthesis.getVoices();
  const want = lang === "ar" ? "ar" : "en";
  return vs.find((v) => v.lang.toLowerCase().startsWith(want)) || null;
}
function speak(text, priority = "normal") {
  if (priority === "critical" && muted) emergencyUnmute(text);   // safety: an alarm is never swallowed by mute
  if (muted) return;                                             // muted: text still shows in the chat, no voice
  if (!("speechSynthesis" in window)) return;
  if (speaking && priority !== "critical") return;     // never queue: drop instead of piling up
  if (priority === "critical") speechSynthesis.cancel();
  const v = pickVoice();
  if (!v) { $("#orbStatus").textContent = enabled ? "Listening (no " + (lang === "ar" ? "Arabic" : "English") + " voice installed: text only)" : "Off"; return; }
  const u = new SpeechSynthesisUtterance(text); u.voice = v; u.lang = v.lang; u.rate = 0.98;
  u.onstart = () => { speaking = true; speakStart = Date.now(); $("#orb").classList.add("speaking"); };
  const done = () => { speaking = false; lastSpeechEnd = Date.now(); $("#orb").classList.remove("speaking"); };
  u.onend = done; u.onerror = done;
  speechSynthesis.speak(u);
}
setInterval(() => { if (speaking && Date.now() - speakStart > 25000) { speechSynthesis.cancel(); speaking = false; lastSpeechEnd = Date.now(); } }, 2000); // un-stick
speechSynthesis && (speechSynthesis.onvoiceschanged = () => {});

/* ------------------------------------------------------------ recognition */
let rec = null, recWanted = false;
function startRecognition() {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { $("#orbStatus").textContent = "Speech recognition needs Chrome or Edge. You can type instead."; return; }
  rec = new SR(); rec.continuous = true; rec.interimResults = false; rec.maxAlternatives = 1;
  rec.lang = lang === "ar" ? "ar-EG" : "en-US";
  rec.onresult = (ev) => {
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      const r = ev.results[i]; if (!r.isFinal) continue;
      const text = r[0].transcript.trim(), conf = r[0].confidence;
      if (speaking || Date.now() - lastSpeechEnd < 2000) continue;      // ignore own voice / echo
      if (text.length < 3) continue;                                    // too short to be meaningful
      if (conf > 0 && conf < 0.4) { send({ type: "no_hear", lang }); continue; }
      userSays(text);
    }
  };
  rec.onnomatch = () => { if (!speaking) send({ type: "no_hear", lang }); };
  rec.onerror = (e) => { if (e.error === "not-allowed") { recWanted = false; $("#orbStatus").textContent = "Microphone permission denied"; } };
  rec.onend = () => { if (recWanted) setTimeout(() => { try { rec.start(); } catch {} }, 300); };
  recWanted = true; try { rec.start(); } catch {}
}
function restartRecognition() { if (!rec) return; recWanted = false; try { rec.stop(); } catch {} setTimeout(startRecognition, 400); }

/* ------------------------------------------------------ voice tone (WebAudio) */
let audioCtx, analyser, tdBuf, voiceSamples = [], vBase = { p: [], e: [] };
function autocorrPitch(buf, sr) {
  let n = buf.length, rms = 0; for (let i = 0; i < n; i++) rms += buf[i] * buf[i]; rms = Math.sqrt(rms / n);
  if (rms < 0.02) return { rms, pitch: 0 };
  const minLag = Math.floor(sr / 400), maxLag = Math.floor(sr / 70); let best = 0, bestLag = 0;
  for (let lag = minLag; lag <= maxLag; lag++) { let s = 0; for (let i = 0; i < n - lag; i += 2) s += buf[i] * buf[i + lag]; if (s > best) { best = s; bestLag = lag; } }
  return { rms, pitch: bestLag ? sr / bestLag : 0 };
}
function startVoiceAnalysis(stream) {
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  const src = audioCtx.createMediaStreamSource(stream); analyser = audioCtx.createAnalyser(); analyser.fftSize = 2048;
  src.connect(analyser); tdBuf = new Float32Array(analyser.fftSize);
  setInterval(() => {
    if (speaking) return;                                              // do not analyse our own TTS
    analyser.getFloatTimeDomainData(tdBuf);
    const { rms, pitch } = autocorrPitch(tdBuf, audioCtx.sampleRate);
    if (pitch > 70 && pitch < 400) voiceSamples.push({ p: pitch, e: rms });
  }, 120);
  setInterval(() => {
    if (voiceSamples.length < 3) { voiceSamples = []; return; }
    const p = voiceSamples.reduce((a, b) => a + b.p, 0) / voiceSamples.length;
    const e = voiceSamples.reduce((a, b) => a + b.e, 0) / voiceSamples.length; voiceSamples = [];
    let tone = null;
    if (vBase.p.length < 15) { vBase.p.push(p); vBase.e.push(e); }
    else {
      const bp = vBase.p.reduce((a, b) => a + b) / vBase.p.length, be = vBase.e.reduce((a, b) => a + b) / vBase.e.length;
      if (p > bp * 1.15 && e > be * 1.2) tone = "tense"; else if (e < be * 0.55) tone = "tired"; else tone = "normal";
    }
    $("#vPitch").textContent = Math.round(p); $("#vTone").textContent = tone || "learning";
    send({ type: "voice", pitch: p, energy: e, tone, lang });
  }, 1000);
}

/* ------------------------------------------------------------------ vision */
let landmarker = null, vidEl = $("#video"), ov = $("#overlay"), octx = ov.getContext("2d");
const roi = document.createElement("canvas"); roi.width = roi.height = 24; const rctx = roi.getContext("2d", { willReadFrequently: true });
const V = { openEAR: [], openRef: null, closedFrames: [], blinks: [], yawns: [], mouthOpenSince: null, eyeClosedSince: null, stress: 0, ppg: [], lastNose: null, motion: 0, hr: null };
const dist = (a, b) => Math.hypot(a.x - b.x, a.y - b.y);
const EYE_R = [33, 160, 158, 133, 153, 144], EYE_L = [362, 385, 387, 263, 373, 380];
const ear = (lm, ix) => (dist(lm[ix[1]], lm[ix[5]]) + dist(lm[ix[2]], lm[ix[4]])) / (2 * dist(lm[ix[0]], lm[ix[3]]));
const bs = (cats, n) => (cats.find((c) => c.categoryName === n) || { score: 0 }).score;

async function loadLandmarker() {
  const base = "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.14";
  const vision = await import(`${base}/vision_bundle.mjs`);
  const files = await vision.FilesetResolver.forVisionTasks(`${base}/wasm`);
  const model = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task";
  const mk = (delegate) => vision.FaceLandmarker.createFromOptions(files, { baseOptions: { modelAssetPath: model, delegate }, runningMode: "VIDEO", numFaces: 1, outputFaceBlendshapes: true });
  try { return await mk("GPU"); } catch { return await mk("CPU"); }
}
function trim(arr, now, ms) { while (arr.length && now - (arr[0].t ?? arr[0]) > ms) arr.shift(); }

function processFace(res, now) {
  const lm = res.faceLandmarks && res.faceLandmarks[0];
  octx.clearRect(0, 0, ov.width, ov.height);
  if (!lm) { V.face = 0; return; }
  V.face = 1;
  // overlay: sparse landmarks
  octx.fillStyle = "rgba(77,163,255,.8)";
  for (let i = 0; i < lm.length; i += 6) octx.fillRect(lm[i].x * ov.width - 1, lm[i].y * ov.height - 1, 2, 2);
  // eyes
  const e = (ear(lm, EYE_R) + ear(lm, EYE_L)) / 2;
  if (V.openEAR.length < 75) { V.openEAR.push(e); if (V.openEAR.length === 75) { const s = [...V.openEAR].sort((a, b) => b - a); V.openRef = s.slice(0, 38).reduce((a, b) => a + b) / 38; } }
  if (V.openRef) {
    const closed = e < V.openRef * 0.25, blinkish = e < V.openRef * 0.6;
    V.closedFrames.push({ t: now, c: closed ? 1 : 0 }); trim(V.closedFrames, now, 60000);
    if (blinkish && !V.eyeClosedSince) V.eyeClosedSince = now;
    if (!blinkish && V.eyeClosedSince) { const d = now - V.eyeClosedSince; if (d > 60 && d < 700) V.blinks.push({ t: now }); V.eyeClosedSince = null; }
    trim(V.blinks, now, 60000);
  }
  // yawn
  const mar = dist(lm[13], lm[14]) / dist(lm[78], lm[308]);
  if (mar > 0.65) { if (!V.mouthOpenSince) V.mouthOpenSince = now; if (now - V.mouthOpenSince > 1200 && !V.yawnCounted) { V.yawns.push({ t: now }); V.yawnCounted = true; } }
  else { V.mouthOpenSince = null; V.yawnCounted = false; }
  trim(V.yawns, now, 600000);
  // blendshape-based stress proxy (heuristic, not a clinical measure)
  const cats = (res.faceBlendshapes && res.faceBlendshapes[0] && res.faceBlendshapes[0].categories) || [];
  const avg = (a, b) => (bs(cats, a) + bs(cats, b)) / 2;
  const s = Math.min(1, 1.2 * (avg("browDownLeft", "browDownRight") + 0.8 * avg("mouthFrownLeft", "mouthFrownRight") + 0.5 * avg("eyeSquintLeft", "eyeSquintRight") + 0.5 * avg("mouthPressLeft", "mouthPressRight")));
  V.stress = 0.9 * V.stress + 0.1 * s;
  // motion (nose) for rPPG gating
  const nose = lm[1]; if (V.lastNose) V.motion = 0.8 * V.motion + 0.2 * dist(nose, V.lastNose) * 100; V.lastNose = { x: nose.x, y: nose.y };
  // forehead ROI -> mean green
  const w = vidEl.videoWidth, h = vidEl.videoHeight; if (!w) return;
  const f = lm[10], c = lm[151], fw = dist(lm[234], lm[454]);
  const cx = f.x + (c.x - f.x) * 0.35, cy = f.y + (c.y - f.y) * 0.35, half = fw * 0.12;
  const sx = (cx - half) * w, sy = (cy - half * 0.7) * h, sw = 2 * half * w, sh = 1.4 * half * h;
  octx.strokeStyle = "#46d39a"; octx.lineWidth = 2; octx.strokeRect((cx - half) * ov.width, (cy - half * 0.7) * ov.height, 2 * half * ov.width, 1.4 * half * ov.height);
  try { rctx.drawImage(vidEl, sx, sy, sw, sh, 0, 0, 24, 24); const d = rctx.getImageData(0, 0, 24, 24).data; let g = 0; for (let i = 1; i < d.length; i += 4) g += d[i]; V.ppg.push({ t: now, g: g / (d.length / 4) }); trim(V.ppg, now, 12000); } catch {}
}
function estimateHr(now) {
  const b = V.ppg; if (b.length < 80 || b[b.length - 1].t - b[0].t < 8000 || V.motion > 1.2) return null;
  const t = b.map((p) => (p.t - b[0].t) / 1000), g = b.map((p) => p.g);
  const sm = g.map((_, i) => { let s = 0, n = 0; for (let j = Math.max(0, i - 7); j <= Math.min(g.length - 1, i + 7); j++) { s += g[j]; n++; } return g[i] - s / n; });
  let best = 0, bestF = 0, tot = 0, cnt = 0;
  for (let f = 0.75; f <= 3.0; f += 0.04) { let re = 0, im = 0; for (let i = 0; i < t.length; i++) { re += sm[i] * Math.cos(2 * Math.PI * f * t[i]); im += sm[i] * Math.sin(2 * Math.PI * f * t[i]); } const p = re * re + im * im; tot += p; cnt++; if (p > best) { best = p; bestF = f; } }
  return best / (tot / cnt) > 3.0 ? bestF * 60 : null;      // require a clear spectral peak
}
function visionLoop() {
  if (!landmarker || vidEl.readyState < 2) { setTimeout(visionLoop, 100); return; }
  const now = performance.now();
  try { processFace(landmarker.detectForVideo(vidEl, now), now); } catch {}
  setTimeout(visionLoop, 66);                                           // ~15 fps to keep laptops responsive
}
setInterval(() => {
  if (!landmarker) return; const now = performance.now();
  if (!V.face) { send({ type: "vision", face: 0 }); return; }
  const hr = estimateHr(now); if (hr) V.hr = V.hr ? 0.7 * V.hr + 0.3 * hr : hr;
  const perclos = V.closedFrames.length ? V.closedFrames.reduce((a, b) => a + b.c, 0) / V.closedFrames.length : 0;
  const bpm = V.blinks.length;
  $("#vBlink").textContent = V.openRef ? bpm : "cal…"; $("#vPerclos").textContent = (perclos * 100).toFixed(0) + "%";
  $("#vYawn").textContent = V.yawns.length; $("#vHr").textContent = V.hr ? Math.round(V.hr) : "–";
  const payload = { type: "vision", face: 1, perclos, yawn: V.yawns.length, stress: V.stress };
  if (V.openRef) payload.blink = bpm; if (V.hr) payload.rppg_hr = V.hr; send(payload);
}, 1000);

/* ------------------------------------------------------------------ enable */
$("#enableBtn").onclick = async () => {
  if (enabled) return;
  const st = $("#camStatus"); st.textContent = "Requesting permissions…";
  let stream;
  try { stream = await navigator.mediaDevices.getUserMedia({ video: { width: 640, height: 480 }, audio: { echoCancellation: true, noiseSuppression: true } }); }
  catch (e) { st.textContent = "Permission denied or no device: " + e.name; return; }
  enabled = true; vidEl.srcObject = stream; await vidEl.play(); $("#camPh").classList.add("hidden");
  ov.width = vidEl.videoWidth || 640; ov.height = vidEl.videoHeight || 480;
  $("#orb").classList.remove("off"); $("#orbStatus").textContent = "Listening"; $("#enableBtn").textContent = "Camera & mic on";
  startVoiceAnalysis(stream); if (!muted) startRecognition(); paintMute();
  setTimeout(() => send({ type: "greet", lang }), 1500);
  st.textContent = "Loading face model (needs internet the first time)…";
  try { landmarker = await loadLandmarker(); st.textContent = "Face tracking on. Hold a neutral face for ~5 s."; visionLoop(); }
  catch (e) { st.textContent = "Face model failed to load: check your internet. Voice still works."; }
};

/* ------------------------------------------------------------------- render */
const metricEls = {};
function drawSpark(cv, data, lo, hi, danger) {
  const w = cv.width = cv.clientWidth * 2, h = cv.height = 68, c = cv.getContext("2d"); c.clearRect(0, 0, w, h);
  if (data.length < 2) return; const mn = Math.min(...data), mx = Math.max(...data), pad = (mx - mn) * 0.2 || 1;
  const y = (v) => h - 6 - ((v - (mn - pad)) / (mx - mn + 2 * pad)) * (h - 12);
  c.strokeStyle = danger ? "#d64545" : getComputedStyle(document.documentElement).getPropertyValue("--accent").trim() || "#c7743a";
  c.lineWidth = 3; c.beginPath(); data.forEach((v, i) => { const x = (i / (data.length - 1)) * w; i ? c.lineTo(x, y(v)) : c.moveTo(x, y(v)); }); c.stroke();
}
function renderState(s) {
  $("#modePill").textContent = s.mode === "live" ? "Live mode" : "Demo mode"; $("#liveSw").checked = s.mode === "live";
  const w = s.wellness; $("#wScore").textContent = Math.round(w); $("#ring").style.setProperty("--v", w);
  $("#ring").style.setProperty("--ringc", w > 70 ? "var(--ok)" : w > 45 ? "var(--warn)" : "var(--alert)");
  $("#wTxt").textContent = w > 70 ? "· good" : w > 45 ? "· watch" : "· needs attention";
  $("#fatBar").style.width = s.fatigue + "%"; $("#strBar").style.width = s.stress + "%";
  $("#baseNote").textContent = s.baseline_ready ? "Personal baseline learned." : "Learning your baseline…";
  const host = $("#metrics");
  for (const [k, m] of Object.entries(s.metrics)) {
    let e = metricEls[k];
    if (!e) { e = metricEls[k] = el("div", "metric", `<div class="n"></div><div class="v"></div><canvas></canvas><span class="src"></span>`); host.appendChild(e); }
    const crit = (m.hi != null && m.value >= m.hi) || (m.lo != null && m.value <= m.lo);
    e.classList.toggle("crit", crit);
    e.querySelector(".n").textContent = m.label; e.querySelector(".v").innerHTML = `${m.value}<small>${esc(m.unit)}</small>`;
    e.querySelector(".src").textContent = m.source; drawSpark(e.querySelector("canvas"), m.history, m.lo, m.hi, crit);
  }
  document.querySelectorAll("#scen button").forEach((b) => b.classList.toggle("on", b.dataset.s === s.scenario));
  // safety override: new critical alert (or a metric entering its danger zone) => unmute at once
  let danger = null;
  for (const a of s.recent_alerts) {
    if (seenAlerts.has(a.id)) continue; seenAlerts.add(a.id);
    if (a.level === "critical" && (alertsPrimed || Date.now() / 1000 - a.ts < 120)) danger = a.text;
  }
  alertsPrimed = true;
  for (const [k, m] of Object.entries(s.metrics)) {
    const c = (m.hi != null && m.value >= m.hi) || (m.lo != null && m.value <= m.lo);
    if (c && prevCrit[k] === false) danger = danger || (m.label + ": " + m.value + " " + m.unit);
    prevCrit[k] = c;
  }
  if (danger) emergencyUnmute(danger);
  // alerts
  const al = $("#alerts"); al.innerHTML = "";
  if (!s.recent_alerts.length) al.innerHTML = '<div class="note">No alerts.</div>';
  [...s.recent_alerts].reverse().forEach((a) => al.appendChild(el("div", "alert " + a.level, `${esc(a.text)}<small>${esc(a.kind)} · ${new Date(a.ts * 1000).toLocaleTimeString()}</small>`)));
  const tk = $("#tickets"); tk.innerHTML = (s.tickets && s.tickets.length) ? "" : '<div class="note">No open requests.</div>';
  (s.tickets || []).forEach((t) => tk.appendChild(el("div", "alert " + (t.status === "open" ? "critical" : "info"), `${esc(t.id)} · ${esc(t.status)}<small>${esc(t.reason)}. A summary was sent to the flight surgeon (arrives after the link delay).</small>`)));
  $("#gen").innerHTML = s.genetic.map((g) => `<div class="gen"><span>${esc(g.name)}</span><span><span class="tag ${g.band}">${g.band}</span> ×${g.relative_risk}</span></div>`).join("");
  // mood-adaptive calm + time of day
  calm = 0.95 * calm + 0.05 * Math.min(1, s.stress / 100 * 1.6); document.documentElement.style.setProperty("--calm", calm.toFixed(2));
}

/* ------------------------------------------------------------ tabs & misc UI */
document.querySelectorAll(".tab").forEach((t) => (t.onclick = () => {
  document.querySelectorAll(".tab").forEach((x) => x.classList.toggle("on", x === t));
  document.querySelectorAll(".view").forEach((v) => v.classList.toggle("on", v.id === "v-" + t.dataset.view));
  if (t.dataset.view === "sens") loadSensors();
}));
$("#langBtn").onclick = () => { lang = lang === "ar" ? "en" : "ar"; $("#langBtn").textContent = lang === "ar" ? "عربي ✓ / EN" : "عربي / EN ✓"; send({ type: "lang", lang }); if (!muted) restartRecognition(); window.ASHE_LANG = lang; document.dispatchEvent(new CustomEvent("ashe-lang", { detail: lang })); };
window.ASHE_LANG = lang;
$("#langBtn").textContent = "عربي ✓ / EN";
$("#themeBtn").onclick = () => { const r = document.documentElement, sp = r.dataset.theme === "earth"; r.dataset.theme = sp ? "space" : "earth"; $("#themeBtn").textContent = sp ? "Warm Earth theme" : "Space theme"; localStorage.setItem("ac-theme", r.dataset.theme); };
function applyTod() { const h = new Date().getHours(); document.documentElement.dataset.tod = h >= 6 && h < 18 ? "day" : "evening"; }
applyTod(); setInterval(applyTod, 600000);
try { const t = localStorage.getItem("ac-theme"), sc = localStorage.getItem("ac-scene"); if (t === "space") $("#themeBtn").click(); } catch {}

fetch("/api/scenarios").then((r) => r.json()).then((list) => list.forEach((n) => { const b = el("button", "small", n); b.dataset.s = n; b.onclick = () => send({ type: "scenario", name: n }); $("#scen").appendChild(b); }));
$("#liveSw").onchange = (e) => send({ type: "mode", mode: e.target.checked ? "live" : "demo" });

async function loadSensors() {
  const g = await (await fetch("/api/ground")).json();
  $("#consent").innerHTML = ""; Object.entries(g.consent).forEach(([k, v]) => { const l = el("label", "switch", `<input type="checkbox" ${v ? "checked" : ""}> ${esc(k)}`); l.querySelector("input").onchange = (e) => send({ type: "consent", key: k, value: e.target.checked }); $("#consent").appendChild(l); });
  const list = await (await fetch("/api/connectors")).json();
  $("#conn").innerHTML = list.map((c) => `<div class="c ${c.status}"><h4>${esc(c.name)}</h4><span class="tag">${esc(c.kind)}</span> <span class="tag">${esc(c.status)}</span><div class="note" style="margin-top:6px">${esc(c.how)}</div><div class="note">Metrics: ${c.provides.length ? esc(c.provides.join(", ")) : "needs a new metric"}</div></div>`).join("");
}

/* ------------------------------------------------------- exercise / knowledge */
$("#planBtn").onclick = async () => {
  const p = await (await fetch("/api/workout")).json();
  $("#plan").innerHTML = p.plan.map((b) => `<div><span>${esc(b.block)}</span><b>${b.minutes} min</b></div>`).join("") + `<div class="note">${esc(p.reason)} ${esc(p.disclaimer)}</div>`;
};
function renderKb(a) {
  $("#kbOut").innerHTML = `<div class="src-box"><b>${esc(a.title || "Answer")}</b>${a.reviewed ? "" : '<span class="badge-un">not clinician-reviewed</span>'}<p>${esc(a.answer)}</p>${a.escalate ? '<p><b>The flight surgeon has been notified.</b></p>' : ""}<div class="note">Sources: ${(a.sources || []).map((s) => esc(s.source)).join(" · ") || "none"}</div><div class="note">${esc(a.disclaimer || "")}</div></div>`;
}
$("#kbBtn").onclick = async () => { const q = $("#kbIn").value.trim(); if (!q) return; renderKb(await (await fetch("/api/kb/ask", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ q }) })).json()); };
$("#kbIn").addEventListener("keydown", (e) => { if (e.key === "Enter") $("#kbBtn").click(); });

/* -------------------------------------------------------------------- games */
const box = () => $("#gameBox"); let gameTimer = null; const stopGame = () => { clearTimeout(gameTimer); gameTimer = null; stopMusic(); };
document.querySelectorAll("[data-game]").forEach((b) => (b.onclick = () => { stopGame(); ({ react: gReact, breath: gBreath, memory: gMemory, sudoku: gSudoku })[b.dataset.game](); }));
function gReact() {
  const stage = el("div", "game-stage", "Tap when it turns green. Tap to start."); box().replaceChildren(stage); const res = []; let t0 = 0, state = "idle";
  const arm = () => { state = "wait"; stage.className = "game-stage"; stage.textContent = "Wait…"; gameTimer = setTimeout(() => { state = "go"; stage.className = "game-stage go"; stage.textContent = "TAP!"; t0 = performance.now(); }, 1500 + Math.random() * 2500); };
  stage.onclick = () => {
    if (state === "idle" || state === "done") { arm(); return; }
    if (state === "wait") { stopGame(); stage.textContent = "Too soon. Tap to retry."; state = "idle"; return; }
    const rt = performance.now() - t0; res.push(rt); send({ type: "game", reaction_ms: rt }); state = "idle";
    stage.className = "game-stage"; stage.innerHTML = `${Math.round(rt)} ms<br><small>avg ${Math.round(res.reduce((a, b) => a + b) / res.length)} ms · tap to go again</small>`;
    $("#gameNote").textContent = "Reaction times are used as one fatigue signal (similar in spirit to the PVT used in sleep research).";
  };
}
function gBreath() {
  const b = el("div", "breath"), t = el("div", "", ""); const stage = el("div", "game-stage"); stage.append(b); stage.append(t); box().replaceChildren(stage);
  let inhale = true; const step = () => { b.style.transitionDuration = inhale ? "4s" : "6s"; b.style.transform = inhale ? "scale(1.9)" : "scale(1)"; t.textContent = inhale ? "Breathe in…" : "Breathe out slowly…"; gameTimer = setTimeout(() => { inhale = !inhale; step(); }, inhale ? 4000 : 6000); }; step();
}
/* ---- tiny synth for game sounds (Web Audio, no audio files) ---- */
let gAudio = null, musicTimer = null, musicOn = true;
try { musicOn = localStorage.getItem("ac-music") !== "off"; } catch {}
const PENTA = [261.63, 293.66, 329.63, 392.0, 440.0, 523.25, 587.33, 659.25, 783.99]; // C major pentatonic: always sounds pleasant
function audioCtx2() { if (!gAudio) gAudio = new (window.AudioContext || window.webkitAudioContext)(); if (gAudio.state === "suspended") gAudio.resume(); return gAudio; }
function tone(freq, dur = 0.35, type = "sine", vol = 0.16, when = 0) {
  const a = audioCtx2(), t = a.currentTime + when, o = a.createOscillator(), g = a.createGain();
  o.type = type; o.frequency.value = freq; g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(vol, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  o.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur + 0.05);
}
function sfxOk() { [0, 2, 4].forEach((n, i) => tone(PENTA[n + 2], 0.25, "triangle", 0.14, i * 0.1)); }
function sfxLevel() { [0, 2, 4, 6].forEach((n, i) => tone(PENTA[n + 1], 0.3, "triangle", 0.13, i * 0.09)); }
function sfxMiss() { tone(330, 0.3, "sine", 0.11); tone(262, 0.45, "sine", 0.11, 0.18); }   // soft, gentle (not harsh)
function startMusic(force = false) {
  stopMusic(); if (!musicOn && !force) return;
  const play = () => {                                                  // slow ambient: soft pad + random pentatonic notes
    const root = PENTA[Math.floor(Math.random() * 3)] / 2;
    tone(root, 3.2, "sine", 0.05); tone(root * 1.5, 3.2, "sine", 0.035);
    for (let i = 0; i < 3; i++) tone(PENTA[Math.floor(Math.random() * PENTA.length)], 1.4, "triangle", 0.04, 0.6 + i * 0.9);
  };
  play(); musicTimer = setInterval(play, 3200);
}
function stopMusic() { if (musicTimer) { clearInterval(musicTimer); musicTimer = null; } }

function gMemory() {
  const wrap = el("div", "game-stage"); const info = el("div", "", "Watch and listen to the pattern, then repeat it. Tap here to start.");
  const grid = el("div", "mem-grid");
  const cells = Array.from({ length: 9 }, (_, i) => { const c = el("button", "", ""); c.dataset.i = i; grid.append(c); return c; });
  const mus = el("button", "small", ""); const setMus = () => { mus.textContent = musicOn ? "Music: on" : "Music: off"; };
  mus.onclick = () => { musicOn = !musicOn; try { localStorage.setItem("ac-music", musicOn ? "on" : "off"); } catch {} setMus(); musicOn ? startMusic() : stopMusic(); }; setMus();
  wrap.style.cssText = "flex-direction:column;gap:10px;height:auto;padding:16px"; wrap.append(info, grid, mus); box().replaceChildren(wrap);
  let seq = [], pos = 0, accept = false;
  const flash = (i, withSound = true) => { cells[i].classList.add("lit"); if (withSound) tone(PENTA[i], 0.4, "sine", 0.2); setTimeout(() => cells[i].classList.remove("lit"), 350); };
  const play = () => {
    accept = false; seq.push(Math.floor(Math.random() * 9)); info.textContent = "Level " + seq.length + " · listen…";
    seq.forEach((s, k) => setTimeout(() => flash(s), 650 * (k + 1)));
    gameTimer = setTimeout(() => { accept = true; pos = 0; info.textContent = "Your turn"; }, 650 * (seq.length + 1));
  };
  info.onclick = () => { if (!seq.length) { audioCtx2(); startMusic(); play(); } };   // first tap also unlocks browser audio
  cells.forEach((c) => (c.onclick = () => {
    if (!accept) return; const i = +c.dataset.i; flash(i);
    if (i !== seq[pos]) { sfxMiss(); info.textContent = `Nice try! You reached level ${seq.length}. Tap here to restart.`; seq = []; accept = false; return; }
    if (++pos === seq.length) { accept = false; setTimeout(sfxLevel, 250); info.textContent = "Correct!"; gameTimer = setTimeout(play, 1300); }
  }));
}

/* ------------------------------------------- companion actions (sing / music) */
const LULLABY = [4, 2, 0, 2, 4, 4, 4, 2, 2, 2, 4, 6, 6, 4, 2, 0, 2, 4, 4, 4, 4, 2, 2, 4, 2, 0]; // simple traditional tune, indexes into PENTA
let musicStopTimer = null;
function playLullaby() {
  audioCtx2(); LULLABY.forEach((n, i) => tone(PENTA[n] , 0.5, "triangle", 0.09, 0.8 + i * 0.55));
}
function runAction(name) {
  if (name === "sing") playLullaby();
  else if (name === "music") { startMusic(true); clearTimeout(musicStopTimer); musicStopTimer = setTimeout(stopMusic, 120000); }
  else if (name === "stopmusic") { stopMusic(); clearTimeout(musicStopTimer); }
}

connect();

/* ------------------------------------------------------------------ sudoku */
// Single-player Sudoku: relaxed (no timer pressure, no penalties). Puzzles are generated on the fly with a
// unique solution; difficulty = number of given digits. Works with mouse, touch and keyboard (1-9, arrows, Backspace).
function gSudoku() {
  const wrap = el("div", "sdk"); box().replaceChildren(wrap);
  const LEVELS = { easy: 40, medium: 32, hard: 26 };
  let level = "easy", sol = [], given = [], cur = [], notes = [], sel = -1, noteMode = false, t0 = 0, tick = null, done = false, hints = 0;
  const shuffle = (a) => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const ok = (g, i, v) => { const r = (i / 9) | 0, c = i % 9, br = r - r % 3, bc = c - c % 3;
    for (let k = 0; k < 9; k++) { if (g[r * 9 + k] === v || g[k * 9 + c] === v || g[(br + ((k / 3) | 0)) * 9 + bc + k % 3] === v) return false; } return true; };
  const fill = (g) => { const i = g.indexOf(0); if (i < 0) return true;
    for (const v of shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9])) { if (ok(g, i, v)) { g[i] = v; if (fill(g)) return true; g[i] = 0; } } return false; };
  const count = (g, lim = 2) => { // number of solutions (stops at lim); picks the most constrained cell first
    let best = -1, bc = 10, bo = null;
    for (let i = 0; i < 81; i++) if (!g[i]) { const o = []; for (let v = 1; v <= 9; v++) if (ok(g, i, v)) o.push(v); if (o.length < bc) { bc = o.length; best = i; bo = o; if (bc <= 1) break; } }
    if (best < 0) return 1; let n = 0;
    for (const v of bo) { g[best] = v; n += count(g, lim - n); g[best] = 0; if (n >= lim) break; } return n; };
  function make() {
    const full = Array(81).fill(0); fill(full); sol = full.slice();
    const p = full.slice(), want = 81 - LEVELS[level];
    let removed = 0; for (const i of shuffle([...Array(81).keys()])) { if (removed >= want) break; const keep = p[i]; p[i] = 0; if (count(p.slice()) === 1) removed++; else p[i] = keep; }
    given = p.map((v) => v !== 0); cur = p.slice(); notes = Array.from({ length: 81 }, () => new Set()); sel = -1; done = false; hints = 0; t0 = Date.now();
  }
  const conflicts = () => { const bad = new Set(); for (let i = 0; i < 81; i++) { const v = cur[i]; if (!v) continue; cur[i] = 0; if (!ok(cur, i, v)) bad.add(i); cur[i] = v; } return bad; };
  const fmtT = (ms) => { const s = Math.floor(ms / 1000); return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0"); };
  function draw() {
    const bad = conflicts(), sv = sel >= 0 ? cur[sel] : 0, filled = cur.filter(Boolean).length;
    const cells = []; for (let i = 0; i < 81; i++) {
      const r = (i / 9) | 0, c = i % 9, cls = ["sc"];
      if (given[i]) cls.push("g"); if (i === sel) cls.push("sel");
      else if (sel >= 0 && ((r === ((sel / 9) | 0)) || (c === sel % 9) || (((r / 3) | 0) === (((sel / 9) | 0) / 3 | 0) && ((c / 3) | 0) === ((sel % 9) / 3 | 0)))) cls.push("peer");
      if (sv && cur[i] === sv && i !== sel) cls.push("same"); if (bad.has(i)) cls.push("bad");
      if (c % 3 === 2 && c < 8) cls.push("rb"); if (r % 3 === 2 && r < 8) cls.push("bb");
      let inner = cur[i] ? cur[i] : (notes[i].size ? `<span class="nt">${[1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => `<i>${notes[i].has(n) ? n : ""}</i>`).join("")}</span>` : "");
      cells.push(`<button class="${cls.join(" ")}" data-i="${i}" aria-label="row ${r + 1} column ${c + 1}">${inner}</button>`);
    }
    const left = [1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => 9 - cur.filter((v) => v === n).length);
    wrap.innerHTML = `
      <div class="sdk-top"><span class="note" id="sdkT">${fmtT(Date.now() - t0)}</span><span class="sp"></span>
        ${["easy", "medium", "hard"].map((l) => `<button class="small ${l === level ? "primary" : ""}" data-lv="${l}">${l}</button>`).join("")}</div>
      <div class="sdk-grid">${cells.join("")}</div>
      <div class="sdk-pad">${[1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => `<button data-n="${n}" ${left[n - 1] <= 0 ? "disabled" : ""}>${n}<small>${Math.max(0, left[n - 1])}</small></button>`).join("")}</div>
      <div class="row sdk-act"><button data-act="note" class="${noteMode ? "primary" : ""}">✎ Notes ${noteMode ? "on" : "off"}</button><button data-act="erase">⌫ Erase</button><button data-act="hint">💡 Hint</button><button data-act="check">✔ Check</button><button data-act="new">↻ New</button></div>
      <div class="sdk-msg note" id="sdkMsg">${done ? "🎉 Solved in " + fmtT(Date.now() - t0) + (hints ? " · " + hints + " hint(s)" : "") + ". Take a slow breath: well done." : filled + "/81 · No rush. Sudoku is a calm way to rest your mind."}</div>`;
    wrap.querySelectorAll(".sc").forEach((b) => (b.onclick = () => { sel = +b.dataset.i; draw(); }));
    wrap.querySelectorAll("[data-n]").forEach((b) => (b.onclick = () => put(+b.dataset.n)));
    wrap.querySelectorAll("[data-lv]").forEach((b) => (b.onclick = () => { level = b.dataset.lv; busy(); }));
    wrap.querySelectorAll("[data-act]").forEach((b) => (b.onclick = () => act(b.dataset.act)));
    wrap.focus({ preventScroll: true });
  }
  function put(n) {
    if (done || sel < 0 || given[sel]) return;
    if (noteMode && !cur[sel]) { notes[sel].has(n) ? notes[sel].delete(n) : notes[sel].add(n); draw(); return; }
    cur[sel] = cur[sel] === n ? 0 : n; notes[sel].clear();
    if (cur[sel]) { // clear that digit from the notes of its row / column / box
      const r = (sel / 9) | 0, c = sel % 9; for (let i = 0; i < 81; i++) { const rr = (i / 9) | 0, cc = i % 9; if (rr === r || cc === c || ((rr / 3) | 0) === ((r / 3) | 0) && ((cc / 3) | 0) === ((c / 3) | 0)) notes[i].delete(n); } }
    if (cur.every((v, i) => v === sol[i])) { done = true; clearInterval(tick); try { sfxLevel(); } catch {} }
    draw();
  }
  function act(a) {
    if (a === "new") return busy();
    if (a === "note") { noteMode = !noteMode; return draw(); }
    if (done) return;
    if (a === "erase") { if (sel >= 0 && !given[sel]) { cur[sel] = 0; notes[sel].clear(); } draw(); }
    else if (a === "hint") { const target = (sel >= 0 && !given[sel] && cur[sel] !== sol[sel]) ? sel : cur.findIndex((v, i) => v !== sol[i]); if (target < 0) return; sel = target; cur[sel] = sol[sel]; given[sel] = true; notes[sel].clear(); hints++; if (cur.every((v, i) => v === sol[i])) { done = true; clearInterval(tick); } draw(); }
    else if (a === "check") { const wrong = cur.filter((v, i) => v && v !== sol[i]).length; draw(); $("#sdkMsg").textContent = wrong ? wrong + " cell(s) are not right yet. Look for red digits or try again." : "All filled digits are correct so far. Keep going 👍"; }
  }
  function busy() { wrap.innerHTML = '<div class="game-stage">Preparing a puzzle…</div>'; setTimeout(() => { make(); draw(); clearInterval(tick); tick = setInterval(() => { const t = $("#sdkT"); if (!t || !wrap.isConnected) { clearInterval(tick); return; } if (!done) t.textContent = fmtT(Date.now() - t0); }, 1000); }, 30); }
  wrap.tabIndex = 0;
  wrap.addEventListener("keydown", (e) => {
    if (e.key >= "1" && e.key <= "9") put(+e.key);
    else if (e.key === "Backspace" || e.key === "Delete" || e.key === "0") act("erase");
    else if (e.key.startsWith("Arrow")) { e.preventDefault(); if (sel < 0) sel = 0; else { const d = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -9, ArrowDown: 9 }[e.key], n = sel + d; if (n >= 0 && n < 81 && !(Math.abs(d) === 1 && ((n / 9) | 0) !== ((sel / 9) | 0))) sel = n; } draw(); wrap.focus(); }
  });
  busy();
}

paintMute();
''',
 'style.css': ''':root{
  --radius:16px; --gap:14px;
  --font:"Segoe UI",system-ui,-apple-system,"Noto Sans Arabic",Tahoma,sans-serif;
  --calm:0;            /* 0..1 set by JS from stress: calmer UI when stressed */
  --alert:#d64545; --ok:#3f9d6b; --warn:#d9892b;
}
/* ---------- Warm Earth (default) ---------- */
:root[data-theme="earth"]{
  --bg:#f6efe4; --bg2:#efe3d0; --panel:#fffaf2; --panel2:#f9f0e1; --text:#3a2f25; --muted:#8a7a68;
  --line:#e6d8c3; --accent:#c7743a; --accent2:#5d8a6a; --chip:#f1e4cf; --shadow:0 6px 22px rgba(120,80,40,.10);
}
:root[data-theme="earth"][data-tod="evening"]{
  --bg:#2b221b; --bg2:#33291f; --panel:#3a2f25; --panel2:#42362a; --text:#f3e7d6; --muted:#b9a68f;
  --line:#54463a; --accent:#e29a5c; --accent2:#8bb597; --chip:#4a3d31; --shadow:0 6px 22px rgba(0,0,0,.35);
}
:root[data-theme="earth"][data-tod="day"]{ --bg:#f3f1e8; }
/* ---------- Space (dark) ---------- */
:root[data-theme="space"]{
  --bg:#0a0e17; --bg2:#0e1422; --panel:#121a2b; --panel2:#18223a; --text:#e6ecf7; --muted:#8190ad;
  --line:#243050; --accent:#4da3ff; --accent2:#46d39a; --chip:#1c2742; --shadow:0 6px 22px rgba(0,0,0,.45);
}
*{box-sizing:border-box}
html,body{margin:0;height:100%}
body{font-family:var(--font);background:var(--bg);color:var(--text);transition:background .8s,color .8s;
  filter:saturate(calc(1 - var(--calm)*.18))}
body.scene-sea{background-image:linear-gradient(180deg,rgba(120,190,200,.22),transparent 40%),radial-gradient(120% 40% at 50% 105%,rgba(60,140,170,.28),transparent 70%)}
body.scene-forest{background-image:linear-gradient(180deg,rgba(110,160,110,.20),transparent 45%),radial-gradient(100% 50% at 20% 110%,rgba(60,110,70,.30),transparent 70%)}
body.scene-desert{background-image:linear-gradient(180deg,rgba(230,170,110,.22),transparent 45%),radial-gradient(120% 40% at 70% 108%,rgba(210,140,70,.30),transparent 70%)}
body.scene-sky{background-image:linear-gradient(180deg,rgba(150,190,235,.28),rgba(250,210,180,.18) 60%,transparent)}
:root[data-theme="space"] body{background-image:radial-gradient(circle at 80% -10%,#16254a 0,transparent 45%)}

header{display:flex;align-items:center;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line);
  background:color-mix(in srgb,var(--panel) 85%,transparent);backdrop-filter:blur(8px);position:sticky;top:0;z-index:5}
header h1{font-size:18px;margin:0;letter-spacing:.3px}
header .sp{flex:1}
.pill{font-size:12px;padding:4px 10px;border-radius:99px;background:var(--chip);color:var(--muted);border:1px solid var(--line)}
.pill.live{color:var(--ok);border-color:var(--ok)} .pill.bad{color:var(--alert);border-color:var(--alert)}
button,select,input{font:inherit;color:inherit}
button{cursor:pointer;border:1px solid var(--line);background:var(--panel2);padding:7px 12px;border-radius:10px;transition:.15s}
button:hover{border-color:var(--accent)} button.primary{background:var(--accent);color:#fff;border-color:transparent}
button.small{padding:4px 8px;font-size:12px}
select,input[type=text]{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:7px 10px}

main{display:grid;grid-template-columns:340px 1fr 320px;gap:var(--gap);padding:var(--gap);max-width:1600px;margin:auto}
@media(max-width:1100px){main{grid-template-columns:1fr}}
.col{display:flex;flex-direction:column;gap:var(--gap);min-width:0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:14px;box-shadow:var(--shadow);transition:background .8s}
.card h2{font-size:13px;margin:0 0 10px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted);font-weight:600}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}

/* camera */
.cam{position:relative;border-radius:12px;overflow:hidden;background:#000;aspect-ratio:4/3}
.cam video,.cam canvas{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scaleX(-1)}
.cam .ph{position:absolute;inset:0;display:grid;place-items:center;color:#9aa;font-size:13px;text-align:center;padding:12px}
.vis-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}
.stat{background:var(--panel2);border-radius:10px;padding:8px;text-align:center}
.stat b{display:block;font-size:17px} .stat span{font-size:11px;color:var(--muted)}

/* companion */
.orb{width:54px;height:54px;border-radius:50%;background:radial-gradient(circle at 35% 30%,color-mix(in srgb,var(--accent) 70%,#fff),var(--accent));
  box-shadow:0 0 0 0 color-mix(in srgb,var(--accent) 45%,transparent);animation:breathe 4s ease-in-out infinite}
.orb.speaking{animation:pulse .9s ease-in-out infinite} .orb.off{filter:grayscale(1);animation:none;opacity:.5}
@keyframes breathe{50%{transform:scale(1.07);box-shadow:0 0 22px 4px color-mix(in srgb,var(--accent) 35%,transparent)}}
@keyframes pulse{50%{transform:scale(1.15);box-shadow:0 0 28px 8px color-mix(in srgb,var(--accent) 50%,transparent)}}
.chat{height:230px;overflow:auto;display:flex;flex-direction:column;gap:6px;margin:10px 0;padding-right:4px}
.msg{max-width:88%;padding:8px 11px;border-radius:12px;font-size:14px;line-height:1.45;unicode-bidi:plaintext}
.msg.ai{background:var(--chip);align-self:flex-start} .msg.me{background:var(--accent);color:#fff;align-self:flex-end}
.msg.earth{background:color-mix(in srgb,var(--accent2) 25%,var(--panel));border:1px solid var(--accent2);align-self:flex-start}
.chat-in{display:flex;gap:6px} .chat-in input{flex:1}

/* tabs */
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.tab{padding:6px 12px;border-radius:99px;font-size:13px} .tab.on{background:var(--accent);color:#fff;border-color:transparent}
.view{display:none} .view.on{display:block}

/* metrics */
.score{display:flex;align-items:center;gap:18px}
.ring{--v:100;width:104px;height:104px;border-radius:50%;display:grid;place-items:center;
  background:conic-gradient(var(--ringc,var(--ok)) calc(var(--v)*1%),var(--chip) 0)}
.ring>div{width:80px;height:80px;border-radius:50%;background:var(--panel);display:grid;place-items:center;font-size:26px;font-weight:700}
.bars{flex:1;display:grid;gap:8px}
.bar{font-size:12px;color:var(--muted)} .bar i{display:block;height:7px;border-radius:6px;background:var(--chip);margin-top:3px;overflow:hidden}
.bar i b{display:block;height:100%;background:var(--accent);width:0;transition:width .6s}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:10px}
.metric{background:var(--panel2);border:1px solid var(--line);border-radius:14px;padding:10px 12px;position:relative}
.metric .n{font-size:12px;color:var(--muted)} .metric .v{font-size:25px;font-weight:700;margin:2px 0}
.metric .v small{font-size:12px;color:var(--muted);font-weight:400;margin-left:4px}
.metric canvas{width:100%;height:34px;display:block}
.metric .src{position:absolute;top:8px;right:8px;font-size:10px;padding:1px 6px;border-radius:99px;background:var(--chip);color:var(--muted)}
.metric.crit{border-color:var(--alert)} .metric.crit .v{color:var(--alert)}

/* alerts */
.alert{border-left:4px solid var(--warn);background:var(--panel2);border-radius:8px;padding:8px 10px;margin-bottom:8px;font-size:13px}
.alert.critical{border-color:var(--alert)} .alert.info{border-color:var(--accent2)}
.alert small{display:block;color:var(--muted);margin-top:2px}
.gen{display:flex;justify-content:space-between;font-size:13px;padding:6px 0;border-bottom:1px dashed var(--line)}
.tag{font-size:11px;padding:2px 8px;border-radius:99px;background:var(--chip)}
.tag.elevated{color:var(--warn)} .tag.high{color:var(--alert)} .tag.lower{color:var(--ok)}
.note{font-size:12px;color:var(--muted);line-height:1.5}
.scen{display:flex;flex-wrap:wrap;gap:6px}
.scen button.on{background:var(--alert);color:#fff;border-color:transparent}

/* exercise / games / sensors */
.plan{display:grid;gap:6px} .plan div{display:flex;justify-content:space-between;background:var(--panel2);padding:8px 12px;border-radius:10px}
.src-box{background:var(--panel2);border-radius:10px;padding:10px;font-size:13px;margin-top:8px}
.badge-un{display:inline-block;background:var(--warn);color:#fff;font-size:11px;padding:1px 7px;border-radius:99px;margin-left:6px}
.game-stage{height:220px;border-radius:14px;display:grid;place-items:center;background:var(--panel2);user-select:none;text-align:center;font-size:18px}
.game-stage.go{background:var(--accent2);color:#fff;cursor:pointer}
.breath{width:90px;height:90px;border-radius:50%;background:var(--accent2);transition:transform 4s ease-in-out}
.mem-grid{display:grid;grid-template-columns:repeat(3,64px);gap:8px;justify-content:center}
.mem-grid button{height:64px;border-radius:12px} .mem-grid button.lit{background:var(--accent);border-color:transparent}
.conn{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.conn .c{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:10px;font-size:13px}
.conn .c h4{margin:0 0 4px;font-size:14px} .conn .c.ready{border-color:var(--ok)}
.switch{display:flex;align-items:center;gap:8px;font-size:13px}
.hidden{display:none!important}

/* =====================================================================
   Profile / welcome / medical card / mute / sudoku  (theme variables only)
   ===================================================================== */
.welcome{max-width:1600px;margin:0 auto;padding:14px var(--gap) 0;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.welcome .w-line{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.welcome .w-hello{font-size:15px;color:var(--text);opacity:.78;letter-spacing:.4px}
.welcome .w-name{font-size:26px;font-weight:700;letter-spacing:.2px;unicode-bidi:plaintext}
.welcome .w-greet{font-size:14px;padding:6px 14px;border-radius:99px;background:var(--chip);border:1px solid var(--line);color:var(--text)}
html[data-wp] .welcome .w-hello,html[data-wp] .welcome .w-name{text-shadow:0 1px 10px color-mix(in srgb,var(--bg) 85%,transparent)}

/* round + rounded-rectangular buttons (same soft-corner language as the rest of the app) */
.rbtn{width:44px;height:44px;border-radius:50%;padding:0;display:grid;place-items:center;font-size:18px;line-height:1;background:var(--panel2);border:1px solid var(--line)}
.rbtn:hover{border-color:var(--accent);transform:translateY(-1px)}
.rbtn.on{background:var(--alert);color:#fff;border-color:transparent}
.rect{border-radius:14px;padding:9px 16px;font-size:14px;background:var(--panel2);border:1px solid var(--line)}
.rect.primary{background:var(--accent);color:#fff;border-color:transparent}
.rect:hover{border-color:var(--accent)} .rect.primary:hover{filter:brightness(1.07)}
.rect-a{text-decoration:none;color:inherit}

.hero{text-align:center;display:flex;flex-direction:column;align-items:center;gap:6px;padding:18px 14px 16px}
.avatar{width:112px;height:112px;border-radius:50%;padding:3px;background:conic-gradient(var(--accent),var(--accent2),var(--accent));box-shadow:var(--shadow)}
.avatar svg{display:block;width:100%;height:100%;border-radius:50%;background:var(--panel)}
.hero-name{font-size:19px;font-weight:700;margin-top:6px;unicode-bidi:plaintext;max-width:100%;overflow-wrap:anywhere}
.hero-sub{margin-top:-2px}
.hero-actions{display:flex;gap:10px;justify-content:center;margin-top:8px;flex-wrap:wrap}
.hero-actions.wide{gap:8px;margin-top:4px}

dl.med{margin:0 0 12px;display:grid;gap:8px}
dl.med>div{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:8px 12px}
dl.med dt{font-size:11px;color:var(--muted);letter-spacing:.3px}
dl.med dd{margin:2px 0 0;font-size:15px;font-weight:600;white-space:pre-wrap;overflow-wrap:anywhere;unicode-bidi:plaintext}
dl.med dd.empty{color:var(--muted);font-weight:400;font-style:italic}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
dl.med .two{background:none;border:0;padding:0}
dl.med .two>div{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:8px 12px}
#medForm{display:grid;gap:10px}
#medForm label{display:grid;gap:4px;font-size:12px;color:var(--muted)}
#medForm input,#medForm textarea{font:inherit;font-size:14px;color:var(--text);background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:8px 11px;width:100%;resize:vertical;outline:none}
#medForm input:focus,#medForm textarea:focus{border-color:var(--accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 25%,transparent)}
#medErr{color:var(--alert);min-height:0}

.mute-btn{margin-inline-start:auto;font-size:13px;padding:8px 12px;border-radius:14px;white-space:nowrap}
.mute-btn.on{background:var(--warn);color:#fff;border-color:transparent}
.orb.muted{filter:grayscale(.85);opacity:.55;animation:none}
.mute-note{margin-top:10px;padding:8px 12px;border-radius:12px;font-size:13px;background:color-mix(in srgb,var(--alert) 14%,var(--panel2));border:1px solid var(--alert);animation:flashIn .5s ease 2}
@keyframes flashIn{50%{background:color-mix(in srgb,var(--alert) 38%,var(--panel2))}}

/* sudoku */
.sdk{display:grid;gap:10px;max-width:440px;margin:0 auto;outline:none}
.sdk-top{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.sdk-top .sp{flex:1}
.sdk-grid{display:grid;grid-template-columns:repeat(9,1fr);border:2px solid var(--text);border-radius:12px;overflow:hidden;background:var(--panel2);aspect-ratio:1}
.sc{all:unset;box-sizing:border-box;display:grid;place-items:center;cursor:pointer;font-size:clamp(15px,3.4vw,24px);font-weight:600;color:var(--accent);border:1px solid var(--line);position:relative;min-width:0}
.sc.g{color:var(--text);font-weight:800;background:color-mix(in srgb,var(--chip) 70%,transparent)}
.sc.rb{border-right:2px solid var(--text)}.sc.bb{border-bottom:2px solid var(--text)}
.sc.peer{background:color-mix(in srgb,var(--accent) 9%,transparent)}
.sc.same{background:color-mix(in srgb,var(--accent2) 28%,transparent)}
.sc.sel{background:color-mix(in srgb,var(--accent) 30%,transparent);box-shadow:inset 0 0 0 2px var(--accent)}
.sc.bad{color:var(--alert);background:color-mix(in srgb,var(--alert) 16%,transparent)}
.sc:focus-visible{box-shadow:inset 0 0 0 2px var(--accent)}
.sc .nt{display:grid;grid-template-columns:repeat(3,1fr);width:100%;height:100%;font-size:clamp(7px,1.3vw,10px);font-weight:500;color:var(--muted)}
.sc .nt i{font-style:normal;display:grid;place-items:center}
.sdk-pad{display:grid;grid-template-columns:repeat(9,1fr);gap:5px}
.sdk-pad button{padding:6px 0;border-radius:12px;font-size:18px;font-weight:700;display:grid;place-items:center;line-height:1}
.sdk-pad button small{font-size:9px;color:var(--muted);font-weight:400}
.sdk-pad button:disabled{opacity:.35;cursor:not-allowed}
.sdk-act{justify-content:center}.sdk-act button{border-radius:12px;font-size:13px;padding:7px 10px}
.sdk-act button.primary{background:var(--accent);color:#fff}
.sdk-msg{text-align:center;min-height:18px}
@media(max-width:520px){.sdk-pad button{font-size:15px}.hero-name{font-size:17px}.welcome .w-name{font-size:22px}}
''',
 'extras.js': '(() => {\n  // ================= styles (all colours come from the app theme variables) =================\n  const css = `\n  body{padding-bottom:78px}\n  header a{color:inherit;text-decoration:none}\n  #ax-bg{position:fixed;inset:0;z-index:-1;pointer-events:none;background-size:cover;background-position:center;background-repeat:no-repeat;transition:opacity .6s}\n  html[data-wp] .card{background:color-mix(in srgb,var(--panel) 78%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}\n  #ax-bar{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);display:flex;gap:6px;z-index:50;padding:6px;border-radius:999px;\n    background:color-mix(in srgb,var(--panel) 88%,transparent);border:1px solid var(--line);box-shadow:var(--shadow);backdrop-filter:blur(10px);max-width:96vw;overflow-x:auto}\n  .ax-btn,#ax-bar button{font:inherit;font-size:13px;padding:8px 14px;border-radius:999px;border:1px solid var(--line);background:var(--panel2);color:var(--text);cursor:pointer;white-space:nowrap;transition:.15s}\n  .ax-btn:hover,#ax-bar button:hover{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 14%,var(--panel2))}\n  .ax-btn.primary{background:var(--accent);color:#fff;border-color:transparent}\n  .ax-btn.primary:hover{filter:brightness(1.08)}\n  .ax-btn.danger{color:var(--alert);border-color:color-mix(in srgb,var(--alert) 50%,var(--line))}\n  .ax-btn.sel{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 24%,var(--panel2));font-weight:600}\n  .ax-btn:disabled{opacity:.45;cursor:not-allowed}\n  #ax-modal{position:fixed;inset:0;z-index:60;display:none;align-items:center;justify-content:center;background:rgba(0,0,0,.45);backdrop-filter:blur(3px);padding:16px}\n  #ax-modal.open{display:flex}\n  #ax-panel{background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);padding:22px 24px;\n    width:min(760px,100%);max-height:90vh;overflow:auto;font-family:var(--font)}\n  #ax-panel h2{margin:0 0 6px;font-size:20px}\n  #ax-panel h3{margin:18px 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:.8px;color:var(--muted)}\n  #ax-panel p{margin:8px 0;line-height:1.5}\n  .ax-muted{color:var(--muted);font-size:13px}\n  .ax-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0}\n  .ax-in{font:inherit;color:var(--text);background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:9px 12px;caret-color:var(--accent);outline:none}\n  .ax-in:focus{border-color:var(--accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 25%,transparent)}\n  .ax-in::placeholder{color:var(--muted)}\n  textarea.ax-in{width:100%;min-height:140px;resize:vertical;line-height:1.5}\n  .ax-grow{flex:1;min-width:140px}\n  .ax-chip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;background:var(--chip);border:1px solid var(--line);font-size:14px}\n  .ax-chip.turn{border-color:var(--accent);background:var(--accent);color:#fff;font-weight:600}\n  .ax-chip button{all:unset;cursor:pointer;opacity:.6;font-size:15px;line-height:1} .ax-chip button:hover{opacity:1}\n  .ax-stats{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0}\n  .ax-stat{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:8px 14px;text-align:center;min-width:90px}\n  .ax-stat b{display:block;font-size:20px} .ax-stat span{font-size:11px;color:var(--muted)}\n  .ax-pads{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:380px;margin:16px auto}\n  .ax-pad{height:112px;border-radius:18px;opacity:.38;cursor:pointer;transition:opacity .12s,transform .12s,box-shadow .12s;border:none}\n  .ax-pad.on{opacity:1;transform:scale(1.05);box-shadow:0 0 30px 6px currentColor}\n  .ax-status{text-align:center;font-size:17px;font-weight:600;margin:10px 0;min-height:26px}\n  .ax-entry{background:var(--panel2);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:10px 0}\n  .ax-entry .t{white-space:pre-wrap;margin:6px 0 10px;line-height:1.5;unicode-bidi:plaintext}\n  .ax-list{list-style:none;margin:0;padding:0} .ax-list li{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:9px 12px;margin:6px 0;font-size:14px}\n  .ax-q{margin:16px 0}\n  .ax-scale{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-top:6px}\n  .ax-sig{border:1px solid var(--warn);border-radius:12px;padding:12px 14px;margin:14px 0;background:color-mix(in srgb,var(--warn) 10%,transparent)}\n  .ax-wp{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin:12px 0}\n  .ax-wp-item{all:unset;cursor:pointer;display:block;border-radius:12px;overflow:hidden;border:2px solid var(--line);background:var(--panel2);transition:.15s;position:relative}\n  .ax-wp-item:hover{border-color:var(--accent);transform:translateY(-2px)}\n  .ax-wp-item.sel{border-color:var(--accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--accent) 35%,transparent)}\n  .ax-wp-item .im{height:86px;background-size:cover;background-position:center}\n  .ax-wp-item .nm{padding:7px 10px;font-size:13px;color:var(--text)}\n  .ax-wp-item .x{position:absolute;top:4px;right:4px;background:rgba(0,0,0,.6);color:#fff;border-radius:50%;width:22px;height:22px;display:grid;place-items:center;font-size:14px}\n  `;\n  const st = document.createElement(\'style\'); st.textContent = css; document.head.appendChild(st);\n\n  // ================= helpers =================\n  const esc = t => String(t).replace(/[&<>"\']/g, c => ({\'&\':\'&amp;\',\'<\':\'&lt;\',\'>\':\'&gt;\',\'"\':\'&quot;\',"\'":\'&#39;\'}[c]));\n  const lsGet = (k, d) => { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } };\n  const lsSet = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } };\n  const fmt = d => new Date(d).toLocaleString(\'en-GB\', { day:\'2-digit\', month:\'short\', year:\'numeric\', hour:\'2-digit\', minute:\'2-digit\' });\n\n  // ================= wallpapers (rich SVG scenes + user uploads) =================\n  const W = 1600, H = 900;\n  let seed = 7; const sr = () => (seed = (seed * 16807) % 2147483647) / 2147483647; // deterministic\n  const S = (inner, defs = \'\') => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice"><defs>${defs}</defs>${inner}</svg>`;\n  const lg = (id, stops) => `<linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1">${stops.map(([o, c, a = 1]) => `<stop offset="${o}" stop-color="${c}" stop-opacity="${a}"/>`).join(\'\')}</linearGradient>`;\n  const rg = (id, stops) => `<radialGradient id="${id}">${stops.map(([o, c, a = 1]) => `<stop offset="${o}" stop-color="${c}" stop-opacity="${a}"/>`).join(\'\')}</radialGradient>`;\n  const stars = n => { seed = 11; return Array.from({ length: n }, () => `<circle cx="${sr()*W|0}" cy="${sr()*H*0.75|0}" r="${(sr()*1.6+0.4).toFixed(1)}" fill="#fff" opacity="${(sr()*0.6+0.3).toFixed(2)}"/>`).join(\'\'); };\n  const wave = (y, amp, len, col, op = 1) => { let d = `M0 ${y}`; for (let x = 0; x <= W + len; x += len) d += ` q${len/4} ${-amp} ${len/2} 0 t${len/2} 0`; return `<path d="${d} V${H} H0Z" fill="${col}" opacity="${op}"/>`; };\n  const hills = (y, amp, col, k = 1) => { seed = 5 * k; let d = `M0 ${y}`; for (let x = 0; x <= W; x += 200) d += ` Q${x+100} ${y - amp * (0.4 + sr())} ${x+200} ${y + (sr()-0.5)*amp*0.5}`; return `<path d="${d} V${H} H0Z" fill="${col}"/>`; };\n  const pine = (x, y, h, col) => `<polygon points="${x},${y-h} ${x-h*0.28},${y-h*0.35} ${x-h*0.14},${y-h*0.35} ${x-h*0.36},${y} ${x+h*0.36},${y} ${x+h*0.14},${y-h*0.35} ${x+h*0.28},${y-h*0.35}" fill="${col}"/>`;\n  const cloud = (x, y, s, op = .9) => `<g opacity="${op}" fill="#fff"><ellipse cx="${x}" cy="${y}" rx="${70*s}" ry="${26*s}"/><ellipse cx="${x-40*s}" cy="${y+6*s}" rx="${45*s}" ry="${20*s}"/><ellipse cx="${x+42*s}" cy="${y+8*s}" rx="${50*s}" ry="${20*s}"/><ellipse cx="${x+6*s}" cy="${y-18*s}" rx="${40*s}" ry="${24*s}"/></g>`;\n  const fish = (x, y, s, col, flip = 1) => `<g transform="translate(${x} ${y}) scale(${s*flip} ${s})"><path d="M0 0 Q30 -22 62 0 Q30 22 0 0Z M62 0 L88 -18 L88 18Z" fill="${col}"/><circle cx="14" cy="-4" r="3" fill="#102"/></g>`;\n  const bird = (x, y, s) => `<path d="M${x} ${y} q${14*s} ${-14*s} ${28*s} 0 q${14*s} ${-14*s} ${28*s} 0" fill="none" stroke="#223" stroke-width="${2.5*s}" stroke-linecap="round"/>`;\n  const acacia = (x, y, s) => `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-4 0 Q0 -60 -2 -90 L6 -90 Q8 -50 6 0Z M0 -85 Q-50 -90 -90 -75 Q-40 -115 0 -108 Q50 -118 95 -78 Q50 -92 0 -85Z" fill="#1d1a12"/></g>`;\n  const giraffe = (x, y, s) => `<g transform="translate(${x} ${y}) scale(${s})" fill="#1d1a12"><rect x="-40" y="-72" width="9" height="72" rx="3"/><rect x="-24" y="-72" width="9" height="72" rx="3"/><rect x="18" y="-72" width="9" height="72" rx="3"/><rect x="34" y="-72" width="9" height="72" rx="3"/><ellipse cx="0" cy="-86" rx="52" ry="26"/><path d="M26 -96 L46 -190 L58 -186 L50 -90Z"/><path d="M-50 -92 Q-64 -80 -60 -56 L-54 -58 Q-56 -76 -46 -84Z"/><ellipse cx="62" cy="-192" rx="20" ry="10" transform="rotate(-24 62 -192)"/><rect x="48" y="-210" width="3" height="16"/><rect x="58" y="-212" width="3" height="16"/></g>`;\n  const elephant = (x, y, s) => `<g transform="translate(${x} ${y}) scale(${s})" fill="#1d1a12"><rect x="-62" y="-50" width="24" height="50" rx="8"/><rect x="-28" y="-50" width="22" height="50" rx="8"/><rect x="18" y="-50" width="22" height="50" rx="8"/><rect x="50" y="-50" width="24" height="50" rx="8"/><ellipse cx="0" cy="-84" rx="92" ry="58"/><circle cx="90" cy="-104" r="42"/><path d="M118 -96 Q150 -80 140 -34 Q138 -14 124 -16 Q132 -40 126 -62 Q112 -70 108 -80Z"/><path d="M72 -112 Q40 -118 44 -80 Q54 -50 78 -64Z" opacity=".85"/><path d="M118 -90 Q136 -78 126 -64" fill="none" stroke="#f3ead2" stroke-width="5" stroke-linecap="round"/></g>`;\n\n  const WP = {\n    day: { name: \'Day\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="1280" cy="170" r="150" fill="url(#sun)"/><circle cx="1280" cy="170" r="62" fill="#fff3b0"/>${cloud(300,190,1.4,.9)}${cloud(760,120,1,.8)}${cloud(1000,290,1.2,.85)}${hills(640,110,\'#7cc47a\',1)}${hills(720,90,\'#4fa05a\',2)}${hills(800,70,\'#2f7d45\',3)}`, lg(\'a\',[[0,\'#5fb7f2\'],[1,\'#d9f1ff\']]) + rg(\'sun\',[[0,\'#fff6c2\',.95],[1,\'#fff6c2\',0]])) },\n    night: { name: \'Night\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/>${stars(260)}<circle cx="1250" cy="170" r="120" fill="url(#mg)"/><circle cx="1250" cy="170" r="48" fill="#f4efd6"/><circle cx="1234" cy="158" r="9" fill="#e0d9b8" opacity=".7"/><circle cx="1268" cy="188" r="12" fill="#e0d9b8" opacity=".6"/>${hills(700,100,\'#0b1424\',4)}${hills(790,70,\'#070d19\',6)}`, lg(\'a\',[[0,\'#04060f\'],[.7,\'#101d3a\'],[1,\'#1d3159\']]) + rg(\'mg\',[[0,\'#f4efd6\',.35],[1,\'#f4efd6\',0]])) },\n    sea: { name: \'Sea\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="1180" cy="330" r="190" fill="url(#sun)"/><circle cx="1180" cy="330" r="64" fill="#fff4c4"/>${cloud(320,170,1.3,.75)}${cloud(820,240,.9,.6)}<rect y="440" width="${W}" height="6" fill="#bfe9ff" opacity=".6"/>${wave(470,10,260,\'#2a8fd0\',.9)}${wave(560,14,300,\'#1b74b8\',.95)}${wave(660,18,340,\'#125a98\')}${wave(770,22,380,\'#0b4378\')}<rect x="1100" y="446" width="160" height="14" fill="#fff4c4" opacity=".35"/><rect x="1130" y="470" width="100" height="8" fill="#fff4c4" opacity=".3"/>${bird(500,260,1.1)}${bird(580,230,.8)}`, lg(\'a\',[[0,\'#59b9f0\'],[.5,\'#a9e0f7\'],[1,\'#e9f7ff\']]) + rg(\'sun\',[[0,\'#fff6c2\',.9],[1,\'#fff6c2\',0]])) },\n    forest: { name: \'Forest\', build: () => { seed = 21; let t1 = \'\', t2 = \'\', t3 = \'\'; for (let i = 0; i < 16; i++) t1 += pine(i * 110 + sr() * 40, 600, 220 + sr() * 120, \'#3f8f58\'); for (let i = 0; i < 14; i++) t2 += pine(i * 125 + sr() * 50 + 30, 690, 300 + sr() * 150, \'#246b3f\'); for (let i = 0; i < 11; i++) t3 += pine(i * 160 + sr() * 60, 820, 420 + sr() * 200, \'#0f4727\'); return S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="1130" cy="190" r="170" fill="url(#sun)"/>${t1}<rect y="560" width="${W}" height="340" fill="url(#mist)"/>${t2}${t3}<rect y="810" width="${W}" height="90" fill="#0b3a1f"/>`, lg(\'a\',[[0,\'#f6e7b4\'],[.45,\'#bfe3b4\'],[1,\'#7fbf86\']]) + rg(\'sun\',[[0,\'#fff3c4\',.95],[1,\'#fff3c4\',0]]) + lg(\'mist\',[[0,\'#d4efe0\',0],[.5,\'#d4efe0\',.55],[1,\'#d4efe0\',0]])); } },\n    desert: { name: \'Desert\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="1050" cy="400" r="220" fill="url(#sun)"/><circle cx="1050" cy="400" r="86" fill="#fff1c9"/><path d="M0 560 Q260 430 560 540 T1120 520 T1600 560 V900 H0Z" fill="#d58f4f"/><path d="M0 650 Q300 540 640 640 T1300 610 T1600 660 V900 H0Z" fill="#c0753a"/><path d="M0 760 Q350 660 760 760 T1600 740 V900 H0Z" fill="#a85f2c"/>${acacia(300,690,1.2)}`, lg(\'a\',[[0,\'#f08a5d\'],[.5,\'#ffc27a\'],[1,\'#ffe9b8\']]) + rg(\'sun\',[[0,\'#fff1c9\',.9],[1,\'#fff1c9\',0]])) },\n    sky: { name: \'Sky\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/>${cloud(250,640,2.4,.95)}${cloud(700,520,2,.9)}${cloud(1150,700,2.6,.95)}${cloud(1450,430,1.7,.85)}${cloud(480,300,1.4,.8)}${cloud(980,220,1.2,.75)}${cloud(120,200,1.1,.7)}${bird(900,380,1.4)}${bird(980,350,1)}${bird(1040,395,1.2)}`, lg(\'a\',[[0,\'#1c7fd6\'],[.6,\'#6fc0f5\'],[1,\'#d3efff\']])) },\n    sunset: { name: \'Sunset\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="800" cy="560" r="260" fill="url(#sun)"/><circle cx="800" cy="560" r="110" fill="#ffd59a"/>${cloud(300,300,1.5,.55)}${cloud(1250,250,1.6,.5)}${wave(600,6,240,\'#c8567a\',.8)}${wave(660,10,300,\'#8c3a80\',.9)}${wave(740,14,340,\'#4a2670\')}${wave(830,18,380,\'#2a1750\')}<rect x="720" y="560" width="160" height="10" fill="#ffd59a" opacity=".5"/><rect x="740" y="590" width="120" height="8" fill="#ffd59a" opacity=".4"/>`, lg(\'a\',[[0,\'#2d1b5e\'],[.35,\'#b0457c\'],[.7,\'#ff8f5a\'],[1,\'#ffd08a\']]) + rg(\'sun\',[[0,\'#ffd59a\',.7],[1,\'#ffd59a\',0]])) },\n    mountains: { name: \'Mountains\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/>${cloud(400,200,1.2,.7)}${cloud(1200,150,1,.6)}<polygon points="0,640 300,280 520,520 700,360 980,650" fill="#6f87a8"/><polygon points="500,700 900,200 1300,700" fill="#4f688b"/><polygon points="900,200 830,300 880,290 920,330 950,290 990,300" fill="#fff"/><polygon points="900,200 1300,700 1000,700" fill="#000" opacity=".15"/><polygon points="1000,700 1350,330 1600,620 1600,700" fill="#8aa0bf"/>${hills(760,60,\'#2f6b4a\',7)}${hills(830,40,\'#1d4f36\',8)}<rect y="840" width="${W}" height="60" fill="#133a28"/>`, lg(\'a\',[[0,\'#7ab6ef\'],[1,\'#e3f3ff\']])) },\n    aurora: { name: \'Aurora\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/>${stars(220)}<path d="M0 360 Q300 150 620 300 T1250 220 T1600 330 L1600 520 Q1300 360 1000 480 T380 450 T0 560Z" fill="url(#g1)" opacity=".75" filter="url(#bl)"/><path d="M0 450 Q350 280 700 400 T1300 330 T1600 420 L1600 560 Q1300 460 950 560 T350 540 T0 620Z" fill="url(#g2)" opacity=".5" filter="url(#bl)"/>${hills(740,60,\'#050b16\',9)}${pine(150,800,160,\'#030812\')}${pine(240,820,220,\'#030812\')}${pine(1380,810,200,\'#030812\')}${pine(1470,830,250,\'#030812\')}<rect y="800" width="${W}" height="100" fill="#030812"/>`, lg(\'a\',[[0,\'#02040c\'],[1,\'#0a1a2e\']]) + lg(\'g1\',[[0,\'#3cffb0\',0],[.5,\'#3cffb0\',.9],[1,\'#4a9dff\',0]]) + lg(\'g2\',[[0,\'#b36bff\',0],[.5,\'#6bd6ff\',.7],[1,\'#3cffb0\',0]]) + `<filter id="bl"><feGaussianBlur stdDeviation="22"/></filter>`) },\n    savanna: { name: \'Savanna animals\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/><circle cx="1000" cy="520" r="260" fill="url(#sun)"/><circle cx="1000" cy="520" r="96" fill="#ffe3a0"/>${hills(640,30,\'#8a5a22\',2)}<rect y="640" width="${W}" height="260" fill="#5a3c16"/>${acacia(260,660,1.5)}${acacia(1340,650,1.2)}${giraffe(520,680,1.5)}${giraffe(640,690,1.15)}${elephant(1050,700,1.25)}${elephant(1240,690,.8)}${bird(700,260,1.2)}${bird(780,230,.9)}`, lg(\'a\',[[0,\'#e8573a\'],[.5,\'#ff9d4a\'],[1,\'#ffd98a\']]) + rg(\'sun\',[[0,\'#ffe3a0\',.8],[1,\'#ffe3a0\',0]])) },\n    underwater: { name: \'Underwater\', build: () => { seed = 3; let f = \'\'; const cols = [\'#ffb347\',\'#ff6f61\',\'#ffe66d\',\'#7ee8fa\',\'#c792ea\']; for (let i = 0; i < 14; i++) f += fish(sr() * 1400 + 60, sr() * 560 + 140, sr() * 0.9 + 0.5, cols[i % 5], i % 2 ? 1 : -1); let b = \'\'; for (let i = 0; i < 40; i++) b += `<circle cx="${sr()*W|0}" cy="${sr()*H|0}" r="${(sr()*9+2).toFixed(1)}" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>`; let k = \'\'; for (let i = 0; i < 18; i++) k += `<path d="M${i*95+20} 900 q-30 -90 0 -170 q30 -70 0 -150" fill="none" stroke="#1d9b6a" stroke-width="12" stroke-linecap="round" opacity=".85"/>`; return S(`<rect width="${W}" height="${H}" fill="url(#a)"/><polygon points="500,0 700,0 900,900 300,900" fill="#fff" opacity=".06"/><polygon points="1000,0 1160,0 1500,900 1000,900" fill="#fff" opacity=".05"/>${b}${f}${k}<path d="M0 860 Q300 800 640 860 T1600 850 V900 H0Z" fill="#d8b878"/>`, lg(\'a\',[[0,\'#38c6e8\'],[.5,\'#1272b8\'],[1,\'#07305e\']])); } },\n    earth: { name: \'Earth from orbit\', build: () => S(`<rect width="${W}" height="${H}" fill="#02040a"/>${stars(300)}<circle cx="800" cy="1500" r="1000" fill="url(#halo)"/><circle cx="800" cy="1500" r="930" fill="url(#ea)"/><ellipse cx="620" cy="640" rx="160" ry="70" fill="#4f8a4a" opacity=".85" transform="rotate(-18 620 640)"/><ellipse cx="1000" cy="680" rx="210" ry="60" fill="#6a9a52" opacity=".8" transform="rotate(10 1000 680)"/><ellipse cx="800" cy="600" rx="260" ry="36" fill="#fff" opacity=".35"/><ellipse cx="400" cy="720" rx="200" ry="30" fill="#fff" opacity=".3"/><ellipse cx="1250" cy="760" rx="220" ry="34" fill="#fff" opacity=".3"/>`, rg(\'halo\',[[.9,\'#5db4ff\',.45],[1,\'#5db4ff\',0]]) + rg(\'ea\',[[0,\'#2f7bd0\'],[.8,\'#154a96\'],[1,\'#0a2a5e\']])) },\n    galaxy: { name: \'Galaxy\', build: () => S(`<rect width="${W}" height="${H}" fill="url(#a)"/>${stars(320)}<ellipse cx="800" cy="450" rx="760" ry="170" fill="url(#g)" transform="rotate(-24 800 450)" filter="url(#bl)"/><ellipse cx="800" cy="450" rx="420" ry="80" fill="#ffe9c4" opacity=".28" transform="rotate(-24 800 450)" filter="url(#bl)"/><circle cx="1250" cy="200" r="46" fill="url(#pl)"/><ellipse cx="1250" cy="200" rx="86" ry="14" fill="none" stroke="#e3c7a0" stroke-width="5" opacity=".7" transform="rotate(-18 1250 200)"/>`, rg(\'a\',[[0,\'#1a1040\'],[1,\'#03030c\']]) + rg(\'g\',[[0,\'#d58bff\',.55],[.6,\'#5a6bff\',.25],[1,\'#5a6bff\',0]]) + rg(\'pl\',[[0,\'#f2b27a\'],[1,\'#a55a2a\']]) + `<filter id="bl"><feGaussianBlur stdDeviation="28"/></filter>`) },\n  };\n  // ---- deep-space wallpapers (generated, no image files needed) ----\n  const SP = (inner, defs = \'\') => S(inner, defs);\n  const starsAll = (n, sd = 31, tint = true) => { seed = sd; const tc = [\'#fff\', \'#fff\', \'#fff\', \'#cfe3ff\', \'#ffe6c8\', \'#ffd0d0\']; return Array.from({ length: n }, () => { const r = sr() ** 2.2 * 1.9 + 0.35, c = tint ? tc[sr() * tc.length | 0] : \'#fff\'; return `<circle cx="${sr()*W|0}" cy="${sr()*H|0}" r="${r.toFixed(2)}" fill="${c}" opacity="${(sr()*0.55+0.4).toFixed(2)}"/>`; }).join(\'\'); };\n  const sparkle = (x, y, s, c = \'#fff\') => `<g transform="translate(${x} ${y})" opacity=".95"><path d="M0 ${-s} Q${s*.08} ${-s*.08} ${s} 0 Q${s*.08} ${s*.08} 0 ${s} Q${-s*.08} ${s*.08} ${-s} 0 Q${-s*.08} ${-s*.08} 0 ${-s}Z" fill="${c}"/><circle r="${s*.12}" fill="#fff"/></g>`;\n  // one cloud layer of fractal noise tinted with [r,g,b] (0..1). k = contrast, off = threshold\n  const cloudF = (id, sd, fx, fy, rgb, k = 2.4, off = -0.78, oct = 5) => `<filter id="${id}" filterUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency="${fx} ${fy}" numOctaves="${oct}" seed="${sd}"/><feColorMatrix type="matrix" values="0 0 0 0 ${rgb[0]}  0 0 0 0 ${rgb[1]}  0 0 0 0 ${rgb[2]}  ${k} 0 0 0 ${off}"/></filter>`;\n  const nlayer = (id, mask, op = 1) => `<rect width="${W}" height="${H}" filter="url(#${id})" opacity="${op}"${mask ? ` mask="url(#${mask})"` : \'\'}/>`;\n  const blob = (id, cx, cy, rx, ry, rot = 0) => `<radialGradient id="${id}g"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient><mask id="${id}" maskUnits="userSpaceOnUse" x="0" y="0" width="${W}" height="${H}"><ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" transform="rotate(${rot} ${cx} ${cy})" fill="url(#${id}g)"/></mask>`;\n  const sphere = (id, cx, cy, r, c0, c1, c2) => `<radialGradient id="${id}" cx=".34" cy=".3" r=".85"><stop offset="0" stop-color="${c0}"/><stop offset=".55" stop-color="${c1}"/><stop offset="1" stop-color="${c2}"/></radialGradient>`;\n\n  Object.assign(WP, {\n    nebula_orion: { grp: \'space\', name: \'Pink nebula\', build: () => SP(`<rect width="${W}" height="${H}" fill="#05030d"/>${nlayer(\'f1\',\'m1\',.95)}${nlayer(\'f2\',\'m2\',.9)}${nlayer(\'f3\',\'m3\',.85)}${starsAll(380,12)}${sparkle(1180,300,46,\'#ffd9ee\')}${sparkle(420,620,30,\'#cfe3ff\')}`,\n      cloudF(\'f1\',4,.0032,.0046,[.95,.25,.62]) + blob(\'m1\',620,430,760,380,-14) + cloudF(\'f2\',9,.0045,.0036,[.28,.42,1],2.2,-.7) + blob(\'m2\',1030,520,640,330,18) + cloudF(\'f3\',17,.006,.007,[1,.74,.42],2.6,-.95) + blob(\'m3\',760,380,420,210,-6)) },\n    nebula_emerald: { grp: \'space\', name: \'Emerald nebula\', build: () => SP(`<rect width="${W}" height="${H}" fill="#020a0c"/>${nlayer(\'f1\',\'m1\',.95)}${nlayer(\'f2\',\'m2\',.8)}${starsAll(340,5)}${sparkle(300,210,38,\'#d4ffec\')}`,\n      cloudF(\'f1\',21,.0036,.005,[.13,.9,.62],2.3,-.75) + blob(\'m1\',820,470,820,380,10) + cloudF(\'f2\',33,.005,.004,[.22,.55,1],2.4,-.9) + blob(\'m2\',520,380,520,250,-22)) },\n    nebula_crimson: { grp: \'space\', name: \'Crimson veil\', build: () => SP(`<rect width="${W}" height="${H}" fill="#0a0305"/>${nlayer(\'f1\',\'m1\',.95)}${nlayer(\'f2\',\'m2\',.85)}${nlayer(\'f3\',\'m3\',.7)}${starsAll(360,8)}${sparkle(1320,170,34,\'#ffe3cf\')}`,\n      cloudF(\'f1\',40,.003,.0052,[.95,.18,.2],2.4,-.8) + blob(\'m1\',760,450,780,370,-8) + cloudF(\'f2\',51,.0042,.0042,[1,.58,.18],2.5,-.92) + blob(\'m2\',980,400,520,250,24) + cloudF(\'f3\',62,.006,.006,[.55,.2,.95],2.4,-.95) + blob(\'m3\',420,560,430,230,-30)) },\n    nebula_pillars: { grp: \'space\', name: \'Dust pillars\', build: () => SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${nlayer(\'f1\',\'m1\',.9)}${nlayer(\'f2\',\'m2\',.75)}<g fill="#241309" opacity=".93"><path d="M300 900 C 290 700 330 560 350 470 C 360 400 410 380 430 440 C 460 520 470 650 480 900Z"/><path d="M640 900 C 630 680 650 480 690 360 C 710 300 760 290 780 350 C 810 450 800 700 830 900Z"/><path d="M980 900 C 985 740 1000 640 1030 580 C 1050 540 1090 548 1100 590 C 1120 680 1110 800 1130 900Z"/></g><g fill="#ffb86b" opacity=".5"><path d="M352 470 C 360 400 410 380 430 440 C 410 430 380 440 352 470Z"/><path d="M692 360 C 710 300 760 290 780 350 C 755 335 720 335 692 360Z"/></g>${starsAll(300,19)}${sparkle(1240,250,34,\'#fff1d6\')}`,\n      lg(\'bg\',[[0,\'#0b0620\'],[.6,\'#3a1b2e\'],[1,\'#7a3b1e\']]) + cloudF(\'f1\',72,.004,.006,[1,.55,.3],2.3,-.8) + blob(\'m1\',800,420,820,380,0) + cloudF(\'f2\',83,.006,.005,[.35,.55,1],2.3,-.95) + blob(\'m2\',1100,300,520,260,-15)) },\n    planet_gas: { grp: \'space\', name: \'Gas giant\', build: () => { let b = \'\'; const bands = [[\'#d9a066\',.0,.1],[\'#f1d3a3\',.1,.2],[\'#b9733f\',.2,.28],[\'#e8c08c\',.28,.42],[\'#a35d34\',.42,.5],[\'#f0d9b5\',.5,.62],[\'#c98a52\',.62,.74],[\'#8e4f2c\',.74,.86],[\'#d8a06a\',.86,1]]; bands.forEach(([c, a, z]) => { b += `<rect x="150" y="${150+a*700}" width="700" height="${(z-a)*700+1}" fill="${c}"/>`; }); return SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${starsAll(300,23)}<g transform="translate(920 -30)"><circle cx="500" cy="480" r="470" fill="url(#halo)"/><g clip-path="url(#pc)">${b.replace(/x="150"/g,\'x="0"\').replace(/width="700"/g,\'width="1000"\')}<ellipse cx="560" cy="640" rx="64" ry="34" fill="#b5482f" opacity=".85"/><ellipse cx="560" cy="640" rx="40" ry="20" fill="#d9704a" opacity=".7"/></g><circle cx="500" cy="480" r="400" fill="url(#shade)"/></g><circle cx="560" cy="210" r="46" fill="url(#moon)"/><circle cx="560" cy="210" r="46" fill="url(#moonsh)"/>`,\n      lg(\'bg\',[[0,\'#02030a\'],[1,\'#0a1024\']]) + rg(\'halo\',[[.8,\'#ffb877\',.3],[1,\'#ffb877\',0]]) + `<clipPath id="pc"><circle cx="500" cy="480" r="400"/></clipPath>` + `<radialGradient id="shade" cx=".28" cy=".32" r=".95"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset=".8" stop-color="#000" stop-opacity=".55"/><stop offset="1" stop-color="#000" stop-opacity=".92"/></radialGradient>` + sphere(\'moon\',0,0,0,\'#e9e6df\',\'#b8b2a6\',\'#6c675f\') + `<radialGradient id="moonsh" cx=".3" cy=".3" r=".9"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".7"/></radialGradient>`); } },\n    planet_ring: { grp: \'space\', name: \'Ringed planet\', build: () => SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${starsAll(330,27)}<g transform="rotate(-16 800 470)"><path d="M310 470 a490 112 0 0 1 980 0 a490 112 0 0 1 -980 0Z M420 470 a380 82 0 0 0 760 0 a380 82 0 0 0 -760 0Z" fill="url(#rg)" fill-rule="evenodd" opacity=".55" clip-path="url(#back)"/><circle cx="800" cy="470" r="215" fill="url(#pl)"/><circle cx="800" cy="470" r="215" fill="url(#plsh)"/><path d="M310 470 a490 112 0 0 0 980 0 a490 112 0 0 0 -980 0Z M420 470 a380 82 0 0 1 760 0 a380 82 0 0 1 -760 0Z" fill="url(#rg)" fill-rule="evenodd" opacity=".9" clip-path="url(#front)"/></g>${sparkle(1350,170,28,\'#cfe3ff\')}`,\n      lg(\'bg\',[[0,\'#05060f\'],[1,\'#141030\']]) + `<clipPath id="back"><rect x="0" y="0" width="${W}" height="470"/></clipPath><clipPath id="front"><rect x="0" y="470" width="${W}" height="500"/></clipPath>` + `<linearGradient id="rg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d7a63"/><stop offset=".3" stop-color="#e8d4b0"/><stop offset=".55" stop-color="#b79c78"/><stop offset=".8" stop-color="#f1e1c3"/><stop offset="1" stop-color="#8d7a63"/></linearGradient>` + sphere(\'pl\',0,0,0,\'#f6d9a8\',\'#c98f58\',\'#5a3320\') + `<radialGradient id="plsh" cx=".3" cy=".3" r=".95"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".78"/></radialGradient>`) },\n    planet_mars: { grp: \'space\', name: \'Red planet\', build: () => { seed = 90; let c = \'\'; for (let i = 0; i < 26; i++) { const a = sr() * 6.28, d = sr() ** .6 * 560, x = 800 + Math.cos(a) * d, y = 1180 + Math.sin(a) * d * .6 - 280, r = 8 + sr() * 36; c += `<ellipse cx="${x|0}" cy="${y|0}" rx="${r}" ry="${r*.55}" fill="#5e2414" opacity=".3"/>`; } return SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${starsAll(260,29)}<circle cx="800" cy="1260" r="1100" fill="url(#atm)"/><g clip-path="url(#pc)"><circle cx="800" cy="1260" r="1040" fill="url(#pl)"/>${c}<path d="M0 760 Q300 700 640 760 T1300 740 T1600 780 V900 H0Z" fill="#7a2d18" opacity=".35"/></g><circle cx="800" cy="1260" r="1040" fill="url(#sh)"/><circle cx="1180" cy="210" r="22" fill="url(#moon)"/><circle cx="340" cy="320" r="11" fill="#b8b2a6"/>`,\n      lg(\'bg\',[[0,\'#05040a\'],[1,\'#1a0d12\']]) + rg(\'atm\',[[.9,\'#ff9a6a\',.5],[1,\'#ff9a6a\',0]]) + `<clipPath id="pc"><circle cx="800" cy="1260" r="1040"/></clipPath>` + sphere(\'pl\',0,0,0,\'#e58a55\',\'#b4492a\',\'#4a1a10\') + `<radialGradient id="sh" cx=".5" cy=".28" r=".72"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>` + sphere(\'moon\',0,0,0,\'#d9d4c8\',\'#9a9488\',\'#5a554c\')); } },\n    sunrise_orbit: { grp: \'space\', name: \'Orbital sunrise\', build: () => SP(`<rect width="${W}" height="${H}" fill="#02040a"/>${starsAll(300,35)}<circle cx="800" cy="1560" r="1100" fill="url(#halo)"/><circle cx="800" cy="1560" r="1010" fill="url(#ea)"/><ellipse cx="620" cy="720" rx="260" ry="40" fill="#fff" opacity=".28"/><ellipse cx="1120" cy="770" rx="300" ry="46" fill="#fff" opacity=".26"/><ellipse cx="800" cy="545" rx="620" ry="9" fill="url(#rim)"/><circle cx="800" cy="548" r="150" fill="url(#flare)"/><circle cx="800" cy="548" r="22" fill="#fff"/><rect x="540" y="545" width="520" height="3" fill="#fff" opacity=".7"/>`,\n      rg(\'halo\',[[.88,\'#5db4ff\',.55],[1,\'#5db4ff\',0]]) + rg(\'ea\',[[0,\'#1d5cb0\'],[.8,\'#0f3a78\'],[1,\'#071c40\']]) + `<linearGradient id="rim" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7cc4ff" stop-opacity="0"/><stop offset=".5" stop-color="#ffe9bd"/><stop offset="1" stop-color="#7cc4ff" stop-opacity="0"/></linearGradient>` + rg(\'flare\',[[0,\'#fff6dc\',.95],[.25,\'#ffd98a\',.55],[1,\'#ffb347\',0]])) },\n    milkyway: { grp: \'space\', name: \'Milky Way\', build: () => SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${nlayer(\'f1\',\'m1\',.8)}${nlayer(\'f2\',\'m2\',.6)}${starsAll(900,41)}<path d="M0 1000 Q500 800 800 900 T1600 760 V900 H0Z" fill="#04070d"/><path d="M0 860 L90 820 L130 850 L210 790 L300 840 L380 800 L470 860 L560 826 L650 880 L720 900 H0Z" fill="#02040a"/>`,\n      lg(\'bg\',[[0,\'#02030a\'],[1,\'#0b1326\']]) + cloudF(\'f1\',101,.004,.0075,[.78,.7,.95],2.6,-.9) + blob(\'m1\',800,420,900,170,-24) + cloudF(\'f2\',113,.007,.009,[1,.8,.55],2.8,-1.05) + blob(\'m2\',800,430,620,100,-24)) },\n    blackhole: { grp: \'space\', name: \'Black hole\', build: () => SP(`<rect width="${W}" height="${H}" fill="#020106"/>${starsAll(320,47)}<ellipse cx="800" cy="450" rx="560" ry="64" fill="url(#acc)" opacity=".9" transform="rotate(-8 800 450)" filter="url(#bl)"/><ellipse cx="800" cy="450" rx="470" ry="22" fill="url(#acc2)" transform="rotate(-8 800 450)"/><circle cx="800" cy="450" r="120" fill="#000"/><circle cx="800" cy="450" r="124" fill="none" stroke="#ffd9a0" stroke-width="3" opacity=".85"/><path d="M360 436 Q800 280 1240 392" fill="none" stroke="#ffcf8a" stroke-width="16" opacity=".5" filter="url(#bl)"/><path d="M360 470 Q800 640 1240 508" fill="none" stroke="#ff9a4a" stroke-width="12" opacity=".4" filter="url(#bl)"/>`,\n      `<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff5a1a" stop-opacity="0"/><stop offset=".3" stop-color="#ff9a3a"/><stop offset=".5" stop-color="#fff0c4"/><stop offset=".7" stop-color="#ff8a3a"/><stop offset="1" stop-color="#ff5a1a" stop-opacity="0"/></linearGradient><linearGradient id="acc2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffc67a" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#ffc67a" stop-opacity="0"/></linearGradient><filter id="bl"><feGaussianBlur stdDeviation="14"/></filter>`) },\n    comet: { grp: \'space\', name: \'Comet\', build: () => SP(`<rect width="${W}" height="${H}" fill="url(#bg)"/>${starsAll(420,53)}<path d="M1180 250 L-40 760 L-40 640Z" fill="url(#tail)" filter="url(#bl)"/><path d="M1180 250 L100 640 L100 600Z" fill="url(#tail2)" opacity=".8"/><circle cx="1180" cy="250" r="90" fill="url(#coma)"/><circle cx="1180" cy="250" r="16" fill="#fff"/>${sparkle(300,160,30,\'#d5e6ff\')}`,\n      lg(\'bg\',[[0,\'#030615\'],[1,\'#0d1a3a\']]) + `<linearGradient id="tail" gradientUnits="userSpaceOnUse" x1="1180" y1="250" x2="-40" y2="700"><stop offset="0" stop-color="#bfe6ff" stop-opacity=".95"/><stop offset=".5" stop-color="#5aa8ff" stop-opacity=".4"/><stop offset="1" stop-color="#5aa8ff" stop-opacity="0"/></linearGradient><linearGradient id="tail2" gradientUnits="userSpaceOnUse" x1="1180" y1="250" x2="100" y2="620"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#ffe3b0" stop-opacity="0"/></linearGradient>` + rg(\'coma\',[[0,\'#ffffff\',.95],[.35,\'#bfe6ff\',.55],[1,\'#bfe6ff\',0]]) + `<filter id="bl"><feGaussianBlur stdDeviation="9"/></filter>`) },\n  });\n\n  const uri = svg => \'data:image/svg+xml;utf8,\' + encodeURIComponent(svg);\n  const svgCache = {};\n  const wpUrl = k => (svgCache[k] = svgCache[k] || uri(WP[k].build()));\n\n  let userWps = lsGet(\'ax_wp_user\', []);               // [{id,name,data}]\n  let fileWps = [];                                    // images found in the "wallpapers" folder next to ASHE: [{name,url}]\n  const fileUrl = n => (fileWps.find(f => f.name === n) || {}).url || null;\n  fetch(\'/api/wallpapers\').then(r => r.json()).then(list => {\n    fileWps = Array.isArray(list) ? list : [];\n    if (curWp().startsWith(\'f:\')) applyWp(curWp());\n    if (view === \'bg\') renderWp();\n  }).catch(() => {});\n  const layer = document.createElement(\'div\'); layer.id = \'ax-bg\'; document.documentElement.appendChild(layer);\n  const curWp = () => lsGet(\'ax_bg2\', \'auto\');\n  function applyWp(choice) {\n    lsSet(\'ax_bg2\', choice);\n    let url = null;\n    if (choice === \'auto\') { const h = new Date().getHours(); url = wpUrl(h >= 6 && h < 18 ? \'day\' : \'night\'); }\n    else if (choice.startsWith(\'u:\')) { const u = userWps.find(x => x.id === choice.slice(2)); url = u ? u.data : wpUrl(\'day\'); }\n    else if (choice.startsWith(\'f:\')) { url = fileUrl(choice.slice(2)); }\n    else if (WP[choice]) url = wpUrl(choice);\n    layer.style.backgroundImage = url ? `url("${url}")` : \'none\';\n    if (url) document.documentElement.setAttribute(\'data-wp\', choice); else document.documentElement.removeAttribute(\'data-wp\');\n  }\n  applyWp(curWp());\n  setInterval(() => { if (curWp() === \'auto\') applyWp(\'auto\'); }, 60000);\n\n  function addUserWp(file) {\n    if (!file || !file.type.startsWith(\'image/\')) return;\n    const fr = new FileReader();\n    fr.onload = () => {\n      const img = new Image();\n      img.onload = () => {\n        const sc = Math.min(1, 1600 / img.width), c = document.createElement(\'canvas\');\n        c.width = Math.round(img.width * sc); c.height = Math.round(img.height * sc);\n        c.getContext(\'2d\').drawImage(img, 0, 0, c.width, c.height);\n        const data = c.toDataURL(\'image/jpeg\', 0.82), id = String(Date.now());\n        const keep = userWps;\n        userWps = [{ id, name: file.name.replace(/\\.[^.]+$/, \'\').slice(0, 18) || \'My image\', data }, ...userWps].slice(0, 6);\n        if (!lsSet(\'ax_wp_user\', userWps)) { userWps = keep; alert(\'Not enough storage for this image. Delete one of your images first.\'); return render(); }\n        applyWp(\'u:\' + id); render();\n      };\n      img.src = fr.result;\n    };\n    fr.readAsDataURL(file);\n  }\n  function delUserWp(id) {\n    userWps = userWps.filter(x => x.id !== id); lsSet(\'ax_wp_user\', userWps);\n    if (curWp() === \'u:\' + id) applyWp(\'auto\'); render();\n  }\n  function renderWp() {\n    const cur = curWp();\n    const item = (key, name, bg, extra = \'\') => `<button class="ax-wp-item ${cur === key ? \'sel\' : \'\'}" data-key="${esc(key)}" onclick="ax.setWp(this.dataset.key)"><div class="im" data-k="${esc(key)}"></div><div class="nm">${esc(name)}</div>${extra}</button>`;\n    const keys = Object.keys(WP), space = keys.filter(k => WP[k].grp === \'space\'), earth = keys.filter(k => WP[k].grp !== \'space\');\n    panel.innerHTML = `<h2>Wallpaper</h2>\n      <p class="ax-muted">“Auto” follows the real time on Earth: day wallpaper from 6 AM to 6 PM, night wallpaper after that.</p>\n      <h3>Space · nebulae, planets &amp; deep space</h3>\n      <div class="ax-wp">${space.map(k => item(k, WP[k].name)).join(\'\')}</div>\n      ${fileWps.length ? `<h3>Your space pictures (wallpapers folder)</h3><div class="ax-wp">${fileWps.map(f => item(\'f:\' + f.name, f.name.replace(/\\.[^.]+$/, \'\').replace(/[_-]+/g, \' \').slice(0, 22))).join(\'\')}</div>` : \'\'}\n      <h3>Scenes</h3>\n      <div class="ax-wp">\n        ${item(\'auto\', \'Auto (day / night)\')}\n        ${earth.map(k => item(k, WP[k].name)).join(\'\')}\n        ${userWps.map(u => item(\'u:\' + u.id, u.name, \'\', `<span class="x" onclick="event.stopPropagation();ax.delWp(\'${u.id}\')" title="Delete">×</span>`)).join(\'\')}\n        ${item(\'none\', \'None (plain theme)\')}\n      </div>\n      <h3>Add your own</h3>\n      <p class="ax-muted">Pick any photo from this computer to use as a wallpaper (up to 6 are kept).</p>\n      <div class="ax-row"><input type="file" id="ax-wp-file" accept="image/*" style="display:none" onchange="ax.addWp(this.files[0])">\n        <button class="ax-btn primary" onclick="document.getElementById(\'ax-wp-file\').click()">Choose image…</button>\n        <button class="ax-btn" onclick="ax.close()">Close</button></div>`;\n    panel.querySelectorAll(\'.ax-wp-item .im\').forEach(el => {\n      const k = el.dataset.k; let url = null;\n      if (k === \'auto\') { const h = new Date().getHours(); url = wpUrl(h >= 6 && h < 18 ? \'day\' : \'night\'); }\n      else if (k.startsWith(\'u:\')) { const u = userWps.find(x => x.id === k.slice(2)); url = u && u.data; }\n      else if (k.startsWith(\'f:\')) url = fileUrl(k.slice(2));\n      else if (WP[k]) url = wpUrl(k);\n      if (url) el.style.backgroundImage = \'url("\' + url + \'")\';\n      else { el.style.background = \'repeating-linear-gradient(45deg,var(--panel2),var(--panel2) 8px,var(--chip) 8px,var(--chip) 16px)\'; }\n    });\n  }\n\n  // ================= sound =================\n  let ac = null, musicOn = true, musicIv = null, mi = 0;\n  const FREQ = [262, 330, 392, 523];\n  const MELODY = [523, 659, 784, 659, 523, 392, 440, 523];\n  function tone(f, d = 0.25, type = \'sine\') {\n    try {\n      ac = ac || new (window.AudioContext || window.webkitAudioContext)();\n      if (ac.state === \'suspended\') ac.resume();\n      const o = ac.createOscillator(), gn = ac.createGain();\n      o.type = type; o.frequency.value = f;\n      gn.gain.setValueAtTime(0.22, ac.currentTime);\n      gn.gain.exponentialRampToValueAtTime(0.001, ac.currentTime + d);\n      o.connect(gn).connect(ac.destination); o.start(); o.stop(ac.currentTime + d);\n    } catch (e) {}\n  }\n  function startMusic() { if (musicIv) return; musicIv = setInterval(() => { if (musicOn && g && !g.over) tone(MELODY[mi++ % MELODY.length] / 2, 0.18, \'triangle\'); }, 300); }\n  function stopMusic() { clearInterval(musicIv); musicIv = null; }\n\n  // ================= shell: bar + modal =================\n  const modal = document.createElement(\'div\'); modal.id = \'ax-modal\';\n  const panel = document.createElement(\'div\'); panel.id = \'ax-panel\'; modal.appendChild(panel); document.body.appendChild(modal);\n  modal.addEventListener(\'mousedown\', e => { if (e.target === modal) close(); });\n  document.addEventListener(\'keydown\', e => { if (e.key === \'Escape\' && view) close(); });\n  const bar = document.createElement(\'div\'); bar.id = \'ax-bar\';\n  bar.innerHTML = `<button onclick="ax.open(\'sleep\')">😴 Sleep</button>\n    <button onclick="ax.open(\'game\')">🎮 Crew game</button>\n    <button onclick="ax.open(\'bg\')">🖼 Wallpaper</button>\n    <button id="ax-ck-btn" onclick="ax.open(\'checkin\')">📋 Daily check-in</button>\n    <button onclick="ax.open(\'diary\')">📓 Diary</button>`;\n  document.body.appendChild(bar);\n  let view = null;\n  function open(tab) { view = tab; modal.classList.add(\'open\'); render(); }\n  function close() { modal.classList.remove(\'open\'); view = null; if (g && !g.over) { gameEnd(\'quit\'); } }\n  function render() {\n    ({ sleep: renderSleep, game: renderGame, bg: renderWp, diary: renderDiary, checkin: renderCheckin }[view] || (() => {}))();\n  }\n\n  // ================= sleep tracking =================\n  let sl = null;\n  const sessions = lsGet(\'ax_sleep2\', []);\n  function findHR(s) {\n    const m = s.metrics || {};\n    for (const k of Object.keys(m)) if (/heart|hr|pulse/i.test(k)) { const v = m[k]; return typeof v === \'object\' ? v.value : v; }\n    return null;\n  }\n  function sleepStart() {\n    sl = { t0: Date.now(), hr: [] };\n    sl.iv = setInterval(async () => {\n      try { const hr = findHR(await (await fetch(\'/api/state\')).json()); if (hr != null) sl.hr.push(hr); } catch (e) {}\n      if (view === \'sleep\') renderSleep();\n    }, 5000);\n    render();\n  }\n  function sleepStop() {\n    clearInterval(sl.iv);\n    const hours = (Date.now() - sl.t0) / 36e5;\n    const avgHr = sl.hr.length ? sl.hr.reduce((a, b) => a + b, 0) / sl.hr.length : null;\n    const spikes = sl.hr.filter(x => x > 100).length;\n    const quality = avgHr == null ? null : Math.max(0, Math.min(100, Math.round(100 - Math.max(0, avgHr - 55) * 1.5 - spikes * 5)));\n    sessions.unshift({ date: Date.now(), hours: +hours.toFixed(2), avg: avgHr && Math.round(avgHr), quality });\n    sessions.splice(10); lsSet(\'ax_sleep2\', sessions);\n    sl = null; render();\n  }\n  function renderSleep() {\n    const rows = sessions.map(s => `<li><b>${fmt(s.date)}</b> &nbsp;·&nbsp; ${s.hours} h &nbsp;·&nbsp; avg pulse ${s.avg ?? \'--\'} &nbsp;·&nbsp; est. quality ${s.quality ?? \'--\'}/100</li>`).join(\'\');\n    panel.innerHTML = `<h2>Sleep tracking</h2>\n      <p class="ax-muted">The score is estimated from pulse readings only. It is not a medical measurement of sleep stages. Keep ASHE open while you sleep.</p>\n      ${sl ? `<p>Sleep session running for <b>${Math.max(0, Math.round((Date.now() - sl.t0) / 60000))} min</b> (${sl.hr.length} pulse samples).</p>\n              <div class="ax-row"><button class="ax-btn primary" onclick="ax.sleepStop()">I\'m awake</button><button class="ax-btn" onclick="ax.close()">Close</button></div>`\n           : `<div class="ax-row"><button class="ax-btn primary" onclick="ax.sleepStart()">Start sleeping</button><button class="ax-btn" onclick="ax.close()">Close</button></div>`}\n      <h3>Last sessions</h3><ul class="ax-list">${rows || \'<li class="ax-muted">No sessions yet.</li>\'}</ul>`;\n  }\n\n  // ================= crew game (max 4 min) =================\n  let g = null;\n  let crew = lsGet(\'ax_crew\', [\'Commander\', \'Crew 1\', \'Crew 2\']);\n  const PAD_COLORS = [\'#e74c3c\', \'#f1c40f\', \'#2ecc71\', \'#3498db\'];\n  function crewAdd() {\n    const el = document.getElementById(\'ax-name\'); if (!el) return;\n    const n = el.value.trim().slice(0, 20);\n    if (n && !crew.includes(n) && crew.length < 8) { crew.push(n); lsSet(\'ax_crew\', crew); }\n    renderGame();\n  }\n  function crewRemove(i) { crew.splice(i, 1); lsSet(\'ax_crew\', crew); renderGame(); }\n  function gameStart() {\n    if (!crew.length) return;\n    g = { seq: [], idx: 0, turn: 0, showing: false, over: false, left: 240, score: 0, best: +(localStorage.ax_best || 0), reason: \'\', timer: null, ivs: [] };\n    startMusic();\n    g.timer = setInterval(() => { g.left--; if (g.left <= 0) gameEnd(\'time\'); else updateHud(); }, 1000);\n    renderGame(); nextRound();\n  }\n  function nextRound() { if (!g || g.over) return; g.seq.push(Math.floor(Math.random() * 4)); g.idx = 0; showSeq(); }\n  function showSeq() {\n    g.showing = true; updateHud(); let i = 0;\n    const iv = setInterval(() => {\n      if (!g || g.over) return clearInterval(iv);\n      if (i >= g.seq.length) { clearInterval(iv); g.showing = false; updateHud(); return; }\n      flash(g.seq[i++]);\n    }, 650);\n    g.ivs.push(iv);\n  }\n  function flash(i) {\n    tone(FREQ[i]);\n    const el = document.getElementById(\'ax-pad\' + i);\n    if (el) { el.classList.add(\'on\'); setTimeout(() => el.classList.remove(\'on\'), 300); }\n  }\n  function press(p) {\n    if (!g || g.over || g.showing) return;\n    flash(p);\n    if (p !== g.seq[g.idx]) return gameEnd(\'wrong\');\n    g.idx++;\n    if (g.idx === g.seq.length) {\n      g.score = g.seq.length; g.turn++;\n      g.best = Math.max(g.best, g.score); localStorage.ax_best = g.best;\n      g.showing = true;\n      setTimeout(nextRound, 800);\n    }\n    updateHud();\n  }\n  function gameEnd(reason) {\n    if (!g || g.over) return;\n    g.over = true; g.reason = reason; clearInterval(g.timer); g.ivs.forEach(clearInterval); stopMusic();\n    if (view === \'game\') updateHud();\n  }\n  function gameReset() { if (g) { clearInterval(g.timer); g.ivs.forEach(clearInterval); } stopMusic(); g = null; renderGame(); }\n  function updateHud() {\n    if (view !== \'game\' || !g) return;\n    const $ = id => document.getElementById(id); if (!$(\'ax-hud-t\')) return;\n    $(\'ax-hud-t\').textContent = `${Math.floor(g.left / 60)}:${String(g.left % 60).padStart(2, \'0\')}`;\n    $(\'ax-hud-s\').textContent = g.score; $(\'ax-hud-b\').textContent = g.best;\n    const who = crew[g.turn % crew.length];\n    $(\'ax-status\').textContent = g.over ? (g.reason === \'time\' ? "Time\'s up! Great teamwork." : g.reason === \'wrong\' ? \'Wrong colour! Game over.\' : \'Game ended.\')\n      : g.showing ? \'Watch the colours…\' : `${who}, repeat the sequence`;\n    $(\'ax-crew\').innerHTML = crew.map((n, i) => `<span class="ax-chip ${!g.over && i === g.turn % crew.length ? \'turn\' : \'\'}">${esc(n)}</span>`).join(\' \');\n    $(\'ax-again\').style.display = g.over ? \'\' : \'none\';\n  }\n  function renderGame() {\n    if (!g) {\n      const chips = crew.map((n, i) => `<span class="ax-chip">${esc(n)} <button title="Remove" onclick="ax.crewRemove(${i})">×</button></span>`).join(\' \');\n      panel.innerHTML = `<h2>Crew game</h2>\n        <p class="ax-muted">Colour memory for the whole crew. Watch the sequence, repeat it, and take turns while it grows by one colour each round. Everyone shares one score. The game ends by itself after 4 minutes.</p>\n        <h3>Crew names</h3>\n        <div class="ax-row">${chips || \'<span class="ax-muted">Add at least one name.</span>\'}</div>\n        <div class="ax-row"><input id="ax-name" class="ax-in ax-grow" maxlength="20" placeholder="Type a name and press Enter" autocomplete="off" onkeydown="if(event.key===\'Enter\'){ax.crewAdd();}">\n          <button class="ax-btn" onclick="ax.crewAdd()">Add</button></div>\n        <div class="ax-row"><button class="ax-btn primary" ${crew.length ? \'\' : \'disabled\'} onclick="ax.gameStart()">Start game</button><button class="ax-btn" onclick="ax.close()">Close</button></div>\n        <p class="ax-muted">Best score: ${localStorage.ax_best || 0}</p>`;\n      const inp = document.getElementById(\'ax-name\'); if (inp) inp.focus();\n      return;\n    }\n    panel.innerHTML = `<h2>Crew game</h2>\n      <div class="ax-row" id="ax-crew"></div>\n      <div class="ax-stats"><div class="ax-stat"><b id="ax-hud-t"></b><span>time left</span></div><div class="ax-stat"><b id="ax-hud-s"></b><span>score</span></div><div class="ax-stat"><b id="ax-hud-b"></b><span>best</span></div></div>\n      <div class="ax-status" id="ax-status"></div>\n      <div class="ax-pads">${PAD_COLORS.map((c, i) => `<button class="ax-pad" id="ax-pad${i}" style="background:${c};color:${c}" onclick="ax.press(${i})" aria-label="pad ${i + 1}"></button>`).join(\'\')}</div>\n      <div class="ax-row" style="justify-content:center">\n        <button class="ax-btn" onclick="ax.toggleMusic()" id="ax-mus">♪ Music: ${musicOn ? \'on\' : \'off\'}</button>\n        <button class="ax-btn primary" id="ax-again" style="display:none" onclick="ax.gameReset()">Play again</button>\n        <button class="ax-btn" onclick="ax.close()">Close</button></div>`;\n    updateHud();\n  }\n\n  // ================= diary (stored only on this device) =================\n  const entries = lsGet(\'ax_diary2\', lsGet(\'ax_diary\', []).map(e => ({ id: e.id, date: e.id, text: e.text })));\n  const DIARY_PROMPT = \'What happened today? How are you feeling?\';\n  let diaryPrompt = DIARY_PROMPT, diaryDraft = \'\', delId = null;\n  function diarySave() {\n    const box = document.getElementById(\'ax-diary-text\');\n    const text = (box && box.value || \'\').trim();\n    if (!text) { if (box) box.focus(); return; }\n    entries.unshift({ id: Date.now(), date: Date.now(), text });\n    lsSet(\'ax_diary2\', entries); diaryDraft = \'\'; diaryPrompt = DIARY_PROMPT; renderDiary();\n  }\n  function diaryAskDelete(id) { delId = id; renderDiary(); }\n  function diaryDelete(id) {\n    const i = entries.findIndex(e => e.id === id); if (i >= 0) entries.splice(i, 1);\n    lsSet(\'ax_diary2\', entries); delId = null; renderDiary();\n  }\n  function renderDiary() {\n    const keep = document.getElementById(\'ax-diary-text\'); if (keep) diaryDraft = keep.value;\n    const list = entries.map(e => `<div class="ax-entry"><div class="ax-muted">${fmt(e.date)}</div><div class="t">${esc(e.text)}</div>\n      ${delId === e.id ? `<span class="ax-muted">Delete this entry? </span><button class="ax-btn danger" onclick="ax.diaryDelete(${e.id})">Yes, delete</button> <button class="ax-btn" onclick="ax.diaryAskDelete(null)">Cancel</button>`\n                      : `<button class="ax-btn danger" onclick="ax.diaryAskDelete(${e.id})">Delete</button>`}</div>`).join(\'\');\n    panel.innerHTML = `<h2>Diary</h2>\n      <p class="ax-muted">Write whatever is on your mind. The diary is saved on this device only. Nobody else can see it, and ASHE never reads it for analysis.</p>\n      <textarea id="ax-diary-text" class="ax-in" placeholder="${esc(diaryPrompt)}"></textarea>\n      <div class="ax-row"><button class="ax-btn primary" onclick="ax.diarySave()">Save entry</button><button class="ax-btn" onclick="ax.close()">Close</button><span class="ax-muted">Ctrl + Enter also saves</span></div>\n      <h3>Your entries (${entries.length})</h3>${list || \'<p class="ax-muted">No entries yet.</p>\'}`;\n    const t = document.getElementById(\'ax-diary-text\');\n    t.value = diaryDraft; t.focus();\n    t.addEventListener(\'keydown\', ev => { if (ev.key === \'Enter\' && (ev.ctrlKey || ev.metaKey)) { ev.preventDefault(); diarySave(); } });\n  }\n\n  // ================= daily check-in + early signals (non-diagnostic) =================\n  const CK_Q = [\n    [\'mood\', \'How is your mood today?\', \'Very low\', \'Excellent\'],\n    [\'load\', \'How heavy is your workload?\', \'Light\', \'Very heavy\'],\n    [\'team\', \'How in sync do you feel with the crew?\', \'Tense\', \'In sync\'],\n  ];\n  const checkins = lsGet(\'ax_checkins\', []);\n  const prefs = lsGet(\'ax_prefs\', { ground: false });\n  const today = () => new Date().toISOString().slice(0, 10);\n  const avg = a => a.reduce((x, y) => x + y, 0) / a.length;\n  let ckDraft = {}, signal = null;\n  function analyze() {\n    signal = null;\n    if (checkins.length < 5) return;\n    const recent = checkins.slice(-3), base = checkins.slice(-10, -3);\n    if (base.length < 2) return;\n    const flags = [];\n    if (avg(base.map(c => c.mood)) - avg(recent.map(c => c.mood)) >= 1.2) flags.push(\'mood\');\n    if (avg(recent.map(c => c.load)) - avg(base.map(c => c.load)) >= 1) flags.push(\'load\');\n    if (avg(base.map(c => c.team)) - avg(recent.map(c => c.team)) >= 1) flags.push(\'team\');\n    const lowRun = recent.every(c => c.mood <= 2);\n    if (lowRun) flags.push(\'lowrun\');\n    if (flags.length >= 2 || lowRun) {\n      const last = localStorage.ax_signal_date;\n      signal = { flags, fresh: !last || (Date.now() - new Date(last).getTime()) > 7 * 864e5 };\n    }\n  }\n  function glowCk() {\n    const b = document.getElementById(\'ax-ck-btn\'); if (!b) return;\n    const doneToday = checkins.some(c => c.date === today());\n    b.style.boxShadow = ((signal && signal.fresh) || !doneToday) ? \'0 0 0 2px var(--warn)\' : \'\';\n  }\n  function signalDone() { localStorage.ax_signal_date = today(); signal = null; glowCk(); }\n  function ckAnswer(k, v) { ckDraft[k] = v; renderCheckin(); }\n  function ckSubmit() {\n    if (!CK_Q.every(([k]) => ckDraft[k])) return;\n    checkins.push({ date: today(), ...ckDraft }); ckDraft = {};\n    checkins.sort((a, b) => a.date.localeCompare(b.date)); lsSet(\'ax_checkins\', checkins);\n    analyze(); glowCk(); renderCheckin();\n  }\n  function ckVent() { signalDone(); diaryPrompt = "What\'s on your mind right now? Write freely. Only you can see this."; open(\'diary\'); }\n  function ckChat() { signalDone(); document.getElementById(\'ax-ck-msg\').innerHTML = "<p>How are you doing with yourself today? If there\'s one small thing that made you smile, tell me about it.</p>"; }\n  function ckGround() {\n    const box = document.getElementById(\'ax-ck-msg\');\n    if (!prefs.ground) { box.innerHTML = \'<p class="ax-muted">Please tick the consent box below first.</p>\'; return; }\n    box.innerHTML = \'<p>The summary that would be sent (no details, no numbers):</p><p><i>Signs of change in mood and team cohesion over recent days. A calm follow-up is suggested.</i></p><button class="ax-btn primary" onclick="ax.ckSendGround()">Confirm</button>\';\n  }\n  function ckSendGround() {\n    const out = lsGet(\'ax_ground_outbox\', []);\n    out.push({ date: new Date().toISOString(), text: \'Signs of change over recent days - calm follow-up suggested\' });\n    lsSet(\'ax_ground_outbox\', out); signalDone();\n    document.getElementById(\'ax-ck-msg\').innerHTML = \'<p>Summary queued for sending. (Delivery to the ground console is not connected yet.)</p>\';\n  }\n  function togGround(v) { prefs.ground = !!v; lsSet(\'ax_prefs\', prefs); }\n  function renderCheckin() {\n    const done = checkins.some(c => c.date === today());\n    const ask = done ? \'<p>✅ Check-in done for today. Thank you.</p>\' :\n      CK_Q.map(([k, q, lo, hi]) => `<div class="ax-q"><b>${q}</b><div class="ax-scale">\n        ${[1, 2, 3, 4, 5].map(n => `<button class="ax-btn ${ckDraft[k] === n ? \'sel\' : \'\'}" onclick="ax.ckAnswer(\'${k}\',${n})">${n}</button>`).join(\'\')}\n        <span class="ax-muted">${lo} → ${hi}</span></div></div>`).join(\'\') +\n      `<button class="ax-btn primary" ${CK_Q.every(([k]) => ckDraft[k]) ? \'\' : \'disabled\'} onclick="ax.ckSubmit()">Save</button>`;\n    const sig = (signal && signal.fresh) ? `<div class="ax-sig"><p>I noticed some change over the past few days. This is not a diagnosis, but we can talk about it calmly if you like.</p>\n      <div class="ax-row"><button class="ax-btn" onclick="ax.ckVent()">Venting session in diary</button>\n      <button class="ax-btn" onclick="ax.ckChat()">Light chat</button>\n      <button class="ax-btn" onclick="ax.ckGround()">Summary for commander (with my consent)</button></div></div>` : \'\';\n    panel.innerHTML = `<h2>Daily check-in</h2>\n      <p class="ax-muted">Just 3 quick questions, and you can skip them. Results are saved on this device only.</p>\n      ${ask}${sig}<div id="ax-ck-msg"></div>\n      <h3>Privacy</h3>\n      <label class="ax-row" style="cursor:pointer"><input type="checkbox" ${prefs.ground ? \'checked\' : \'\'} onchange="ax.togGround(this.checked)"> I agree that a general summary may be sent to the commander when I need follow-up</label>\n      <div class="ax-row"><button class="ax-btn" onclick="ax.close()">Close</button></div>`;\n  }\n  analyze(); glowCk();\n\n  window.ax = {\n    open, close, sleepStart, sleepStop,\n    gameStart, press, gameReset, crewAdd, crewRemove,\n    toggleMusic: () => { musicOn = !musicOn; const b = document.getElementById(\'ax-mus\'); if (b) b.textContent = \'♪ Music: \' + (musicOn ? \'on\' : \'off\'); },\n    setWp: k => { applyWp(k); renderWp(); }, addWp: addUserWp, delWp: delUserWp,\n    diarySave, diaryDelete, diaryAskDelete,\n    ckAnswer, ckSubmit, ckVent, ckChat, ckGround, ckSendGround, togGround,\n  };\n})();\n',
 'crew.js': '''
(() => {
  const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  /* ---------- 1) crew card in the right column ---------- */
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
    <h2>Crew buddy network · شبكة أفاق الطاقم</h2>
    <div id="crewList"><div class="note">Loading…</div></div>
    <div class="row" style="margin-top:10px">
      <button class="primary" id="crewUnwell">I feel unwell · حاسس بتعب</button>
      <button id="crewOk">I'm OK · أنا كويس</button>
    </div>
    <div class="note" id="crewMsg" style="margin-top:8px"></div>
    <p class="note">Other crew are simulated in this prototype until their sensors are connected.</p>`;
  const main = document.querySelector("main");
  if (main && main.lastElementChild) main.lastElementChild.prepend(card);
  const list = document.getElementById("crewList");
  const msg = document.getElementById("crewMsg");
  const dot = (bad) => `<span style="display:inline-block;width:9px;height:9px;border-radius:50%;margin-inline-end:6px;background:${bad ? "var(--alert)" : "var(--ok)"}"></span>`;
  function renderCrew(d) {
    list.innerHTML = d.members.map((m) => {
      const bad = m.status === "unwell";
      const tag = d.you_status === "unwell" && d.buddy === m.id ? " · buddy" : "";
      return `<div class="row" style="justify-content:space-between;padding:6px 0;border-bottom:1px dashed var(--line)">
        <span>${dot(bad)}<b>${esc(m.name)}</b> <span class="note">${esc(m.name_ar)} · ${esc(m.role)}</span></span>
        <span class="note">${bad ? "unwell · تعبان" : "OK · تمام"}${m.simulated ? " (sim)" : ""}${tag}</span></div>`;
    }).join("");
  }
  async function loadCrew() { try { renderCrew(await (await fetch("/api/crew")).json()); } catch (e) {} }
  async function post(path, body) {
    const r = await fetch(path, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body || {}) });
    return r.json();
  }
  document.getElementById("crewUnwell").onclick = async () => {
    const r = await post("/api/crew/unwell", {});
    msg.textContent = (r.notified ? "Crew notified. · اتبعت تنبيه للطاقم. " : "Crew was notified a moment ago. · التنبيه اتبعت قبل كده. ") + (r.guidance ? r.guidance.answer : "");
    loadCrew();
  };
  document.getElementById("crewOk").onclick = async () => { await post("/api/crew/status", { status: "ok" }); msg.textContent = ""; loadCrew(); };
  loadCrew();
  setInterval(loadCrew, 3000);

  /* ---------- 2) "Medical database" tab in the centre column ---------- */
  const tabs = document.querySelector(".tabs");
  const centreCard = tabs && tabs.parentElement;
  if (tabs && centreCard) {
    const tab = document.createElement("button");
    tab.className = "tab";
    tab.dataset.view = "db";
    tab.textContent = "Medical database · قاعدة البيانات";
    tabs.appendChild(tab);

    const view = document.createElement("div");
    view.className = "view";
    view.id = "v-db";
    view.innerHTML = `
      <input type="text" id="dbSearch" placeholder="Search · ابحث (مثال: صداع، سكر، blood pressure)" dir="auto" style="width:100%;margin-bottom:10px">
      <div id="dbList"><div class="note">Loading…</div></div>`;
    centreCard.appendChild(view);

    tab.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach((x) => x.classList.toggle("on", x === tab));
      document.querySelectorAll(".view").forEach((v) => v.classList.toggle("on", v === view));
      loadDb();
    });

    let entries = [];
    const CAT = { reference: "Normal values · القيم الطبيعية", first_aid: "First aid · الإسعافات الأولية" };
    function renderDb() {
      const q = document.getElementById("dbSearch").value.trim().toLowerCase();
      const hit = (e) => !q || [e.title, e.title_ar, e.text, e.text_ar].join(" ").toLowerCase().includes(q);
      const shown = entries.filter(hit);
      const groups = {};
      shown.forEach((e) => { (groups[e.category] = groups[e.category] || []).push(e); });
      const html = Object.keys(groups).map((c) => `
        <h3 style="margin:14px 0 6px">${esc(CAT[c] || c)}</h3>` + groups[c].map((e) => `
        <div class="src-box">
          <b>${esc(e.title)}</b> · <span class="note">${esc(e.title_ar)}</span>
          ${e.reviewed ? "" : '<span class="badge-un">not clinician-reviewed</span>'}
          <p>${esc(e.text_ar)}</p>
          <p class="note">${esc(e.text)}</p>
          <div class="note">Source: ${esc(e.source)}</div>
        </div>`).join("")).join("");
      document.getElementById("dbList").innerHTML = html || '<div class="note">No matches · مفيش نتايج</div>';
    }
    async function loadDb() {
      if (!entries.length) {
        try { entries = await (await fetch("/api/kb/entries")).json(); } catch (e) { entries = []; }
      }
      renderDb();
    }
    document.getElementById("dbSearch").addEventListener("input", renderDb);
  }
})();
''',
 'profile.js': '''/* ASHE profile: welcome banner (name + time-of-day greeting), astronaut hero card and Medical Card.
   Data stays on this device (localStorage). Uses only the app's theme variables. */
(() => {
  const $ = (id) => document.getElementById(id);
  const KEY = "ashe_profile";
  const load = () => { try { return Object.assign({ name: "", cond: "", h: "", w: "" }, JSON.parse(localStorage.getItem(KEY) || "{}")); } catch { return { name: "", cond: "", h: "", w: "" }; } };
  const save = (p) => { try { localStorage.setItem(KEY, JSON.stringify(p)); return true; } catch { return false; } };
  let profile = load();
  const L = () => (window.ASHE_LANG === "en" ? "en" : "ar");

  /* ---------- welcome + greeting ---------- */
  function greeting(d = new Date()) {
    const morning = d.getHours() < 12;                       // 00:00–11:59 morning, 12:00–23:59 evening
    return morning ? { en: "Good Morning", ar: "صباح الخير", icon: "☀️" } : { en: "Good Evening", ar: "مساء الخير", icon: "🌙" };
  }
  function paintWelcome() {
    const g = greeting(), name = (profile.name || "").trim();
    // Bilingual on purpose: the app starts in Arabic mode but the brief asks for "Welcome" + Good Morning / Evening.
    $("wHello").textContent = "Welcome · أهلاً";
    $("wName").textContent = name || "Astronaut";
    $("wGreet").textContent = g.en + " · " + g.ar; $("wGreetIcon").textContent = g.icon;
    $("heroName").textContent = name || "Astronaut";
    $("heroSub").textContent = L() === "en" ? "Astronaut · Mission ASHE" : "رائد فضاء · مهمة ASHE";
  }

  /* ---------- medical card ---------- */
  const fmtNum = (v, unit) => (v === "" || v == null || isNaN(+v)) ? "" : (+v) + " " + unit;
  function setDd(id, text, empty = "Not set · غير محدد") { const e = $(id); e.textContent = text || empty; e.classList.toggle("empty", !text); }
  function paintCard() {
    setDd("mName", profile.name); setDd("mCond", profile.cond);
    setDd("mH", fmtNum(profile.h, "cm")); setDd("mW", fmtNum(profile.w, "kg"));
    const h = +profile.h, w = +profile.w, row = $("mBmiRow");
    if (h > 0 && w > 0) { $("mBmi").textContent = (w / ((h / 100) ** 2)).toFixed(1) + " kg/m²"; row.classList.remove("hidden"); } else row.classList.add("hidden");
  }
  function showForm(on) {
    $("medForm").classList.toggle("hidden", !on); $("medView").classList.toggle("hidden", on);
    if (on) {
      $("fName").value = profile.name; $("fCond").value = profile.cond; $("fH").value = profile.h; $("fW").value = profile.w; $("medErr").textContent = "";
      $("medCard").scrollIntoView({ behavior: "smooth", block: "nearest" }); setTimeout(() => $("fName").focus(), 50);
    }
  }
  $("medForm").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = $("fName").value.trim(), cond = $("fCond").value.trim(), h = $("fH").value.trim(), w = $("fW").value.trim();
    const bad = (v, lo, hi) => v !== "" && !(+v >= lo && +v <= hi);
    if (!name) { $("medErr").textContent = "Please enter the astronaut's name · اكتب اسم رائد الفضاء"; $("fName").focus(); return; }
    if (bad(h, 50, 260)) { $("medErr").textContent = "Height must be between 50 and 260 cm · الطول بين 50 و260 سم"; $("fH").focus(); return; }
    if (bad(w, 20, 300)) { $("medErr").textContent = "Weight must be between 20 and 300 kg · الوزن بين 20 و300 كجم"; $("fW").focus(); return; }
    profile = { name: name.slice(0, 40), cond: cond.slice(0, 400), h, w };
    if (!save(profile)) { $("medErr").textContent = "Could not save on this device (storage is full or blocked)."; return; }
    paintWelcome(); paintCard(); showForm(false);
  });
  $("medCancel").onclick = () => showForm(false);
  ["medEdit", "pfEdit", "pfMedBtn"].forEach((id) => ($(id).onclick = () => showForm(true)));

  /* ---------- hero round buttons ---------- */
  $("pfMute").onclick = () => document.dispatchEvent(new CustomEvent("ashe-toggle-mute"));
  $("pfWall").onclick = () => { if (window.ax) window.ax.open("bg"); };
  $("pfTheme").onclick = () => $("themeBtn").click();

  document.addEventListener("ashe-lang", paintWelcome);
  paintWelcome(); paintCard(); setInterval(paintWelcome, 30000);
  if (!profile.name) showForm(true);                         // first launch: ask for the astronaut's details
})();
''',
}

import tempfile as _tf
_FRONT_DIR = _tf.mkdtemp(prefix="ashe_")
for _n, _c in FRONTEND.items():
    with open(os.path.join(_FRONT_DIR, _n), "w", encoding="utf-8") as _f:
        _f.write(_c)


# ---- module: core ----

"""ASHE core engine: sensors (Demo/Live), personal baseline, anomaly
detection, trend forecasting, Wellness Score, and probabilistic genetic risk.

Pure standard library so it runs and tests anywhere.
"""

import math
import random
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List, Optional

# metric: (normal mean, noise sd, unit, low-danger, high-danger)
METRICS: Dict[str, dict] = {
    "hr": dict(mean=68, sd=2.0, unit="bpm", lo=45, hi=110, label="Heart rate"),
    "hrv": dict(mean=62, sd=4.0, unit="ms", lo=25, hi=None, label="HRV"),
    "spo2": dict(mean=98, sd=0.4, unit="%", lo=92, hi=None, label="SpO2"),
    "temp": dict(mean=36.7, sd=0.08, unit="°C", lo=35.5, hi=38.0, label="Body temp"),
    "resp": dict(mean=15, sd=0.8, unit="/min", lo=8, hi=24, label="Breathing"),
    "bp_sys": dict(mean=118, sd=3.0, unit="mmHg", lo=90, hi=150, label="Systolic BP"),
    "co2": dict(mean=0.35, sd=0.02, unit="kPa", lo=None, hi=0.7, label="Cabin CO2"),
    "radiation": dict(mean=0.55, sd=0.04, unit="mSv/d", lo=None, hi=1.5, label="Radiation"),
}

# Hardware-dependent metrics are simulated in Demo mode.
SIMULATED = list(METRICS.keys())

SCENARIOS = {
    "normal": {},
    "fatigue": {"hrv": -22, "hr": +9, "resp": +1.5},
    "cardiac": {"hr": +52, "hrv": -30, "bp_sys": +32, "spo2": -2.5},
    "hypoxia": {"spo2": -9, "hr": +18, "resp": +7},
    "co2": {"co2": +0.55, "resp": +5, "hr": +8},
    "infection": {"temp": +1.9, "hr": +20, "hrv": -18, "resp": +3},
    "radiation": {"radiation": +1.3, "hrv": -8},
}


@dataclass
class Baseline:
    """Personal baseline learned from the first samples, then slowly adapted."""
    warmup: int = 20
    n: int = 0
    mean: float = 0.0
    m2: float = 0.0
    ema: float = 0.0

    def update(self, x: float, adapt: bool = True) -> None:
        self.n += 1
        if self.n <= self.warmup:
            d = x - self.mean
            self.mean += d / self.n
            self.m2 += d * (x - self.mean)
            self.ema = self.mean
        elif adapt:
            # adapt very slowly, and only on non-anomalous samples
            self.ema += 0.002 * (x - self.ema)

    @property
    def ready(self) -> bool:
        return self.n >= self.warmup

    @property
    def center(self) -> float:
        return self.ema if self.n > self.warmup else self.mean

    @property
    def sd(self) -> float:
        if self.n < 2:
            return 1.0
        return max(math.sqrt(self.m2 / max(self.n - 1, 1)), 1e-6)

    def z(self, x: float, floor_sd: float = 0.0) -> float:
        return (x - self.center) / max(self.sd, floor_sd, 1e-6)


@dataclass
class Alert:
    id: str
    level: str  # info | warning | critical
    metric: str
    text: str
    ts: float
    kind: str = "threshold"  # threshold | anomaly | forecast | vision | voice


class Engine:
    def __init__(self, rng: Optional[random.Random] = None):
        self.rng = rng or random.Random()
        self.mode = "demo"  # demo | live
        self.scenario = "normal"
        self.scenario_since = time.time()
        self.t0 = time.time()
        self.baselines: Dict[str, Baseline] = {k: Baseline() for k in METRICS}
        self.history: Dict[str, Deque] = {k: deque(maxlen=120) for k in METRICS}
        self.values: Dict[str, float] = {k: v["mean"] for k, v in METRICS.items()}
        self.live_values: Dict[str, float] = {}
        self.live_seen: Dict[str, float] = {}
        self.vision: Dict[str, float] = {}
        self.voice: Dict[str, float] = {}
        self.alerts: List[Alert] = []
        self._last_alert: Dict[str, float] = {}
        self._streak: Dict[str, int] = {}
        self.vision_base = {"blink": Baseline(warmup=10), "perclos": Baseline(warmup=10),
                            "pitch": Baseline(warmup=10), "energy": Baseline(warmup=10)}
        self.activity_log: Deque = deque(maxlen=50)
        self.game_scores: List[float] = []

    # ------------------------------------------------------------------ input
    def set_scenario(self, name: str) -> bool:
        if name not in SCENARIOS:
            return False
        self.scenario = name
        self.scenario_since = time.time()
        return True

    def set_mode(self, mode: str) -> None:
        if mode in ("demo", "live"):
            self.mode = mode

    def ingest_sensor(self, readings: Dict[str, float]) -> List[str]:
        """Real sensor readings (e.g. ESP32 -> POST /api/sensor)."""
        accepted = []
        for k, v in readings.items():
            if k in METRICS and isinstance(v, (int, float)) and math.isfinite(v):
                self.live_values[k] = float(v)
                self.live_seen[k] = time.time()
                accepted.append(k)
        return accepted

    def ingest_vision(self, d: Dict[str, float]) -> None:
        for k in ("blink", "perclos", "yawn", "stress", "mood", "rppg_hr", "head_tilt", "face"):
            if k in d and isinstance(d[k], (int, float)) and math.isfinite(d[k]):
                self.vision[k] = float(d[k])
        for k in ("blink", "perclos"):
            if k in self.vision:
                self.vision_base[k].update(self.vision[k])

    def ingest_voice(self, d: Dict[str, float]) -> None:
        for k in ("pitch", "energy", "rate"):
            if k in d and isinstance(d[k], (int, float)) and math.isfinite(d[k]):
                self.voice[k] = float(d[k])
        for k in ("pitch", "energy"):
            if k in self.voice and self.voice[k] > 0:
                self.vision_base[k].update(self.voice[k])

    def record_game(self, reaction_ms: float) -> None:
        if 80 <= reaction_ms <= 5000:
            self.game_scores.append(reaction_ms)
            self.game_scores = self.game_scores[-30:]

    # ------------------------------------------------------------------- tick
    def _scenario_offset(self, key: str) -> float:
        offs = SCENARIOS.get(self.scenario, {})
        if key not in offs:
            return 0.0
        ramp = min(1.0, (time.time() - self.scenario_since) / 4.0)  # 4 s ramp
        return offs[key] * ramp

    def tick(self) -> dict:
        now = time.time()
        for k, m in METRICS.items():
            live_ok = (self.mode == "live" and k in self.live_values
                       and now - self.live_seen.get(k, 0) < 10)
            if live_ok:
                v = self.live_values[k]
            elif k == "hr" and self.vision.get("rppg_hr", 0) > 35 and self.mode == "live":
                v = self.vision["rppg_hr"]
            else:
                phase = sum(ord(c) for c in k) % 7
                drift = math.sin((now - self.t0) / 40.0 + phase) * m["sd"] * 0.6
                target = m["mean"] + drift + self._scenario_offset(k)
                v = 0.8 * self.values[k] + 0.2 * (target + self.rng.gauss(0, m["sd"]))
            self.values[k] = v
            self.history[k].append((now, v))
            sd_floor = m["sd"] * 0.5
            base = self.baselines[k]
            anomalous = base.ready and abs(base.z(v, sd_floor)) > 3
            base.update(v, adapt=not anomalous)
        alerts = self._evaluate(now)
        return self.snapshot(alerts)

    # ------------------------------------------------------------- evaluation
    def _emit(self, key: str, level: str, metric: str, text: str, kind: str,
              cooldown: float = 25.0) -> Optional[Alert]:
        now = time.time()
        if now - self._last_alert.get(key, 0) < cooldown:
            return None
        self._last_alert[key] = now
        a = Alert(id=f"{key}-{int(now)}", level=level, metric=metric, text=text, ts=now, kind=kind)
        self.alerts.append(a)
        self.alerts = self.alerts[-60:]
        return a

    def forecast(self, k: str, horizon_s: float = 600.0) -> Optional[dict]:
        """Linear trend over the last ~30 samples -> time until a danger limit."""
        h = list(self.history[k])[-30:]
        if len(h) < 15:
            return None
        t0 = h[0][0]
        xs = [t - t0 for t, _ in h]
        ys = [v for _, v in h]
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        den = sum((x - mx) ** 2 for x in xs)
        if den < 1e-9:
            return None
        slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den
        m = METRICS[k]
        cur = ys[-1]
        # fit quality: residual sd vs. trend magnitude
        res = math.sqrt(sum((y - (my + slope * (x - mx))) ** 2 for x, y in zip(xs, ys)) / n)
        if abs(slope) * (xs[-1] - xs[0]) < 2.5 * max(res, 1e-6):
            return None  # trend not distinguishable from noise
        limit = None
        if slope > 0 and m["hi"] is not None:
            limit = m["hi"]
        elif slope < 0 and m["lo"] is not None:
            limit = m["lo"]
        if limit is None:
            return None
        if (slope > 0 and cur >= limit) or (slope < 0 and cur <= limit):
            return None  # already past it; threshold alert covers this
        eta = (limit - cur) / slope
        if 0 < eta <= horizon_s:
            return {"metric": k, "eta_s": eta, "limit": limit}
        return None

    def _evaluate(self, now: float) -> List[Alert]:
        new: List[Alert] = []
        for k, m in METRICS.items():
            v = self.values[k]
            level = None
            if m["hi"] is not None and v >= m["hi"]:
                level = "critical"
            elif m["lo"] is not None and v <= m["lo"]:
                level = "critical"
            self._streak[k + "T"] = self._streak.get(k + "T", 0) + 1 if level else 0
            if level and self._streak[k + "T"] >= 3:
                a = self._emit(k + "T", "critical", k,
                               f"{m['label']} outside safe range: {v:.1f} {m['unit']}", "threshold", 40)
                if a:
                    new.append(a)
                continue
            base = self.baselines[k]
            if base.ready:
                z = base.z(v, m["sd"] * 0.5)
                self._streak[k + "A"] = self._streak.get(k + "A", 0) + 1 if abs(z) > 3.5 else 0
                if self._streak[k + "A"] >= 4:
                    a = self._emit(k + "A", "warning", k,
                                   f"{m['label']} deviates from your personal baseline ({z:+.1f}σ)",
                                   "anomaly", 60)
                    if a:
                        new.append(a)
            fc = self.forecast(k)
            if fc:
                mins = fc["eta_s"] / 60
                a = self._emit(k + "F", "info", k,
                               f"{m['label']} trending toward its limit in ~{max(mins, 0.5):.0f} min",
                               "forecast", 90)
                if a:
                    new.append(a)
        # vision-derived
        pc = self.vision.get("perclos")
        if pc is not None and pc > 0.35:
            a = self._emit("perclos", "warning", "fatigue", "Eyes closing for long periods: fatigue signs", "vision", 90)
            if a:
                new.append(a)
        if self.vision.get("yawn", 0) >= 3:
            a = self._emit("yawn", "info", "fatigue", "Repeated yawning detected", "vision", 120)
            if a:
                new.append(a)
        return new

    # ---------------------------------------------------------------- scoring
    def fatigue_index(self) -> float:
        """0-100 from blink/PERCLOS/yawns/HRV/voice and reaction-time game."""
        parts, weights = [], []
        pc = self.vision.get("perclos")
        if pc is not None:
            parts.append(min(pc / 0.4, 1.0)); weights.append(2.0)
        yw = self.vision.get("yawn")
        if yw is not None:
            parts.append(min(yw / 4.0, 1.0)); weights.append(1.0)
        b = self.baselines["hrv"]
        if b.ready:
            parts.append(min(max(-b.z(self.values["hrv"], 2.0), 0) / 4.0, 1.0)); weights.append(1.5)
        en = self.vision_base["energy"]
        if en.ready and "energy" in self.voice:
            parts.append(min(max(-en.z(self.voice["energy"]), 0) / 3.0, 1.0)); weights.append(0.8)
        if len(self.game_scores) >= 3:
            ref = sorted(self.game_scores)[: max(1, len(self.game_scores) // 3)]
            base = sum(ref) / len(ref)
            last = sum(self.game_scores[-3:]) / 3
            parts.append(min(max((last - base) / max(base, 1) / 0.5, 0), 1.0)); weights.append(1.2)
        if not parts:
            return 0.0
        return 100 * sum(p * w for p, w in zip(parts, weights)) / sum(weights)

    def stress_index(self) -> float:
        parts = []
        s = self.vision.get("stress")
        if s is not None:
            parts.append(min(max(s, 0), 1))
        p = self.vision_base["pitch"]
        if p.ready and "pitch" in self.voice and self.voice["pitch"] > 0:
            parts.append(min(max(p.z(self.voice["pitch"]), 0) / 3.0, 1.0))
        b = self.baselines["hr"]
        if b.ready:
            parts.append(min(max(b.z(self.values["hr"], 2.0), 0) / 5.0, 1.0))
        return 100 * sum(parts) / len(parts) if parts else 0.0

    def wellness(self) -> float:
        penalty = 0.0
        for k, m in METRICS.items():
            b = self.baselines[k]
            if not b.ready:
                continue
            z = abs(b.z(self.values[k], m["sd"] * 0.5))
            penalty += min(max(z - 1.5, 0) / 6.0, 1.0) * 14
        penalty += self.fatigue_index() * 0.25 + self.stress_index() * 0.2
        return max(0.0, min(100.0, 100.0 - penalty))

    # ---------------------------------------------------------------- genetics
    GENETIC_SAMPLE = [  # sample (synthetic) genome profile: baseline relative risk
        ("Bone density loss", 1.15, "bone"),
        ("Cardiovascular strain", 1.05, "cardio"),
        ("Radiation sensitivity", 0.95, "radiation"),
        ("Sleep-circadian disruption", 1.20, "sleep"),
    ]

    def genetic_risk(self) -> List[dict]:
        """Relative risk adjusted by live data. Probabilistic, NOT a diagnosis."""
        out = []
        fat = self.fatigue_index() / 100
        for name, rr, tag in self.GENETIC_SAMPLE:
            adj = rr
            if tag == "cardio":
                b = self.baselines["hr"]
                if b.ready:
                    adj += min(max(b.z(self.values["hr"], 2.0), 0) / 10, 0.4)
            elif tag == "radiation":
                adj += min(max(self.values["radiation"] - 0.55, 0) / 2.0, 0.5)
            elif tag == "sleep":
                adj += fat * 0.35
            elif tag == "bone":
                adj += 0.05
            band = "lower" if adj < 1.0 else "average" if adj < 1.15 else "elevated" if adj < 1.4 else "high"
            out.append({"name": name, "relative_risk": round(adj, 2), "band": band})
        return out

    # --------------------------------------------------------------- snapshot
    def snapshot(self, new_alerts: Optional[List[Alert]] = None) -> dict:
        now = time.time()
        metrics = {}
        for k, m in METRICS.items():
            hist = [round(v, 2) for _, v in list(self.history[k])[-40:]]
            src = "simulated"
            if self.mode == "live" and k in self.live_values and now - self.live_seen.get(k, 0) < 10:
                src = "sensor"
            elif self.mode == "live" and k == "hr" and self.vision.get("rppg_hr", 0) > 35:
                src = "camera"
            metrics[k] = {
                "value": round(self.values[k], 2), "unit": m["unit"], "label": m["label"],
                "lo": m["lo"], "hi": m["hi"], "source": src, "history": hist,
                "baseline": round(self.baselines[k].center, 2) if self.baselines[k].ready else None,
            }
        return {
            "type": "state", "ts": now, "mode": self.mode, "scenario": self.scenario,
            "metrics": metrics, "wellness": round(self.wellness(), 1),
            "fatigue": round(self.fatigue_index(), 1), "stress": round(self.stress_index(), 1),
            "vision": self.vision, "voice": self.voice,
            "genetic": self.genetic_risk(),
            "alerts": [a.__dict__ for a in (new_alerts or [])],
            "recent_alerts": [a.__dict__ for a in self.alerts[-8:]],
            "baseline_ready": all(b.ready for b in self.baselines.values()),
        }

# ---- module: connectors ----

"""Unified sensor connector registry.

Any device posts the same payload to POST /api/sensor:
    {"device": "whoop", "readings": {"hr": 61, "hrv": 70, "spo2": 97}}
Each connector below declares which metrics it can provide and how it would connect.
Only the generic HTTP path is implemented in this prototype; vendor SDK/OAuth wiring is a
documented TODO per connector (status: "planned"). Nothing here claims a live vendor link.
"""
from typing import Dict, List

CONNECTORS: List[Dict] = [
    {"id": "generic-http", "name": "Generic HTTP / ESP32", "kind": "dev-board", "status": "ready",
     "provides": ["hr", "spo2", "temp", "co2", "resp", "bp_sys", "radiation"],
     "how": "POST JSON readings to /api/sensor. Example: MAX30102 on ESP32 sending hr and spo2."},
    {"id": "whoop", "name": "WHOOP", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv", "resp", "temp"], "how": "WHOOP developer API (OAuth) -> map to /api/sensor."},
    {"id": "oura", "name": "Oura Ring", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv", "temp"], "how": "Oura Cloud API (OAuth) -> sleep, HRV, temperature trend."},
    {"id": "garmin", "name": "Garmin", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv", "spo2", "resp"], "how": "Garmin Health API (partner approval required)."},
    {"id": "polar", "name": "Polar H10 chest strap", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv"], "how": "Bluetooth LE heart-rate service via Web Bluetooth in Chrome."},
    {"id": "apple-health", "name": "Apple Watch", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv", "spo2", "resp"], "how": "HealthKit via a companion iOS app posting to /api/sensor."},
    {"id": "health-connect", "name": "Samsung / Google Health Connect", "kind": "wearable", "status": "planned",
     "provides": ["hr", "hrv", "spo2", "temp"], "how": "Android Health Connect via a companion app."},
    {"id": "hexoskin", "name": "Smart shirt (Hexoskin-class)", "kind": "space-grade", "status": "planned",
     "provides": ["hr", "resp"], "how": "Vendor SDK; also movement and breathing volume."},
    {"id": "core-temp", "name": "Core body temperature pill/patch", "kind": "space-grade", "status": "planned",
     "provides": ["temp"], "how": "Vendor receiver -> /api/sensor."},
    {"id": "cgm", "name": "Continuous glucose monitor", "kind": "space-grade", "status": "planned",
     "provides": [], "how": "Needs a new 'glucose' metric (not in this prototype yet)."},
    {"id": "eeg-sleep", "name": "Sleep EEG headband", "kind": "space-grade", "status": "planned",
     "provides": [], "how": "Needs sleep-stage metrics (not in this prototype yet)."},
    {"id": "eda", "name": "EDA (skin conductance) sensor", "kind": "space-grade", "status": "planned",
     "provides": [], "how": "Needs a stress-conductance metric (not in this prototype yet)."},
    {"id": "imu", "name": "Exercise IMU sensors", "kind": "space-grade", "status": "planned",
     "provides": [], "how": "Form and load monitoring for the exercise coach."},
    {"id": "dosimeter", "name": "Personal radiation dosimeter", "kind": "space-grade", "status": "planned",
     "provides": ["radiation"], "how": "Vendor reader -> /api/sensor."},
]

# ---- module: knowledge ----

"""Medical / exercise knowledge base with retrieval (RAG-style) and citations.

IMPORTANT: the entries below are SAMPLE DRAFT content written to demonstrate the
retrieval + citation + escalation mechanism. Every entry carries a `source`
reference pointing to the document family it should be checked against, and a
`reviewed` flag that is False until a doctor / physical therapist has verified it
against that source. Replace/extend entries in data/protocols.json (same schema)
with reviewed protocol text. This is an educational prototype, not a medical device.
"""

import json
import math
import os
import re
from collections import Counter
from typing import Dict, List

DEFAULT_ENTRIES: List[dict] = [

    {
        "id": "ref-blood-01", "category": "reference",
        "title": "Normal adult blood values (typical ranges)", "title_ar": "القيم الطبيعية لتحاليل الدم",
        "text": "Typical adult ranges, which vary by lab: hemoglobin 13.5-17.5 g/dL for men and 12-15.5 g/dL for women; white blood cells 4-11 x10^9/L; platelets 150-400 x10^9/L; fasting glucose 70-99 mg/dL; sodium 135-145 mmol/L; potassium 3.5-5.0 mmol/L; creatinine 0.7-1.3 mg/dL for men and 0.6-1.1 for women.",
        "text_ar": "المدى الطبيعي التقريبي للبالغين (بيختلف حسب المعمل): الهيموجلوبين 13.5-17.5 جم/دل للرجالة و12-15.5 للستات؛ كرات الدم البيضا 4-11 ×10⁹/لتر؛ الصفائح 150-400 ×10⁹/لتر؛ سكر الصيام 70-99 مجم/دل؛ الصوديوم 135-145 ملي مول/لتر؛ البوتاسيوم 3.5-5.0 ملي مول/لتر؛ الكرياتينين 0.7-1.3 مجم/دل للرجالة و0.6-1.1 للستات.",
        "tags": ["blood", "lab", "hemoglobin", "glucose", "sodium", "potassium", "creatinine", "platelets", "normal", "range", "average",
                 "دم", "تحاليل", "تحليل", "هيموجلوبين", "سكر", "صوديوم", "بوتاسيوم", "كرياتينين", "صفائح", "طبيعي", "المعدل", "المتوسط", "نسبة"],
        "red_flags": [],
        "source": "Standard adult reference intervals (general clinical references; verify against the lab report)",
        "reviewed": False,
    },
    {
        "id": "ref-vitals-01", "category": "reference",
        "title": "Normal adult vital signs", "title_ar": "العلامات الحيوية الطبيعية للبالغين",
        "text": "Resting heart rate about 60-100 bpm (trained people can be lower); blood pressure below 120/80 mmHg; breathing 12-20 breaths per minute; body temperature 36.1-37.2 C; oxygen saturation 95-100%. ASHE's own alert limits are stricter, so a reading near a limit is worth watching.",
        "text_ar": "النبض وقت الراحة حوالي 60-100 نبضة/دقيقة (الرياضيين ممكن أقل)؛ الضغط أقل من 120/80 ملي زئبق؛ التنفس 12-20 نفس/دقيقة؛ حرارة الجسم 36.1-37.2 درجة مئوية؛ تشبع الأكسجين 95-100%. ولو قراءة قريبة من الحدود دي، راقبها.",
        "tags": ["heart rate", "pulse", "blood pressure", "bp", "breathing", "respiration", "temperature", "oxygen", "spo2", "normal", "vitals",
                 "نبض", "ضغط", "تنفس", "أكسجين", "اكسجين", "حرارة الجسم", "طبيعي", "المعدل", "علامات حيوية"],
        "red_flags": [],
        "source": "Standard adult vital-sign ranges (general clinical references; verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "ref-body-01", "category": "reference",
        "title": "Other body substances (typical values)", "title_ar": "مواد أخرى في الجسم (قيم تقريبية)",
        "text": "Typical adult values: vitamin D 30-100 ng/mL; ferritin 24-336 ng/mL for men and 11-307 for women; HbA1c below 5.7%; total cholesterol below 200 mg/dL; LDL below 100 mg/dL; HDL above 40 mg/dL for men and 50 for women; triglycerides below 150 mg/dL; uric acid 3.4-7.0 mg/dL for men and 2.4-6.0 for women; magnesium 1.7-2.2 mg/dL.",
        "text_ar": "قيم تقريبية للبالغين: فيتامين D 30-100 نانوجرام/مل؛ الفيريتين 24-336 للرجالة و11-307 للستات؛ السكر التراكمي أقل من 5.7%؛ الكوليسترول الكلي أقل من 200 مجم/دل؛ LDL أقل من 100؛ HDL أعلى من 40 للرجالة و50 للستات؛ الدهون الثلاثية أقل من 150؛ حمض اليوريك 3.4-7.0 للرجالة و2.4-6.0 للستات؛ المغنيسيوم 1.7-2.2 مجم/دل.",
        "tags": ["vitamin", "iron", "ferritin", "cholesterol", "triglycerides", "uric", "magnesium", "hba1c", "normal",
                 "فيتامين", "حديد", "فيريتين", "كوليسترول", "دهون", "يوريك", "مغنيسيوم", "سكر تراكمي", "طبيعي"],
        "red_flags": [],
        "source": "Standard adult reference intervals (general clinical references; verify against the lab report)",
        "reviewed": False,
    },
    {
        "id": "ref-liver-01", "category": "reference",
        "title": "Liver and kidney markers (typical values)", "title_ar": "مؤشرات الكبد والكلى (قيم تقريبية)",
        "text": "Typical adult values: ALT 7-56 U/L; AST 10-40 U/L; total bilirubin 0.1-1.2 mg/dL; albumin 3.5-5.0 g/dL; BUN 7-20 mg/dL. eGFR above 90 mL/min is considered normal kidney filtration.",
        "text_ar": "قيم تقريبية للبالغين: ALT من 7 لـ 56 وحدة/لتر؛ AST من 10 لـ 40؛ البيليروبين الكلي 0.1-1.2 مجم/دل؛ الألبumin 3.5-5.0 جم/دل؛ اليوريا 7-20 مجم/دل. معدل الترشيح eGFR فوق 90 يعتبر طبيعي.",
        "tags": ["liver", "kidney", "alt", "ast", "bilirubin", "albumin", "urea", "bun", "egfr", "normal",
                 "كبد", "كلى", "كلية", "بيليروبين", "ألبومين", "يوريا", "طبيعي"],
        "red_flags": [],
        "source": "Standard adult reference intervals (general clinical references; verify against the lab report)",
        "reviewed": False,
    },
    {
        "id": "ref-gas-01", "category": "reference",
        "title": "Arterial blood gas (typical values)", "title_ar": "غازات الدم الشريانية (قيم تقريبية)",
        "text": "Typical adult values: pH 7.35-7.45; PaO2 75-100 mmHg; PaCO2 35-45 mmHg; bicarbonate 22-26 mmol/L. A low pH with high CO2 suggests breathing problems and needs the flight surgeon.",
        "text_ar": "قيم تقريبية للبالغين: الـ pH من 7.35 لـ 7.45؛ الأكسجين في الشريان PaO2 من 75 لـ 100 ملي زئبق؛ ثاني أكسيد الكربون PaCO2 من 35 لـ 45؛ البيكربونات 22-26 ملي مول/لتر. الـ pH المنخفض مع CO2 مرتفع يعني مشكلة في التنفس ولازم طبيب الرحلة.",
        "tags": ["blood gas", "ph", "co2", "pao2", "bicarbonate", "oxygen", "normal", "غازات", "حموضة", "طبيعي", "أكسجين"],
        "red_flags": [],
        "source": "Standard adult reference intervals (general clinical references; verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-general-01", "category": "first_aid",
        "title": "Feeling physically unwell", "title_ar": "حاسس بتعب جسدي",
        "text": "If you feel physically unwell: stop what you are doing and sit or lie down in a safe position. Sip water slowly, breathe slowly and steadily, and check your vitals on the dashboard. Tell your crew buddy now so someone stays near you. If you feel worse, or have chest pain, confusion or trouble breathing, report to the flight surgeon immediately.",
        "text_ar": "لو حاسس بتعب جسدي: وقّف الشغل واقعد أو اتمدد في وضع آمن. اشرب مية على مهل، وتنفس ببطء وبانتظام، وبص على قراءاتك في الداشبورد. كلم زميلك فوراً عشان حد يفضل جنبك. ولو التعب زاد، أو حسيت بألم في الصدر أو تشوش أو صعوبة في التنفس، بلّغ طبيب الرحلة على طول.",
        "tags": ["unwell", "sick", "not well", "tired body", "feel bad", "physically", "تعبان", "تعب", "مش حاسس بخير", "جسدي", "جسم"],
        "red_flags": ["chest", "confus", "breath", "faint", "صدر", "تشوش", "تنفس", "إغماء", "اغمى"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-headache-01", "category": "first_aid",
        "title": "Headache", "title_ar": "صداع",
        "text": "For a headache: rest in a dim, quiet spot, drink water, and check that you are not dehydrated or overly stressed. Use only the pain reliever in your onboard medical kit, following its label or the flight surgeon's protocol. A sudden, very severe headache, or one with vomiting, weakness, confusion or vision changes, needs the flight surgeon at once.",
        "text_ar": "للصداع: ارتاح في مكان هادي ونوره خفيف، اشرب مية، وتأكد إنك مش عطشان أو متوتر أكتر من اللازم. استخدم بس المسكن الموجود في الكيت الطبي للرحلة وعلى حسب الورقة المكتوبة عليه أو بروتوكول طبيب الرحلة. الصداع المفاجئ الشديد جداً، أو اللي معاه قيء أو ضعف أو تشوش أو مشكلة في النظر، يتبلّغ لطبيب الرحلة فوراً.",
        "tags": ["headache", "head", "migraine", "صداع", "مصدع", "راسي", "دماغ"],
        "red_flags": ["sudden", "vomit", "confus", "weak", "vision", "فجأة", "قيء", "تشوش", "ضعف"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-dizzy-01", "category": "first_aid",
        "title": "Dizziness or light-headedness", "title_ar": "دوخة أو دوار",
        "text": "For dizziness: sit down right away, lower your head between your knees if needed, or lie down with your legs raised. Stand up slowly. Sip water or an electrolyte drink from the kit. Fainting, chest pain or a racing heartbeat needs the flight surgeon at once.",
        "text_ar": "للدوخة: اقعد على طول، وحط راسك بين رجليك لو لازم، أو اتمدد ورجليك لفوق. قوم ببطء. اشرب مية أو مشروب أملاح من الكيت. لو اغمى عليك، أو في ألم بالصدر، أو نبضك سريع جداً، بلّغ طبيب الرحلة فوراً.",
        "tags": ["dizzy", "dizziness", "faint", "lightheaded", "دايخ", "دوخة", "دوار", "اغمى"],
        "red_flags": ["faint", "chest", "racing", "إغماء", "اغمى", "صدر"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-nausea-01", "category": "first_aid",
        "title": "Nausea", "title_ar": "غثيان",
        "text": "For nausea: sit upright, sip cool water in small amounts, avoid strong smells and heavy food, and rest. If you vomit blood, cannot keep fluids down for several hours, or have severe abdominal pain, report to the flight surgeon.",
        "text_ar": "للغثيان: اقعد معتدل، اشرب مية باردة بجرعات صغيرة، وابعد عن الريحة القوية والأكل التقيل، وارتاح. لو قيأت دم، أو مش قادر تشرب سوائل لساعات، أو في وجع بطن شديد، بلّغ طبيب الرحلة.",
        "tags": ["nausea", "nauseous", "vomit", "sick", "غثيان", "مغثي", "قيء", "ترجيع"],
        "red_flags": ["blood", "abdominal", "دم", "بطن"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-fever-01", "category": "first_aid",
        "title": "Fever", "title_ar": "حرارة وسخونية",
        "text": "For fever: rest, drink fluids regularly, wear light clothing, and check your temperature every few hours. Use medication only from the onboard kit, following its label or the flight surgeon's protocol. Tell the flight surgeon if your temperature is above 38 C, lasts more than 48 hours, or comes with a rash, stiff neck or confusion.",
        "text_ar": "للحرارة: ارتاح، اشرب سوائل بانتظام، البس هدوم خفيفة، وقيس الحرارة كل كام ساعة. الدوا من الكيت بس، وعلى حسب الورقة المكتوبة أو بروتوكول طبيب الرحلة. بلّغ طبيب الرحلة لو الحرارة فوق 38 درجة، أو استمرت أكتر من 48 ساعة، أو ظهر معاها طفح أو تيبس في الرقبة أو تشوش.",
        "tags": ["fever", "temperature", "hot", "chills", "حرارة", "سخن", "سخونية", "حمى", "برد"],
        "red_flags": ["confus", "rash", "stiff", "تشوش", "طفح", "تيبس"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-cut-01", "category": "first_aid",
        "title": "Minor cut or scrape", "title_ar": "جرح بسيط أو خدش",
        "text": "For a minor cut or scrape: wash your hands, press a clean gauze pad firmly on the wound for about 10 minutes, rinse with saline if available, then cover it with a sterile dressing. Check when you last had a tetanus booster. Bleeding that does not stop after 10 minutes of firm pressure, or a deep or gaping wound, needs the flight surgeon at once.",
        "text_ar": "للجرح البسيط أو الخدش: اغسل إيدك، واضغط على الجرح بشاش نظيف لحد 10 دقايق، واغسله بمحلول ملح لو متاح، وبعدين غطيه بشاش معقم. اتأكد إنك أخدت تطعيم الكزاز في آخر 10 سنين. النزيف اللي مش بيقف بعد 10 دقايق ضغط، أو الجرح العميق، يتبلّغ لطبيب الرحلة فوراً.",
        "tags": ["cut", "wound", "bleeding", "scrape", "injury", "جرح", "خدش", "نزيف", "دم"],
        "red_flags": ["bleed", "deep", "نزيف", "عميق"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "fa-chest-01", "category": "first_aid",
        "title": "Chest pain or pressure", "title_ar": "ألم أو ضغط في الصدر",
        "text": "For chest pain or pressure: stop all activity and sit or lie down immediately. Do not exercise. Tell the flight surgeon at once and have your crew buddy stay with you. Do not wait to see whether it passes.",
        "text_ar": "لألم أو ضغط في الصدر: وقّف أي نشاط واقعد أو اتمدد على طول. ما تتمرنش. بلّغ طبيب الرحلة فوراً، وخلي زميلك يفضل جنبك. ما تستناش تشوف هل هيعدي ولا لأ.",
        "tags": ["chest", "chest pain", "صدر", "وجع الصدر", "ألم الصدر", "ضغط الصدر"],
        "red_flags": ["chest", "صدر"],
        "source": "General first-aid principles (verify with the flight surgeon)",
        "reviewed": False,
    },
    {
        "id": "ex-resist-01", "category": "exercise",
        "title": "Daily resistance session (bone & muscle protection)",
        "text": "Resistance training several days a week targets the large muscle groups of the legs, back and "
                "trunk to counter muscle and bone loss in microgravity. Scale load and volume down when sleep is "
                "poor, HRV is low or fatigue is high; keep movement quality over load.",
        "tags": ["resistance", "strength", "bone", "muscle", "microgravity", "weights", "تمرين", "مقاومة", "عظام", "عضلات"],
        "source": "NASA Human Research Program - Exercise countermeasures (verify against current HRP documents)",
        "reviewed": False,
    },
    {
        "id": "ex-cardio-01", "category": "exercise",
        "title": "Aerobic session",
        "text": "Moderate aerobic exercise supports cardiovascular conditioning. Use a conservative intensity "
                "when resting heart rate is above your baseline or fatigue is high; stop and report chest pain, "
                "fainting, or severe breathlessness.",
        "tags": ["cardio", "aerobic", "treadmill", "bike", "heart", "كارديو", "جري", "قلب"],
        "source": "ACSM exercise testing & prescription guidance (verify edition)",
        "reviewed": False,
    },
    {
        "id": "inj-strain-01", "category": "injury",
        "title": "Suspected muscle strain",
        "text": "Stop the aggravating movement, rest the area, apply gentle compression and cold for short "
                "periods if available, and avoid loading the muscle until pain settles. Escalate to the flight "
                "surgeon if there is severe pain, visible deformity, numbness, or no improvement in a few days.",
        "tags": ["strain", "muscle", "pulled", "pain", "شد", "عضلي", "وجع", "ألم", "إصابة", "injury"],
        "source": "Published physical-therapy first-line guidance (verify with clinician)",
        "reviewed": False,
        "red_flags": ["numbness", "deformity", "severe", "can't move", "تنميل", "ما أقدرش أحرك", "شديد"],
    },
    {
        "id": "inj-back-01", "category": "injury",
        "title": "Back pain in microgravity",
        "text": "Back discomfort is common during spaceflight. Gentle mobility and core activation can help; "
                "avoid heavy spinal loading while symptomatic. Escalate if pain radiates, with leg weakness or "
                "numbness, or with fever.",
        "tags": ["back", "spine", "lumbar", "ظهر", "فقرات", "وجع الظهر"],
        "source": "NASA HRP - Spaceflight musculoskeletal risk reference (verify)",
        "reviewed": False,
        "red_flags": ["weakness", "numbness", "fever", "ضعف", "تنميل", "حرارة"],
    },
    {
        "id": "sleep-01", "category": "sleep",
        "title": "Sleep hygiene on a mission",
        "text": "Keep a regular sleep window, dim and warm the light in the evening, avoid screens and intense "
                "exercise shortly before sleep, and use slow breathing. Report persistent insomnia to the "
                "flight surgeon rather than self-medicating.",
        "tags": ["sleep", "insomnia", "نوم", "أرق", "circadian", "melatonin"],
        "source": "NASA HRP - Sleep & circadian countermeasures (verify)",
        "reviewed": False,
    },
    {
        "id": "env-co2-01", "category": "environment",
        "title": "Elevated cabin CO2 symptoms",
        "text": "Headache, drowsiness and faster breathing can accompany elevated CO2. Move to better-ventilated "
                "air, report to mission control, and avoid strenuous exercise until levels normalize.",
        "tags": ["co2", "headache", "ventilation", "صداع", "ثاني أكسيد الكربون", "تنفس"],
        "source": "NASA-STD-3001 vol. 2 - environmental limits (verify limits against standard)",
        "reviewed": False,
    },
    {
        "id": "mind-01", "category": "mental",
        "title": "Slow breathing for acute stress",
        "text": "Slow paced breathing (longer exhale than inhale) for a few minutes can reduce acute stress. "
                "Persistent low mood, hopelessness, or thoughts of self-harm require direct contact with the "
                "flight surgeon or behavioral health support.",
        "tags": ["stress", "anxiety", "breathing", "قلق", "توتر", "تنفس", "mood"],
        "source": "NASA HRP - Behavioral health & performance (verify)",
        "reviewed": False,
    },
]

TOKEN = re.compile(r"[\w؀-ۿ]+")


_AR_PREFIXES = ("وال", "ولل", "وال", "بال", "لل", "ال", "ل", "ب", "و")


def tokenize(text: str) -> List[str]:
    out: List[str] = []
    for t in (t.lower() for t in TOKEN.findall(text)):
        out.append(t)
        # Arabic clitic stripping so "لضغط" / "الدم" still match the tags "ضغط" / "دم"
        for pre in _AR_PREFIXES:
            if t.startswith(pre) and len(t) - len(pre) >= 3:
                out.append(t[len(pre):])
                break
    return out


class KnowledgeBase:
    def __init__(self, path: str | None = None):
        self.entries = list(DEFAULT_ENTRIES)
        if path and os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                loaded = json.load(f)
            ids = {e["id"] for e in loaded}
            self.entries = loaded + [e for e in DEFAULT_ENTRIES if e["id"] not in ids]
        self._docs = [Counter(tokenize(" ".join([e["title"], e["text"], " ".join(e.get("tags", []))]))
                              + tokenize(" ".join(e.get("tags", [])) * 2)) for e in self.entries]
        df: Counter = Counter()
        for d in self._docs:
            df.update(d.keys())
        n = len(self._docs)
        self._idf = {t: math.log(1 + n / c) for t, c in df.items()}

    def search(self, query: str, k: int = 3) -> List[dict]:
        q = tokenize(query)
        scored = []
        for e, d in zip(self.entries, self._docs):
            s = 0.0
            for t in q:
                if t in d:
                    s += self._idf.get(t, 0) * (1 + math.log(d[t]))
                elif len(t) >= 3:
                    # light morphology tolerance (Arabic suffixes/prefixes): prefix match
                    for dt in d:
                        if len(dt) >= 3 and (t.startswith(dt) or dt.startswith(t)):
                            s += 0.6 * self._idf.get(dt, 0)
                            break
            if s > 0:
                scored.append((s, e))
        scored.sort(key=lambda x: -x[0])
        return [e for _, e in scored[:k]]

    def answer(self, query: str, state: dict | None = None, lang: str | None = None) -> dict:
        lang = lang or ("ar" if AR_RE.search(query) else "en")
        ar = lang == "ar"
        hits = self.search(query)
        if not hits:
            return {"answer": ("معنديش بروتوكول للحالة دي، هبلّغ طبيب الرحلة." if ar else
                               "I don't have a protocol for that. I'll flag it for the flight surgeon."),
                    "sources": [], "escalate": True, "reviewed": False}
        top = hits[0]
        q = query.lower()
        flags = [f for f in top.get("red_flags", []) if f.lower() in q]
        notes = []
        if state:
            if state.get("fatigue", 0) > 60:
                notes.append("ارهاقك عالي النهارده، خلّي المجهود خفيف." if ar else
                             "Your fatigue is high today, so reduce intensity.")
            if state.get("wellness", 100) < 50:
                notes.append("حالتك العامة تحت المتوسط، خلّي النشاط هادي." if ar else
                             "Your wellness score is low; keep activity gentle.")
        body = top["text_ar"] if ar and top.get("text_ar") else top["text"]
        text = body + (" " + " ".join(notes) if notes else "")
        if flags:
            if ar:
                text += " لو فيه علامات خطر زي (" + "، ".join(flags) + ") هبلّغ طبيب الرحلة فوراً."
            else:
                text += " Warning signs mentioned (" + ", ".join(flags) + "): I'm notifying the flight surgeon."
        title = (top.get("title_ar") or top["title"]) if ar else top["title"]
        return {
            "answer": text, "title": title,
            "sources": [{"id": e["id"], "title": e["title"], "source": e["source"], "reviewed": e["reviewed"]}
                        for e in hits],
            "escalate": bool(flags),
            "reviewed": all(e["reviewed"] for e in hits),
            "disclaimer": ("نسخة تعليمية تجريبية: مش تشخيص. البروتوكولات لازم يراجعها دكتور أو معالج طبيعي." if ar else
                           "Educational prototype: not a diagnosis. Protocols must be reviewed by a doctor/PT."),
        }

    def workout_plan(self, state: dict | None = None) -> dict:
        fat = (state or {}).get("fatigue", 0)
        wellness = (state or {}).get("wellness", 100)
        factor = 1.0
        if fat > 60 or wellness < 50:
            factor = 0.6
        elif fat > 35:
            factor = 0.8
        block = lambda m: max(5, round(m * factor / 5) * 5)
        plan = [
            {"block": "Warm-up and mobility", "minutes": block(10)},
            {"block": "Resistance (legs, back, trunk)", "minutes": block(40)},
            {"block": "Aerobic", "minutes": block(30)},
            {"block": "Cool-down and breathing", "minutes": 10},
        ]
        return {
            "plan": plan, "intensity_factor": factor,
            "reason": "Reduced because of fatigue/wellness." if factor < 1 else "Normal intensity.",
            "sources": [e["id"] for e in self.entries if e["category"] == "exercise"],
            "disclaimer": "Sample plan for demonstration. Needs review by a PT/doctor.",
        }

# ---- module: companion ----

"""Voice companion brain: varied empathetic replies (Egyptian Arabic + English),
anti-repetition, cooldowns, proactive check-ins, optional LLM (Claude API).

Falls back to the canned library when no ANTHROPIC_API_KEY is set or the call fails.
"""

import json
import os
import random
import re
import time
import urllib.request
from datetime import datetime
from collections import deque
from typing import Deque, Dict, List, Optional

# ----------------------------------------------------------------- libraries
LIB: Dict[str, Dict[str, List[str]]] = {
    "ar": {
        "greet": [
            "أهلاً بيك، إزيك النهارده؟",
            "صباح الخير يا بطل، نمت كويس؟",
            "إزيك؟ نورت. حابب نتكلم شوية؟",
            "هاي، أنا هنا لو احتجت أي حاجة.",
        ],
        "tired": [
            "باين عليك تعبان. إيه أكتر حاجة مرهقاك دلوقتي؟",
            "الإرهاق ده طبيعي في الرحلات الطويلة. تحب ناخد استراحة خمس دقايق؟",
            "جسمك بيقولك يرتاح. هتقدر تنام شوية قبل المهمة الجاية؟",
            "أنا سامعك. جرّب نفس عميق ثلاث مرات، وقولي بعدها حاسس بإيه.",
        ],
        "anxious": [
            "حاسس إنك قلقان. خد نفس معايا: شهيق أربع ثواني، وزفير ست ثواني.",
            "القلق في الرحلات الطويلة شيء طبيعي جداً، وإنت مش لوحدك. إيه اللي شاغلك بالظبط؟",
            "خلينا نفكك الموضوع سوا. إيه أسوأ حاجة بتخوفك دلوقتي؟",
            "أنا معاك. ركز على اللي في إيدك دلوقتي، وخطوة خطوة.",
        ],
        "angry": [
            "واضح إنك متضايق، وده من حقك. تحب تفضفض وأنا هسمع من غير ما أقاطعك؟",
            "الضغط بيطلع في الغضب أحياناً. إيه اللي حصل؟",
            "خد دقيقة تهدا. لما تكون جاهز قولي إيه اللي ضايقك.",
        ],
        "lonely": [
            "الوحشة صعبة، وإنت بعيد جداً عن أهلك. تحب نتكلم عن حد واحشك؟",
            "أنا هنا معاك طول الرحلة. تحب أسمعك حاجة عن الأرض؟",
            "شعورك طبيعي، وهو معناه إنك إنسان. تحب نعمل مكالمة مسجلة لحد من أهلك؟",
            "حابب أحكيلك عن الجو الليلة في بلدك؟",
        ],
        "sleep": [
            "قلة النوم بتأثر على كل حاجة. إيه اللي بيصحيك؟",
            "خلينا نظبط روتين للنوم النهارده: إضاءة هادية وتنفس بطيء قبلها بنص ساعة.",
            "لو النوم مش جاي، ممكن نعمل تمرين استرخاء عضلي. تحب نبدأ؟",
        ],
        "doubt": [
            "إنت وصلت لهنا بجهد سنين، ومش صدفة. الشك طبيعي وهو بيعدي.",
            "حاسس إنك بتقسى على نفسك. إيه اللي نجحت فيه الأسبوع ده؟",
            "الإحباط ده مؤقت. خلينا نقسم المشكلة لحاجات صغيرة.",
        ],
        "happy": [
            "الحمد لله، فرحتني! إيه اللي حصل؟",
            "ده خبر حلو. استمتع باللحظة دي.",
            "حلو أوي إنك مبسوط. تحب نحتفل بلعبة سريعة؟",
        ],
        "pain": [
            "حاسس بوجع فين بالظبط؟ ولو من صفر لعشرة قد إيه؟",
            "خلينا نشوف الوجع ده. من إمتى بدأ، وبيزيد مع الحركة؟",
            "هبلغ الطبيب لو الوجع قوي. قولي أكتر عنه.",
        ],
        "exercise": [
            "تمام، هطلعلك برنامج تمرين على حسب حالتك النهارده. تحب نبدأ؟",
            "التمرين مهم للعضلات والعظام. اختار: مقاومة ولا كارديو؟",
        ],
        "game": [
            "فكرة حلوة. اختار لعبة تحت وخد خمس دقايق راحة.",
            "هتلاقي الألعاب في تبويب الألعاب. جرّب لعبة رد الفعل، بتفرق.",
        ],
        "thanks": ["على الرحب، أنا هنا دايماً.", "ولا يهمك، ده شغلي وأنا مبسوط بيه."],
        "unclear": [
            "ممكن تقولي أكتر؟ أنا سامعك.",
            "مش متأكد إني فهمت. تحب تحكيلي بطريقة تانية؟",
            "كمّل، أنا معاك.",
            "حاسس إن في حاجة في بالك. إيه هي؟",
            "تمام. وإيه اللي حاسس بيه دلوقتي؟",
        ],
        "no_hear": [
            "مش سامع صوتك بوضوح، ممكن تعيد؟",
            "قرّب من المايك شوية، الصوت ضعيف عندي.",
            "الصوت مش واصل كويس. تقدر تكرر الجملة؟",
            "في ضوضاء مغطية على صوتك. تعيد تاني؟",
        ],
        "tense_voice": [
            "صوتك فيه شدّ شوية، أنا سامعك.",
            "حاسس من صوتك إن في توتر. خد نفس ولو عايز تحكي أنا هنا.",
            "نبرتك مش مرتاحة. عايز نهدا سوا لحظة؟",
        ],
        "tired_voice": [
            "صوتك واطي وتعبان. أنا معاك لو عايز تستريح.",
            "باين عليك مرهق. تحب أقترح عليك استراحة قصيرة؟",
        ],
        "face_tired": [
            "ملامحك تعبانة شوية. إيه اللي مسهّرك؟",
            "عينيك بتقفل كتير. تحب نخلي بالنا من الراحة؟",
        ],
        "face_stress": [
            "حاسس إن في حاجة مضايقاك. تحب نتكلم؟",
            "ملامحك فيها توتر. خد نفس وقولي لو أقدر أساعد.",
        ],
        "sing": [
            "مش هعرف أغني بصوت حقيقي، بس هدندنلك لحن هادي وأقولك كلمات كتبتها ليك. نجمة بعيدة بتبصلك، والأرض كلها مستنياك. ارتاح شوية يا بطل، بكرة الطريق أقرب ليك.",
        ],
        "music": ["حاضر، هشغّل موسيقى هادية. قولي وقّف الموسيقى لما تحب.", "تمام، موسيقى هادية دلوقتي. استرخي."],
        "stopmusic": ["تمام، وقفتها.", "حاضر، وقّفت الموسيقى."],
        "joke": [
            "قالوا لرائد الفضاء: خد القهوة بالراحة. قال: ما هي كل مرة بتطير مني!",
            "سألوا رائد فضاء: بتخاف من إيه؟ قال: من حد يقولي «نزّل رجليك على الأرض»، وأنا مفيش أرض!",
            "إيه أحسن حاجة في الفضاء؟ إن مفيش زحمة مرور. وإيه أسوأ حاجة؟ إن مفيش حد يوصّلك.",
            "ليه القمر مابيحتاجش حلاق؟ عشان كل شهر بيقصّ نفسه!",
        ],
        "story": [
            "كان في رائد فضاء صغير زرع بذرة فاصوليا في كوباية على المحطة. كل يوم كان بيكلمها، وبعد أسبوعين طلعت ورقة خضرا. وقتها فهم إن الحياة بتلاقي طريقها حتى في أبعد مكان.",
            "مرة رائد فضاء بص من الشباك على الأرض، لقى سحابة على شكل قلب فوق بلده. ابتسم، وعرف إن في ناس تحت بتفكر فيه.",
        ],
        "fact": [
            "معلومة: المحطة الفضائية الدولية بتلف حوالي ستة عشر لفة حوالين الأرض في اليوم، يعني بتشوف حوالي ستة عشر شروق.",
            "معلومة: في الجاذبية الصغرى العمود الفقري بيتمدد، فالرواد ممكن يطولوا كام سنتيمتر، وبيرجعوا لطولهم بعد الرجوع.",
            "معلومة: الدموع في الفضاء ما بتنزلش، بتفضل متجمعة على العين زي نقطة ميّه.",
        ],
        "who": ["أنا ASHE، رفيقك في الرحلة. بسمعك وبساعدك تهتم بصحتك، ولو احتاجت دكتور هبلغه."],
        "goodbye": ["تصبح على خير، نوم هادي.", "مع السلامة، وأنا هنا لو احتجتني."],
        "doctor": ["تمام، هبلّغ الطبيب دلوقتي وأبعتله ملخص بحالتك. أنا معاك لحد ما يرد."],
        "alert_info": ["لاحظت تغيير بسيط: {text}. مفيش داعي للقلق دلوقتي."],
        "alert_warning": ["انتبه: {text}. عايزك تاخد استراحة وأنا هراقب."],
        "alert_critical": ["تنبيه مهم: {text}. هبلغ الطبيب. خد نفس وأنا معاك."],
    },
    "en": {
        "greet": [
            "Hi there, how are you doing today?",
            "Good to see you. Did you sleep okay?",
            "Hey. I'm here if you want to talk.",
        ],
        "tired": [
            "You seem tired. What's weighing on you most right now?",
            "Fatigue is normal on long missions. Want a five-minute break?",
            "Your body is asking for rest. Can you get a short nap before the next task?",
        ],
        "anxious": [
            "I can tell you're anxious. Breathe with me: in for four, out for six.",
            "Anxiety on a long mission is completely normal, and you're not alone. What's on your mind?",
            "Let's break it down together. What's the worst part right now?",
        ],
        "angry": [
            "You sound frustrated, and that's fair. Want to vent? I'll just listen.",
            "Pressure can come out as anger. What happened?",
            "Take a minute to settle. When you're ready, tell me what bothered you.",
        ],
        "lonely": [
            "Homesickness is hard when you're this far away. Want to talk about someone you miss?",
            "I'm here with you the whole trip. Want to hear something about home?",
            "Feeling this way means you're human. Want to record a message for family?",
        ],
        "sleep": [
            "Poor sleep affects everything. What's been keeping you up?",
            "Let's set a wind-down routine: dim light and slow breathing for half an hour.",
            "If sleep won't come, we can try muscle relaxation. Want to start?",
        ],
        "doubt": [
            "You got here through years of work. Doubt is normal and it passes.",
            "You sound hard on yourself. What went well this week?",
            "This frustration is temporary. Let's split the problem into small pieces.",
        ],
        "happy": ["That's great to hear! What happened?", "Lovely, enjoy the moment.", "Want to celebrate with a quick game?"],
        "pain": [
            "Where exactly does it hurt, and how bad from zero to ten?",
            "Let's look at it. When did it start, and does movement make it worse?",
            "I'll alert the doctor if it's severe. Tell me more.",
        ],
        "exercise": [
            "Sure, I'll build today's workout around how you're doing. Ready?",
            "Exercise protects your muscles and bones. Resistance or cardio?",
        ],
        "game": ["Nice idea. Pick a game below and take five.", "Try the reaction game, it also helps me gauge fatigue."],
        "thanks": ["Anytime. I'm always here.", "Of course, that's what I'm for."],
        "unclear": [
            "Tell me more, I'm listening.",
            "I'm not sure I got that. Could you say it another way?",
            "Go on, I'm with you.",
            "It feels like something is on your mind. What is it?",
        ],
        "no_hear": [
            "I can't hear you clearly, could you repeat that?",
            "Move a bit closer to the mic, the audio is faint.",
            "The audio isn't coming through well. Can you say it again?",
            "Some noise is covering your voice. Try again?",
        ],
        "tense_voice": [
            "Your voice sounds a bit tense. I'm listening.",
            "I can hear some tension. Take a breath, and talk if you want to.",
        ],
        "tired_voice": [
            "Your voice sounds low and tired. I'm here if you want to rest.",
            "You sound worn out. Want a short break?",
        ],
        "face_tired": ["You look tired. What kept you up?", "Your eyes are closing a lot. Shall we take care of rest?"],
        "face_stress": ["Something seems to be bothering you. Want to talk?", "I see some tension. Breathe, and tell me if I can help."],
        "sing": [
            "I can't sing with a real voice, but I'll hum a soft tune and share a few lines I wrote for you. A far-off star is watching you, the Earth is waiting, warm and blue. Rest a while, you've come so far, tomorrow's closer than you are.",
        ],
        "music": ["Sure, some calm music now. Say stop the music whenever you like.", "Okay, relaxing music coming up."],
        "stopmusic": ["Okay, stopped.", "Done, the music is off."],
        "joke": [
            "Why did the astronaut break up with the Earth? He needed more space.",
            "How does the moon cut its hair? Eclipse it.",
            "Why did the sun go to school? To get a little brighter.",
        ],
        "story": [
            "An astronaut once planted a bean in a cup on the station. He talked to it every day, and two weeks later a green leaf appeared. He learned that life finds a way, even in the farthest place.",
            "One day an astronaut looked out the window and saw a heart-shaped cloud over his hometown. He smiled, knowing people down there were thinking of him.",
        ],
        "fact": [
            "Fun fact: the International Space Station circles the Earth about sixteen times a day, so the crew sees roughly sixteen sunrises.",
            "Fun fact: in microgravity the spine lengthens, so astronauts can grow a few centimeters taller, and return to normal after landing.",
            "Fun fact: tears don't fall in space. They stay on the eye as a little ball of water.",
        ],
        "who": ["I'm ASHE, your companion on this trip. I listen, help you look after your health, and call the doctor if needed."],
        "goodbye": ["Good night, sleep well.", "Take care, I'm here if you need me."],
        "doctor": ["Okay, I'm notifying the flight surgeon now and sending a summary of how you're doing. I'm with you until they reply."],
        "alert_info": ["I noticed a small change: {text}. Nothing to worry about right now."],
        "alert_warning": ["Heads up: {text}. Take a break, I'll keep watching."],
        "alert_critical": ["Important alert: {text}. I'm notifying the doctor. Breathe, I'm with you."],
    },
}

INTENTS = [
    ("stopmusic", r"وقف.{0,12}موسيق|اقفل.{0,12}موسيق|بطل.{0,6}موسيق|stop (the )?music|turn off (the )?music"),
    ("music", r"موسيق|شغل.{0,8}(أغني|اغني|مزيك)|play (some )?(calm |relaxing )?music|\bmusic\b"),
    ("sing", r"غن[يّى]|دندن|\bsing\b|hum (me )?a"),
    ("joke", r"نكتة|نكته|اضحكني|هزار|joke|make me laugh|something funny"),
    ("story", r"قصة|قصه|حكاية|احكيلي|bedtime story|tell me a story|\bstory\b"),
    ("fact", r"معلومة|معلومه|اعرفني|حاجة عن الفضاء|fun fact|\bfact\b|tell me something about space"),
    ("doctor", r"عايز.{0,8}(دكتور|طبيب)|اندهلي.{0,6}(دكتور|طبيب)|بلغ.{0,6}(الدكتور|الطبيب)|call (the |a )?doctor|need (a |the )?doctor|flight surgeon|emergency|طوارئ|إسعاف"),
    ("status", r"حالتي|صحتي|نبضي|ضغطي|how am i|my (heart|health|status|pulse|vitals)|how('s| is) my"),
    ("time", r"الساعة كام|الساعة كم|كام الساعة|what time|time is it"),
    ("who", r"اسمك|إنت مين|انت مين|who are you|your name|what are you"),
    ("goodbye", r"تصبح على خير|مع السلامة|good ?night|goodbye|\bbye\b"),
    ("unwell", r"تعبان جسد|تعب جسد|حاسس بتعب|حاسس.{0,6}بتعب|مش حاسس بخير|مش (كويس|مرتاح)|مش حاسس بنفسي|i feel (sick|unwell|ill)|not feeling (well|good)|feel sick|physically (tired|unwell)"),
    ("firstaid", r"صداع|مصدع|دايخ|دوخة|دوار|غثيان|مغثي|عندي حرارة|سخن|حمى|جرح|نزيف|وجع.{0,6}صدر|ألم.{0,6}صدر|chest pain|headache|dizz|nause|fever|\bcut\b|bleed|faint"),
    ("reference", r"طبيعي|المعدل|المتوسط|المفروض|normal (range|level|value|blood|pressure|heart|glucose)|reference (range|value)|average (blood|heart|pressure)|what is normal"),
    ("pain", r"وجع|ألم|بيوجع|بيوجعني|pain|hurts?|ache|sore|injur|اتصبت|إصابة"),
    ("exercise", r"تمرين|رياضة|اتمرن|workout|exercise|train"),
    ("game", r"لعبة|العب|ألعاب|game|play|bored|زهقان|ملل"),
    ("anxious", r"قلقان|خايف|قلق|متوتر|توتر|panic|anxious|scared|afraid|worried|nervous|stress"),
    ("angry", r"متضايق|زعلان|غضبان|عصبي|angry|mad|furious|annoyed|frustrated"),
    ("lonely", r"وحيد|لوحدي|وحشة|واحشني|وحشتني|lonely|alone|miss (home|my)|homesick"),
    ("sleep", r"نوم|مش عارف أنام|سهران|أرق|sleep|insomnia|can't sleep|awake"),
    ("doubt", r"محبط|فاشل|مش قادر|إحباط|يأس|hopeless|useless|can't do|doubt|failure|give up"),
    ("tired", r"تعبان|تعب|مرهق|إرهاق|مصدع|tired|exhausted|fatigue|drained|sleepy"),
    ("happy", r"مبسوط|سعيد|فرحان|حلو|happy|glad|great|good news"),
    ("thanks", r"شكرا|شكراً|تسلم|thanks|thank you"),
    ("greet", r"إزيك|ازيك|أهلا|اهلا|صباح|مساء|السلام عليكم|hello|hi\b|hey|good morning|how are you"),
]

AR_RE = re.compile(r"[؀-ۿ]")
PROTOCOL_INTENTS = ("unwell", "firstaid", "reference")


class Companion:
    def __init__(self, rng: Optional[random.Random] = None):
        self.rng = rng or random.Random()
        self.last_by_key: Dict[str, str] = {}
        self.recent: Deque[str] = deque(maxlen=12)
        self.cooldown: Dict[str, float] = {}
        self.last_user: Dict[str, float] = {}
        self.history: Deque[dict] = deque(maxlen=14)
        self.last_proactive = 0.0
        self.api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
        self.model = os.environ.get("ASTROCARE_MODEL", "claude-sonnet-5-5")

    # ------------------------------------------------------------------ utils
    def pick(self, lang: str, key: str, **fmt) -> str:
        pool = LIB.get(lang, LIB["en"]).get(key) or LIB["en"][key]
        choices = [p for p in pool if p not in self.recent and p != self.last_by_key.get(key)]
        if not choices:
            choices = [p for p in pool if p != self.last_by_key.get(key)] or pool
        msg = self.rng.choice(choices)
        self.last_by_key[key] = msg
        self.recent.append(msg)
        return msg.format(**fmt) if fmt else msg

    def ready(self, key: str, seconds: float) -> bool:
        now = time.time()
        if now - self.cooldown.get(key, 0) < seconds:
            return False
        self.cooldown[key] = now
        return True

    @staticmethod
    def detect_lang(text: str, default: str = "ar") -> str:
        return "ar" if AR_RE.search(text) else ("en" if text.strip() else default)

    @staticmethod
    def classify(text: str) -> str:
        t = text.lower()
        for name, pat in INTENTS:
            if re.search(pat, t):
                return name
        return "unclear"

    # ------------------------------------------------------------------ input
    def duplicate(self, text: str, window: float = 6.0) -> bool:
        key = re.sub(r"\s+", " ", text.strip().lower())
        now = time.time()
        if now - self.last_user.get(key, 0) < window:
            return True
        self.last_user[key] = now
        if len(self.last_user) > 50:
            for k in sorted(self.last_user, key=self.last_user.get)[:20]:
                self.last_user.pop(k, None)
        return False

    def reply(self, text: str, lang: str, state: Optional[dict] = None) -> str:
        text = (text or "").strip()
        lang = lang if lang in LIB else self.detect_lang(text)
        if len(text) < 2:
            return self.pick(lang, "no_hear") if self.ready("no_hear", 20) else ""
        if self.duplicate(text):
            return ""
        self.history.append({"role": "user", "content": text})
        intent = self.classify(text)
        lg = self.detect_lang(text, lang)
        out = None
        if self.api_key and intent not in PROTOCOL_INTENTS:
            out = self._llm(text, lang, state)
        if not out:
            out = self.special(intent, lg, state, text) or self.pick(lg, intent)
        self.history.append({"role": "assistant", "content": out})
        return out


    def special(self, intent: str, lang: str, state: Optional[dict], text: str = "") -> Optional[str]:
        """Replies that depend on live data (time, the astronaut's own readings)."""
        if intent in PROTOCOL_INTENTS:
            return kb.answer(text, state, lang)["answer"]
        if intent == "time":
            t = datetime.now().strftime("%H:%M")
            return f"الساعة دلوقتي {t}." if lang == "ar" else f"It's {t} right now."
        if intent == "status" and state and state.get("metrics"):
            hr = state["metrics"].get("hr", {})
            demo = hr.get("source") == "simulated"
            w, f, st = round(state.get("wellness", 0)), round(state.get("fatigue", 0)), round(state.get("stress", 0))
            if lang == "ar":
                out = f"حالتك العامة {w} من 100. نبضك حوالي {round(hr.get('value', 0))} نبضة في الدقيقة"
                out += " (قراءة تجريبية)" if demo else ""
                out += f". الإرهاق {f} من 100 والتوتر {st} من 100."
                if w < 50:
                    out += " ده أقل من المعتاد، تحب أبلّغ الطبيب؟"
            else:
                out = f"Your overall wellness is {w} out of 100. Your pulse is about {round(hr.get('value', 0))} bpm"
                out += " (demo reading)" if demo else ""
                out += f". Fatigue is {f} and stress is {st} out of 100."
                if w < 50:
                    out += " That's lower than usual. Want me to notify the doctor?"
            return out
        return None

    # ------------------------------------------------------------ proactive
    def check_in(self, state: dict, lang: str) -> Optional[dict]:
        """Decide whether the companion should speak first. At most one message."""
        now = time.time()
        if now - self.last_proactive < 45:
            return None
        for a in state.get("alerts", []):
            lvl = a.get("level", "info")
            if lvl == "critical" or self.ready("alert_" + lvl, 60):
                self.last_proactive = now
                return {"text": self.pick(lang, "alert_" + lvl, text=a["text"]),
                        "priority": "critical" if lvl == "critical" else "normal", "reason": "alert"}
        fat, stress = state.get("fatigue", 0), state.get("stress", 0)
        vis = state.get("vision", {})
        if vis.get("perclos", 0) > 0.3 and fat > 45 and self.ready("face_tired", 180):
            self.last_proactive = now
            return {"text": self.pick(lang, "face_tired"), "priority": "normal", "reason": "face"}
        if (vis.get("stress", 0) > 0.6 or stress > 65) and self.ready("face_stress", 180):
            self.last_proactive = now
            return {"text": self.pick(lang, "face_stress"), "priority": "normal", "reason": "face"}
        return None

    def voice_note(self, voice_tone: str, lang: str) -> Optional[str]:
        if voice_tone == "tense" and self.ready("tense_voice", 120):
            return self.pick(lang, "tense_voice")
        if voice_tone == "tired" and self.ready("tired_voice", 120):
            return self.pick(lang, "tired_voice")
        return None

    def no_hear(self, lang: str) -> Optional[str]:
        return self.pick(lang, "no_hear") if self.ready("no_hear", 20) else None

    # -------------------------------------------------------------------- LLM
    def _llm(self, text: str, lang: str, state: Optional[dict]) -> Optional[str]:
        ctx = ""
        if state:
            ctx = (f"Wellness {state.get('wellness')}/100, fatigue {state.get('fatigue')}, "
                   f"stress {state.get('stress')}. Recent alerts: "
                   f"{[a['text'] for a in state.get('recent_alerts', [])[-3:]]}")
        system = (
            "You are ASHE, a warm, concise voice companion and friend-doctor for an astronaut on a long "
            "mission. Reply in the user's language (Egyptian Arabic if they write Arabic). Keep it to 1-3 short "
            "sentences. Be supportive; ask gentle questions instead of labeling emotions. Never diagnose; "
            "for injury or danger signs say you'll notify the flight surgeon. Do not repeat earlier phrases. "
            f"Current readings: {ctx}"
        )
        body = json.dumps({
            "model": self.model, "max_tokens": 200, "system": system,
            "messages": list(self.history)[-10:],
        }).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=body, method="POST",
            headers={"x-api-key": self.api_key, "anthropic-version": "2023-06-01",
                     "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read())
            return "".join(b.get("text", "") for b in data.get("content", [])).strip() or None
        except Exception:
            return None

# ---- module: groundlink ----

"""Ground-control link: store-and-forward with one-way light-time delay,
summary-only telemetry, explicit consent, tiered escalation, and read-only policy.

The spacecraft side batches summaries into packets stamped with a delivery time
(`now + delay`). The ground console only sees packets whose delivery time has passed.
"""

import time
from collections import deque
from typing import Deque, Dict, List, Optional

DEFAULT_CONSENT = {"vitals": True, "psychological": False, "genetic": False, "location": True}


class GroundLink:
    def __init__(self, delay_s: float = 8.0):
        self.delay_s = delay_s  # demo-compressed; "real" = minutes. Configurable.
        self.real_minutes = 12.0
        self.consent: Dict[str, bool] = dict(DEFAULT_CONSENT)
        self.outbox: Deque[dict] = deque(maxlen=500)
        self.delivered: Deque[dict] = deque(maxlen=200)
        self.tickets: List[dict] = []
        self.messages_down: Deque[dict] = deque(maxlen=50)  # earth -> ship (also delayed)
        self.last_summary = 0.0
        self.link_up = True

    # --------------------------------------------------------------- settings
    def set_delay(self, seconds: float, label_minutes: Optional[float] = None) -> None:
        self.delay_s = max(0.0, min(float(seconds), 120.0))
        if label_minutes is not None:
            self.real_minutes = max(0.0, min(float(label_minutes), 24.0))

    def set_consent(self, key: str, value: bool) -> bool:
        if key in self.consent:
            self.consent[key] = bool(value)
            return True
        return False

    # ------------------------------------------------------------- ship side
    def build_summary(self, state: dict) -> dict:
        """Summaries only. Never raw audio/video. Sections gated by consent."""
        s: dict = {"ts": state["ts"], "scenario_hint": None}
        if self.consent["vitals"]:
            s["vitals"] = {k: {"value": v["value"], "unit": v["unit"], "source": v["source"]}
                           for k, v in state["metrics"].items()}
            s["wellness"] = state["wellness"]
        if self.consent["psychological"]:
            s["psychological"] = {"fatigue": state["fatigue"], "stress": state["stress"]}
        else:
            s["psychological"] = "withheld (no consent)"
        if self.consent["genetic"]:
            s["genetic"] = state["genetic"]
        else:
            s["genetic"] = "withheld (no consent)"
        s["alerts"] = [a["text"] for a in state.get("recent_alerts", [])[-3:]]
        return s

    def push(self, payload: dict, kind: str = "telemetry", priority: str = "normal") -> dict:
        pkt = {"kind": kind, "priority": priority, "sent_at": time.time(),
               "deliver_at": time.time() + (self.delay_s if self.link_up else 10**9), "payload": payload}
        self.outbox.append(pkt)
        return pkt

    def maybe_send_summary(self, state: dict, every_s: float = 5.0) -> None:
        now = time.time()
        if now - self.last_summary >= every_s:
            self.last_summary = now
            self.push(self.build_summary(state), "telemetry")

    # -------------------------------------------------------------- escalation
    def escalate(self, level: str, state: dict, reason: str) -> Optional[dict]:
        """level: 1 gentle note (onboard only), 2 suggest action, 3 notify doctor with summary."""
        if level < 3:
            return None
        if any(t["status"] == "open" and t["reason"] == reason for t in self.tickets):
            return None  # one ticket per reason until acknowledged
        brief = {
            "reason": reason,
            "wellness": state["wellness"],
            "fatigue": state["fatigue"],
            "stress": state["stress"] if self.consent["psychological"] else "withheld",
            "recent_alerts": [a["text"] for a in state.get("recent_alerts", [])[-4:]],
            "suggested_contact": "Schedule private conference with the astronaut.",
            "advisory_only": True,
        }
        ticket = {"id": f"T{len(self.tickets) + 1:03d}", "status": "open", "reason": reason,
                  "created": time.time(), "brief": brief, "ack_at": None}
        self.tickets.append(ticket)
        self.push(ticket, "escalation", "critical")
        return ticket

    def acknowledge(self, ticket_id: str) -> Optional[dict]:
        for t in self.tickets:
            if t["id"] == ticket_id and t["status"] == "open":
                t["status"] = "acknowledged"
                t["ack_at"] = time.time()
                return t
        return None

    # -------------------------------------------------------------- ground side
    def pump(self) -> None:
        now = time.time()
        while self.outbox and self.outbox[0]["deliver_at"] <= now:
            self.delivered.append(self.outbox.popleft())

    def ground_view(self) -> dict:
        self.pump()
        latest = next((p for p in reversed(self.delivered) if p["kind"] == "telemetry"), None)
        now = time.time()
        return {
            "type": "ground", "ts": now,
            "link": {"up": self.link_up, "delay_s": self.delay_s, "one_way_label_min": self.real_minutes,
                     "in_flight": len(self.outbox)},
            "consent": self.consent,
            "latest": latest["payload"] if latest else None,
            "age_s": (now - latest["payload"]["ts"]) if latest else None,
            "escalations": [p["payload"] for p in list(self.delivered) if p["kind"] == "escalation"][-10:],
            "tickets": self.tickets[-10:],
            "downlink": list(self.messages_down)[-10:],
            "policy": "Advisory only. Read-only: no control over life-support or any ship system.",
        }

    def send_to_ship(self, text: str) -> dict:
        msg = {"text": text[:500], "sent_at": time.time(), "arrives_at": time.time() + self.delay_s}
        self.messages_down.append(msg)
        return msg

    def arrived_for_ship(self) -> List[dict]:
        now = time.time()
        out = []
        for m in self.messages_down:
            if m["arrives_at"] <= now and not m.get("shown"):
                m["shown"] = True
                out.append(m)
        return out

# ---- module: main ----

"""ASHE FastAPI server: ship app (/), ground console (/console), WebSocket + REST."""

import asyncio
import json
import os
from contextlib import asynccontextmanager
from typing import Any, Dict, Set

from fastapi import Body, FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = _FRONT_DIR

engine = Engine()
companion = Companion()
link = GroundLink(delay_s=float(os.environ.get("ASTROCARE_DELAY_S", "8")))
kb = KnowledgeBase(os.path.join(ROOT, "data", "protocols.json"))

ship_clients: Set[WebSocket] = set()
ground_clients: Set[WebSocket] = set()
lang_pref = {"lang": "ar"}
wellness_low_ticks = {"n": 0}


# ---- crew buddy network ----
CREW_ROSTER: List[dict] = [
    {"id": "you", "name": "You", "name_ar": "أنت", "role": "Astronaut", "status": "ok", "simulated": False},
    {"id": "cmd", "name": "Commander", "name_ar": "القائد", "role": "Commander", "status": "ok", "simulated": True},
    {"id": "eng", "name": "Engineer", "name_ar": "المهندس", "role": "Engineer", "status": "ok", "simulated": True},
    {"id": "doc", "name": "Doctor", "name_ar": "الدكتور", "role": "Medical officer", "status": "ok", "simulated": True},
]
CREW_NOTIFY_COOLDOWN_S = 120.0
_crew_last_notify: Dict[str, float] = {"t": 0.0}


def crew_view() -> dict:
    buddy = next((m for m in CREW_ROSTER if m["id"] != "you" and m["status"] == "ok"), None)
    return {
        "members": [dict(m) for m in CREW_ROSTER],
        "you_status": next(m["status"] for m in CREW_ROSTER if m["id"] == "you"),
        "buddy": buddy["id"] if buddy else None,
    }


def crew_set_status(member_id: str, status: str) -> bool:
    if status not in ("ok", "unwell"):
        return False
    for m in CREW_ROSTER:
        if m["id"] == member_id:
            m["status"] = status
            return True
    return False


async def crew_notify(member_id: str, lang: str) -> Optional[dict]:
    """Tell the other crew that someone feels physically unwell. The first free crew member is the buddy."""
    now = time.time()
    if now - _crew_last_notify["t"] < CREW_NOTIFY_COOLDOWN_S:
        return None
    _crew_last_notify["t"] = now
    who = next(m for m in CREW_ROSTER if m["id"] == member_id)
    buddy = next((m for m in CREW_ROSTER if m["id"] != member_id and m["status"] == "ok"), None)
    if lang == "ar":
        text = f"تنبيه للطاقم: {who['name_ar']} حاسس بتعب جسدي. " + (
            f"{buddy['name_ar']}، طمّن عليه من فضلك." if buddy else "محتاج حد يطمن عليه.")
    else:
        text = f"Crew alert: {who['name']} feels physically unwell. " + (
            f"{buddy['name']}, please check on them." if buddy else "Someone please check on them.")
    payload = {"type": "crew_alert", "text": text, "from": member_id,
               "buddy": buddy["id"] if buddy else None, "ts": now}
    await send_all(ship_clients, payload)
    await send_all(ship_clients, {"type": "speak", "text": text, "priority": "normal", "reason": "crew"})
    return payload


async def send_all(clients: Set[WebSocket], msg: Dict[str, Any]) -> None:
    dead = []
    for ws in list(clients):
        try:
            await ws.send_text(json.dumps(msg))
        except Exception:
            dead.append(ws)
    for ws in dead:
        clients.discard(ws)


async def loop() -> None:
    while True:
        try:
            state = engine.tick()
            link.maybe_send_summary(state)
            # escalation: critical alert, or sustained low wellness
            for a in state["alerts"]:
                if a["level"] == "critical":
                    link.escalate(3, state, f"{a['metric']}: {a['text']}")
            wellness_low_ticks["n"] = wellness_low_ticks["n"] + 1 if state["wellness"] < 40 else 0
            if wellness_low_ticks["n"] >= 10:
                link.escalate(3, state, "Sustained low wellness score")
            # onboard companion goes first
            if ship_clients:
                note = companion.check_in(state, lang_pref["lang"])
                if note:
                    await send_all(ship_clients, {"type": "speak", **note})
                for m in link.arrived_for_ship():
                    await send_all(ship_clients, {"type": "ground_msg", "text": m["text"]})
                state["tickets"] = link.tickets[-5:]
                state["crew"] = crew_view()
                await send_all(ship_clients, state)
            if ground_clients:
                await send_all(ground_clients, link.ground_view())
        except Exception as e:  # never let the loop die
            print("loop error:", repr(e))
        await asyncio.sleep(1.0)


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(loop())
    yield
    task.cancel()


app = FastAPI(title="ASHE", lifespan=lifespan)


# ----------------------------------------------------------------- websockets
@app.websocket("/ws")
async def ws_ship(ws: WebSocket):
    await ws.accept()
    ship_clients.add(ws)
    try:
        while True:
            raw = await ws.receive_text()
            try:
                msg = json.loads(raw)
            except Exception:
                continue
            t = msg.get("type")
            if t == "vision":
                engine.ingest_vision(msg)
            elif t == "voice":
                engine.ingest_voice(msg)
                tone = msg.get("tone")
                if tone:
                    note = companion.voice_note(tone, msg.get("lang", lang_pref["lang"]))
                    if note:
                        await send_all(ship_clients, {"type": "speak", "text": note, "priority": "normal",
                                                      "reason": "voice"})
            elif t == "speech":
                lang = msg.get("lang", lang_pref["lang"])
                lang_pref["lang"] = lang
                text = str(msg.get("text", ""))[:500]
                state = engine.snapshot()
                reply = companion.reply(text, lang, state)
                if reply:
                    await send_all(ship_clients, {"type": "speak", "text": reply, "priority": "normal",
                                                  "reason": "reply"})
                intent = companion.classify(text)
                if intent in ("sing", "music", "stopmusic"):
                    await send_all(ship_clients, {"type": "action", "name": intent})
                elif intent == "doctor":
                    link.escalate(3, state, "Astronaut asked for the flight surgeon")
                if intent in ("unwell", "firstaid"):
                    crew_set_status("you", "unwell")
                    await crew_notify("you", lang)
                if intent in ("pain", "exercise", "reference", "unwell", "firstaid"):
                    ans = kb.answer(text, state, lang)
                    await send_all(ship_clients, {"type": "kb", **ans})
                    if ans.get("escalate"):
                        link.escalate(3, state, "Injury red-flag reported: " + text[:80])
            elif t == "greet":
                lang = msg.get("lang", lang_pref["lang"])
                await send_all(ship_clients, {"type": "speak", "text": companion.pick(lang, "greet"),
                                              "priority": "normal", "reason": "greet"})
            elif t == "no_hear":
                note = companion.no_hear(msg.get("lang", lang_pref["lang"]))
                if note:
                    await send_all(ship_clients, {"type": "speak", "text": note, "priority": "low",
                                                  "reason": "no_hear"})
            elif t == "lang":
                if msg.get("lang") in ("ar", "en"):
                    lang_pref["lang"] = msg["lang"]
            elif t == "scenario":
                engine.set_scenario(str(msg.get("name", "normal")))
            elif t == "mode":
                engine.set_mode(str(msg.get("mode", "demo")))
            elif t == "game":
                engine.record_game(float(msg.get("reaction_ms", 0)))
            elif t == "consent":
                link.set_consent(str(msg.get("key")), bool(msg.get("value")))
    except WebSocketDisconnect:
        pass
    finally:
        ship_clients.discard(ws)


@app.websocket("/ws/ground")
async def ws_ground(ws: WebSocket):
    await ws.accept()
    ground_clients.add(ws)
    try:
        while True:
            raw = await ws.receive_text()
            try:
                msg = json.loads(raw)
            except Exception:
                continue
            if msg.get("type") == "ack":
                link.acknowledge(str(msg.get("id")))
            elif msg.get("type") == "to_ship":
                link.send_to_ship(str(msg.get("text", "")))
    except WebSocketDisconnect:
        pass
    finally:
        ground_clients.discard(ws)


# ------------------------------------------------------------------------ REST
@app.post("/api/sensor")
async def api_sensor(payload: Dict[str, Any] = Body(...)):
    readings = payload.get("readings", payload)
    accepted = engine.ingest_sensor({k: v for k, v in readings.items() if k != "device"})
    return {"accepted": accepted, "mode": engine.mode,
            "note": "Switch to Live mode in the UI to use these readings." if engine.mode != "live" else "ok"}


@app.get("/api/state")
async def api_state():
    return engine.snapshot()


@app.get("/api/scenarios")
async def api_scenarios():
    return list(SCENARIOS.keys())


@app.get("/api/connectors")
async def api_connectors():
    return CONNECTORS


@app.post("/api/kb/ask")
async def api_kb(payload: Dict[str, Any] = Body(...)):
    return kb.answer(str(payload.get("q", "")), engine.snapshot())


@app.get("/api/workout")
async def api_workout():
    return kb.workout_plan(engine.snapshot())


@app.get("/api/ground")
async def api_ground():
    return link.ground_view()


@app.post("/api/ground/delay")
async def api_delay(payload: Dict[str, Any] = Body(...)):
    link.set_delay(float(payload.get("seconds", 8)), payload.get("label_minutes"))
    return {"delay_s": link.delay_s}


@app.post("/api/ground/consent")
async def api_consent(payload: Dict[str, Any] = Body(...)):
    ok = link.set_consent(str(payload.get("key")), bool(payload.get("value")))
    return JSONResponse({"ok": ok, "consent": link.consent}, status_code=200 if ok else 400)


@app.get("/api/crew")
async def api_crew():
    return crew_view()


@app.post("/api/crew/unwell")
async def api_crew_unwell(payload: Optional[Dict[str, Any]] = None):
    crew_set_status("you", "unwell")
    lang = lang_pref["lang"]
    sent = await crew_notify("you", lang)
    guidance = kb.answer("unwell", engine.snapshot(), lang)
    return {"ok": True, "notified": bool(sent), "guidance": guidance}


@app.post("/api/crew/status")
async def api_crew_status(payload: Dict[str, Any] = Body(...)):
    ok = crew_set_status("you", str(payload.get("status", "ok")))
    return {"ok": ok, "crew": crew_view()}


@app.get("/api/kb/entries")
async def api_kb_entries():
    return [{"id": e["id"], "category": e.get("category", ""), "title": e.get("title", ""),
             "title_ar": e.get("title_ar", ""), "text": e.get("text", ""), "text_ar": e.get("text_ar", ""),
             "source": e.get("source", ""), "reviewed": bool(e.get("reviewed"))} for e in kb.entries]


# ----------------------------------------------------------------- static pages
@app.get("/console")
async def console_page():
    return FileResponse(os.path.join(FRONT, "console.html"))


# ---- wallpapers folder: drop space pictures next to ASHE.exe in a folder called "wallpapers" ----
_WP_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".avif"}


def _wp_dir() -> str:
    import sys
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "wallpapers")


@app.get("/api/wallpapers")
async def api_wallpapers():
    from urllib.parse import quote
    d = _wp_dir()
    try:
        names = sorted(n for n in os.listdir(d) if os.path.splitext(n)[1].lower() in _WP_EXT and os.path.isfile(os.path.join(d, n)))
    except OSError:
        names = []
    return [{"name": n, "url": "/wallpapers/" + quote(n)} for n in names]


@app.get("/wallpapers/{name}")
async def wallpaper_file(name: str):
    d = os.path.realpath(_wp_dir())
    p = os.path.realpath(os.path.join(d, os.path.basename(name)))
    if os.path.dirname(p) != d or os.path.splitext(p)[1].lower() not in _WP_EXT or not os.path.isfile(p):
        return JSONResponse({"error": "not found"}, status_code=404)
    return FileResponse(p)


app.mount("/", StaticFiles(directory=FRONT, html=True), name="static")


def run():
    import socket, threading, time, webbrowser, uvicorn
    port = 8765
    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning", log_config=None))
    threading.Thread(target=server.run, daemon=True).start()
    for _ in range(100):
        try:
            socket.create_connection(("127.0.0.1", port), 0.2).close()
            break
        except OSError:
            time.sleep(0.1)
    url = f"http://127.0.0.1:{port}/"
    try:
        import webview
    except ImportError:
        webbrowser.open(url)
        while True:
            time.sleep(1)
    webview.create_window("ASHE", url, width=1280, height=820)
    webview.start()

if __name__ == "__main__":
    run()

