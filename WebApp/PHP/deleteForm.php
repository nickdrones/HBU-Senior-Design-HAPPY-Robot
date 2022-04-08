<?php
    require_once 'loginfo.php';

    session_start();

    if(isset($_SESSION['firstname']))
    {
        $fname = $_SESSION['firstname'];
        $lname = $_SESSION['lastname'];
        $email = $_SESSION['email'];

        echo "<br><div style = 'text-align: center;'><h2>Welcome back $fname $lname.<br>This is the Delete Form!</h2></div>";
    }

    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    $query   = "SELECT * FROM users WHERE email='$email'";
    $result  = $con->query($query);

    if ($result->num_rows != 1) die("User not found");

    $row = $result->fetch_array(MYSQLI_ASSOC);
    $pn  = $row['permissionNumber'];

    $query   = "SELECT * FROM permissions WHERE permissionNumber='$pn'";
    $result  = $con->query($query);

    $row = $result->fetch_array(MYSQLI_ASSOC);
    $delete  = $row['deleting'];

    if($delete != 1){
        die("User not allowed to delete");
    }

    //Check if the page is loaded because the user submitted a Delete Form
    if(isset($_POST['delete'])){
        $pCode = $_POST['pCode'];
        $query = "DELETE FROM parts WHERE partCode = $pCode;";

        $result = $con->query($query);
        echo "<br>Query: $query<br>Result: $result<br>";
        
        if(!result) echo "Unable to delete";
    }

    //create HTML file body
    echo <<<_END
        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "http://localhost/InventoryProject/CSS/table.css" media = "screen"/>
            </head>

            <body>
    _END;

    //here we will create the table
    $query = "SELECT * FROM parts";
    $result = $con->query($query);
    if(!$result)
        die("Error executing the query");

    $rows = $result->num_rows;

    echo <<<_END
        <div class = "table-users">
            <div class = "header"> PARTS </div>
            <table cellspacing = "0">
                <tr>
                    <td> Part Name </td>
                    <td> Semester </td>
                    <td> Current Stock </td>
                    <td> Initial Stock </td>
                    <td> Quantity Per Student </td>
                    <td> Buy Price </td>
                    <td> Action </td>
                </tr>
    _END;

    for ($j = 0; $j < $rows; $j++)
    {
        $row = $result->fetch_array(MYSQLI_BOTH);

        $v1 = htmlspecialchars($row['partName']);
        $v2 = htmlspecialchars($row['semester']);
        $v3 = htmlspecialchars($row['currentStock']);
        $v4 = htmlspecialchars($row['initialStock']);
        $v5 = htmlspecialchars($row['perStudent']);
        $v6 = htmlspecialchars($row['buyPrice']);
        $v8 = htmlspecialchars($row['partCode']);

        echo <<<_END
            <tr>
                <td>$v1</td>
                <td>$v2</td>
                <td>$v3</td>
                <td>$v4</td>
                <td>$v5</td>
                <td>$v6</td>
                <td>
                    <form action = 'deleteForm.php' method = 'post'>
                        <input type = 'hidden' name = 'delete' value = 'yes'>
                        <input type = 'hidden' name = 'pCode' value = '$v7'>
                        <input type = 'submit' value = 'DELETE RECORD'>
                    </form>
                </td>
            </tr>
        _END;
    }

    echo <<<_END
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><a href = "landingPage.php" style = "">Go Back</a><br></td>
                    <td><a href = "logOut.php" style = "">Log Out</a><br></td>
                </tr>
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

    function get_post($con, $var){
        return $con->real_escape_string($var);
    }
?>