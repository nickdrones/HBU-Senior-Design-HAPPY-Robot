<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    //Check if the page is loaded because the user is adding a customer
    if(isset($_POST['checked'])){
        $email = sanitizeMySQL($con, $_POST['uEmail']);
        $lastname = sanitizeMySQL($con, $_POST['coLN']);
        $firstname = sanitizeMySQL($con, $_POST['coFN']);
        $password = sanitizeMySQL($con, $_POST['pw']);
        $verify = sanitizeMySQL($con, $_POST['pwV']);
        $phone = sanitizeMySQL($con, $_POST['phone']);
        $hash = password_hash($password, PASSWORD_DEFAULT);

        if($password == $verify)
            add_user($con, $firstname, $lastname, $username, $hash, $phone);

        else
            die("Passwords do not match");
        //header('Location: .php');
    }

    //create HTML file body
    echo <<<_END
        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "table.css" media = "screen"/>
            </head>

            <body>
                <div class = "table-users">
                <div class = "header"> USER REGISTRATION FORM </div>
                
                <table cellspacing = "0">
                    <form method = "post" action = "register.php">
                        <tr>
                            <td>*Email: </td>
                            <td><input type = "text" name = "uEmail" placeholder = "email*" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*First Name: </td>
                            <td><input type = "text" name = "uFN" placeholder = "name*"required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Last Name: </td>
                            <td><input type = "text" name = "uLN" placeholder = "name*"required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Password: </td>
                            <td><input type = "text" name = "pw" placeholder = "password*" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>*Verify Password: </td>
                            <td><input type = "text" name = "pwV" placeholder = "password*" required = 'required'></td>
                        </tr>
                        <tr>
                            <td>Phone: </td>
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

    function add_user($con, $fn, $ln, $un, $pw, $ph)
    {
        //prepare statements are very common ways of doing things
        $stmt = $con->prepare('INSERT INTO users VALUES(?, ?, ?, ?, ?)');

        $stmt->bind_param("ssss", $fn, $ln, $un, $pw, $ph);
        $stmt->execute();
    }
?>