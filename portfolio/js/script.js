// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

// Check for saved theme preference or default to 'light'
const currentTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', currentTheme);
updateThemeIcon(currentTheme);

themeToggle.addEventListener('click', () => {
    const theme = html.getAttribute('data-theme');
    const newTheme = theme === 'light' ? 'dark' : 'light';

    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
});

function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector('i');
    icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
}

// Mobile Menu Toggle
const mobileToggle = document.getElementById('mobileToggle');
const navMenu = document.getElementById('navMenu');

mobileToggle.addEventListener('click', () => {
    mobileToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Navbar Scroll Effect
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// Active Navigation Link
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;

        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Typing Animation
const typingText = document.getElementById('typingText');
const phrases = [
    'highly passionate about technology',
    'an Engineering Student',
    'a Python Developer',
    'a Machine Learning Enthusiast',
    'a Problem Solver',
    'an IoT Developer'
];

let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingSpeed = 100;

function type() {
    const currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
        typingText.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 50;
    } else {
        typingText.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 100;
    }

    if (!isDeleting && charIndex === currentPhrase.length) {
        isDeleting = true;
        typingSpeed = 2000; // Pause at end
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typingSpeed = 500; // Pause before next phrase
    }

    setTimeout(type, typingSpeed);
}

// Start typing animation
setTimeout(type, 1000);

// Particle Background
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particles = [];
const particleCount = 80;

class Particle {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2 + 1;
        this.speedX = Math.random() * 1 - 0.5;
        this.speedY = Math.random() * 1 - 0.5;
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > canvas.width) this.x = 0;
        if (this.x < 0) this.x = canvas.width;
        if (this.y > canvas.height) this.y = 0;
        if (this.y < 0) this.y = canvas.height;
    }

    draw() {
        const theme = html.getAttribute('data-theme');
        ctx.fillStyle = theme === 'dark' ? 'rgba(255, 255, 255, 0.5)' : 'rgba(0, 0, 0, 0.3)';
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
    }
}

function initParticles() {
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
}

function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    particles.forEach(particle => {
        particle.update();
        particle.draw();
    });

    connectParticles();
    requestAnimationFrame(animateParticles);
}

function connectParticles() {
    const theme = html.getAttribute('data-theme');
    const lineColor = theme === 'dark' ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';

    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 120) {
                ctx.strokeStyle = lineColor;
                ctx.lineWidth = 0.5;
                ctx.beginPath();
                ctx.moveTo(particles[i].x, particles[i].y);
                ctx.lineTo(particles[j].x, particles[j].y);
                ctx.stroke();
            }
        }
    }
}

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

initParticles();
animateParticles();

// Scroll Reveal Animation
const revealElements = document.querySelectorAll('.reveal, .skill-item, .tech-item, .project-card, .contact-item, .contact-form');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('reveal-visible');
            }, index * 100);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(element => {
    revealObserver.observe(element);
});

// Skills Filter
const skillsFilterBtns = document.querySelectorAll('.skills-filter .filter-btn');
const skillCategories = document.querySelectorAll('.skill-category');

skillsFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all buttons
        skillsFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        skillCategories.forEach(category => {
            if (filter === 'all') {
                category.classList.remove('hidden');
            } else {
                const categoryType = category.getAttribute('data-category');
                if (categoryType === filter) {
                    category.classList.remove('hidden');
                } else {
                    category.classList.add('hidden');
                }
            }
        });
    });
});

// Projects Filter
const projectsFilterBtns = document.querySelectorAll('.projects-filter .filter-btn');
const projectCards = document.querySelectorAll('.project-card');

projectsFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all buttons
        projectsFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        projectCards.forEach(card => {
            if (filter === 'all') {
                card.classList.remove('hidden');
            } else {
                const category = card.getAttribute('data-category');
                if (category === filter) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            }
        });
    });
});

// Certifications Carousel
const track = document.getElementById('certificationsTrack');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const certCards = document.querySelectorAll('.cert-card');

let currentIndex = 0;
const cardsToShow = window.innerWidth <= 640 ? 1 : window.innerWidth <= 968 ? 2 : 3;
const maxIndex = Math.max(0, certCards.length - cardsToShow);

function updateCarousel() {
    const cardWidth = certCards[0].offsetWidth;
    const gap = 32; // 2rem gap
    const offset = -(currentIndex * (cardWidth + gap));
    track.style.transform = `translateX(${offset}px)`;
}

nextBtn.addEventListener('click', () => {
    if (currentIndex < maxIndex) {
        currentIndex++;
        updateCarousel();
    }
});

prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
});

window.addEventListener('resize', () => {
    updateCarousel();
});

// Contact Form
const contactForm = document.getElementById('contactForm');
const formStatus = document.getElementById('formStatus');

contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
    };

    try {
        const response = await fetch('http://localhost:5000/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (response.ok) {
            formStatus.textContent = 'Message sent successfully! I\'ll get back to you soon.';
            formStatus.className = 'form-status success';
            contactForm.reset();
        } else {
            formStatus.textContent = data.error || 'Failed to send message. Please try again.';
            formStatus.className = 'form-status error';
        }
    } catch (error) {
        formStatus.textContent = 'Failed to send message. Please try emailing directly.';
        formStatus.className = 'form-status error';
    }

    setTimeout(() => {
        formStatus.style.display = 'none';
    }, 5000);
});

// Resume Download
const downloadResumeBtn = document.getElementById('downloadResume');

downloadResumeBtn.addEventListener('click', async (e) => {
    e.preventDefault();

    try {
        const response = await fetch('http://localhost:5000/api/download-resume');

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Sandesh_Bhatta_Resume.pdf';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        } else {
            alert('Resume download is currently unavailable. Please contact directly.');
        }
    } catch (error) {
        alert('Resume download is currently unavailable. Please contact directly.');
    }
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Profile Image Placeholder
const profileImage = document.getElementById('profileImage');
profileImage.onerror = function () {
    this.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="400" height="400"%3E%3Crect fill="%236366f1" width="400" height="400"/%3E%3Ctext fill="white" font-family="Arial" font-size="120" x="50%25" y="50%25" text-anchor="middle" dy=".3em"%3ESB%3C/text%3E%3C/svg%3E';
};

// Project Images Placeholder
document.querySelectorAll('.project-image img').forEach(img => {
    img.onerror = function () {
        const projectTitle = this.closest('.project-card').querySelector('.project-title').textContent;
        const initial = projectTitle.charAt(0);
        this.src = `data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="400" height="200"%3E%3Crect fill="%23667eea" width="400" height="200"/%3E%3Ctext fill="white" font-family="Arial" font-size="60" x="50%25" y="50%25" text-anchor="middle" dy=".3em"%3E${initial}%3C/text%3E%3C/svg%3E`;
    };
});
