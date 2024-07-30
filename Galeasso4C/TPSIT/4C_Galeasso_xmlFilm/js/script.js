//PARSING XML

const carica=()=>{
	fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/4C_catalogoFilm.xml")    //url catalogo film
	.then((catalogo)=>catalogo.text())
	.then((datixml)=>{
		let mioXML=new DOMParser(); //si trova nel browser, crea un oggetto di tipo DOMParser. Serve per usare parseFromString()
		let parseXML=mioXML.parseFromString(datixml,"text/xml");    //parsa l'XML
		 
		for(let element of parseXML.getElementsByTagName("film")){
			let div = document.createElement("div");
			div.innerHTML = "<div class=\"row d-flex justify-content-center align-items-center\">" +
				"<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">"+element.querySelector("titolo").innerHTML+"</div>" +
				"<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">"+element.querySelector("genere").getAttribute("value")+"</div>" +
				"<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">"+element.querySelector("anno").getAttribute("value")+"</div>" +
				"</div>";
			document.getElementById("datixml").appendChild(div);
		}
	})
}