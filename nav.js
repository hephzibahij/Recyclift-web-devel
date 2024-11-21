document.addEventListener('DOMContentLoaded', () => {
    const hamburgerMenu = document.getElementById('hamburger-menu');
    const navLink = document.getElementById('nav-link');

    hamburgerMenu.addEventListener('click', () => {
        navLink.classList.toggle('open');
    });

    const navItems = document.querySelectorAll('.nav-link a');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            navLink.classList.remove('open');
        });
    });
});