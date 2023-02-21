const buttons = document.querySelectorAll(".card");
buttons.forEach((e) => {
    e.addEventListener('click', () => {
        window.location.replace(window.origin+"/search")
    })
})