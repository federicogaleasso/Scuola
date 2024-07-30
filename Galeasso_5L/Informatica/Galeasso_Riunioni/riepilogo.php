<?php
session_start();

if (isset($_SESSION["persone"]) && !empty($_SESSION["persone"])) {
    $persone = $_SESSION["persone"];

    echo "<h1>Riepilogo</h1>";

    echo "<table border='1'>";

	echo "<tr>";
	echo "<th></th>";
	$orari = ["9-11", "11-13", "14-16", "16-18"];
	foreach ($orari as $orario) {
        echo "<th>$orario</th>";
    }
    echo "</tr>";

    $giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"];

    foreach ($giorni as $giorno) {
        echo "<tr><th>$giorno</th>";
        foreach ($orari as $orario) {
            $contDisp = 0;
            foreach ($persone as $persona) {
                if ($persona["giorni"] === $giorno && $persona["orari"] === $orario) {
                    $contDisp++;
                }
            }
            echo "<td>$contDisp</td>";
        }
        echo "</tr>";
    }

    echo "</table>";

} else {
    echo "<p>Nessun dato disponibile.</p>";
}

echo "<br/>";
echo "<a href='index.php'>Nuovo inserimento</a><br/>";
echo "<a href='logout.php'>Logout</a>";
?>
