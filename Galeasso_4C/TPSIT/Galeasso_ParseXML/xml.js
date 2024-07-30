//PARSING XML

fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/4C_catalogoFilm.xml")    //url catalogo film
.then((miaVariabile)=>miaVariabile.text)
.then((mioTesto)=>{
    let mioXML=new DOMParser(); //si trova nel browser, crea un oggetto di tipo DOMParser. Serve per usare parseFromString()
    let parseXML=mioXML.parseFromString(mioTesto, "application/xml")    //parsa l'XML
    console.log(parseXML)
})