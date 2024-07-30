import { StatusBar } from 'expo-status-bar';
import { React, useState } from 'react';
import { StyleSheet, Text, View, Button, Modal, TextInput, Image, Switch, FlatList, TouchableOpacity, Alert } from 'react-native';

export default function App() {
	const [visualizza, setVisualizza] = useState(false);
	const [testo, setTesto] = useState("");
	const [visualizzaImg, setVisualizzaImg] = useState(false);
	const arrayAlunni=[
		{
			nome:"mario",
			cognome:"rossi",
			eta:18
		},
		{
			nome:"luca",
			cognome:"verdi",
			eta:18
		},
		{
			nome:"giulia",
			cognome:"gialli",
			eta:18
		},
	]

	const show =()=>{
		setVisualizza(!visualizza)
	}
	
	const caricaTesto =(testo)=>{
		setTesto(testo)
	}

	const modifica =()=>{
		setVisualizzaImg(!visualizzaImg)
	}

	const premi =(arrayAlunni)=>{
		Alert.alert(arrayAlunni.item.nome)
	}

	const singolaOpzione =(arrayAlunni)=>{
		return(
			<TouchableOpacity onPress={()=>premi(arrayAlunni)}>
				<View>
					<Text>{arrayAlunni.item.nome}</Text>
					<Text>{arrayAlunni.item.cognome}</Text>
					<Text>{arrayAlunni.item.eta}</Text>
				</View>
			</TouchableOpacity>
		)
	}

	return (
	<View style={styles.container}>
		<Text>Carrello</Text>
		<Button title="Visualizza Carrello" onPress={show}/>
		<StatusBar style="auto" hidden={false}/>
		<Modal visible={visualizza}>
			<Text>Finestra Modale</Text>
			<TextInput style={styles.casellaTesto} onChangeText={caricaTesto} />
			<Text>{testo}</Text>
			<Button title="Prova"/>
			<Switch value={visualizzaImg} onChange={modifica}/>
			{visualizzaImg == true && (<Image style={styles.immagine} source={{uri: "https://www.neveitalia.it/foto/albums/userpics/10594/monviso_da_pian_regina_home.jpg"}} />)}
			<FlatList data={arrayAlunni} renderItem={singolaOpzione} keyExtractor={(item, index) => index.toString()} />
		</Modal>
	</View>
	);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  casellaTesto: {
	backgroundColor:"yellow",
  },
  immagine: {
	height:300,
	width:300
  }
});
