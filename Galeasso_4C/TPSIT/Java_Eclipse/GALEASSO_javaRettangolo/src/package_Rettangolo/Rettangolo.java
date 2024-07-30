package package_Rettangolo;

//classe Rettangolo
public class Rettangolo {
	
	//Attributi privati (base, altezza)
	private double base;
	private double altezza;
	
	//Metodi getter e setter per l'attributo base
	public double get_base() {
		return base;
	}

	public void set_base(double base) {
		this.base = base;
	}
	
	//Metodi getter e setter per l'attributo altezza
	public double get_altezza() {
		return altezza;
	}
	
	public void set_altezza(double altezza) {
		this.altezza = altezza;
	}
	
	//Metodo per il calcolo dell'area del rettangolo
	public double calcolaArea() {
		return base * altezza;
	}
	
	//Metodo main
	public static void main(String[] args) {
		
		//Creazione di due istanze della classe Rettangolo
		Rettangolo r1 = new Rettangolo();
		r1.set_base(2);
		r1.set_altezza(3);
	
	    Rettangolo r2 = new Rettangolo();
	    r2.set_base(2);
	    r2.set_altezza(2);
	    
	    // Calcolo delle aree dei due rettangoli
	    double area_r1 = r1.calcolaArea();
	    double area_r2 = r2.calcolaArea();
	    
	    //Confronto per determinare il rettangolo con l'area maggiore
	    if (area_r1 > area_r2) {
	    	System.out.println("L'area del rettangolo 1 (" + area_r1 + ") è maggiore dell'area del rettangolo 2 (" + area_r2 + ")");
	    } else if (area_r2 > area_r1) {
			System.out.println("L'area del rettangolo 2 (" + area_r2 + ") è maggiore dell'area del rettangolo 1 (" + area_r1 + ")");
	    } else {
			System.out.println("L'area dei due rettangoli è uguale (" + area_r1 + ")");
	    }
	}

}