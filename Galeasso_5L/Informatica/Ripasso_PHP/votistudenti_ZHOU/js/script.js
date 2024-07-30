let records = [];

let count = 0;

const subjectMap = {
    "0": "Matematica",
    "1": "Inglese",
    "2": "Informatica",
    "3": "TPSIT",
    "4": "Sistemi e Reti"
}

function addScore(){
    let firstName   = document.querySelector("#firstname").value;
    let score       = document.querySelector("#score").value;
    let subject     = document.querySelector("#subjectList").selectedOptions[0].value;

    let errorTextElement = document.querySelector("#errorText");

    if(firstName.trim().length == 0){
        errorTextElement.textContent = "Cognome non deve essere vuoto o solo spazio";
        return;
    }

    if(isNaN(parseInt(score))){
        errorTextElement.textContent = "Il voto deve essere un numero";
        return;
    }

    score = parseInt(score);

    if(score < 0 || score > 10){
        errorTextElement.textContent = "Il voto deve essere compreso tra 0 e 10";
        return;
    }

    subject = subjectMap[subject]

    errorTextElement.textContent = "";

    let scoreRecordMap = new Map();

    scoreRecordMap.set("firstname", firstName)
        .set("score", score)
        .set("subject", subject);

    records.push(scoreRecordMap);
    let trElement = document.createElement("tr");
    trElement.setAttribute("id", `n${count++}`);

    if(records.length-1 == 0){
        let trElement = document.createElement("tr");
        let tdElement = document.createElement("th");
        tdElement.textContent = "Cognome";
        trElement.appendChild(tdElement);

        tdElement = document.createElement("th");
        tdElement.textContent = "Voto";
        trElement.appendChild(tdElement);

        tdElement = document.createElement("th");
        tdElement.textContent = "Materia";
        trElement.appendChild(tdElement);

        tdElement = document.createElement("th");
        tdElement.textContent = "Elimina";
        trElement.appendChild(tdElement);

        document.querySelector("#scoreTable").appendChild(trElement);
        document.querySelector("#scoreTable").style.border = "1px black solid";
        document.querySelector("#scoreTable").style.borderCollapse = "collapse";
        
    }

    for(let [k, v] of scoreRecordMap){
        let tdElement = document.createElement("td");
        tdElement.textContent = v;
        trElement.appendChild(tdElement);
    }

    scoreRecordMap.set("id", count-1)

    let tdElement = document.createElement("td");
    tdElement.innerHTML = `<div class="btn"><span><input type='button' value='Elimina' onclick="eliminaRecord(${count-1})"/></span><div>`;
    trElement.appendChild(tdElement);

    tdElement = document.createElement("td");
    tdElement.setAttribute("id", `c${count-1}`);
    tdElement.style.color = "red";
    tdElement.style.display = "none"
    trElement.appendChild(tdElement);

    document.querySelector("#scoreTable").appendChild(trElement)
}

function eliminaRecord(num){
    document.querySelector("#scoreTable").removeChild(document.querySelector(`#n${num}`));
    records = records.filter((val) => val.get("id") != num)

    if(records.length == 0){
        document.querySelector("#scoreTable").removeChild(document.querySelector("tr"))
    }
}

function send(){
    let firstName = document.querySelector("#firstnameToSearch").value;
    let subject = subjectMap[document.querySelector("#subjectToSearch").selectedOptions[0].value];
    let errorTextElement = document.querySelector("#errorText");

    if(firstName.trim().length == 0){
        errorTextElement.textContent = "Cognome da cercare non deve essere vuoto o solo spazio";
        return;
    }

    let tmp = records.map((val) => {
        let obj = {};
        val.forEach((val, key) => {
            obj[key] = val;
        })

        return obj
    });

    let formData = new FormData();
    formData.append("data", JSON.stringify(tmp));
    formData.append("firstname", firstName);
    formData.append("subject", subject)
    
    fetch("student_score.php", {
        method: "POST",
        body: formData,
    }).then(response => {
        return response.text();
    }).then((text) => {
        if(text.startsWith("<!DOCTYPE html>")){
            let newWindow = window.open();

            if(newWindow){
                newWindow.document.write(text);
            }
            else
            {
                alert("Impossibile aprire popup, poichè è stato bloccato per questo sito.")
            }
        }else if(text.startsWith("err")){
            let [_, txt] = text.split("@");
            errorTextElement.innerHTML = txt;
        }else{
            for(let msg of text.split("\n")){
                let [id, txt] = msg.split("@", 2);
                console.log(id, txt)
                let errorRecordtxt = document.querySelector(`#c${id}`);
                errorRecordtxt.style.width = "max-content";
                errorRecordtxt.style.display = "block";
                errorRecordtxt.innerHTML = txt;
                errorRecordtxt.style.borderWidth = "0px";
            }
        }

    });

}