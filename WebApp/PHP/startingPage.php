<?php
    echo <<< _END
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="http://localhost/InventoryProject/CSS/inventory.css" media="screen"/>
    </head>
    
    <body>
    
    <div class="wrapper fadeInDown">
      <div id="formContent">
        <!-- Tabs Titles -->
        <h2 class="active"> Landing Page </a> </h2>
    
        <!-- Icon -->
        <div class="fadeIn first">
        <img src="http://localhost/InventoryManagement/images/squirrel.jpg" id="icon" alt="squirrel" />
        </div>
    
        <!-- Login Form -->
        <div id="login">  
          <form action="login.php" method ="post">
              <input type="submit" class="fadeIn fourth" value="Log In">
          </form>
          <form action="register.php" method ="post">
              <input type="submit" class="fadeIn fourth" value="Register">
          </form>
        </div>
    
        <!-- Sign Up Form -->
    
      </div>
    </div>
    
    </body>
    </html>
    _END;
?>
