let contEuro = 0
let contCuore = 0

const caricaEuro = () => {
    caricaE(++contEuro);
}

const caricaE = (valore) => {
    document.getElementById("contatoreR").innerHTML = valore;
    if (contEuro === 9) {
        contEuro = 0
        document.getElementById("contatoreL").innerHTML = valore;
    }
}

//

const caricaCuore = () => {
    caricaC(--contCuore);
}

const caricaC = (valoree) => {
    document.getElementById("contatoreR").innerHTML = valoree;
}