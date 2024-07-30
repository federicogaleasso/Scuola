//sebastiano soave 3C
const start=()=>{
    //alert("corretto")
    let messaggio="a"
    let nome=document.querySelector("#nome").value
    if (nome==undefined || nome=="") {
        alert ("cella nome è vuota")
        messaggio="errore"
    }
    let cognome=document.getElementById("cognome").value
    if (cognome==undefined || cognome=="") {
        alert ("cella cognome è vuota")
        messaggio="errore"
    }
    let matricola=document.querySelector("#matricola").value
    if (matricola==undefined || matricola=="") {
        alert ("cella matricola è vuota")
        messaggio="errore"    
    }
    let telefono=document.getElementById("telefono").value
    if (telefono==undefined || telefono=="") {
        alert ("cella telefono è vuota")
        messaggio="errore"
    }
    let regione=document.getElementById("regione").value
    if (messaggio=="errore") {
        document.getElementById("output").innerHTML = messaggio
    }else{
        let messaggio="Ciao "+ nome + " " + cognome + " " + "matricola: " + matricola + " " +  "il numero di telefono: " +  telefono + " " + "la regione: " + regione    
        document.getElementById("output").innerHTML = messaggio    
    }
     
    
}
