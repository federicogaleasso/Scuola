package concorrente;

public class inizio {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("INIZIO");
		
		stampa console = new stampa();
		stampa console2 = new stampa();
		//console.visualizza();
		console.start();
		console2.start();
		
		System.out.println("FINE");
		
	}

}
