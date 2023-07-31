var darkMode = document.getElementById('navbar-brand-mode');
darkMode.onclick = () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        darkMode.src = '/static/images/Vector.png';
    } else {
        darkMode.src = '/static/images/Group 1.png';
    }
}