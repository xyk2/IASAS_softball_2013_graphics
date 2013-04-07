<?php
	$quantity = $_POST['home'];
	$file = fopen("graphics.json","w");
	fwrite($file,$quantity);
	fclose($file);
	echo $quantity;
?>
