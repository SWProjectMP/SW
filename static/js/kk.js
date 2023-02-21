const button = document.querySelector("#sd");
let csrf = document.querySelectorAll("body input")[0];
button.addEventListener('click', (e) =>{
    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if(xhr.readyState == XMLHttpRequest.DONE){
            if(xhr.status == 200){
                const data = JSON.parse(xhr.responseText)["data"]
                console.log(data)
            }
        }
    }

    csrf = encodeURIComponent(csrf.value)

    xhr.open('POST', '/api/test/');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.send('csrfmiddlewaretoken='+csrf+"&tags=[Python, Cpp, JavaScript]");
})