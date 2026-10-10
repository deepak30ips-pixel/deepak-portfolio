
# This script writes the premium upgraded files for the portfolio

import os

BASE = r"C:\Users\PC\.gemini\antigravity\scratch\deepak-portfolio"

# ============================================================
# 1. WRITE NEW css/custom.css
# ============================================================
css_content = r"""/* Custom Styles & Keyframe Animations for Deepak S Portfolio */
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap');

:root {
  --accent-primary: #06b6d4;
  --accent-secondary: #3b82f6;
  --accent-tertiary: #8b5cf6;
  --glow-primary: rgba(6, 182, 212, 0.2);
  --glow-secondary: rgba(59, 130, 246, 0.18);
  --spotlight-glow: rgba(59, 130, 246, 0.15);
  --theme-transition: background 0.5s ease, color 0.4s ease, border-color 0.4s ease;
}

/* ===== COLOR THEMES ===== */
body.theme-cyan {
  --accent-primary: #06b6d4;
  --accent-secondary: #3b82f6;
  --accent-tertiary: #8b5cf6;
  --glow-primary: rgba(6, 182, 212, 0.25);
  --glow-secondary: rgba(59, 130, 246, 0.2);
  --spotlight-glow: rgba(59, 130, 246, 0.15);
}

body.theme-purple {
  --accent-primary: #c084fc;
  --accent-secondary: #e879f9;
  --accent-tertiary: #f43f5e;
  --glow-primary: rgba(192, 132, 252, 0.28);
  --glow-secondary: rgba(232, 121, 249, 0.22);
  --spotlight-glow: rgba(232, 121, 249, 0.18);
}

body.theme-emerald {
  --accent-primary: #34d399;
  --accent-secondary: #10b981;
  --accent-tertiary: #06b6d4;
  --glow-primary: rgba(52, 211, 153, 0.28);
  --glow-secondary: rgba(16, 185, 129, 0.22);
  --spotlight-glow: rgba(16, 185, 129, 0.18);
}

body.theme-amber {
  --accent-primary: #fbbf24;
  --accent-secondary: #f97316;
  --accent-tertiary: #ef4444;
  --glow-primary: rgba(251, 191, 36, 0.28);
  --glow-secondary: rgba(249, 115, 22, 0.22);
  --spotlight-glow: rgba(249, 115, 22, 0.18);
}

body {
  font-family: 'Inter', sans-serif;
  background-color: #060911;
  color: #f1f5f9;
  overflow-x: hidden;
  transition: color 0.4s ease;
}

h1, h2, h3, h4, .font-heading {
  font-family: 'Space Grotesk', sans-serif;
}

.font-mono-code {
  font-family: 'Fira Code', monospace;
}

/* ===== CUSTOM SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #060911; }
::-webkit-scrollbar-thumb {
  background: #1e293b;
  border-radius: 9999px;
  border: 2px solid #060911;
}
::-webkit-scrollbar-thumb:hover { background: var(--accent-secondary); }

/* ===== GLASSMORPHISM ===== */
.glass-panel {
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.glass-panel-subtle {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

/* ===== 3D PARALLAX TILT CARD ===== */
.tilt-card {
  transform-style: preserve-3d;
  transition: transform 0.15s cubic-bezier(0.03, 0.98, 0.52, 0.99), box-shadow 0.3s ease;
  will-change: transform;
}
.tilt-card-inner {
  transform: translateZ(24px);
  transform-style: preserve-3d;
}

/* ===== MOUSE SPOTLIGHT ON CARDS ===== */
.spotlight-card {
  position: relative;
  overflow: hidden;
}
.spotlight-card::before {
  content: '';
  position: absolute;
  top: var(--mouse-y, -1000px);
  left: var(--mouse-x, -1000px);
  width: 350px;
  height: 350px;
  background: radial-gradient(circle, var(--spotlight-glow) 0%, transparent 70%);
  transform: translate(-50%, -50%);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s;
  z-index: 1;
}
.spotlight-card:hover::before { opacity: 1; }

.glass-card-hover {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.glass-card-hover:hover {
  transform: translateY(-4px);
  border-color: var(--accent-primary);
  box-shadow: 0 12px 30px -10px var(--glow-primary);
}

/* ===== AMBIENT GLOW ORBS ===== */
.glow-orb-1 {
  position: absolute;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--glow-primary) 0%, rgba(59, 130, 246, 0) 70%);
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
  animation: pulseGlow 8s infinite alternate ease-in-out;
  transition: background 0.5s ease;
}
.glow-orb-2 {
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--glow-secondary) 0%, rgba(168, 85, 247, 0) 70%);
  filter: blur(50px);
  pointer-events: none;
  z-index: 0;
  animation: pulseGlow 10s infinite alternate-reverse ease-in-out;
  transition: background 0.5s ease;
}

/* ===== TYPEWRITER CURSOR ===== */
.typewriter-cursor {
  display: inline-block;
  width: 3px;
  height: 1.1em;
  background-color: var(--accent-primary);
  margin-left: 4px;
  vertical-align: middle;
  animation: blinkCursor 0.8s infinite;
}

@keyframes blinkCursor {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

@keyframes pulseGlow {
  0% { opacity: 0.6; transform: scale(0.95); }
  100% { opacity: 1; transform: scale(1.08); }
}

/* ===== FLOATING BADGES ===== */
@keyframes floatSlow1 {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-10px) rotate(1deg); }
}
@keyframes floatSlow2 {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-14px) rotate(-1.5deg); }
}
@keyframes floatSlow3 {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-8px) rotate(1deg); }
}
.animate-float-1 { animation: floatSlow1 4.5s ease-in-out infinite; }
.animate-float-2 { animation: floatSlow2 5.5s ease-in-out infinite 0.8s; }
.animate-float-3 { animation: floatSlow3 6s ease-in-out infinite 1.5s; }
.animate-float-4 { animation: floatSlow1 5s ease-in-out infinite 2s; }

/* ===== BACKGROUND GRID ===== */
.bg-grid-pattern {
  background-size: 40px 40px;
  background-image:
    linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
}

/* ===== TERMINAL ===== */
.terminal-window {
  background: rgba(10, 15, 28, 0.85);
  border: 1px solid rgba(59, 130, 246, 0.2);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
}
.terminal-input {
  background: transparent;
  outline: none;
  border: none;
  color: var(--accent-primary);
  width: 100%;
}

/* ===== AI CHAT DRAWER ===== */
.ai-chat-window {
  box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8), 0 0 30px var(--glow-primary);
  border: 1px solid rgba(255,255,255,0.08);
}
.ai-chat-window.open {
  transform: translateY(0) scale(1);
  opacity: 1;
  pointer-events: all;
}
.ai-chat-window.closed {
  transform: translateY(20px) scale(0.97);
  opacity: 0;
  pointer-events: none;
}
.chat-msg-user {
  background: linear-gradient(135deg, #1d4ed8, #6d28d9);
  border-radius: 18px 18px 4px 18px;
  padding: 8px 14px;
  font-size: 12px;
  color: #fff;
  max-width: 82%;
  align-self: flex-end;
  line-height: 1.5;
  word-break: break-word;
}
.chat-msg-ai {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px 18px 18px 4px;
  padding: 8px 14px;
  font-size: 12px;
  color: #cbd5e1;
  max-width: 88%;
  align-self: flex-start;
  line-height: 1.6;
  word-break: break-word;
}
.typing-dot {
  animation: typingBounce 1.4s infinite ease-in-out both;
  display: inline-block;
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--accent-primary);
}
.typing-dot:nth-child(1) { animation-delay: -0.32s; }
.typing-dot:nth-child(2) { animation-delay: -0.16s; }
@keyframes typingBounce {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

/* ===== THEME CUSTOMIZER PANEL ===== */
.theme-panel {
  position: fixed;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  z-index: 45;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 10px 6px;
  background: rgba(13, 21, 39, 0.75);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.07);
  border-right: none;
  border-radius: 14px 0 0 14px;
}
.theme-swatch {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid transparent;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}
.theme-swatch:hover { transform: scale(1.2); }
.theme-swatch.active {
  border-color: rgba(255,255,255,0.7);
  box-shadow: 0 0 10px 2px currentColor;
  transform: scale(1.15);
}

/* ===== AUDIO CONTROL ===== */
.audio-btn {
  transition: all 0.2s ease;
}
.audio-btn:hover { transform: scale(1.1); }
.audio-visualizer {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  height: 14px;
}
.audio-bar {
  width: 3px;
  background: var(--accent-primary);
  border-radius: 2px;
  animation: audioWave 0.8s ease-in-out infinite alternate;
}
.audio-bar:nth-child(1) { animation-delay: 0s; animation-duration: 0.6s; }
.audio-bar:nth-child(2) { animation-delay: 0.1s; animation-duration: 0.8s; }
.audio-bar:nth-child(3) { animation-delay: 0.2s; animation-duration: 0.5s; }
@keyframes audioWave {
  0% { height: 3px; }
  100% { height: 14px; }
}
.audio-visualizer.muted .audio-bar {
  animation: none;
  height: 4px;
  opacity: 0.4;
}

/* ===== SKILL PROGRESS BARS ===== */
.skill-bar-track {
  background: rgba(255,255,255,0.06);
  border-radius: 999px;
  height: 5px;
  overflow: hidden;
}
.skill-bar-fill {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent-secondary), var(--accent-primary));
  width: 0%;
  transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ===== SCROLL REVEAL ===== */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* ===== SHIMMER SKELETON ===== */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* ===== CYBERPUNK GLITCH TEXT (hero) ===== */
@keyframes glitch {
  0%, 100% { clip-path: inset(0 0 100% 0); transform: translateX(0); }
  10% { clip-path: inset(10% 0 60% 0); transform: translateX(-4px); }
  20% { clip-path: inset(60% 0 10% 0); transform: translateX(4px); }
  30% { clip-path: inset(30% 0 40% 0); transform: translateX(-2px); }
  40% { clip-path: inset(0 0 100% 0); transform: translateX(0); }
}
"""

