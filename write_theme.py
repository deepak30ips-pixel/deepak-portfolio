
# Write Red-Black-Silver Grunge Theme
import os

css = r"""/* Custom Styles & Keyframe Animations for Deepak S Portfolio — Red Grunge Edition */
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap');

:root {
  --accent-primary: #dc2626;
  --accent-secondary: #ef4444;
  --accent-tertiary: #b91c1c;
  --accent-silver: #9ca3af;
  --accent-silver-light: #d1d5db;
  --glow-primary: rgba(220, 38, 38, 0.22);
  --glow-secondary: rgba(185, 28, 28, 0.18);
  --spotlight-glow: rgba(220, 38, 38, 0.18);
  --bg-deep: #080808;
  --bg-card: #0f0f0f;
  --bg-surface: #151515;
  --slash-angle: 145deg;
  --theme-transition: background 0.5s ease, color 0.4s ease, border-color 0.4s ease;
}

/* Override all themes to use the red-grunge color system */
body.theme-cyan,
body.theme-purple,
body.theme-emerald,
body.theme-amber {
  --accent-primary: #dc2626;
  --accent-secondary: #ef4444;
  --accent-tertiary: #b91c1c;
  --glow-primary: rgba(220, 38, 38, 0.22);
  --glow-secondary: rgba(185, 28, 28, 0.18);
  --spotlight-glow: rgba(220, 38, 38, 0.18);
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-deep);
  color: #e5e7eb;
  overflow-x: hidden;
  transition: color 0.4s ease;
  position: relative;
}

/* === DIAGONAL SLASH BACKGROUND === */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background:
    linear-gradient(var(--slash-angle), transparent 0%, transparent 38%,
      rgba(185, 28, 28, 0.07) 38%, rgba(185, 28, 28, 0.07) 42%,
      transparent 42%, transparent 58%,
      rgba(30, 30, 30, 0.55) 58%, rgba(30, 30, 30, 0.55) 63%,
      transparent 63%, transparent 75%,
      rgba(180, 180, 180, 0.04) 75%, rgba(180, 180, 180, 0.04) 80%,
      transparent 80%),
    radial-gradient(ellipse at 15% 50%, rgba(180, 0, 0, 0.12) 0%, transparent 55%),
    radial-gradient(ellipse at 85% 70%, rgba(100, 100, 100, 0.06) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

h1, h2, h3, h4, .font-heading {
  font-family: 'Space Grotesk', sans-serif;
}

.font-mono-code {
  font-family: 'Fira Code', monospace;
}

/* ===== CUSTOM SCROLLBAR ===== */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0a0a; }
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #7f1d1d, #dc2626);
  border-radius: 9999px;
}
::-webkit-scrollbar-thumb:hover { background: #ef4444; }

/* ===== GLASSMORPHISM ===== */
.glass-panel {
  background: rgba(12, 12, 12, 0.72);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.04), 0 4px 20px rgba(0,0,0,0.5);
}

.glass-panel-subtle {
  background: rgba(255, 255, 255, 0.025);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.05);
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
  width: 380px;
  height: 380px;
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
  transform: translateY(-5px);
  border-color: rgba(220, 38, 38, 0.4);
  box-shadow: 0 16px 40px -10px rgba(185, 28, 28, 0.35), 0 0 0 1px rgba(220,38,38,0.1);
}

/* ===== AMBIENT GLOW ORBS — RED ===== */
.glow-orb-1 {
  position: absolute;
  width: 700px;
  height: 700px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(180, 0, 0, 0.14) 0%, transparent 70%);
  filter: blur(70px);
  pointer-events: none;
  z-index: 0;
  animation: pulseGlow 9s infinite alternate ease-in-out;
}
.glow-orb-2 {
  position: absolute;
  width: 550px;
  height: 550px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(120, 120, 120, 0.08) 0%, transparent 70%);
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
  animation: pulseGlow 12s infinite alternate-reverse ease-in-out;
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
  0% { opacity: 0.5; transform: scale(0.94); }
  100% { opacity: 1; transform: scale(1.1); }
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

/* ===== BACKGROUND GRID (subtle) ===== */
.bg-grid-pattern {
  background-size: 50px 50px;
  background-image:
    linear-gradient(to right, rgba(255, 255, 255, 0.018) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.018) 1px, transparent 1px);
}

/* ===== TERMINAL ===== */
.terminal-window {
  background: rgba(8, 8, 8, 0.92);
  border: 1px solid rgba(220, 38, 38, 0.25);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(220,38,38,0.08);
}
.terminal-input {
  background: transparent;
  outline: none;
  border: none;
  color: #ef4444;
  width: 100%;
}

/* ===== AI CHAT DRAWER ===== */
.ai-chat-window {
  box-shadow: 0 25px 70px -15px rgba(0, 0, 0, 0.9), 0 0 30px rgba(185,28,28,0.15);
  border: 1px solid rgba(220, 38, 38, 0.15);
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
  background: linear-gradient(135deg, #7f1d1d, #dc2626);
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
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 18px 18px 18px 4px;
  padding: 8px 14px;
  font-size: 12px;
  color: #d1d5db;
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
  background: #dc2626;
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
  background: rgba(10, 10, 10, 0.82);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(220, 38, 38, 0.18);
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
  background: #dc2626;
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
  background: rgba(255,255,255,0.05);
  border-radius: 999px;
  height: 5px;
  overflow: hidden;
}
.skill-bar-fill {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #7f1d1d, #dc2626, #f87171);
  width: 0%;
  transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ===== SCROLL REVEAL ===== */
.reveal {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 0.75s ease, transform 0.75s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* ===== CYBERPUNK GLITCH TEXT (hero) ===== */
@keyframes glitch {
  0%, 100% { clip-path: inset(0 0 100% 0); transform: translateX(0); }
  10% { clip-path: inset(10% 0 60% 0); transform: translateX(-4px); }
  20% { clip-path: inset(60% 0 10% 0); transform: translateX(4px); }
  30% { clip-path: inset(30% 0 40% 0); transform: translateX(-2px); }
  40% { clip-path: inset(0 0 100% 0); transform: translateX(0); }
}

/* ===== RED GRUNGE TEXTURE OVERLAYS ===== */
/* Diagonal slash accents on section cards */
.glass-panel::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    var(--slash-angle),
    transparent 0%, transparent 88%,
    rgba(220, 38, 38, 0.04) 88%, rgba(220, 38, 38, 0.04) 91%,
    transparent 91%
  );
  pointer-events: none;
  border-radius: inherit;
  z-index: 0;
}

/* ===== NAVBAR RED ACCENT STRIP ===== */
nav::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(220,38,38,0.5), transparent);
}
nav { position: relative; }

/* ===== GRUNGE NOISE OVERLAY ===== */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 180px 180px;
  opacity: 1;
  pointer-events: none;
  z-index: 0;
}

/* ===== SECTION HEADING ACCENT ===== */
.section-label {
  display: inline-block;
  position: relative;
  padding-left: 14px;
}
.section-label::before {
  content: '';
  position: absolute;
  left: 0; top: 50%;
  transform: translateY(-50%);
  width: 4px; height: 100%;
  background: #dc2626;
  border-radius: 2px;
}

/* ===== SHIMMER SKELETON ===== */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* ===== HERO PROFILE FRAME ===== */
.hero-profile-frame {
  background: linear-gradient(145deg, #7f1d1d, #dc2626, #374151, #6b7280);
  box-shadow: 0 24px 60px rgba(180, 0, 0, 0.4), 0 0 0 1px rgba(220,38,38,0.2);
}

/* ===== BUTTON GRADIENTS ===== */
.btn-primary {
  background: linear-gradient(135deg, #7f1d1d 0%, #dc2626 50%, #b91c1c 100%);
  box-shadow: 0 4px 20px rgba(185, 28, 28, 0.35);
}
.btn-primary:hover {
  background: linear-gradient(135deg, #dc2626 0%, #ef4444 50%, #dc2626 100%);
  box-shadow: 0 6px 28px rgba(220, 38, 38, 0.5);
}

/* ===== TAG / BADGE STYLE ===== */
.tag-red {
  background: rgba(127, 29, 29, 0.15);
  color: #fca5a5;
  border: 1px solid rgba(220, 38, 38, 0.25);
}

/* ===== SECTION DIVIDER ===== */
.slash-divider {
  height: 2px;
  background: linear-gradient(90deg,
    transparent 0%, #7f1d1d 20%, #dc2626 50%, #6b7280 80%, transparent 100%);
  margin: 4px 0;
  border-radius: 2px;
}
"""

