<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    //Check if the page is loaded because the user is adding a customer
    if(!empty($_POST['fName']) && !empty($_POST['lName']) && !empty($_POST['email']) && !empty($_POST['password']) && !empty($_POST['vPassword']) && !empty($_POST['phone'])){
        $em = sanitizeMySQL($con, $_POST['email']);
        $ln = sanitizeMySQL($con, $_POST['lName']);
        $fn = sanitizeMySQL($con, $_POST['fName']);
        $pw = sanitizeMySQL($con, $_POST['password']);
        $verify = sanitizeMySQL($con, $_POST['vPassword']);
        $ph = sanitizeMySQL($con, $_POST['phone']);
        $hash = password_hash($pw, PASSWORD_DEFAULT);

        if($pw === $verify)
        {
            $query   = "SELECT * FROM users WHERE email='$em'";
            $result  = $con->query($query);

            if ($result->num_rows > 0) die("Email already in use.");
            
            $query = "INSERT INTO users(FirstName, LastName, email, password, phone) VALUES ('$fn', '$ln', '$em', '$hash', '$ph')";
    
            $result = $con->query($query);
    
            if(!result){
                die("Unable to insert");
            }
            else header("Location: http://localhost/InventoryProject/HTML/homePage.html");
        }

        else
            die("Passwords do not match");
    }

    $result->close();
    $con->close();

    function sanitizeString($var)
    {
        if(get_magic_quotes_gpc())
            $var = stripslashes($var);
        $var = strip_tags($var);
        $var = htmlentities($var);
        return $var;
    }

    function sanitizeMySQL($con, $var)
    {
        $var = $con->real_escape_string($var);
        $var = sanitizeString($var);
        return $var;
    }
?>