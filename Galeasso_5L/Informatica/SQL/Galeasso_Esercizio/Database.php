<?php
	private class Database{
		private static $host="localhost";
		private static $username="root";
		private static $password="";
		private static $dbname="Esercizio";
		private static $connessione;
		
		public static function collegati(){
			$connessione = new msqli(
				self::$host,
				self::$username,
				self::$password,
				self::$dbname
			);
		}
		
		public static function executeQuery($query){
			$res = self::$connessione->query($query);
			return $res;
		}
	}
?>
