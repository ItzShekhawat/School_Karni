<?php

    #DataBase setting and connection code -----------------------------------------------------
    $user_DB = "root";
    $password_DB = '';
    $dbPalestra = 'dbpalestra';
    $db = mysqli_connect("localhost", $user_DB, $password_DB, $dbPalestra) or die("Connection failed");

    // End DataBase setting and connection code --------------------------------------------------
    if(isset($_POST['submit'])){

        $username = htmlentities($_POST["name"], ENT_HTML5,'ISO-8859-1');
        $surname = htmlentities($_POST["surname"], ENT_HTML5,'ISO-8859-1');
        $age = htmlentities($_POST["age"], ENT_HTML5,'ISO-8859-1');
        $sesso = htmlentities($_POST["sesso"], ENT_HTML5,'ISO-8859-1');
        $corso = $_POST["corso"]; // Array
        $email = htmlentities($_POST["email"], ENT_HTML5,'ISO-8859-1');
    } 

    // Preventing sql-injection 
    /* 
    $username = stripslashes($username);
    $username = mysql_real_escape_string($username);

    $email = stripslashes($email);
    $email= mysql_real_escape_string($email);

    */

    $query_controll = "Select email from `tContatti` WHERE email = '$email' ";

    $query_result = mysqli_query($db,$query_controll);

    if ($query_result == FALSE){
        echo "Sorry, we already contacted you on your email";       
    }else{
        
        foreach($corso as $c){
            $query = "INSERT INTO `tContatti`(`name`, `surname`, `age`, `sesso`, `corso`, `email` ) VALUES ('$username', '$surname', $age, '$sesso', '$c', '$email')";
        }
    
        $result = mysqli_query($db, $query) or die("Query is not working");
    
        if($result){
            echo "We will contact you soon";
        }else{
            echo "You already have an account with us";
        }
    }



    //---------------------------------------------------------------------------------------------

    /*
    $row = mysqli_fetch_array($result);
    if ($row["user"] == $username && $row["email"] == $email)
    {
        echo "We will contact you soon  via email mr " .$username ."on your email : " . $email;
    }else{
        echo "Something is not working, please try later ";
    }
    */
 
    
?>