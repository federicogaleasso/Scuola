const carica = () => {
    let email = document.querySelector("#e").value
    let password = document.querySelector("#p").value
    if (email === "prova@prova.it" && password === "prova") {
        alert("Benvenuto!")
    } else {
        alert("Siamo spiacenti email o password errate")
    }
}