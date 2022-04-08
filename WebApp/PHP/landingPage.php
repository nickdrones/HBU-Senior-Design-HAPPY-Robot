<?php // authenticate.php
    require_once 'loginfo.php';
    $con = new mysqli($hn, $username, $password, $db);

    if($con->connect_error){
        die("Error connecting to DB". $con->connect_error);
    }

    session_start();
    if(isset($_SESSION['firstname']))
    {
        $fname = $_SESSION['firstname'];
        $lname = $_SESSION['lastname'];
        $email = $_SESSION['email'];
    }

    echo <<< _END
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="http://localhost/InventoryProject/CSS/inventory.css" media="screen"/>
    </head>
    <style>
        .bgimg {
        background-image: url('http://localhost/InventoryProject/images/squirrel.jpg');
        min-height: 100%;
        background-position: center;
        background-size: cover;
        }
    </style>
    <body>
        <div class = "bgimg">
        <div class = "wrapper fadeInDown">
            <div id = "formContent">
                <h2 class="active"> Landing Page </h2>
                <div class="fadeIn first">
                <img src="http://localhost/InventoryProject/images/smile.jpg" id="icon" alt="Squirrel Icon" />
                </div>
                <div id = "login" class = "fadeIn second">
                    <p><br>Hello! <b>$fname $lname</b> Welcome to the Landing Page.<br>Please select what action you would like to do.</p>
                </div>
                <div id="formFooter" class = "fadeIn third">
    _END;

    $query   = "SELECT * FROM users WHERE email='$email'";
    $result  = $con->query($query);

    if ($result->num_rows != 1) die("User not found");

    $row = $result->fetch_array(MYSQLI_ASSOC);
    $pn  = $row['permissionNumber'];

    $query   = "SELECT * FROM permissions WHERE permissionNumber='$pn'";
    $result  = $con->query($query);

    $row = $result->fetch_array(MYSQLI_ASSOC);
    $read  = $row['reading'];
    $insert  = $row['inserting'];
    $delete  = $row['deleting'];
    $update  = $row['updating'];

    if($read == 1){
        echo "<a class = 'underlineHover' href = 'readForm.php'>READ</a><br>";
    }
    
    if($insert == 1){
        echo "<a class = 'underlineHover' href = 'insertForm.php'>INSERT</a><br>";
    }

    if($delete == 1){
        echo "<a class = 'underlineHover' href = 'deleteForm.php'>DELETE</a><br>";
    }

    if($update == 1){
        echo "<a class = 'underlineHover' href = 'updateForm.php'>UPDATE</a><br>";
    }

    if($pn == 8){
        echo "<a class = 'underlineHover' href = 'permissionForm.php'>PERMISSIONS</a><br>";
    }

    echo <<< _END
                    <a class = "underlineHover" href = "logOut.php" style = "">Log Out</a><br>
                </div>
            </div>
        </div>
        </div>
    </body>
</html>
_END;
?>