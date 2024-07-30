const carica = (mioButton) => {
    let qta = document.querySelector("#" + mioButton + "1").value
    let nuovoElemento = document.createElement("div")
    nuovoElemento.innerText = "Quantità: " + qta
    document.querySelector("#carrello").appendChild(nuovoElemento)
}