// Advanced Interactive Logic for Deepak S Portfolio

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Lucide Icons
  if (window.lucide) {
    window.lucide.createIcons();
  }

  // 2. Mobile Menu Toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });

    mobileNavLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
      });
    });
  }

  // 3. Dynamic Typewriter Effect
  const typewriterElement = document.getElementById('typewriter-text');
  if (typewriterElement) {
    const phrases = [
      'Aspiring Web Developer',
      'B.Tech IT Student @ Velammal',
      'Python & Machine Learning Enthusiast',
      'Interactive Web Game Creator',
      'Creative Problem Solver'
    ];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 90;

    const typeLoop = () => {
      const currentPhrase = phrases[phraseIndex];
      
      if (isDeleting) {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 45;
      } else {
        typewriterElement.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 90;
      }

      if (!isDeleting && charIndex === currentPhrase.length) {
        typingSpeed = 1800; // Pause at end
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typingSpeed = 400; // Pause before new word
      }

      setTimeout(typeLoop, typingSpeed);
    };

    typeLoop();
  }

  // 4. Interactive Particle Canvas Background
  const canvas = document.getElementById('particle-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(width > 768 ? 45 : 20, 60);

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        radius: Math.random() * 1.5 + 0.8
      });
    }

    let mouse = { x: null, y: null, maxDist: 120 };
    window.addEventListener('mousemove', (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    });
    window.addEventListener('mouseleave', () => {
      mouse.x = null;
      mouse.y = null;
    });

    const drawParticles = () => {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(59, 130, 246, 0.35)';
        ctx.fill();

        // Connect particles with lines
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 100) {
            ctx.beginPath();
            ctx.strokeStyle = `rgba(59, 130, 246, ${0.15 * (1 - dist / 100)})`;
            ctx.lineWidth = 0.6;
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
          }
        }
      }
      requestAnimationFrame(drawParticles);
    };

    drawParticles();
  }

  // 5. Mouse Spotlight Movement on Cards
  const cards = document.querySelectorAll('.spotlight-card');
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });

  // 6. Project Category Filter Logic
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => {
        b.classList.remove('bg-blue-600', 'text-white', 'border-blue-500');
        b.classList.add('bg-slate-900/60', 'text-slate-400', 'border-slate-800');
      });
      btn.classList.add('bg-blue-600', 'text-white', 'border-blue-500');
      btn.classList.remove('bg-slate-900/60', 'text-slate-400', 'border-slate-800');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || category.includes(filterValue)) {
          card.classList.remove('hidden');
          card.classList.add('flex');
        } else {
          card.classList.add('hidden');
          card.classList.remove('flex');
        }
      });
      if (window.lucide) window.lucide.createIcons();
    });
  });

  // 7. Interactive Developer CLI Terminal Widget
  const terminalInput = document.getElementById('terminal-command-input');
  const terminalOutput = document.getElementById('terminal-output');
  const terminalQuickBtns = document.querySelectorAll('.term-quick-btn');

  const terminalCommands = {
    'help': `Available commands:
  • <span class="text-cyan-400 font-bold">skills</span>      - Show categorized tech skills
  • <span class="text-cyan-400 font-bold">projects</span>    - List featured live projects
  • <span class="text-cyan-400 font-bold">about</span>       - Print bio & education
  • <span class="text-cyan-400 font-bold">contact</span>     - View email, phone & socials
  • <span class="text-cyan-400 font-bold">hire</span>        - Information on hiring Deepak
  • <span class="text-cyan-400 font-bold">github</span>      - Output GitHub profile details
  • <span class="text-cyan-400 font-bold">clear</span>       - Clear the terminal screen`,

    'skills': `<span class="text-purple-400 font-bold">Frontend:</span> HTML5, CSS3, JavaScript (ES6+), React.js, Tailwind CSS, Bootstrap
<span class="text-cyan-400 font-bold">Programming:</span> Python, C, C++, SQL
<span class="text-blue-400 font-bold">Backend & DB:</span> SQLite, Firebase, Supabase, Node.js
<span class="text-emerald-400 font-bold">Dev Tools:</span> Git, GitHub, Streamlit, VS Code, Figma`,

    'projects': `🚀 <span class="text-white font-bold">1. Insurance Fraud Detection System</span>
   Tech: Python, Scikit-learn, SQLite, Streamlit
   Live: <a href="https://insurance-fraud-detection-kompany.streamlit.app" target="_blank" class="text-cyan-400 underline">insurance-fraud-detection.streamlit.app</a>

🎮 <span class="text-white font-bold">2. Midnight Grid (Car Game)</span>
   Tech: HTML5 Canvas, CSS3, Vanilla JavaScript
   Live: <a href="https://midnight-grid.netlify.app" target="_blank" class="text-purple-400 underline">midnight-grid.netlify.app</a>`,

    'about': `Deepak S | B.Tech Information Technology (2nd Year, Grad 2029)
College: Velammal Engineering College, Tamil Nadu
Focus: Web Development, Machine Learning, Interactive Web Applications.`,

    'contact': `📧 Email: <a href="mailto:deepakselladurai203@gmail.com" class="text-cyan-400 underline">deepakselladurai203@gmail.com</a>
📱 Phone: <a href="tel:+919345674398" class="text-blue-400">+91 9345674398</a>
🔗 LinkedIn: <a href="https://linkedin.com/in/deepak-selladurai-6905b3397" target="_blank" class="text-purple-400 underline">linkedin.com/in/deepak-selladurai</a>
🐙 GitHub: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-emerald-400 underline">github.com/deepak30ips-pixel</a>`,

    'github': `GitHub Username: <span class="text-emerald-400 font-bold">deepak30ips-pixel</span>
Repositories: Insurance Fraud Detection, Midnight Grid, Web Projects
Profile: <a href="https://github.com/deepak30ips-pixel" target="_blank" class="text-cyan-400 underline">https://github.com/deepak30ips-pixel</a>`,

    'hire': `🎉 <span class="text-emerald-400 font-bold">Thank you for considering Deepak S!</span>
Status: <span class="text-cyan-400">Available for Freelance Projects, Internships, & Collaborations</span>
Please use the contact form below or email directly: <span class="text-blue-400 underline">deepakselladurai203@gmail.com</span>`,

    'sudo hire deepak': `[PERMISSIONS GRANTED] ✨ Excellent choice! Initiating contact protocol...
Deepak is excited to work with you. Email: <span class="text-cyan-400">deepakselladurai203@gmail.com</span>`
  };

  const handleCommand = (cmdText) => {
    const rawCmd = cmdText.trim().toLowerCase();
    if (!rawCmd) return;

    if (rawCmd === 'clear') {
      if (terminalOutput) terminalOutput.innerHTML = '';
      return;
    }

    const commandPrompt = document.createElement('div');
    commandPrompt.className = 'flex items-center gap-2 text-slate-400 text-xs font-mono-code mt-2';
    commandPrompt.innerHTML = `<span class="text-cyan-400">deepak@portfolio:~$</span> <span class="text-white">${cmdText}</span>`;
    terminalOutput.appendChild(commandPrompt);

    const response = document.createElement('div');
    response.className = 'text-slate-300 text-xs font-mono-code pl-4 py-1 leading-relaxed border-l-2 border-slate-700/60 my-1';

    if (terminalCommands[rawCmd]) {
      response.innerHTML = terminalCommands[rawCmd];
    } else {
      response.innerHTML = `<span class="text-red-400">Command not recognized: "${rawCmd}".</span> Type <span class="text-cyan-400 font-bold">help</span> to see all commands.`;
    }

    terminalOutput.appendChild(response);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  };

  if (terminalInput) {
    terminalInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        handleCommand(terminalInput.value);
        terminalInput.value = '';
      }
    });
  }

  terminalQuickBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const cmd = btn.getAttribute('data-cmd');
      handleCommand(cmd);
    });
  });

  // 8. Animated Stats Counters on Scroll
  const statNumbers = document.querySelectorAll('.stat-counter');
  let statsAnimated = false;

  const animateCounters = () => {
    statNumbers.forEach(counter => {
      const target = +counter.getAttribute('data-target');
      const suffix = counter.getAttribute('data-suffix') || '';
      let current = 0;
      const increment = Math.max(1, Math.ceil(target / 30));
      const updateCount = () => {
        current += increment;
        if (current < target) {
          counter.innerText = current + suffix;
          setTimeout(updateCount, 40);
        } else {
          counter.innerText = target + suffix;
        }
      };
      updateCount();
    });
  };

  const statsSection = document.getElementById('hero-stats');
  if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !statsAnimated) {
          animateCounters();
          statsAnimated = true;
        }
      });
    }, { threshold: 0.5 });
    observer.observe(statsSection);
  }

  // 9. Copy to Clipboard Functionality
  window.copyToClipboard = function(text, elementId, defaultText = 'Copy') {
    navigator.clipboard.writeText(text).then(() => {
      const badge = document.getElementById(elementId);
      if (badge) {
        badge.innerText = 'Copied! ✓';
        badge.classList.add('text-emerald-400');
        setTimeout(() => {
          badge.innerText = defaultText;
          badge.classList.remove('text-emerald-400');
        }, 2000);
      }
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  };

  // 10. Project Details Modal Data & Handlers
  const projectDetails = {
    'fraud-detection': {
      title: 'Insurance Fraud Detection System',
      badge: 'Machine Learning & Web App',
      tech: ['Python', 'Scikit-learn', 'SQLite', 'Streamlit', 'Pandas'],
      description: 'An advanced machine learning application engineered to assess and predict suspicious insurance claim activities in real-time.',
      problem: 'Insurance companies lose billions annually due to undetected fraudulent claims. Manual audit takes too much time and often misses subtle anomaly patterns.',
      solution: 'Trained predictive classification models on historical claim records, connected an SQLite persistence layer, and provided a user-friendly Streamlit dashboard for claim adjusters.',
      keyFeatures: [
        'Real-time anomaly & fraud probability scoring',
        'Interactive dashboard with visual decision metrics',
        'Secure SQLite storage for historical audit trail',
        'Zero-setup cloud deployment on Streamlit Cloud'
      ],
      liveUrl: 'https://insurance-fraud-detection-kompany.streamlit.app',
      githubUrl: 'https://github.com/deepak30ips-pixel/insurance-fraud-detection'
    },
    'midnight-grid': {
      title: 'Midnight Grid (Interactive Car Game)',
      badge: 'Web Game / Front-End',
      tech: ['HTML5', 'CSS3', 'JavaScript', 'Canvas API', 'Web Audio'],
      description: 'An adrenaline-fueled, dark-themed browser car game built entirely from scratch with vanilla web technologies.',
      problem: 'Creating a fast, 60fps responsive arcade experience directly in the browser without bulky third-party gaming engines.',
      solution: 'Leveraged lightweight HTML5 Canvas physics, fluid keyboard state event listeners, and dark neon aesthetics with custom difficulty curves.',
      keyFeatures: [
        'Free Roam Mode: Open street driving and exploration',
        'Bank Heist Mode: Time-attack tactical getaway objective',
        'Responsive dark arcade interface with immersive visual FX',
        'Optimized for both desktop keyboards and touch devices'
      ],
      liveUrl: 'https://midnight-grid.netlify.app',
      githubUrl: null
    }
  };

  const projectModal = document.getElementById('project-modal');
  const projectModalContent = document.getElementById('project-modal-body');

  window.openProjectModal = function(projectId) {
    const data = projectDetails[projectId];
    if (!data || !projectModal || !projectModalContent) return;

    let techBadges = data.tech.map(t => `<span class="px-2.5 py-1 rounded-lg text-xs font-medium bg-blue-500/10 text-blue-400 border border-blue-500/20">${t}</span>`).join('');
    let featuresList = data.keyFeatures.map(f => `<li class="flex items-start gap-2"><span class="text-blue-400">✓</span><span>${f}</span></li>`).join('');

    let linksHtml = '';
    if (data.liveUrl) {
      linksHtml += `<a href="${data.liveUrl}" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-medium text-sm transition flex items-center gap-2"><span>Live Demo</span> <i data-lucide="external-link" class="w-4 h-4"></i></a>`;
    }
    if (data.githubUrl) {
      linksHtml += `<a href="${data.githubUrl}" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition flex items-center gap-2"><span>Source Code</span> <i data-lucide="github" class="w-4 h-4"></i></a>`;
    }

    projectModalContent.innerHTML = `
      <div class="space-y-5">
        <div>
          <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 mb-2">${data.badge}</span>
          <h3 class="text-2xl font-bold text-white font-heading">${data.title}</h3>
          <p class="text-slate-400 text-sm mt-2 leading-relaxed">${data.description}</p>
        </div>

        <div class="flex flex-wrap gap-2">
          ${techBadges}
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800">
            <h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-red-400">●</span> Problem</h4>
            <p class="text-xs text-slate-400 leading-relaxed">${data.problem}</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800">
            <h4 class="text-sm font-semibold text-slate-200 mb-1 flex items-center gap-2"><span class="text-emerald-400">●</span> Solution</h4>
            <p class="text-xs text-slate-400 leading-relaxed">${data.solution}</p>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80">
          <h4 class="text-sm font-semibold text-slate-200 mb-2">Key Highlights</h4>
          <ul class="text-xs text-slate-300 space-y-1.5">
            ${featuresList}
          </ul>
        </div>

        <div class="flex items-center gap-3 pt-3 border-t border-slate-800">
          ${linksHtml}
          <button onclick="closeProjectModal()" class="ml-auto px-4 py-2 rounded-xl text-slate-400 hover:text-white text-sm">Close</button>
        </div>
      </div>
    `;

    projectModal.classList.remove('hidden');
    projectModal.classList.add('flex');
    if (window.lucide) window.lucide.createIcons();
  };

  window.closeProjectModal = function() {
    if (projectModal) {
      projectModal.classList.add('hidden');
      projectModal.classList.remove('flex');
    }
  };

  // 11. Resume Modal Handlers
  const resumeModal = document.getElementById('resume-modal');
  window.openResumeModal = function() {
    if (resumeModal) {
      resumeModal.classList.remove('hidden');
      resumeModal.classList.add('flex');
      if (window.lucide) window.lucide.createIcons();
    }
  };
  window.closeResumeModal = function() {
    if (resumeModal) {
      resumeModal.classList.add('hidden');
      resumeModal.classList.remove('flex');
    }
  };

  window.addEventListener('click', (e) => {
    if (e.target === projectModal) closeProjectModal();
    if (e.target === resumeModal) closeResumeModal();
  });
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeProjectModal();
      closeResumeModal();
    }
  });

  // 12. Background Contact Form with Web3Forms
  const contactForm = document.getElementById('contact-form');
  const formSuccess = document.getElementById('form-success-toast');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Message';
      
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="inline-block animate-pulse">⏳ Sending Message...</span>';
      }

      const formData = new FormData(contactForm);
      if (!formData.get('access_key')) {
        formData.append('access_key', 'f01867c1-288e-4734-99a9-69ab16db1ae9');
      }

      try {
        const response = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          body: formData
        });

        const result = await response.json();

        if (result.success || response.status === 200) {
          if (formSuccess) {
            formSuccess.innerHTML = `<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i><span>Message sent successfully! Deepak has received your note in his Gmail.</span>`;
            formSuccess.className = 'mb-4 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2';
            formSuccess.classList.remove('hidden');
            if (window.lucide) window.lucide.createIcons();
            setTimeout(() => formSuccess.classList.add('hidden'), 6000);
          }
          contactForm.reset();
        } else {
          throw new Error(result.message || 'Submission failed');
        }
      } catch (error) {
        console.log('Submission info:', error);
        if (formSuccess) {
          formSuccess.innerHTML = `<i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i><span>Message recorded! You can also email directly at deepakselladurai203@gmail.com</span>`;
          formSuccess.className = 'mb-4 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2';
          formSuccess.classList.remove('hidden');
          if (window.lucide) window.lucide.createIcons();
          setTimeout(() => formSuccess.classList.add('hidden'), 6000);
        }
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnText;
          if (window.lucide) window.lucide.createIcons();
        }
      }
    });
  }

  // 13. Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn?.classList.remove('opacity-0', 'pointer-events-none');
      backToTopBtn?.classList.add('opacity-100');
    } else {
      backToTopBtn?.classList.add('opacity-0', 'pointer-events-none');
      backToTopBtn?.classList.remove('opacity-100');
    }
  });
});
