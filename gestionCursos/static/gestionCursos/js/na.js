const navToggle = document.querySelector(".navv-toggle");
const navMenu = document.querySelector(".navv-menu");

navToggle.addEventListener("click",() => {  
    navMenu.classList.toggle("navv-menu_visible");
    navToggle.setAttribute("aria-label", "Cerrar menú");
});

window.addEventListener("click",e =>{
    if (navMenu.classList.contains("navv-menu_visible") && e.target != navToggle) {
        navMenu.classList.toggle("navv-menu_visible");
        navToggle.setAttribute("aria-label", "Abrir menú");
    }
})