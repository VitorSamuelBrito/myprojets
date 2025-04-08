let body = document.querySelector("body") 
let tenis = document.querySelector(".img-tenis")
// let são as varaiveis
// querySeleor é um seletor
// O document é o HTML

function altervisual(cor, image){
    body.style.background = cor
    tenis.src = image
}