html_patch = """
  <!-- Red-Black Grunge custom color overrides for Tailwind inline classes -->
  <style>
    /* Hero typewriter gradient — red to silver */
    #typewriter-text {
      background: linear-gradient(90deg, #ef4444, #dc2626, #9ca3af) !important;
      -webkit-background-clip: text !important;
      -webkit-text-fill-color: transparent !important;
      background-clip: text !important;
    }
    /* Glow dot in logo → red */
    .logo-dot { background: #dc2626 !important; box-shadow: 0 0 10px #dc2626 !important; }
    /* Active filter button → red */
    .filter-btn[data-active="true"], .filter-btn.active-filter {
      background: #b91c1c !important;
      border-color: #dc2626 !important;
    }
    /* Nav hover → red */
    nav a:hover { color: #f87171 !important; }
    /* Let's talk button → red gradient */
    .lets-talk-btn {
      background: linear-gradient(135deg, #7f1d1d, #dc2626) !important;
      box-shadow: 0 4px 18px rgba(185,28,28,0.4) !important;
    }
    /* Skill tags border → red on hover */
    [class*="hover:border-blue-400"]:hover,
    [class*="hover:border-cyan-400"]:hover,
    [class*="hover:border-purple-400"]:hover,
    [class*="hover:border-emerald-400"]:hover,
    [class*="hover:border-pink-400"]:hover {
      border-color: rgba(220,38,38,0.55) !important;
    }
    /* Cyan text → red override */
    .text-cyan-400 { color: #ef4444 !important; }
    .text-cyan-300 { color: #fca5a5 !important; }
    .border-cyan-400, .border-cyan-500 { border-color: rgba(220,38,38,0.4) !important; }
    .bg-cyan-400 { background-color: #dc2626 !important; }
    .bg-cyan-500\\/10, .bg-\\[\\#06b6d4\\] { background-color: rgba(127,29,29,0.15) !important; }
    .text-blue-400 { color: #9ca3af !important; }
    .text-purple-400 { color: #d1d5db !important; }
    .text-emerald-400 { color: #6b7280 !important; }
    /* Profile card frame: red → silver */
    #user-profile-img ~ div.absolute { background: rgba(0,0,0,0.75) !important; }
    /* Stat counter accent */
    .stat-counter.text-cyan-400 { color: #ef4444 !important; }
    /* Section label text */
    [class*="text-cyan-400"][class*="tracking-widest"] { color: #f87171 !important; }
    /* Check circle icons */
    [data-lucide="check-circle"] { color: #dc2626 !important; }
    /* Pulse dot — available badge */
    .bg-emerald-400.animate-pulse { background-color: #dc2626 !important; }
    /* Stars rating — keep amber */
    .text-amber-400 { color: #fbbf24 !important; }
    /* Body bg override */
    .bg-\\[\\#060911\\] { background-color: #080808 !important; }
    /* Selection */
    ::selection { background: rgba(220,38,38,0.4); color: #fff; }
    /* Terminal prompt color */
    .text-cyan-400.font-bold { color: #f87171 !important; }
    /* Floating badges border accent */
    .border-blue-400\\/30 { border-color: rgba(220,38,38,0.3) !important; }
    .border-purple-400\\/30 { border-color: rgba(180,180,180,0.2) !important; }
    .border-cyan-400\\/30 { border-color: rgba(220,38,38,0.3) !important; }
    .border-emerald-400\\/30 { border-color: rgba(150,150,150,0.2) !important; }
    /* About quote block */
    .bg-blue-500\\/5 { background: rgba(127,29,29,0.08) !important; }
    .border-blue-500\\/10 { border-color: rgba(220,38,38,0.12) !important; }
    /* Project card ML badge */
    .bg-blue-500\\/10.text-blue-400 { background: rgba(127,29,29,0.15) !important; color: #fca5a5 !important; }
    .border-blue-500\\/20 { border-color: rgba(220,38,38,0.2) !important; }
    /* Game badge */
    .bg-purple-500\\/10.text-purple-400 { background: rgba(75,75,75,0.15) !important; color: #d1d5db !important; }
    /* Live demo btn → red */
    a[class*="from-blue-600"][class*="to-cyan-600"],
    a[class*="from-purple-600"][class*="to-indigo-600"] {
      background: linear-gradient(135deg, #7f1d1d, #dc2626) !important;
    }
    a[class*="from-blue-600"][class*="to-cyan-600"]:hover,
    a[class*="from-purple-600"][class*="to-indigo-600"]:hover {
      background: linear-gradient(135deg, #b91c1c, #ef4444) !important;
    }
    /* Contact send btn */
    button[type="submit"], #contact-send-btn {
      background: linear-gradient(135deg, #7f1d1d, #dc2626) !important;
      box-shadow: 0 4px 20px rgba(185,28,28,0.4) !important;
    }
    /* Input focus borders */
    input:focus, textarea:focus, select:focus {
      border-color: rgba(220,38,38,0.5) !important;
      box-shadow: 0 0 0 2px rgba(220,38,38,0.12) !important;
    }
    /* Hero bg gradient orbs */
    .absolute.-top-24.-left-24 { background: rgba(180,0,0,0.1) !important; }
    .absolute.-bottom-24.-right-24 { background: rgba(80,80,80,0.1) !important; }
    /* Profile card gradient border */
    .bg-gradient-to-tr.from-cyan-500 {
      background: linear-gradient(145deg, #7f1d1d, #dc2626, #4b5563, #6b7280) !important;
      box-shadow: 0 24px 60px rgba(180,0,0,0.35) !important;
    }
    /* Hero right col inner glow */
    .bg-gradient-to-tr.from-cyan-500\\/20 {
      background: radial-gradient(ellipse, rgba(180,0,0,0.18) 0%, transparent 70%) !important;
    }
    /* AI chat button red */
    #ai-chat-btn, button[onclick*="toggleChat"] {
      background: linear-gradient(135deg, #7f1d1d, #dc2626) !important;
      box-shadow: 0 8px 24px rgba(185,28,28,0.45) !important;
    }
    /* Skill icon bg colors */
    .bg-blue-500\\/10 { background: rgba(127,29,29,0.1) !important; }
    .bg-cyan-500\\/10 { background: rgba(100,100,100,0.1) !important; }
    .bg-purple-500\\/10 { background: rgba(90,90,90,0.1) !important; }
    .bg-emerald-500\\/10 { background: rgba(80,80,80,0.1) !important; }
    .bg-pink-500\\/10 { background: rgba(127,29,29,0.1) !important; }
    /* Border accent on icon boxes */
    .border-blue-500\\/20 { border-color: rgba(220,38,38,0.2) !important; }
    .border-cyan-500\\/20 { border-color: rgba(150,150,150,0.15) !important; }
    .border-purple-500\\/20 { border-color: rgba(130,130,130,0.15) !important; }
    .border-emerald-500\\/20 { border-color: rgba(110,110,110,0.15) !important; }
    .border-pink-500\\/20 { border-color: rgba(220,38,38,0.18) !important; }
    /* Hero name badge */
    .glass-panel .text-cyan-300 { color: #fca5a5 !important; }
    /* pwa theme-color override via meta */
  </style>
"""

css_path = r"C:\Users\PC\.gemini\antigravity\scratch\deepak-portfolio\css\custom.css"
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("✅ custom.css written")

# Patch index.html to inject the style block before </head>
html_path = r"C:\Users\PC\.gemini\antigravity\scratch\deepak-portfolio\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove existing injected style block if present
import re
content = re.sub(r'\s*<!-- Red-Black Grunge.*?</style>', '', content, flags=re.DOTALL)

# Inject before </head>
content = content.replace('</head>', html_patch + '\n</head>', 1)

# Update theme-color meta
content = content.replace('content="#060911"', 'content="#080808"')

# Change body bg class
content = content.replace('bg-[#060911]', 'bg-[#080808]')

# Change logo dot
content = content.replace(
    'w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_10px_#06b6d4]',
    'w-2.5 h-2.5 rounded-full bg-red-600 shadow-[0_0_10px_#dc2626] logo-dot'
)
# Change DEEPAK.DEV color
content = content.replace(
    '<span class="text-cyan-400">.DEV</span>',
    '<span class="text-red-500">.DEV</span>'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ index.html patched")
print("Done!")
