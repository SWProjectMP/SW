const form = document.querySelector(".input-cont");
const form_button = document.querySelector(".btn");
const error_boxes = document.querySelectorAll(".error")

const handleError = (data) => {
    switch(data["error"]){
        case "User already exists":
            error_boxes[1].classList.remove("hide");
            break;
    }
}

const handleAJAXResponse = (data) => {
    if(data["status"] != "OK") handleError(data);
    if(data["status"] == "OK"){
        window.location.replace(window.location.origin)
    }
}

const setAJAX = (username, email, password, csrfmiddlewaretoken) => {
    let xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if(xhr.readyState == XMLHttpRequest.DONE){
            if(xhr.status == 200){
                const data = JSON.parse(xhr.responseText)["data"]
                handleAJAXResponse(data);
            }
        }
    }

    xhr.open('POST', '/api/register/');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send('email='+email+'&password='+password+'&csrfmiddlewaretoken='+csrfmiddlewaretoken+'&username='+username);
}

form.addEventListener("submit", (e) => {
    e.preventDefault();



    const email = encodeURIComponent(form.email.value);
    const username = encodeURIComponent(form.username.value);
    const password = encodeURIComponent(form.password.value);
    const csrfmiddlewaretoken = encodeURIComponent(form.csrfmiddlewaretoken.value);

    setAJAX(username, email, password, csrfmiddlewaretoken)

})