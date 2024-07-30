// Dichiarazione del package
package com.example.galeasso_calcolatrice;

// Import delle librerie necessarie
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import android.content.Intent;

// Definizione della classe principale MainActivity
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    // Dichiarazione delle variabili di istanza
    private TextView display;
    private StringBuilder input;
    private double num1, num2;
    private char operazione;

    View.OnClickListener mioListener2 = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            Toast.makeText(MainActivity.this, "LISTENER 2", Toast.LENGTH_SHORT).show();
        }
    };

    // Metodo chiamato quando l'activity viene creata
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //LISTENER 2
        //Con questo secondo tipo di listener vado a creare un oggetto all'interno dell'Activity che implementa l'interfaccia "View.OnClickListener". Può essere utilizzato da chiunque.
        Button btnL2 = (Button) findViewById(R.id.btnL2);
        btnL2.setOnClickListener(mioListener2);

        //LISTENER 3 (Creato a RUN-TIME)
        Button btnL3 = (Button) findViewById(R.id.btnL3);
        btnL3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View vista) {
                Toast.makeText(MainActivity.this, "LISTENER 3", Toast.LENGTH_SHORT).show();
            }
        });

        //LISTENER 4
        //Solo con "this", da errore! Il parametro deve essere un oggetto che implementi l'interfaccia viewOCL(). "this" richiama se stesso (oggetto di tipo Activity).
        Button btnL4 = (Button) findViewById(R.id.btnL4);
        btnL4.setOnClickListener(this);

        // Inizializzazione degli elementi (display e input)
        display = findViewById(R.id.display);
        input = new StringBuilder();

        Intent IntentShare = getIntent();
        String testoShare = IntentShare.getStringExtra(Intent.EXTRA_TEXT);
        if(testoShare != null) {
            display.setText(testoShare);
        }

        // Impostazione dei listener per i pulsanti numerici da 0 a 9
        setNumberButtonListener(R.id.btn0, "0");
        setNumberButtonListener(R.id.btn1, "1");
        setNumberButtonListener(R.id.btn2, "2");
        setNumberButtonListener(R.id.btn3, "3");
        setNumberButtonListener(R.id.btn4, "4");
        setNumberButtonListener(R.id.btn5, "5");
        setNumberButtonListener(R.id.btn6, "6");
        setNumberButtonListener(R.id.btn7, "7");
        setNumberButtonListener(R.id.btn8, "8");
        setNumberButtonListener(R.id.btn9, "9");

        // Impostazione dei listener per i pulsanti degli operatori
        setOperatorButtonListener(R.id.btnSomma, '+');
        setOperatorButtonListener(R.id.btnSottr, '-');
        setOperatorButtonListener(R.id.btnMolt, '*');
        setOperatorButtonListener(R.id.btnDivis, '/');

        // Impostazione del listener per il pulsante di calcolo del risultato
        findViewById(R.id.btnRisultato).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (input.length() > 0) {
                    try {
                        num2 = Double.parseDouble(input.toString());
                    }
                    catch (NumberFormatException nfe) {
                        num2 = 18;
                    }
                    catch (NullPointerException npe) {

                    }
                    double risultato = Calcola();
                    input.setLength(0);
                    input.append(risultato);
                    aggiornaDisplay();
                }
            }
        });

        // Impostazione del listener per il pulsante di cancellazione
        findViewById(R.id.btnCancella).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setLength(0);
                aggiornaDisplay();
            }
        });
    }

    // Metodo per impostare il listener per i pulsanti numerici
    private void setNumberButtonListener(int btnId, String number) {
        Button button = findViewById(btnId);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (display.getText().toString().equals("NaN")) {
                    input.setLength(0);
                }
                input.append(number);
                aggiornaDisplay();
            }
        });
    }

    // Metodo per impostare il listener per i pulsanti degli operatori
    private void setOperatorButtonListener(int btnId, char op) {
        Button button = findViewById(btnId);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (input.length() > 0) {
                    num1 = Double.parseDouble(input.toString());
                    operazione = op;
                    input.append(operazione);
                    aggiornaDisplay();

                }
            }
        });
    }

    // Metodo per eseguire l'operazione in base all'operatore selezionato
    private double Calcola() {
        switch (operazione) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                if (num2 != 0) {
                    return num1 / num2;
                } else {
                    // Gestione della divisione per zero
                    Toast.makeText(this, "Non puoi dividere per 0", Toast.LENGTH_SHORT).show(); // Notifica Toast
                }
            default:
                return Double.NaN;
        }
    }

    // Metodo per aggiornare il display con l'input corrente
    private void aggiornaDisplay() {
        display.setText(input.toString());
    }

    //LISTENER 1
    //Questo è il primo tipo di listener, ed è dichiarato nel file "activity_main.xml".
    // E' presente infatti il metodo onClick. In questo caso vado a chiamare il mio metodo "metodo_listener_btn_1" e lo vado ad utilizzare per stampare un toast.
    public void metodo_listener_btn_1(View view){
        Toast.makeText(this, "LISTENER 1", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onClick(View v) {
        Toast.makeText(this, "LISTENER 4", Toast.LENGTH_SHORT).show();
    }
}