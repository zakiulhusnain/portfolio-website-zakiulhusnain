// ========== MOBILE MENU TOGGLE ==========
const menuIcon = document.getElementById('menu-icon');
const navbar = document.getElementById('navbar');

menuIcon.addEventListener('click', () => {
    navbar.classList.toggle('open');
});

// Close menu when a link is clicked
navbar.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        navbar.classList.remove('open');
    });
});

// ========== HEADER SCROLL EFFECT ==========
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    // Active nav link
    updateActiveNav();
});

// ========== ACTIVE NAV LINK ON SCROLL ==========
function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.navbar a');

    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.offsetHeight;

        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
}

// ========== SCROLL REVEAL ANIMATIONS ==========
const fadeEls = document.querySelectorAll(
    '.skill-card, .project-card, .service-card, .about-content, .contact-container'
);

fadeEls.forEach(el => {
    el.classList.add('fade-in');
});

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
            setTimeout(() => {
                entry.target.classList.add('visible');
            }, i * 80);
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

fadeEls.forEach(el => observer.observe(el));