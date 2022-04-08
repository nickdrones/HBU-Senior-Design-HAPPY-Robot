<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);

    if($con->connect_error){
        die("Error connecting to DB". $con->connect_error);
    }

        $partName = $_POST['partName'];
        $semester = $_POST['semester'];
        $currentStock = $_POST['currentStock'];
        $initialStock = $_POST['initialStock'];
        $quantity = $_POST['quantity'];
        $buyPrice = $_POST['buyPrice'];

        $query = "INSERT INTO parts (partName, semester, currentStock, initialStock, quantity, buyPrice) VALUES ('$partName', '$semester', '$currentStock', '$initialStock', '$quantity', '$buyPrice')";
        $result = $con->query($query);
        
        if(!result) echo "Insertion Failed";

     //create table
     $query = "SELECT * FROM parts";
     $result = $con->query($query);
     if(!$result)
         die("Error executing the query.");
     $rows = $result->num_rows;
 
     echo <<< _END
        <div class = "table-users">
        <div class = "header"> Item Addition </div>
        _END;

        
        //create HTML body
        echo <<< _END

        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "table.css" media = "screen"/>
            </head>
            <body>
            <form action="addPart.php" method="post">
                <pre>
                    Part Name: <input type="text" name="Part Name">

                    Semester: <input type="text" name="semester">

                    Current Stock: <input type="text" name="currentStock">

                    Initial Stock: <input type="text" name="initialStock">

                    Quantity Per Student: <input type="text" name="quantity">

                    Buy Price: <input type="text" name="buyPrice">

                    <input type="submit" value="Submit Item Info">
                </pre>
            </form>
    _END;


    echo <<< _END
    </table>
    </body>
    </html>
 _END;

 function get_post($con, $var){
    return $con->real_escape_string($var);
 }

 $result->close();
 $con->close();
 ?>
