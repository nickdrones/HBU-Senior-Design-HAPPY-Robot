<?php
    require_once 'loginfo.php';

    session_start();

    if(isset($_SESSION['firstname']))
    {
        $fname = $_SESSION['firstname'];
        $lname = $_SESSION['lastname'];

        echo "Welcome back $fname $lname.<br>This is the part display page!<br>";
    }

    $con = new mysqli($hn, $username, $password, $db);
    
    //check connection to database
    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

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
            <div class = "header"> Parts </div>
            <table cellspacing = "0">
                <tr>
                    <td> Part Name </td>
                    <td> Semester </td>
                    <td> Current Stock </td>
                    <td> Initial Stock </td>
                    <td> Quantity Per Student </td>
                    <td> Buy Price </td>
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
            </tr>
        _END;
    }

    echo <<<_END
                <tr>
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

    function get_post($con, $var){
        return $con->real_escape_string($var);
    }
?>