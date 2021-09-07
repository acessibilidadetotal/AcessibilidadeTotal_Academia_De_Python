var hamburguer = document.querySelector(".hamburguer");

hamburguer.addEventListener("click", function() {
    document.querySelector(".sidebar").classList.toggle("show-menu");
});

function protegercodigo() {
    if (event.button == 2 || event.button == 3) {
        alert('Codigo protegido!');
    }
}
document.onmousedown = protegercodigo