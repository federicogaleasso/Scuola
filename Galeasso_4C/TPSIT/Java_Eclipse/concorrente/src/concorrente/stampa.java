package concorrente;

public class stampa extends Thread {

	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			System.out.println(i);
		}
		System.out.println();
	}

	

	
}
