<?php
    require_once 'loginfo.php';

    session_start();

    if(isset($_SESSION['firstname']))
    {
        $fname = $_SESSION['firstname'];
        $lname = $_SESSION['lastname'];
        $email = $_SESSION['email'];

        echo "<br><div style = 'text-align: center;'><h2>Welcome back $fname $lname.<br>This is the Insert Form!</h2></div>";
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
    $insert  = $row['inserting'];

    if($insert != 1){
        die("User not allowed to insert");
    }

    //Check if the page is loaded because the user is adding a product
    if(isset($_POST['insert'])){
        $pCode = get_post($con, $_POST['pCode']);
        $pName = get_post($con, $_POST['pName']);
        $semester = get_post($con, $_POST['semester']);
        $cStock = get_post($con, $_POST['cStock']);
        $iStock = get_post($con, $_POST['iStock']);
        $perStudent = get_post($con, $_POST['perStudent']);
        $bPrice = get_post($con, $_POST['bPrice']);
        $query = "INSERT INTO parts (partName, semester, currentStock, initialStock, perStudent, buyPrice) VALUES ('$pName', '$semester', '$cStock', '$iStock', '$perStudent', '$bPrice')";

        $result = $con->query($query);
        echo "<br>Query: $query<br>Result: $result<br>";

        if(!result) echo "Unable to insert";
    }

    //create HTML file body
    echo <<<_END
    <html>
        <head>
            <link rel = "stylesheet" type = "text/css" href = "http://localhost/InventoryProject/CSS/table.css" media = "screen"/>
        </head>

        <body>
            <div class = "table-users">
            <div class = "header"> PART INSERT FORM </div>
            
            <table cellspacing = "0">
                <form method = "post" action = "insertForm.php">
                    <tr>
                        <td>*Part Name: </td>
                        <td><input type = "text" required name = 'pName' placeholder = 'name'></td>
                    </tr>
                    <tr>
                        <td>*Semester: </td>
                        <td><input type = "text" required name = 'semester' placeholder = 'semester'></td>
                    </tr>
                    <tr>
                        <td>*Current Stock: </td>
                        <td><input type = "text" required name = 'cStock' placeholder = 'current stock'></td>
                    </tr>
                    <tr>
                        <td>*Initial Stock: </td>
                        <td><input type = "text" required name = 'iStock' placeholder = 'initial stock'></td>
                    </tr>
                    <tr>
                        <td>*Quantity Per Student: </td>
                        <td><input type = "text" required name = 'perStudent' placeholder = 'quantity'></td>
                    </tr>
                    <tr>
                        <td>*Buy Price: </td>
                        <td><input type = "text" required name = 'bPrice' placeholder = 'buy price'></td>
                    </tr>
                    <tr>
                        <td><input type = 'hidden' name = 'insert' value = 'yes'></td>
                        <td><input type = "submit" value = "ADD PRODUCT"></td>
                    </tr>
                </form>
                <tr>
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