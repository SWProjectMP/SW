const login_form = document.querySelector(".container");
const login_button = document.querySelector(".btn");
const logo = document.querySelector("#logo_ref");
console.log(logo);
logo.addEventListener('click', () => {
    window.location.replace(window.location.origin);
    console.log('bbb')
})

login_form.addEventListener("submit", (e) => {
    e.preventDefault();

    const username = encodeURIComponent(login_form.username.value);
    const password = encodeURIComponent(login_form.password.value);
    const csrfmiddlewaretoken = encodeURIComponent(login_form.csrfmiddlewaretoken.value);

    setAJAX(username, password, csrfmiddlewaretoken);

})

const handleAJAXError = (data) => {
    switch(data["error"]){
        case "Incorrect password or username":
            console.log("Incorrect password or username");
            break;
    }
}

const handleAJAXResponse = (data) => {
    if (data["status"] == "OK") window.location.replace(window.location.origin);
    if (data["status"] != "OK") handleAJAXError(data);
}

const setAJAX = (username, password, csrfmiddlewaretoken) => {
    let xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if(xhr.readyState == XMLHttpRequest.DONE){
            if(xhr.status == 200){
                const data = JSON.parse(xhr.responseText)["data"]
                handleAJAXResponse(data);
            }
        }
    }

    xhr.open('POST', '/api/login/');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send('password='+password+'&csrfmiddlewaretoken='+csrfmiddlewaretoken+'&username='+username);
}