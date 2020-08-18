const menuBtn = document.querySelector(".menu-btn");
const navBar = document.querySelector(".navbar");
const navItems = document.querySelectorAll(".navbar__item");

let showMenu = false;

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu(){
    if(!showMenu){
        navBar.classList.add('open');
        menuBtn.classList.add('open');
        navItems.forEach(item => item.classList.add('open'));

        showMenu = true;
    } else {
        menuBtn.classList.remove('open');
        navBar.classList.remove('open');
        navItems.forEach(item => item.classList.remove('open'));

        showMenu = false;
    }
}