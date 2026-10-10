// Advanced Interactive Logic for Deepak S Portfolio — Premium Edition
document.addEventListener('DOMContentLoaded', () => {

  // ── 0. CINEMATIC PRELOADER ────────────────────────────────────────
  (() => {
    const preloader   = document.getElementById('preloader');
    const bar         = document.getElementById('preloader-bar');
    const pct         = document.getElementById('preloader-pct');
    const statusLines = [
      document.getElementById('pst-1'),
      document.getElementById('pst-2'),
      document.getElementById('pst-3'),
      document.getElementById('pst-4'),
    ];
    if (!preloader || !bar) return;

    document.body.classList.add('preloader-active');

    let progress = 0;
    const milestones = [
      { at: 10,  lineIdx: 0 },
      { at: 40,  lineIdx: 1 },
      { at: 75,  lineIdx: 2 },
      { at: 100, lineIdx: 3 },
    ];

    const tick = setInterval(() => {
      // Accelerate toward milestones, then slow slightly near 100
      const step = progress < 80 ? (Math.random() * 3 + 1.5) : (Math.random() * 1.2 + 0.4);
      progress = Math.min(100, progress + step);

      if (bar) bar.style.width = progress + '%';
      if (pct)  pct.textContent  = Math.floor(progress) + '%';

      // Activate status lines at thresholds
      milestones.forEach(m => {
        const line = statusLines[m.lineIdx];
        if (!line) return;
        if (progress >= m.at && !line.classList.contains('active') && !line.classList.contains('done')) {
          // Mark previous lines as done
          statusLines.slice(0, m.lineIdx).forEach(l => {
            if (l) { l.classList.remove('active'); l.classList.add('done'); }
          });
          line.classList.add('active');
        }
      });

      if (progress >= 100) {
        clearInterval(tick);
        // Mark all done
        statusLines.forEach(l => { if (l) { l.classList.remove('active'); l.classList.add('done'); } });

        // Short pause then fade out preloader
        setTimeout(() => {
          preloader.classList.add('preloader-hidden');
          document.body.classList.remove('preloader-active');
          // Remove from DOM after transition
          setTimeout(() => { preloader.remove(); }, 800);
        }, 350);
      }
    }, 35);
  })();

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

  // ── 4.5. ANIMATED SKILL PROFICIENCY BARS ─────────────────────
  (() => {
    const skillProfContainer = document.getElementById('skills-proficiency');
    if (!skillProfContainer) return;

    let animated = false;
    const animateBars = () => {
      if (animated) return;
      animated = true;
      const fills = skillProfContainer.querySelectorAll('.skill-bar-fill');
      fills.forEach(fill => {
        const target = fill.getAttribute('data-target') || '80';
        setTimeout(() => {
          fill.style.width = target + '%';
        }, 150);
      });
    };

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateBars();
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.25 });
      observer.observe(skillProfContainer);
    } else {
      animateBars();
    }
  })();

  // Add hover sounds to interactive elements
  document.querySelectorAll('a, button, .glass-card-hover').forEach(el => {
    el.addEventListener('mouseenter', () => playSound('hover'));
  });
  document.querySelectorAll('button[type="submit"], .filter-btn').forEach(el => {
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

  // ── 6. PARTICLE CANVAS (RED theme) ───────────────────────────
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
        ctx.fillStyle = 'rgba(220,38,38,0.35)'; ctx.fill();
        for (let j = i+1; j < particles.length; j++) {
          const p2 = particles[j], d = Math.hypot(p.x-p2.x, p.y-p2.y);
          if (d < 100) {
            ctx.beginPath();
            ctx.strokeStyle = `rgba(220,38,38,${0.12*(1-d/100)})`;
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
    'help': `Available commands:\n  <span class="text-cyan-400 font-bold">skills</span>      - Show tech skills\n  <span class="text-cyan-400 font-bold">projects</span>    - List live projects\n  <span class="text-cyan-400 font-bold">about</span>       - Print bio &amp; education\n  <span class="text-cyan-400 font-bold">contact</span>     - Show contact details\n  <span class="text-cyan-400 font-bold">hire</span>        - Hiring info\n  <span class="text-cyan-400 font-bold">github</span>      - GitHub profile details\n  <span class="text-cyan-400 font-bold">clear</span>       - Clear terminal`,
    'skills': `<span class="text-purple-400 font-bold">Frontend:</span> HTML5, CSS3, JavaScript (ES6+), React.js, Tailwind CSS, Bootstrap\n<span class="text-cyan-400 font-bold">Programming:</span> Python, C, C++, SQL\n<span class="text-blue-400 font-bold">Backend &amp; DB:</span> SQLite, Firebase, Supabase, Node.js\n<span class="text-emerald-400 font-bold">Dev Tools:</span> Git, GitHub, Streamlit, VS Code, Figma`,
    'projects': `🚀 <span class="text-white font-bold">1. Insurance Fraud Detection System</span>\n   Tech: Python, Scikit-learn, SQLite, Streamlit\n   Live: <a href="https://insurance-fraud-detection-kompany.streamlit.app" target="_blank" class="text-cyan-400 underline">insurance-fraud-detection.streamlit.app</a>\n\n🎮 <span class="text-white font-bold">2. Midnight Grid (Car Game)</span>\n   Tech: HTML5 Canvas, CSS3, Vanilla JavaScript\n   Live: <a href="https://midnight-grid.netlify.app" target="_blank" class="text-purple-400 underline">midnight-grid.netlify.app</a>`,
    'about': `Deepak S | B.Tech Information Technology (2nd Year, Grad 2029)\nCollege: Velammal Engineering College, Tamil Nadu\nFocus: Web Development, Machine Learning, Interactive Web Applications.`,
    'contact': `📧 Email: <a href="mailto:deepakselladurai203@gmail.com" class="text-cyan-400 underline">deepakselladurai203@gmail.com</a>\n📱 Phone: <a href="tel:+919345674398" class="text-blue-400">+91 9345674398</a>\n🔗 LinkedIn: <a href="https://linkedin.com/in/deepak-selladurai-6905b3397" target="_blank" class="text-purple-400 underline">linkedin.com/in/deepak-selladurai</a>\n🐙 GitHub: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-emerald-400 underline">github.com/deepak30ips-pixel</a>`,
    'github': `GitHub: <span class="text-emerald-400 font-bold">@deepak30ips-pixel</span>\nRepos: Insurance Fraud Detection, Midnight Grid\nProfile: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-cyan-400 underline">https://github.com/deepak30ips-pixel</a>`,
    'hire': `🎉 <span class="text-emerald-400 font-bold">Thank you for considering Deepak S!</span>\nStatus: <span class="text-cyan-400">Available for Freelance, Internships &amp; Collaborations</span>\nEmail: <span class="text-blue-400">deepakselladurai203@gmail.com</span>`,
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
          <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-red-500/10 text-red-400 border border-red-500/20 mb-2">${d.badge}</span>
          <h3 class="text-2xl font-bold text-white font-heading">${d.title}</h3>
          <p class="text-slate-400 text-sm mt-2 leading-relaxed">${d.description}</p>
        </div>
        <div class="flex flex-wrap gap-2">${d.tech.map(t=>`<span class="px-2.5 py-1 rounded-lg text-xs font-medium bg-red-500/10 text-red-400 border border-red-500/20">${t}</span>`).join('')}</div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800"><h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-red-400">●</span> Problem</h4><p class="text-xs text-slate-400 leading-relaxed">${d.problem}</p></div>
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800"><h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-emerald-400">●</span> Solution</h4><p class="text-xs text-slate-400 leading-relaxed">${d.solution}</p></div>
        </div>
        <div class="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80"><h4 class="text-sm font-semibold text-slate-200 mb-2">Key Highlights</h4><ul class="text-xs text-slate-300 space-y-1.5">${d.keyFeatures.map(f=>`<li class="flex items-start gap-2"><span class="text-red-400">✓</span><span>${f}</span></li>`).join('')}</ul></div>
        <div class="flex items-center gap-3 pt-3 border-t border-slate-800">
          ${d.liveUrl ? `<a href="${d.liveUrl}" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-red-700 to-red-600 hover:from-red-600 hover:to-red-500 text-white font-medium text-sm transition flex items-center gap-2"><span>Live Demo</span><i data-lucide="external-link" class="w-4 h-4"></i></a>` : ''}
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

}); // END DOMContentLoaded
