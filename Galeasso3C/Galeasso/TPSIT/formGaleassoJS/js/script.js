const invio = () => {
    let name=document.querySelector('#n').value
    let surname=document.querySelector('#c').value
    let matricola=document.querySelector('#m').value
    let cellulare=document.querySelector('#nt').value
    let regione=document.querySelector('#rItalia').value

    if (name==undefined||name=="") {
        alert("Nome vuoto!")
    }
    if (surname==undefined||surname=="") {
        alert("Cognome vuoto!")
    }
    if (isNaN(matricola)==undefined||isNaN(matricola)=="") {
        alert("Matricola vuota!")
    }
    if (cellulare==undefined||cellulare=="") {
        alert("Numero di telefono vuoto!")
    }
    if (regione>'19'||regione<'0' ) {
        alert("Regione vuota!")
    }
    
    document.querySelector("body").append(name) 
    document.querySelector("div").append(name)
    document.querySelector("body").append(surname) 
    document.querySelector("div").append(surname)
    document.querySelector("body").append(matricola) 
    document.querySelector("div").append(matricola)
    document.querySelector("body").append(cellulare) 
    document.querySelector("div").append(cellulare)
}