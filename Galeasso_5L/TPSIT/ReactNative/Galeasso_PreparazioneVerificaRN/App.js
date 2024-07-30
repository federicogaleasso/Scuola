import React, { useState, useEffect } from "react";
import { FlatList, Modal, StyleSheet, Text, TextInput, TouchableOpacity, View, Alert } from "react-native";
import prodottiJson from './prodotti.json';

const App = () => {

	const arrayProdotti = [
		{
			nome: "Prodotto 1",
			prezzo: 5,
			quantita: 10
		},
		{
			nome: "Prodotto 2",
			prezzo: 10,
			quantita: 15
		},
		{
			nome: "Prodotto 3",
			prezzo: 15,
			quantita: 20
		}
	]

	const [prodotti, setProdotti] = useState(prodottiJson);
	const [nome, setNome] = useState("");
	const [prezzo, setPrezzo] = useState();
	const [quantita, setQuantita] = useState();
	const [finestraModale, setFinestraModale] = useState(false);

	// useEffect(() => {
	// 	const URL = "https://raw.githubusercontent.com/federicogaleasso/NodeJS/main/prodotti.json"
	// 	fetch(URL)
	// 	.then(response => response.json())
	// 	.then(data => {
	// 		setProdotti(data)
	// 	})
	// }, [])

	const aggiungiProdotto = () => {
		if (!nome || !prezzo || !quantita) {
			Alert.alert("Errore","Compilare tutti i campi")
		} else {
			const prodottoEsistente = prodotti.find(prodotto => prodotto.nome == nome)
			if(prodottoEsistente){
				Alert.alert("Attenzione","Prodotto già presente")
			} else {
				if(!parseFloat(prezzo) || !parseInt(quantita)){
					Alert.alert("Errore","Compilare i campi correttamente")
				} else {
					setProdotti([...prodotti, { nome, prezzo: parseFloat(prezzo), quantita: parseInt(quantita) }]);
					setNome("");
					setPrezzo("");
					setQuantita("");
					Alert.alert("Aggiunta","Prodotto aggiunto con successo")
				}
			}
		}
	};

	const visualizzaProdotti = (prodotti) => {
		return (
			<View style={styles.prodotto}>
				<Text style={styles.titolo}><Text style={styles.boldText}>{prodotti.item.nome}</Text></Text>
				<Text style={styles.whiteText}>Prezzo: <Text style={styles.boldText}>{prodotti.item.prezzo}</Text></Text>
				<Text style={styles.whiteText}>Quantità: <Text style={styles.boldText}>{prodotti.item.quantita}</Text></Text>
				<TouchableOpacity onPress={() => eliminaProdotto(prodotti.item.nome)} style={styles.redButton}>
					<Text style={styles.whiteText}>Elimina</Text>
				</TouchableOpacity>
			</View>
		);
	}

	const eliminaProdotto = (nome) => {
		// for(let i=0;i<prodotti.length;i++){
		// 	if(prodotti[i].nome == nome){
		// 		prodotti.splice(i,1)
		// 	}
		// }
		
		const nuovoArrayProdotti = prodotti.filter(prodotto => prodotto.nome !== nome);
		setProdotti(nuovoArrayProdotti);
		Alert.alert("Eliminazione","Prodotto eliminato con successo")

		// if(nuovoArrayProdotti.length == 0){
		//  	Alert.alert("Attenzione","Nessun prodotto rimasto")
		// }
	};

	const vediFinestraModale = () => (
		setFinestraModale(true)
	);

	const nascondiFinestraModale = () => (
		setFinestraModale(false)
	);

	return (
		<View style={styles.container}>
			<Text style={styles.titolo}>Galeasso Federico - Carrello</Text>
			<TextInput placeholder="Nome" value={nome} onChangeText={setNome} style={styles.input} placeholderTextColor="#fff" />
			<TextInput placeholder="Prezzo" value={prezzo} onChangeText={setPrezzo} style={styles.input} keyboardType="numeric" placeholderTextColor="#fff" />
			<TextInput placeholder="Quantità" value={quantita} onChangeText={setQuantita} style={styles.input} keyboardType="numeric" placeholderTextColor="#fff" />
			<TouchableOpacity onPress={aggiungiProdotto} style={styles.bluButton}>
				<Text style={styles.whiteText}>Aggiungi Prodotto</Text>
			</TouchableOpacity>
			<TouchableOpacity onPress={vediFinestraModale} style={styles.bluButton}>
				<Text style={styles.whiteText}>Visualizza Prodotti</Text>
			</TouchableOpacity>
			<Modal visible={finestraModale} >
				<View style={styles.finestraModale}>
					{ prodotti.length == 0 ? (
							<Text style={styles.titolo}>Nessun prodotto rimasto</Text>
						) : (
							<FlatList data={prodotti} renderItem={visualizzaProdotti} keyExtractor={(item, index) => index.toString()} />
						)
					}
					<TouchableOpacity onPress={nascondiFinestraModale} style={styles.bluButton}>
						<Text style={styles.whiteText}>Chiudi</Text>
					</TouchableOpacity>
				</View>
			</Modal>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: "center",
		alignItems: "center",
		padding: 37,
		backgroundColor: "#121212",
	},
	input: {
		width: "100%",
		padding: 10,
		marginTop: 10,
		borderColor: "#444",
		borderWidth: 1,
		borderRadius: 5,
		backgroundColor: "#1f1f1f",
		color: "#fff",
	},
	prodotto: {
		padding: 15,
		marginVertical: 5,
		backgroundColor: "#1e1e1e",
		borderColor: "#333",
		borderWidth: 1,
		borderRadius: 5,
		width: 350,
	},
	prodottoText: {
		color: "#ccc",
	},
	bluButton: {
		backgroundColor: "#0d6efd",
		padding: 10,
		borderRadius: 5,
		marginTop: 10,
		width: "100%",
	},
	redButton: {
		backgroundColor: "#dc3545",
		padding: 5,
		borderRadius: 5,
		marginTop: 10,
	},
	whiteText: {
		color: "#fff",
		textAlign: "center",
	},
	boldText: {
		fontWeight: "bold",
		color: "#fff",
	},
	finestraModale: {
		flex: 1,
		justifyContent: "center",
		alignItems: "center",
		padding: 20,
		backgroundColor: "#121212",
	},
	titolo: {
		fontSize: 25,
		fontWeight: "bold",
		color: "#fff",
		textAlign: "center",
	},
});

export default App;