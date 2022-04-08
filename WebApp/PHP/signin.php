<?php
    require_once 'logininfo.php';
    $con = new mysqli($hn, $username, $password, $db);

    if($con->connect_error){
        die("Error connecting to DB". $con->connect_error);
    }

    echo <<< _END
        <div class = "table-users">
        <div class = "header"> SIGN IN </div>
        <table cellspacing = "0">
            <tr>
            </tr>
        _END;

     //create HTML body
     echo <<< _END
        <html>
            <head>
                <link rel = "stylesheet" type = "text/css" href = "table.css" media = "screen"/>
            </head>
            <body>
            <form action="form.php" method="post">
                <pre>
                    Email: <input type="text" name="email">
                    Password: <input type="text" name="password">
                    <input type="submit" value="SUBMIT">
                </pre>
            </form>
        </html>
    _END;

?>
