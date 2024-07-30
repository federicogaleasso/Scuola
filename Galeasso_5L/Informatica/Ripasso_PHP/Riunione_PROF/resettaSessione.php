<?php 
    // Avvia una sessione PHP o ripristina quella corrente se esiste
    session_start();
    
    // Distrugge tutte le informazioni registrate per una sessione
    session_destroy();
    
    // Reindirizza il browser a un'altra pagina (in questo caso, index.html)
    header("Location:index.html");
?>
