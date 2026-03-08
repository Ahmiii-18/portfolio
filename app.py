import gradio as gr

# ─── YOUR INFO ─────────────────────────────────────────────────────
NAME = "Ahmad Sheraz"
ROLE = "AI & Robotics Student"
BIO = (
    "Interested in the virtual world of Robotics and Artificial Intelligence, "
    "with a focus on Machine Learning. Studying BSc in Robotics & AI at the "
    "University of Lahore, while actively building web apps and sharpening my coding skills."
)

SKILLS = {
    "Languages":   ["Python", "C++", "JavaScript"],
    "Web":         ["HTML", "CSS"],
    "Interests":   ["Machine Learning", "Robotics", "AI", "Web Development"],
    "Tools":       ["Git", "GitHub", "VS Code"],
}

PROJECTS = [
    {
        "title": "🌙 Ramadan Countdown App",
        "description": (
            "A web-based Ramadan countdown application built and published via GitHub Pages. "
            "Displays a live countdown to Ramadan with a clean, interactive browser interface."
        ),
        "tech": "HTML · CSS · JavaScript · GitHub Pages",
        "link": "https://github.com/Ahmiii-18",
    },
    {
        "title": "⚡ Speed Test App",
        "description": (
            "A browser-based internet speed testing application. "
            "Measures and displays real-time download/upload speeds directly in the web browser."
        ),
        "tech": "HTML · CSS · JavaScript · GitHub Pages",
        "link": "https://github.com/Ahmiii-18",
    },
]

EDUCATION = [
    {
        "degree": "BSRAi — Robotics and Artificial Intelligence",
        "school": "University of Lahore (UOL)",
        "year": "2024 – 2028",
        "detail": "Studying AI, Robotics, and Machine Learning",
    },
]

CONTACT = {
    "Email":    "ahmadshiraz912@icloud.com",
    "LinkedIn": "linkedin.com/in/ahmad-shiraz-8bb9a63a9",
    "GitHub":   "github.com/Ahmiii-18",
    "Location": "Lahore, Punjab, Pakistan",
}

# ─── CSS ───────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;700;900&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:         #020409;
  --bg2:        #060b14;
  --glass:      rgba(255,255,255,0.04);
  --glass2:     rgba(255,255,255,0.07);
  --border:     rgba(255,255,255,0.08);
  --border2:    rgba(99,179,255,0.3);
  --cyan:       #00d4ff;
  --blue:       #4f8ef7;
  --violet:     #bf87ff;
  --green:      #00ffb3;
  --orange:     #ff8c42;
  --text:       #f0f4ff;
  --muted:      #6b7799;
  --radius:     16px;
  --mono:       'Fira Code', monospace;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body, .gradio-container {
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: 'Outfit', sans-serif !important;
  min-height: 100vh;
  overflow-x: hidden;
}

footer, .svelte-1ipelgc { display: none !important; }
.gradio-container { padding: 0 !important; max-width: 100% !important; }

/* ── Canvas bg ── */
#particles-canvas {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  z-index: 0;
  opacity: 0.5;
}

.portfolio-wrap { position: relative; z-index: 1; }

/* ── HERO ── */
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 24px 60px;
  position: relative;
  overflow: hidden;
}

.hero-glow {
  position: absolute;
  width: 700px; height: 700px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0,212,255,0.06) 0%, transparent 70%);
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  animation: pulse-glow 4s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
  50%       { opacity: 1;   transform: translate(-50%, -50%) scale(1.1); }
}

.hero-badge {
  display: inline-block;
  font-family: var(--mono);
  font-size: 11px;
  color: var(--cyan);
  letter-spacing: .2em;
  text-transform: uppercase;
  border: 1px solid rgba(0,212,255,0.3);
  background: rgba(0,212,255,0.05);
  padding: 6px 18px;
  border-radius: 20px;
  margin-bottom: 32px;
  animation: fadeInDown .8s ease both;
}

.hero-name {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(42px, 8vw, 88px);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
  animation: fadeInUp .8s .1s ease both;
}

