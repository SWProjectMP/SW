const tags = document.querySelectorAll(".all__tegs");
const facults = document.querySelectorAll(".fac__first__section li");
const send = document.querySelector(".search__text");
const rs2 = document.querySelectorAll(".result__main__text");
rs2.forEach((e) => {
    e.addEventListener("click", (e) => {
        const id = e.target.getAttribute('project-id');
        window.location.replace(window.origin+"/project/"+id);
    })
})
const get_xhr = (tags, faculty, csrf_token) => {
    tags = encodeURIComponent(tags);
    faculty = encodeURIComponent(faculty);
    // last_id = encodeURIComponent(last_id);
    csrf_token = encodeURIComponent(csrf_token.value);
    
    window.location.replace(window.location.origin+"/search/?"+"faculty="+faculty+"&tags="+JSON.stringify(tags)+"&csrfmiddlewaretoken="+csrf_token)

}

send.addEventListener('click', (e) => {
    e.preventDefault();
    fc = document.querySelectorAll(".fac__choose");
    last_id = document.querySelectorAll(".rs2");
    // last_id = last_id[last_id.length-1].getAttribute('project-id')
    f_send = ''
    t_send = [];
    csrf_token = document.querySelector('input[name=csrfmiddlewaretoken]');
    fc.forEach((e) => {
        e.classList.contains('clicked') ? f_send=e.getAttribute("facult-name") : ""
    })
    tags.forEach((e) => {
        e.classList.contains('clicked') ? t_send.push(e.getAttribute('tag-name')) : ""
    })
    get_xhr(t_send, f_send, csrf_token)

})

tags.forEach((element) => {
    element.addEventListener("click", () => {
        if(element.classList.contains('clicked')){
            element.classList.remove('clicked');
        } else{
            element.classList.add('clicked');
        }
    })
})
facults.forEach((element) => {
    const selectb = element.querySelector(".fs__text");
    const select = element.querySelector(".fac__choose");
    const sel = (e) => {
        facults.forEach((el) => {
            el.querySelector(".fac__choose").classList.remove('clicked');
        })
        e.classList.contains('clicked') ? e.classList.remove('clicked') : e.classList.add('clicked')
    }
    select.addEventListener("click", (e) => {
        sel(e.target)
    })
    selectb.addEventListener("click", (e) => {
        sel(e.target.previousSibling.previousSibling);
    })
    
})