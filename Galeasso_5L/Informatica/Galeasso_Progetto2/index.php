<?php
	echo "<a href='index.php'>Home</a> | <a href='index.php?page=login'>Login</a>";
	
	echo "<p></p>";
	
	switch($_GET['page']){
		case "login":
		?>
		<form action="pagina.php" method="post">
			Username: <input type="text" name="username" id="username"/>
			<br>
			Password: <input type="password" name="password" id="password"/>
			<br>
			<input type="button" value="Login" onclick="login_function()"/>
		</form>
		
		<script>			
			const login_function = () => {
				const username = document.getElementById("username").value;
                const password = document.getElementById("password").value;
                
                if (username === "" || password === ""){
                    alert("Compila tutti i campi");
                    return
                }
                
                alert("Utente loggato!");
			}
		</script>
		<?php
		break;
		
		default:
		echo "Home Page";
		break;
	}
?>