.hero-name .line1 { display: block; color: var(--text); }
.hero-name .line2 {
  display: block;
  background: linear-gradient(90deg, var(--cyan), var(--violet));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-role {
  font-size: 18px;
  color: var(--muted);
  font-weight: 400;
  margin-bottom: 28px;
  animation: fadeInUp .8s .2s ease both;
}
.hero-role span { color: var(--blue); font-weight: 600; }

.hero-bio {
  font-size: 16px;
  color: var(--muted);
  line-height: 1.8;
  max-width: 580px;
  margin: 0 auto 48px;
  animation: fadeInUp .8s .3s ease both;
}

.hero-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 52px;
  animation: fadeInUp .8s .4s ease both;
}
.hero-chip {
  font-family: var(--mono);
  font-size: 12px;
  padding: 6px 16px;
  border-radius: 20px;
  border: 1px solid;
}
.chip-cyan   { color: var(--cyan);   border-color: rgba(0,212,255,0.3);   background: rgba(0,212,255,0.05); }
.chip-violet { color: var(--violet); border-color: rgba(191,135,255,0.3); background: rgba(191,135,255,0.05); }
.chip-green  { color: var(--green);  border-color: rgba(0,255,179,0.3);   background: rgba(0,255,179,0.05); }

.scroll-hint {
  position: absolute;
  bottom: 32px; left: 50%;
  transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  color: var(--muted); font-size: 12px; letter-spacing: .1em;
  animation: fadeIn 1s 1s ease both;
}
.scroll-line {
  width: 1px; height: 48px;
  background: linear-gradient(to bottom, var(--cyan), transparent);
  animation: scrollPulse 1.5s ease-in-out infinite;
}
@keyframes scrollPulse { 0%,100%{opacity:.3} 50%{opacity:1} }

/* ── SECTIONS ── */
.section {
  padding: 100px 24px;
  max-width: 1080px;
  margin: 0 auto;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 56px;
}
.section-num {
  font-family: var(--mono);
  font-size: 12px;
  color: var(--cyan);
  opacity: .6;
}
.section-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: .05em;
}
.section-line {
  flex: 1; height: 1px;
  background: linear-gradient(90deg, rgba(0,212,255,.2), transparent);
}

/* ── GLASS CARD ── */
.g-card {
  background: var(--glass);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
  backdrop-filter: blur(12px);
  transition: all .3s cubic-bezier(.4,0,.2,1);
  position: relative;
  overflow: hidden;
}
.g-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,212,255,.4), transparent);
  opacity: 0;
  transition: opacity .3s;
}
.g-card:hover {
  background: var(--glass2);
  border-color: var(--border2);
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(0,212,255,.08);
}
.g-card:hover::before { opacity: 1; }

/* ── SKILLS ── */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}
.skill-label {
  font-family: var(--mono);
  font-size: 10px;
  color: var(--cyan);
  letter-spacing: .15em;
  text-transform: uppercase;
  margin-bottom: 16px;
  opacity: .8;
}
.pills { display: flex; flex-wrap: wrap; gap: 8px; }
.pill {
  font-size: 13px; font-weight: 500;
  padding: 5px 14px;
  border-radius: 8px;
  border: 1px solid rgba(79,142,247,.25);
  background: rgba(79,142,247,.08);
  color: #a8c4ff;
  transition: all .2s;
}
.pill:hover {
  background: rgba(79,142,247,.2);
  border-color: var(--blue);
  color: #fff;
  transform: scale(1.05);
}

/* ── PROJECTS ── */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 24px;
}
.proj-number {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--cyan);
  opacity: .5;
  margin-bottom: 12px;
}
.proj-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 14px;
  color: var(--text);
}
.proj-desc {
  font-size: 14px;
  color: var(--muted);
  line-height: 1.75;
  margin-bottom: 24px;
}
.proj-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
.proj-tech {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--violet);
  background: rgba(191,135,255,.08);
  border: 1px solid rgba(191,135,255,.2);
  padding: 5px 12px;
  border-radius: 6px;
}
.proj-link {
  font-size: 13px;
  font-weight: 600;
  color: var(--cyan);
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: gap .2s;
}
.proj-link:hover { gap: 10px; }
.proj-accent {
  position: absolute;
  top: -20px; right: -20px;
  width: 120px; height: 120px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0,212,255,.06), transparent 70%);
  pointer-events: none;
}

