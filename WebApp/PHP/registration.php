<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    //Check if the page is loaded because the user is adding a customer
    if(isset($_POST['checked'])){
        $em = sanitizeMySQL($con, $_POST['uEmail']);
        $ln = sanitizeMySQL($con, $_POST['uLN']);
        $fn = sanitizeMySQL($con, $_POST['uFN']);
        $pw = sanitizeMySQL($con, $_POST['pw']);
        $verify = sanitizeMySQL($con, $_POST['pwV']);
        $ph = sanitizeMySQL($con, $_POST['phone']);
        $hash = password_hash($password, PASSWORD_DEFAULT);

        if($pw === $verify)
        {
            $query = "INSERT INTO users(FirstName, LastName, email, password, phone) VALUES ('$fn', '$ln', '$em', '$pw', '$ph')";
    
            $result = $con->query($query);
    
            if(!result){
                die("Unable to insert");
            }
            else header('Location: login.php');
        }

        else
            die("Passwords do not match");
    }

    //create HTML file body
    echo <<<_END
        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "http://localhost/InventoryProject/CSS/table.css" media = "screen"/>
            </head>

            <body>
                <div class = "table-users">
                <div class = "header"> USER REGISTRATION FORM </div>
                
                <table cellspacing = "0">
                    <form method = "post" action = "register.php">
                        <tr>
                            <td>*Email: </td>
                            <td><input type = "text" name = "uEmail" placeholder = "email" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*First Name: </td>
                            <td><input type = "text" name = "uFN" placeholder = "first name"required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Last Name: </td>
                            <td><input type = "text" name = "uLN" placeholder = "last name" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Password: </td>
                            <td><input type = "password" name = "pw" placeholder = "password" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Verify Password: </td>
                            <td><input type = "password" name = "pwV" placeholder = "password" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Phone: </td>
                            <td><input type = "text" name = "phone" placeholder = "123-456-7890"></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td><input type = "hidden" name = "checked" value = "true">
                            <input type = "submit" value = "Submit User Info"></td>
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
?>