<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

<form action="" method="post">

enter name:<input type="text" name="uName"><br/>
enter password:<input type="password" name="uPWD"><br/>

<input type="submit">
<input type="reset">

</form>

<?php
if(isset($_POST["uName"])){
	$uName=$_POST["uName"];
	$uPWD=$_POST["uPWD"];

$Link=mysqli_connect("localhost","root","fred70267","user");
$add="INSERT INTO user2(name,pwd) VALUES ('$uName','$uPWD')";
mysqli_query($Link,$add);

$read="SELECT * FROM user2";
$readresult=mysqli_query($Link,$read);
	echo "<table border='1'>";
	echo "<tr><td>number</td><td>name</td><td>pwd</td><td>update</td><td>delete</td></tr>";
while($result=mysqli_fetch_array($readresult)){

	echo "<tr>";
	echo "<td>".$result[0]."</td><td>".$result[1]."</td><td>".$result[2]."</td>";
	
	echo "<td><a href='del.php?no=".$result[0]."'>update</a></td>";
	echo "<td><a href='del.php?no=".$result[0]."'>delete</a></td>";
	echo "</tr>";

}
	echo "</table>";
}



?>

</body>
</html>