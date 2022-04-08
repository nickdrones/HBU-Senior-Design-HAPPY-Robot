<?php // authenticate.php
    if(isset($_SESSION['firstname']))
    {
        destroySession();
        echo"<br><div class = 'center'>You have been logged out. Please <a data-transition = 'slide' href = 'http://localhost/InventoryProject/HTML/homePage.html'>click here</a> to refresh the screen.</div>";
    }
    else 
    {
        echo "<div class = 'center'>You cannot log out because you are not logged in</div>";
        die("<p><a href = 'http://localhost/InventoryProject/HTML/homePage.html'>Click here to continue</a></p>");
    }
?>