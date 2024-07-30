var vettore=[];
var temp =[]

const visualizza = ()=> {
    fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json")
    .then((dati)=>dati.json())
    .then((misure)=> {
        let i
        let div_misure = document.getElementById("misure");
        let header = document.createElement("div");
        div_misure.className = "col-sm-6";
        header.innerHTML = "<div class=\"row\">" +
            "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">DEVICE</div>" +
            "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">TIMESTAMP</div>" +
            "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">TEMPERATURA<br /></div>" +
            "<div class=\"col-sm-3 bg-warning border d-flex justify-content-center align-items-center p-2\">UMIDITA'</div>" +
            "</div>";
        div_misure.appendChild(header);

        for (var misura of misure) {
            let row = document.createElement("div");
            row.innerHTML = "<div class=\"row flag\">" + 
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + misura.lora_device_id + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTimestamp(misura.measured_at) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTemperature(misura.data.sensor1.lowRes.temperature) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + misura.data.sensor1.lowRes.humidity + "</div>" +
                "</div>";
            div_misure.appendChild(row);

            vettore[i] = misura.data.sensor1.lowRes.humidity
            temp[i] = misura.data.sensor1.lowRes.temperature
            console.log(vettore[i])
        }

    })
}
const cleanTimestamp = (timestamp)=> 
    timestamp.substring(8, 10) + "/" + timestamp.substring(5, 7) + "/" + timestamp.substring(0, 4);

const cleanTemperature = (temperature)=>
    temperature /= 10;

const CrescenteTmp = ()=> {
    vettore.sort()
    fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json")
    .then((dati)=>dati.json())
    .then((misure)=> {
        let i = 0
        let div_misure = document.getElementById("misure");

        misure.forEach(function ({misura}) {
            let row = document.querySelector("flag");
            row.innerHTML = "<div class=\"row\">" + 
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + misura.lora_device_id + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTimestamp(misura.measured_at) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTemperature(temp[i]) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + vettore[i] + "</div>" +
                "</div>";
            div_misure.appendChild(row);

            i++
        })
    })
    
}

const DecrescenteTmp = ()=> {
    //
}

const CrescenteUmd = ()=> {
    vettore.sort()
    fetch("https://raw.githubusercontent.com/icobasco/sample_data_files/master/pera_misure_sample.json")
    .then((dati)=>dati.json())
    .then((misure)=> {
        let i = 0
        let div_misure = document.getElementById("misure");

        misure.forEach(function ({misura}) {
            let row = document.querySelector("flag");
            row.innerHTML = "<div class=\"row\">" + 
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + misura.lora_device_id + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTimestamp(misura.measured_at) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + cleanTemperature(misura.data.sensor1.lowRes.temperature) + "</div>" +
                "<div class=\"col-sm-3 bg-dark border d-flex justify-content-center\">" + vettore[i] + "</div>" +
                "</div>";
            div_misure.appendChild(row);

            i++
        })
    })
}

const DecrescenteUmd = ()=> {
    //
}