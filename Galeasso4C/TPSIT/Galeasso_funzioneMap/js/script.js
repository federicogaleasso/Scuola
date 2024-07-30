const visualizza=()=>{
    let mioArray=[5,5,6,5,2,3]
    console.log(
        mioArray.map((elemento,indice)=>{  //FUNZIONE MAP
            return elemento*2;  //Moltiplica *2 ogni elemento dell'array
        })
    )
}