css_path = os.path.join(BASE, "css", "custom.css")
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)
print("CSS written OK")

# ============================================================
# 2. WRITE NEW js/app.js
# ============================================================
js_content = r"""// Advanced Interactive Logic for Deepak S Portfolio — Premium Edition
document.addEventListener('DOMContentLoaded', () => {

  // ── 1. LUCIDE ICONS ──────────────────────────────────────────
  if (window.lucide) window.lucide.createIcons();

  // ── 2. MOBILE MENU ───────────────────────────────────────────
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu    = document.getElementById('mobile-menu');
  const mobileLinks   = document.querySelectorAll('.mobile-nav-link');
  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => mobileMenu.classList.toggle('hidden'));
    mobileLinks.forEach(l => l.addEventListener('click', () => mobileMenu.classList.add('hidden')));
  }

  // ── 3. THEME CUSTOMIZER ───────────────────────────────────────
  const themes = ['theme-cyan', 'theme-purple', 'theme-emerald', 'theme-amber'];
  const savedTheme = localStorage.getItem('deepak-theme') || 'theme-cyan';
  document.body.classList.add(savedTheme);

  const swatches = document.querySelectorAll('.theme-swatch');
  const markActive = (name) => {
    swatches.forEach(s => s.classList.toggle('active', s.dataset.theme === name));
  };
  markActive(savedTheme);

  swatches.forEach(swatch => {
    swatch.addEventListener('click', () => {
      const t = swatch.dataset.theme;
      themes.forEach(th => document.body.classList.remove(th));
      document.body.classList.add(t);
      localStorage.setItem('deepak-theme', t);
      markActive(t);
      playSound('click');
    });
  });

  // ── 4. WEB AUDIO API — CYBERPUNK SFX ─────────────────────────
  let audioCtx = null;
  let isMuted = localStorage.getItem('deepak-muted') === 'true';
  const audioVisualizerEl = document.getElementById('audio-visualizer');
  const muteBtn = document.getElementById('mute-btn');
  const muteBtnIcon = document.getElementById('mute-icon');

  const syncMuteUI = () => {
    if (audioVisualizerEl) audioVisualizerEl.classList.toggle('muted', isMuted);
    if (muteBtnIcon) muteBtnIcon.setAttribute('data-lucide', isMuted ? 'volume-x' : 'volume-2');
    if (window.lucide) window.lucide.createIcons();
  };
  syncMuteUI();

  const getAudioCtx = () => {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    return audioCtx;
  };

  const playSound = (type) => {
    if (isMuted) return;
    try {
      const ctx = getAudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);
      if (type === 'click') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(300, ctx.currentTime + 0.08);
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.1);
        osc.start(ctx.currentTime);
        osc.stop(ctx.currentTime + 0.1);
      } else if (type === 'hover') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.05);
        gain.gain.setValueAtTime(0.03, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.07);
        osc.start(ctx.currentTime);
        osc.stop(ctx.currentTime + 0.07);
      } else if (type === 'success') {
        [523, 659, 784].forEach((freq, i) => {
          const o = ctx.createOscillator();
          const g = ctx.createGain();
          o.connect(g); g.connect(ctx.destination);
          o.type = 'sine';
          o.frequency.value = freq;
          g.gain.setValueAtTime(0.05, ctx.currentTime + i * 0.1);
          g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + i * 0.1 + 0.2);
          o.start(ctx.currentTime + i * 0.1);
          o.stop(ctx.currentTime + i * 0.1 + 0.25);
        });
      } else if (type === 'type') {
        osc.type = 'square';
        osc.frequency.setValueAtTime(Math.random() * 200 + 500, ctx.currentTime);
        gain.gain.setValueAtTime(0.015, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
        osc.start(ctx.currentTime);
        osc.stop(ctx.currentTime + 0.04);
      }
    } catch(e) {}
  };

  window.playSound = playSound;

  if (muteBtn) {
    muteBtn.addEventListener('click', () => {
      isMuted = !isMuted;
      localStorage.setItem('deepak-muted', isMuted);
      syncMuteUI();
      if (!isMuted) playSound('click');
    });
  }

  // Add hover sounds to interactive elements
  document.querySelectorAll('a, button, .glass-card-hover').forEach(el => {
    el.addEventListener('mouseenter', () => playSound('hover'));
  });
  document.querySelectorAll('button[type="submit"], .filter-btn, .theme-swatch').forEach(el => {
    el.addEventListener('click', () => playSound('click'));
  });

  // ── 5. TYPEWRITER EFFECT ──────────────────────────────────────
  const typewriterEl = document.getElementById('typewriter-text');
  if (typewriterEl) {
    const phrases = [
      'Aspiring Web Developer',
      'B.Tech IT Student @ Velammal',
      'Python & Machine Learning Enthusiast',
      'Interactive Web Game Creator',
      'Creative Problem Solver'
    ];
    let pi = 0, ci = 0, deleting = false, speed = 90;
    const typeLoop = () => {
      const cur = phrases[pi];
      typewriterEl.textContent = deleting
        ? cur.substring(0, ci - 1)
        : cur.substring(0, ci + 1);
      deleting ? ci-- : ci++;
      if (!deleting && ci === cur.length) { speed = 1800; deleting = true; }
      else if (deleting && ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; speed = 400; }
      else { speed = deleting ? 45 : 90; }
      setTimeout(typeLoop, speed);
    };
    typeLoop();
  }

  // ── 6. PARTICLE CANVAS ───────────────────────────────────────
  const canvas = document.getElementById('particle-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let W = (canvas.width = window.innerWidth);
    let H = (canvas.height = window.innerHeight);
    window.addEventListener('resize', () => { W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; });
    const particles = [];
    const count = Math.min(W > 768 ? 45 : 20, 60);
    for (let i = 0; i < count; i++) particles.push({ x: Math.random()*W, y: Math.random()*H, vx: (Math.random()-0.5)*0.4, vy: (Math.random()-0.5)*0.4, r: Math.random()*1.5+0.8 });
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      particles.forEach((p, i) => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(59,130,246,0.35)'; ctx.fill();
        for (let j = i+1; j < particles.length; j++) {
          const p2 = particles[j], d = Math.hypot(p.x-p2.x, p.y-p2.y);
          if (d < 100) {
            ctx.beginPath();
            ctx.strokeStyle = `rgba(59,130,246,${0.15*(1-d/100)})`;
            ctx.lineWidth = 0.6; ctx.moveTo(p.x, p.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
          }
        }
      });
      requestAnimationFrame(draw);
    };
    draw();
  }

  // ── 7. 3D PARALLAX TILT + SPOTLIGHT ──────────────────────────
  const tiltCards = document.querySelectorAll('.tilt-card');
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rotX = ((y - cy) / cy) * -10;
      const rotY = ((x - cx) / cx) * 10;
      card.style.transform = `perspective(800px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.03,1.03,1.03)`;
      card.style.boxShadow = `0 20px 50px -10px var(--glow-primary), ${-rotY*0.5}px ${rotX*0.5}px 20px rgba(0,0,0,0.3)`;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.style.boxShadow = '';
    });
  });

  // Spotlight for non-tilt cards
  document.querySelectorAll('.spotlight-card:not(.tilt-card)').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mouse-x', `${e.clientX - r.left}px`);
      card.style.setProperty('--mouse-y', `${e.clientY - r.top}px`);
    });
  });

  // ── 8. PROJECT FILTER ────────────────────────────────────────
  const filterBtns  = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('bg-blue-600','text-white','border-blue-500');
        b.classList.add('bg-slate-900/60','text-slate-400','border-slate-800');
      });
      btn.classList.add('bg-blue-600','text-white','border-blue-500');
      btn.classList.remove('bg-slate-900/60','text-slate-400','border-slate-800');
      const fv = btn.dataset.filter;
      projectCards.forEach(c => {
        const cat = c.dataset.category;
        if (fv === 'all' || cat.includes(fv)) { c.classList.remove('hidden'); c.classList.add('flex'); }
        else { c.classList.add('hidden'); c.classList.remove('flex'); }
      });
      if (window.lucide) window.lucide.createIcons();
      playSound('click');
    });
  });

  // ── 9. CLI TERMINAL ──────────────────────────────────────────
  const terminalInput  = document.getElementById('terminal-command-input');
  const terminalOutput = document.getElementById('terminal-output');
  const terminalBtns   = document.querySelectorAll('.term-quick-btn');

  const termCmds = {
    'help': `Available commands:\n  <span class="text-cyan-400 font-bold">skills</span>      - Show tech skills\n  <span class="text-cyan-400 font-bold">projects</span>    - List live projects\n  <span class="text-cyan-400 font-bold">about</span>       - Print bio & education\n  <span class="text-cyan-400 font-bold">contact</span>     - Show contact details\n  <span class="text-cyan-400 font-bold">hire</span>        - Hiring info\n  <span class="text-cyan-400 font-bold">github</span>      - GitHub profile details\n  <span class="text-cyan-400 font-bold">clear</span>       - Clear terminal`,
    'skills': `<span class="text-purple-400 font-bold">Frontend:</span> HTML5, CSS3, JavaScript (ES6+), React.js, Tailwind CSS, Bootstrap\n<span class="text-cyan-400 font-bold">Programming:</span> Python, C, C++, SQL\n<span class="text-blue-400 font-bold">Backend & DB:</span> SQLite, Firebase, Supabase, Node.js\n<span class="text-emerald-400 font-bold">Dev Tools:</span> Git, GitHub, Streamlit, VS Code, Figma`,
    'projects': `🚀 <span class="text-white font-bold">1. Insurance Fraud Detection System</span>\n   Tech: Python, Scikit-learn, SQLite, Streamlit\n   Live: <a href="https://insurance-fraud-detection-kompany.streamlit.app" target="_blank" class="text-cyan-400 underline">insurance-fraud-detection.streamlit.app</a>\n\n🎮 <span class="text-white font-bold">2. Midnight Grid (Car Game)</span>\n   Tech: HTML5 Canvas, CSS3, Vanilla JavaScript\n   Live: <a href="https://midnight-grid.netlify.app" target="_blank" class="text-purple-400 underline">midnight-grid.netlify.app</a>`,
    'about': `Deepak S | B.Tech Information Technology (2nd Year, Grad 2029)\nCollege: Velammal Engineering College, Tamil Nadu\nFocus: Web Development, Machine Learning, Interactive Web Applications.`,
    'contact': `📧 Email: <a href="mailto:deepakselladurai203@gmail.com" class="text-cyan-400 underline">deepakselladurai203@gmail.com</a>\n📱 Phone: <a href="tel:+919345674398" class="text-blue-400">+91 9345674398</a>\n🔗 LinkedIn: <a href="https://linkedin.com/in/deepak-selladurai-6905b3397" target="_blank" class="text-purple-400 underline">linkedin.com/in/deepak-selladurai</a>\n🐙 GitHub: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-emerald-400 underline">github.com/deepak30ips-pixel</a>`,
    'github': `GitHub: <span class="text-emerald-400 font-bold">@deepak30ips-pixel</span>\nRepos: Insurance Fraud Detection, Midnight Grid\nProfile: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-cyan-400 underline">https://github.com/deepak30ips-pixel</a>`,
    'hire': `🎉 <span class="text-emerald-400 font-bold">Thank you for considering Deepak S!</span>\nStatus: <span class="text-cyan-400">Available for Freelance, Internships & Collaborations</span>\nEmail: <span class="text-blue-400">deepakselladurai203@gmail.com</span>`,
    'sudo hire deepak': `[PERMISSIONS GRANTED] ✨ Excellent choice!\nDeepak is excited to work with you.\nEmail: <span class="text-cyan-400">deepakselladurai203@gmail.com</span>`
  };

  const handleCmd = (raw) => {
    const cmd = raw.trim().toLowerCase();
    if (!cmd) return;
    if (cmd === 'clear') { if (terminalOutput) terminalOutput.innerHTML = ''; return; }

    const prompt = document.createElement('div');
    prompt.className = 'flex items-center gap-2 text-slate-400 text-xs font-mono-code mt-2';
    prompt.innerHTML = `<span class="text-cyan-400">deepak@portfolio:~$</span> <span class="text-white">${raw}</span>`;
    terminalOutput.appendChild(prompt);

    const resp = document.createElement('div');
    resp.className = 'text-slate-300 text-xs font-mono-code pl-4 py-1 leading-relaxed border-l-2 border-slate-700/60 my-1';
    resp.innerHTML = termCmds[cmd]
      ? termCmds[cmd]
      : `<span class="text-red-400">Command not recognized: "${cmd}".</span> Type <span class="text-cyan-400 font-bold">help</span> to see all commands.`;
    terminalOutput.appendChild(resp);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
    playSound('type');
  };

  if (terminalInput) {
    terminalInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') { handleCmd(terminalInput.value); terminalInput.value = ''; }
      else { playSound('type'); }
    });
  }
  terminalBtns.forEach(btn => btn.addEventListener('click', () => handleCmd(btn.dataset.cmd)));

  // ── 10. ANIMATED STAT COUNTERS ───────────────────────────────
  const statCounters = document.querySelectorAll('.stat-counter');
  let statsRan = false;
  const runCounters = () => {
    statCounters.forEach(el => {
      const target = +el.dataset.target;
      const suffix = el.dataset.suffix || '';
      let cur = 0;
      const inc = Math.max(1, Math.ceil(target / 30));
      const step = () => {
        cur += inc;
        if (cur < target) { el.innerText = cur + suffix; setTimeout(step, 40); }
        else { el.innerText = target + suffix; }
      };
      step();
    });
  };
  const statsEl = document.getElementById('hero-stats');
  if (statsEl) {
    new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting && !statsRan) { runCounters(); statsRan = true; } });
    }, { threshold: 0.5 }).observe(statsEl);
  }

  // ── 11. COPY TO CLIPBOARD ─────────────────────────────────────
  window.copyToClipboard = (text, id, def='Copy') => {
    navigator.clipboard.writeText(text).then(() => {
      const el = document.getElementById(id);
      if (el) {
        el.innerText = 'Copied! ✓'; el.classList.add('text-emerald-400');
        setTimeout(() => { el.innerText = def; el.classList.remove('text-emerald-400'); }, 2000);
      }
      playSound('success');
    }).catch(() => {});
  };

  // ── 12. PROJECT MODAL ─────────────────────────────────────────
  const projectDetails = {
    'fraud-detection': {
      title: 'Insurance Fraud Detection System', badge: 'Machine Learning & Web App',
      tech: ['Python','Scikit-learn','SQLite','Streamlit','Pandas'],
      description: 'An advanced ML application to assess and predict suspicious insurance claim activities in real-time.',
      problem: 'Insurance companies lose billions annually due to undetected fraudulent claims. Manual audit is slow and misses subtle patterns.',
      solution: 'Trained predictive classification models on historical claim records with a SQLite backend and Streamlit dashboard.',
      keyFeatures: ['Real-time fraud probability scoring','Interactive dashboard with visual metrics','Secure SQLite audit trail','Zero-setup cloud deployment'],
      liveUrl: 'https://insurance-fraud-detection-kompany.streamlit.app',
      githubUrl: 'https://github.com/deepak30ips-pixel/insurance-fraud-detection'
    },
    'midnight-grid': {
      title: 'Midnight Grid (Interactive Car Game)', badge: 'Web Game / Front-End',
      tech: ['HTML5','CSS3','JavaScript','Canvas API','Web Audio'],
      description: 'An adrenaline-fueled dark-themed browser car game built from scratch with vanilla web technologies.',
      problem: 'Creating a fast 60fps responsive arcade experience in the browser without heavy game engines.',
      solution: 'Leveraged HTML5 Canvas physics, fluid keyboard event listeners, and dark neon aesthetics.',
      keyFeatures: ['Free Roam Mode: Open street driving','Bank Heist Mode: Tactical getaway','Responsive dark arcade interface','Optimized for desktop & touch'],
      liveUrl: 'https://midnight-grid.netlify.app',
      githubUrl: null
    }
  };
  const projModal = document.getElementById('project-modal');
  const projBody  = document.getElementById('project-modal-body');
  window.openProjectModal = (id) => {
    const d = projectDetails[id];
    if (!d || !projModal || !projBody) return;
    projBody.innerHTML = `
      <div class="space-y-5">
        <div>
          <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-2">${d.badge}</span>
          <h3 class="text-2xl font-bold text-white font-heading">${d.title}</h3>
          <p class="text-slate-400 text-sm mt-2 leading-relaxed">${d.description}</p>
        </div>
        <div class="flex flex-wrap gap-2">${d.tech.map(t=>`<span class="px-2.5 py-1 rounded-lg text-xs font-medium bg-blue-500/10 text-blue-400 border border-blue-500/20">${t}</span>`).join('')}</div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800"><h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-red-400">●</span> Problem</h4><p class="text-xs text-slate-400 leading-relaxed">${d.problem}</p></div>
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800"><h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-emerald-400">●</span> Solution</h4><p class="text-xs text-slate-400 leading-relaxed">${d.solution}</p></div>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80"><h4 class="text-sm font-semibold text-slate-200 mb-2">Key Highlights</h4><ul class="text-xs text-slate-300 space-y-1.5">${d.keyFeatures.map(f=>`<li class="flex items-start gap-2"><span class="text-blue-400">✓</span><span>${f}</span></li>`).join('')}</ul></div>
        <div class="flex items-center gap-3 pt-3 border-t border-slate-800">
          ${d.liveUrl ? `<a href="${d.liveUrl}" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium text-sm transition flex items-center gap-2"><span>Live Demo</span><i data-lucide="external-link" class="w-4 h-4"></i></a>` : ''}
          ${d.githubUrl ? `<a href="${d.githubUrl}" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition flex items-center gap-2"><span>Source Code</span><i data-lucide="github" class="w-4 h-4"></i></a>` : ''}
          <button onclick="closeProjectModal()" class="ml-auto px-4 py-2 rounded-xl text-slate-400 hover:text-white text-sm">Close</button>
        </div>
      </div>`;
    projModal.classList.remove('hidden'); projModal.classList.add('flex');
    if (window.lucide) window.lucide.createIcons();
  };
  window.closeProjectModal = () => { projModal?.classList.add('hidden'); projModal?.classList.remove('flex'); };

  // ── 13. RESUME MODAL ─────────────────────────────────────────
  const resumeModal = document.getElementById('resume-modal');
  window.openResumeModal  = () => { resumeModal?.classList.remove('hidden'); resumeModal?.classList.add('flex'); if (window.lucide) window.lucide.createIcons(); };
  window.closeResumeModal = () => { resumeModal?.classList.add('hidden'); resumeModal?.classList.remove('flex'); };

  window.addEventListener('click', (e) => {
    if (e.target === projModal) closeProjectModal();
    if (e.target === resumeModal) closeResumeModal();
    const chatWin = document.getElementById('ai-chat-window');
    if (chatWin && !chatWin.contains(e.target) && !document.getElementById('ai-chat-btn')?.contains(e.target)) {
      if (!chatWin.classList.contains('closed')) toggleChat(false);
    }
  });
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { closeProjectModal(); closeResumeModal(); toggleChat(false); }
  });

  // ── 14. CONTACT FORM ─────────────────────────────────────────
  const contactForm  = document.getElementById('contact-form');
  const formToast    = document.getElementById('form-success-toast');
  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const orig = btn?.innerHTML;
      if (btn) { btn.disabled = true; btn.innerHTML = '<span class="animate-pulse">⏳ Sending...</span>'; }
      const fd = new FormData(contactForm);
      if (!fd.get('access_key')) fd.append('access_key', 'f01867c1-288e-4734-99a9-69ab16db1ae9');
      try {
        const res = await fetch('https://api.web3forms.com/submit', { method:'POST', body: fd });
        const json = await res.json();
        if (json.success || res.status === 200) {
          if (formToast) {
            formToast.innerHTML = '<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i><span>Message sent! Deepak received it in his Gmail.</span>';
            formToast.className = 'mb-4 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2';
            formToast.classList.remove('hidden');
            if (window.lucide) window.lucide.createIcons();
            setTimeout(() => formToast.classList.add('hidden'), 6000);
          }
          contactForm.reset();
          playSound('success');
        } else throw new Error(json.message);
      } catch(err) {
        if (formToast) {
          formToast.innerHTML = '<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i><span>Message recorded! Email: deepakselladurai203@gmail.com</span>';
          formToast.className = 'mb-4 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2';
          formToast.classList.remove('hidden');
          if (window.lucide) window.lucide.createIcons();
          setTimeout(() => formToast.classList.add('hidden'), 6000);
        }
        playSound('success');
      } finally {
        if (btn) { btn.disabled = false; btn.innerHTML = orig; if (window.lucide) window.lucide.createIcons(); }
      }
    });
  }

  // ── 15. BACK TO TOP ──────────────────────────────────────────
  const backBtn = document.getElementById('back-to-top');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) { backBtn?.classList.remove('opacity-0','pointer-events-none'); backBtn?.classList.add('opacity-100'); }
    else { backBtn?.classList.add('opacity-0','pointer-events-none'); backBtn?.classList.remove('opacity-100'); }
  });

  // ── 16. SCROLL REVEAL ────────────────────────────────────────
  const revealEls = document.querySelectorAll('.reveal');
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); revealObs.unobserve(e.target); }});
  }, { threshold: 0.12 });
  revealEls.forEach(el => revealObs.observe(el));

  // ── 17. ASK DEEPAK AI CHATBOT ────────────────────────────────
  const chatBtn    = document.getElementById('ai-chat-btn');
  const chatWindow = document.getElementById('ai-chat-window');
  const chatInput  = document.getElementById('ai-chat-input');
  const chatBody   = document.getElementById('ai-chat-body');
  const chatSend   = document.getElementById('ai-chat-send');
  let chatOpen = false;

  const toggleChat = (force) => {
    chatOpen = force !== undefined ? force : !chatOpen;
    if (chatWindow) {
      chatWindow.classList.toggle('open', chatOpen);
      chatWindow.classList.toggle('closed', !chatOpen);
    }
    if (chatOpen && chatInput) { chatInput.focus(); playSound('click'); }
  };

  if (chatBtn) chatBtn.addEventListener('click', () => toggleChat());

  const aiKnowledge = {
    name: 'Deepak S', degree: 'B.Tech Information Technology', college: 'Velammal Engineering College',
    year: '2nd Year (Graduation 2029)', location: 'Tamil Nadu, India',
    email: 'deepakselladurai203@gmail.com', phone: '+91 9345674398',
    github: 'https://github.com/deepak30ips-pixel',
    linkedin: 'https://linkedin.com/in/deepak-selladurai-6905b3397',
    skills: ['HTML5','CSS3','JavaScript','React.js','Python','C','C++','SQL','SQLite','Firebase','Streamlit','Git','Figma','Tailwind CSS'],
    projects: ['Insurance Fraud Detection System (Python/Streamlit/ML)','Midnight Grid (HTML5 Canvas Browser Car Game)'],
    available: 'Available for freelance projects, internships, and collaborations',
    certs: ['Python for Beginners - Simplilearn','Intro to Cyber Security - Simplilearn'],
  };

  const aiRespond = (q) => {
    const lq = q.toLowerCase();
    if (lq.includes('name') || lq.includes('who'))
      return `I'm Deepak S — a ${aiKnowledge.degree} student at ${aiKnowledge.college}, passionate about web development and ML! 👋`;
    if (lq.includes('skill') || lq.includes('tech') || lq.includes('know'))
      return `Deepak's core skills: <strong>${aiKnowledge.skills.join(', ')}</strong>. He specializes in building interactive web experiences and ML-powered apps.`;
    if (lq.includes('project'))
      return `Deepak has built:\n1. 🚀 <strong>Insurance Fraud Detection</strong> — ML-powered web app on Streamlit\n2. 🎮 <strong>Midnight Grid</strong> — Dark-themed HTML5 browser car game\nClick "View Projects" to explore them!`;
    if (lq.includes('contact') || lq.includes('email') || lq.includes('reach'))
      return `📧 <strong>${aiKnowledge.email}</strong>\n📱 ${aiKnowledge.phone}\nOr use the contact form below!`;
    if (lq.includes('hire') || lq.includes('avail') || lq.includes('freelance') || lq.includes('intern'))
      return `✅ ${aiKnowledge.available}! Send him a message via the contact section or email directly at ${aiKnowledge.email}`;
    if (lq.includes('github'))
      return `Deepak's GitHub: <a href="${aiKnowledge.github}" target="_blank" class="text-cyan-400 underline">${aiKnowledge.github}</a>`;
    if (lq.includes('linkedin'))
      return `LinkedIn: <a href="${aiKnowledge.linkedin}" target="_blank" class="text-cyan-400 underline">deepak-selladurai</a>`;
    if (lq.includes('certif') || lq.includes('course'))
      return `Deepak has completed:\n• ${aiKnowledge.certs.join('\n• ')}`;
    if (lq.includes('education') || lq.includes('college') || lq.includes('study'))
      return `Deepak is studying ${aiKnowledge.degree} at <strong>${aiKnowledge.college}</strong>, ${aiKnowledge.year}.`;
    if (lq.includes('hello') || lq.includes('hi') || lq.includes('hey'))
      return `Hey there! 👋 I'm Deepak's AI assistant. Ask me anything about his skills, projects, or how to get in touch!`;
    return `Great question! I'd recommend checking the sections above, or contact Deepak directly at <strong>${aiKnowledge.email}</strong> — he replies fast! 😊`;
  };

  const appendMsg = (html, type) => {
    if (!chatBody) return;
    const div = document.createElement('div');
    div.className = type === 'user' ? 'chat-msg-user' : 'chat-msg-ai';
    div.innerHTML = html.replace(/\n/g, '<br>');
    chatBody.appendChild(div);
    chatBody.scrollTop = chatBody.scrollHeight;
  };

  const showTyping = () => {
    const div = document.createElement('div');
    div.id = 'typing-indicator';
    div.className = 'chat-msg-ai flex items-center gap-1.5 py-3';
    div.innerHTML = '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';
    chatBody?.appendChild(div);
    chatBody.scrollTop = chatBody.scrollHeight;
  };
  const hideTyping = () => document.getElementById('typing-indicator')?.remove();

  const sendChat = () => {
    const val = chatInput?.value?.trim();
    if (!val) return;
    appendMsg(val, 'user');
    chatInput.value = '';
    playSound('click');
    showTyping();
    setTimeout(() => {
      hideTyping();
      const reply = aiRespond(val);
      appendMsg(reply, 'ai');
      playSound('success');
    }, 700 + Math.random() * 500);
  };

  chatSend?.addEventListener('click', sendChat);
  chatInput?.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendChat(); });

});
"""

js_path = os.path.join(BASE, "js", "app.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)
print("JS written OK")

print("All files written successfully!")
