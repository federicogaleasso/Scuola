import { StyleSheet, Text, View, Button, Alert } from 'react-native'
import React from 'react'

const App = () => {

	const visualizza = () =>{
		Alert.alert("Benvenuto")
	}

  return (
	<View style={styles.body}>
	  <Text style={styles.testo}>Federico</Text>
	  <Text style={styles.testo}>Galeasso</Text>
	  <Button title='POPUP' onPress={visualizza}/>
	</View>
  )
}

export default App

const styles = StyleSheet.create({
	body:{
		backgroundColor: "red",
		display:"flex",
		justifyContent:"center",
		alignItems:"center",
		flex:1,
	},
	testo:{
		color: "white",
		fontSize:20,
	}
})