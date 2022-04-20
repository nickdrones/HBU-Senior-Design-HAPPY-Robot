<?php
    if(isset($_POST['submit'])){
        $dCode = get_post($con, $_POST['destinationCode']);
        $oCode = get_post($con, $_POST['originCode']);
        $rEmail = get_post($con, $_POST['rEmail']);
        $rPhone = get_post($con, $_POST['rPhone']);

        echo "<br><div style = 'text-align: center;'><h2>Destination Code: $dCode.<br>Origin Code: $oCode.<br>Recipient Email: $rEmail.<br>Recipient Phone: $rPhone.<br></h2></div>";
    }
    echo <<<_END
        <html>
            <head>
            </head>
            <body>
                <p>test</p>
            </body>
        </html>
    _END;
?>