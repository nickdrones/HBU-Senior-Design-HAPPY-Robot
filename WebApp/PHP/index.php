<?php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);

    if($con -> connect_error)
        die("Error connecting to DB" . $con -> connect_error);

    echo "<p>Connection Successful</p>";
    
    $query = "SELECT * FROM parts";
    $result = $con -> query($query);
    if(!$result)
        die("Error executing the query");

    $rows = $result -> num_rows;
    for ($j = 0; $j < $rows; $j++)
    {
        $row = $result -> fetch_array(MYSQLI_NUM);
        echo 'Part Name: ' . htmlspecialchars($row[1]) . '<br>';
        echo 'Description: ' . htmlspecialchars($row[3]) . '<br>';
        echo '<br>';
    }

    $result -> close();
    $con -> close();
?>