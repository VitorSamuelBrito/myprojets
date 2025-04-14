const navigator = document.querySelector('.navigator')
const allLi = document.querySelectorAll('li')

allLi.forEach((li, index) => {

    li.addEventListener("click", e => {
        navigator.querySelector(".activeLi").classList.remove("activeLi")
        li.classList.add("activeLi")

        const indicator = document.querySelector(".indicator")
        indicator.style.transform = `translateX(calc(${index * 137}px))`
    })
});