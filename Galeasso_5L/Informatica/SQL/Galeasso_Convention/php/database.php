<?php
	class Database {
		private static $host = 'localhost';
		private static $username = 'root';
		private static $password = '';
		private static $database = 'Galeasso_Convention';
		public static $connection;

		public static function connessione () {
			self::$connection = new mysqli(self::$host, self::$username, self::$password, self::$database);
			return true;
		}
		
		public static function eseguiQuery ($query) {
			$risultato = self::$connection->query($query);
			return $risultato;
		}
		
		public static function disconnessione () {
			self::$connection->close();
			echo "Connessione chiusa <br>";
		}
	}
?>