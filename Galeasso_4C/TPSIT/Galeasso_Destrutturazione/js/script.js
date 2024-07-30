const visualizza =()=>{
    let alunno={
        nome:"Mario",
        cognome:"Rossi",
        eta:25,
        sesso:"M",
        telefono:{
            cellulare:7856478904,
            fisso:7835436783,
            fax:7685467873
        }
    }
    console.log(alunno.nome+" "+alunno.cognome+" "+alunno.telefono.cellulare)
    
    const{nome,cognome, telefono:{cellulare}}=alunno //DESTRUTTURAZIONE --> tira fuori dal literal object quello che vogliamo
    console.log(nome+" "+cognome+" "+cellulare) //Da qui in poi si evita di scrivere alunno.nome, basta scrivere nome
}