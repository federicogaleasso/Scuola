//PARSING XML

const carica=()=>{
	fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/4C_catalogoFilm.xml")    //url catalogo film
	.then((catalogo)=>catalogo.text())
	.then((datixml)=>{
		 let mioXML=new DOMParser(); //si trova nel browser, crea un oggetto di tipo DOMParser. Serve per usare parseFromString()
		 let parseXML=mioXML.parseFromString(datixml,"text/xml")    //parsa l'XML
		 console.log(parseXML.querySelector("titolo"))
		 let div_datixml = document.getElementById("datixml");
		 let header = document.createElement("div");
		  div_datixml.className = "col-sm-5";
		  header.innerHTML = "<div class=\"row\">" +
		      "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">TITOLO</div>" +
		      "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">GENERE</div>" +
		      "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">ANNO</div>" +
		      "</div>";
		  div_datixml.appendChild(header);
	})
}
