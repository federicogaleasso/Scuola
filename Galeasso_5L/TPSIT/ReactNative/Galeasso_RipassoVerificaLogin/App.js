import { Button, FlatList, Modal, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native'
import React,{useState} from 'react'
let credenziali={
    nome:"",
    pwd:""
}

let mieiDati=[
  {
    nome:"andrea",
    cognome:"giordano"
  },
  {
    nome:"enrico",
    cognome:"allione"
  },
  {
    nome:"pier",
    cognome:"verga"
  }

]
const App = () => {
  const [mioStato, setmioStato] = useState(false)

  const [controllaFlat, setControllaFlat] = useState(false)

  const carica=(parametro,scelta)=>{
    if (scelta==1){
      credenziali.nome=parametro
    }else{
      credenziali.pwd=parametro
    }
   
  }

  const controlla=()=>{
    if(credenziali.nome=="andrea" && credenziali.pwd=="123"){
        setControllaFlat(true)
    }else{
      setmioStato(true)
      setTimeout(()=>{
        setmioStato(false)
      },5000)
    }
  }
  const visualizza=(utenti)=>{
    return(
      <View>
          <Text>IIS  DENINA</Text>
          <Text>{utenti.item.nome}</Text>
          <Text>{utenti.item.cognome}</Text>
          <Button title='CLICCA'/>
      </View>
    )
  }
  return (
    <View style={styles.contenitore}>
      <View style={styles.mioForm}>
        <View><Text style={styles.testo}>LOGIN FORM</Text></View>
        <View>
          <TextInput onChangeText={(testo)=>carica(testo,1)} style={styles.sfondo} placeholder='Inserisci Nome Utente'/>
          <TextInput onChangeText={(testo)=>carica(testo,2)} style={styles.sfondo} placeholder='Inserisci Password'/>
          <TouchableOpacity onPress={controlla} style={styles.mioButton}>
              <Text>CLICCA</Text>
              <Text>Andrea</Text>
          </TouchableOpacity>
        </View>
      </View>

      {
      controllaFlat && (
              <FlatList
              data={mieiDati}
              renderItem={visualizza}
       
              />
      )}

      <Modal visible={mioStato}>
        <Text>CREDENZIALI ERRATE!!!!</Text>
      </Modal>
    </View>
  )
}

export default App

const styles = StyleSheet.create({
  contenitore:{
    backgroundColor:"yellow",
    flex:1,
    justifyContent:"center",
    alignItems:"center"

  },
  mioForm:{
    borderWidth:1,
    borderColor:"red",
    borderStyle:"solid",
    width:300,
    justifyContent:"center",
    alignItems:"center"
  },
  testo:{
    fontSize:30,
    color:"blue"
  },
  sfondo:{
    backgroundColor:"green",
    borderRadius:10,
  },
  mioButton:{
    backgroundColor:"pink",
    justifyContent:"center",
    alignItems:"center",
    borderRadius:20
  }

})