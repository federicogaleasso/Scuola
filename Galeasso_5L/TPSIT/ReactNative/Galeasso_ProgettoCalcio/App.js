import { StatusBar } from 'expo-status-bar';
import { React } from 'react';
import { StyleSheet, Text, View, FlatList, TouchableOpacity, Alert, Image } from 'react-native';

export default function App() {
	const arrayCalcio=[
		{
			squadra1:"Italia",
			squadra2:"Francia",
			immagine1: "https://flagpedia.net/data/flags/h80/it.png",
			immagine2: "https://flagpedia.net/data/flags/h80/fr.png",
			punteggio1:3,
			punteggio2:2,
		},
		{
			squadra1:"Italia",
			squadra2:"Francia",
			immagine1: "https://flagpedia.net/data/flags/h80/it.png",
			immagine2: "https://flagpedia.net/data/flags/h80/fr.png",
			punteggio1:3,
			punteggio2:2,
		},
		{
			squadra1:"Italia",
			squadra2:"Francia",
			immagine1: "https://flagpedia.net/data/flags/h80/it.png",
			immagine2: "https://flagpedia.net/data/flags/h80/fr.png",
			punteggio1:3,
			punteggio2:2,
		},
		{
			squadra1:"Italia",
			squadra2:"Francia",
			immagine1: "https://flagpedia.net/data/flags/h80/it.png",
			immagine2: "https://flagpedia.net/data/flags/h80/fr.png",
			punteggio1:3,
			punteggio2:2,
		},
	]

	const premi =(arrayCalcio)=>{
		Alert.alert(arrayCalcio.item.squadra1 + " VS " + arrayCalcio.item.squadra2, "Punteggio: " + arrayCalcio.item.punteggio1 + " - " + arrayCalcio.item.punteggio2)
	}

	const divPartite =(arrayCalcio)=>{
		return(
			<TouchableOpacity onPress={()=>premi(arrayCalcio)} style={styles.buttonPartita}>
				<View>
					<Text style={styles.testoSquadre}>{arrayCalcio.item.squadra1} VS {arrayCalcio.item.squadra2}</Text>
					<View style={styles.divGrigio}>
						<View>
							<Image style={styles.immagine} source={{uri: arrayCalcio.item.immagine1}} />
							<Text style={styles.testoPunteggio}>{arrayCalcio.item.punteggio1}</Text>
						</View>
						<View>
							<Image style={styles.immagineFreccia} source={{uri: "https://cdn.icon-icons.com/icons2/1580/PNG/512/2849833-arrow-arrows-forward-interface-multimedia-navigation-right_107957.png"}} />
						</View>
						<View>
							<Image style={styles.immagine} source={{uri: arrayCalcio.item.immagine2}} />
							<Text style={styles.testoPunteggio}>{arrayCalcio.item.punteggio2}</Text>
						</View>
					</View>
				</View>
			</TouchableOpacity>
		)
	}

	return (
	<View style={styles.container}>
		<FlatList data={arrayCalcio} renderItem={divPartite} keyExtractor={(item, index) => index.toString()} />
		<StatusBar style="auto" hidden={false}/>
	</View>
	);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
	marginTop:25,
  },
  casellaTesto: {
	backgroundColor:"yellow",
  },
  immagine: {
	height:40,
	width:60,
	margin:7,
  },
  testoSquadre: {
	backgroundColor:"#000000",
	color:"#fff",
	width:400,
	textAlign:"center",
	fontWeight:"bold",
  },
  divGrigio: {
	backgroundColor:"#808080",
	color:"#000000",
	width:400,
	textAlign:"center",
	fontWeight:"bold",
  },
  testoPunteggio: {
	color:"#000000",
	textAlign:"center",
	fontWeight:"bold",
	display:"flex",
	width:500,
	marginTop:15,
	position:"absolute",
  },
  immagineFreccia: {
	height:20,
	width:50,
	marginLeft:320,
  },
  buttonPartita: {
	marginBottom:10,
  }
});