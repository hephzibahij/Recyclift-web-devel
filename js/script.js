const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.nav-links');

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('open');
})

document.addEventListener('DOMContentLoaded', function() {
    const subscribeButton = document.querySelector('.btn-success');

    subscribeButton.addEventListener('click', function(event) {
        event.preventDefault();
        alert('Thank you for subscribing!');
        // Additional interactive behavior can be added here
    });
});