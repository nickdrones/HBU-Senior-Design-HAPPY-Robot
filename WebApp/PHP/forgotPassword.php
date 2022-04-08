<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    //Check if the page is loaded because the user is adding a customer
    if(isset($_POST['checked'])){
        $email = sanitizeMySQL($con, $_POST['uEmail']);
        //header('Location: .php');
    }

    //create HTML file body
    echo <<<_END
        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "http://localhost/InventoryProject/CSS/table.css" media = "screen"/>
            </head>

            <body>
                <div class = "table-users">
                <div class = "header"> FORGOTTEN PASSWORD FORM </div>
                
                <table cellspacing = "0">
                    <form method = "post" action = "register.php">
                        <tr>
                            <td>Please Enter Your Email: </td>
                            <td><input type = "text" name = "uEmail" placeholder = "email*" required = 'required'></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td><input type = "hidden" name = "checked" value = "true">
                            <input type = "submit" value = "Send Password Reset"></td>
                        </tr>
                    </form>
                </table>
            </body>
        </html>
    _END;

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

    function add_user($con, $fn, $ln, $un, $pw, $ph)
    {
        //prepare statements are very common ways of doing things
        $stmt = $con->prepare('INSERT INTO users VALUES(?, ?, ?, ?, ?)');

        $stmt->bind_param("ssss", $fn, $ln, $un, $pw, $ph);
        $stmt->execute();
    }
?>