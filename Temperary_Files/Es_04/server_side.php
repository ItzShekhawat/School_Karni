PHP working <br>
<?php
    echo ($_GET);
    $username = $_GET["username"];
    $email = $_GET["email"];
    $password = $_GET["password"];

    echo($username);

    header("Location:index.html");

?>