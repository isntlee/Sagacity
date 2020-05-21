

fetch('/home')
    .then(response => response.text())
    .then(data => {console.log(data)
    });