/* ── EDUCATION ── */
.edu-card {
  display: flex;
  align-items: flex-start;
  gap: 28px;
}
.edu-icon {
  width: 52px; height: 52px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(0,212,255,.15), rgba(191,135,255,.15));
  border: 1px solid rgba(0,212,255,.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 22px;
  flex-shrink: 0;
}
.edu-degree {
  font-size: 18px; font-weight: 700;
  margin-bottom: 6px;
}
.edu-school { font-size: 14px; color: var(--blue); margin-bottom: 6px; font-weight: 500; }
.edu-detail { font-size: 13px; color: var(--muted); }
.edu-year {
  margin-left: auto; flex-shrink: 0;
  font-family: var(--mono); font-size: 12px;
  color: var(--green);
  background: rgba(0,255,179,.06);
  border: 1px solid rgba(0,255,179,.2);
  padding: 6px 14px; border-radius: 8px;
  white-space: nowrap;
}

/* ── CONTACT ── */
.contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
}
.contact-icon { font-size: 22px; margin-bottom: 12px; }
.contact-lbl {
  font-family: var(--mono); font-size: 10px;
  color: var(--cyan); letter-spacing: .15em;
  text-transform: uppercase; margin-bottom: 6px; opacity: .7;
}
.contact-val { font-size: 14px; color: var(--text); word-break: break-all; }

/* ── FOOTER ── */
.site-footer {
  text-align: center;
  padding: 40px 24px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 13px;
  font-family: var(--mono);
  letter-spacing: .05em;
}
.site-footer span { color: var(--cyan); }

/* ── ANIMATIONS ── */
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-20px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* ── Divider ── */
.divider {
  width: 100%; height: 1px;
  background: linear-gradient(90deg, transparent, var(--border), transparent);
  max-width: 1080px;
  margin: 0 auto;
}
"""

# ─── HTML BUILDERS ─────────────────────────────────────────────────
def skills_html():
    cards = ""
    for group, items in SKILLS.items():
        pills = "".join(f'<span class="pill">{s}</span>' for s in items)
        cards += f"""
        <div class="g-card">
          <div class="skill-label">{group}</div>
          <div class="pills">{pills}</div>
        </div>"""
    return f'<div class="skills-grid">{cards}</div>'

def projects_html():
    cards = ""
    for i, p in enumerate(PROJECTS):
        num = str(i + 1).zfill(2)
        cards += f"""
        <div class="g-card">
          <div class="proj-accent"></div>
          <div class="proj-number">PROJECT_{num}</div>
          <div class="proj-title">{p['title']}</div>
          <div class="proj-desc">{p['description']}</div>
          <div class="proj-footer">
            <span class="proj-tech">{p['tech']}</span>
            <a class="proj-link" href="{p['link']}" target="_blank">View on GitHub →</a>
          </div>
        </div>"""
    return f'<div class="projects-grid">{cards}</div>'

def education_html():
    cards = ""
    for e in EDUCATION:
        cards += f"""
        <div class="g-card">
          <div class="edu-card">
            <div class="edu-icon">🎓</div>
            <div>
              <div class="edu-degree">{e['degree']}</div>
              <div class="edu-school">{e['school']}</div>
              <div class="edu-detail">{e['detail']}</div>
            </div>
            <div class="edu-year">{e['year']}</div>
          </div>
        </div>"""
    return cards

def contact_html():
    icons = {"Email": "✉️", "LinkedIn": "💼", "GitHub": "🐙", "Location": "📍"}
    cards = ""
    for label, value in CONTACT.items():
        icon = icons.get(label, "🔗")
        cards += f"""
        <div class="g-card">
          <div class="contact-icon">{icon}</div>
          <div class="contact-lbl">{label}</div>
          <div class="contact-val">{value}</div>
        </div>"""
    return f'<div class="contact-grid">{cards}</div>'

# ─── FULL PAGE ─────────────────────────────────────────────────────
PAGE = f"""
<canvas id="particles-canvas"></canvas>

