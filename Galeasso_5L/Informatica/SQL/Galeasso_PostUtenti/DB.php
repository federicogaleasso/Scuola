<?php
    class Database {
        private static $host = "localhost";
        private static $username = "root";
        private static $password = "";
        private static $database = "esConnDDLDMLQL";
        private static $connessione;

        public static function collegati(){
            self::$connessione = new mysqli(
                self::$host, 
                self::$username, 
                self::$password, 
                self::$database
            );
        }

        public static function executeQuery($query){
            $res = self::$connessione->query($query);
            if (!$res) {
                echo "Errore nella query: " . self::$connessione->error;
            }
            return $res;
        }
    }
?>