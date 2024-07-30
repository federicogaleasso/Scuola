#ESERCIZIO

#Visualizza un menù all'utente con le voci

# + --> SOMMA
# - --> SOTTRAI
# X --> MOLTIPLICA
# : --> DIVIDI
# E --> EXIT

# Ogni voce del menù deve richiamare una funzione che chiede  all'utente di inserire N numeri e restituire il risultato delle relative operazioni (Per la divisione solo due numeri - valutare il caso della divisione per zero).

SOMMA(){
	echo -n "Inserisci il numero di numeri: "
	read Numeri
	for (( i=0; i<$Numeri; i++ ))
	do
		echo -n "Inserisci il numero: "
		read  N
		Som=$(( Som + N ))
	done
return $Som
}

SOTT(){
	echo -n "Inserisci il numero di numeri: "
	read Numeri
	for (( i=0; i<$Numeri; i++ ))
	do
		echo -n "Inserisci il numero: "
		read  N
		Sot=$N
		Sot=$(( Sot - N ))
	done
	Sot=$(( Sot - N ))
return $Sot	
}

MOLT() {
	Moltiplicazione=1
	echo -n "Inseisci il numero di numeri: "
	read Numeri
	for (( i=0; i<$Numeri; i++ ))
	do
		echo -n "Inserisci il numero: "
		read N
		Moltiplicazione=$(( Moltiplicazione * N ))
	done
return $Moltiplicazione
}

DIVIS() {
	echo -n "Inserisci il primo numero: "
	read N1
	echo -n "Inserisci il secondo numero: "
	read N2
	if [[ N1 -eq 0 ]]
	then
		echo "Impossibile"
		else 
			Div=$(( N1/N2 ))
	fi
return $Div
}

echo "Scegli una voce del seguente menù"
echo -n "+ --> SOMMA
- --> SOTTRAI
x --> MOLTIPLICA
: --> DIVIDI
E --> EXIT
La tua scelta --> "
read Menu

case $Menu in
	"+")
		SOMMA
		s=$?
		echo "La somma vale $Som"
	;;
	"-")
		SOTT
		so=$?
		echo "La sottrazione vale $Sot"
	;;
	"x")
		MOLT
		m=$?
		echo "La moltiplicazione vale $Moltiplicazione"
	;;
	":")
		DIVIS
		divis=$?
		echo "La divisione vale $Div"
	;;
esac