<div class="portfolio-wrap">

  <!-- HERO -->
  <section class="hero">
    <div class="hero-glow"></div>
    <div class="hero-badge">BSRAi · University of Lahore · 2024</div>
    <h1 class="hero-name">
      <span class="line1">Ahmad</span>
      <span class="line2">Sheraz</span>
    </h1>
    <p class="hero-role">
      <span>{ROLE}</span> — Building the Future
    </p>
    <p class="hero-bio">{BIO}</p>
    <div class="hero-chips">
      <span class="hero-chip chip-cyan">🤖 Robotics</span>
      <span class="hero-chip chip-violet">🧠 AI / ML</span>
      <span class="hero-chip chip-green">💻 Web Dev</span>
    </div>
    <div class="scroll-hint">
      <span>SCROLL</span>
      <div class="scroll-line"></div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- SKILLS -->
  <section class="section">
    <div class="section-header">
      <span class="section-num">01</span>
      <h2 class="section-title">SKILLS</h2>
      <div class="section-line"></div>
    </div>
    {skills_html()}
  </section>

  <div class="divider"></div>

  <!-- PROJECTS -->
  <section class="section">
    <div class="section-header">
      <span class="section-num">02</span>
      <h2 class="section-title">PROJECTS</h2>
      <div class="section-line"></div>
    </div>
    {projects_html()}
  </section>

  <div class="divider"></div>

  <!-- EDUCATION -->
  <section class="section">
    <div class="section-header">
      <span class="section-num">03</span>
      <h2 class="section-title">EDUCATION</h2>
      <div class="section-line"></div>
    </div>
    {education_html()}
  </section>

  <div class="divider"></div>

  <!-- CONTACT -->
  <section class="section">
    <div class="section-header">
      <span class="section-num">04</span>
      <h2 class="section-title">CONTACT</h2>
      <div class="section-line"></div>
    </div>
    {contact_html()}
  </section>

  <!-- FOOTER -->
  <footer class="site-footer">
    <span>{NAME}</span> · BSRAi · UOL · Built with Python &amp; Gradio
  </footer>

</div>

<script>
// ── Particle field ──────────────────────────────────────────────────
(function() {{
  const canvas = document.getElementById('particles-canvas');
  const ctx = canvas.getContext('2d');
  let W, H, particles = [];

  function resize() {{
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }}

  function randomParticle() {{
    return {{
      x: Math.random() * W,
      y: Math.random() * H,
      r: Math.random() * 1.5 + 0.3,
      dx: (Math.random() - 0.5) * 0.3,
      dy: (Math.random() - 0.5) * 0.3,
      alpha: Math.random() * 0.6 + 0.1,
    }};
  }}

  function init() {{
    resize();
    particles = Array.from({{length: 120}}, randomParticle);
  }}

  function draw() {{
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {{
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(0,212,255,${{p.alpha}})`;
      ctx.fill();
      p.x += p.dx; p.y += p.dy;
      if (p.x < 0 || p.x > W) p.dx *= -1;
      if (p.y < 0 || p.y > H) p.dy *= -1;
    }});

    // draw lines between close particles
    for (let i = 0; i < particles.length; i++) {{
      for (let j = i + 1; j < particles.length; j++) {{
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist < 100) {{
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(0,212,255,${{(1 - dist/100) * 0.12}})`;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }}
      }}
    }}

    requestAnimationFrame(draw);
  }}

  window.addEventListener('resize', resize);
  init();
  draw();
}})();
</script>
"""

# ─── GRADIO APP ────────────────────────────────────────────────────
with gr.Blocks(css=CSS, title="Ahmad Sheraz — Portfolio") as demo:
    gr.HTML(PAGE)

if __name__ == "__main__":

    demo.launch()
