<?php
echo <<< _END
<html>
<head>
    <link rel="stylesheet" type="text/css" href="inventory.css" media="screen"/>
</head>

<body>

<div class="wrapper fadeInDown">
  <div id="formContent">
    <!-- Tabs Titles -->
    <h2 class="active"> Log In </a> </h2>

    <!-- Icon -->
    <div class="fadeIn first">
      <img src="http://localhost/InventoryManagement/images/squirrel.jpg" id="icon" alt="Mask Icon" />
    </div>

    <!-- Login Form -->
    <div id="login">  
      <form action="authenticate.php" method ="post">
          <input type="text" id="login" class="fadeIn second" name="login" placeholder="username*" required autocomplete="off">
          <input type="password" id="password" class="fadeIn third" name="pswd" placeholder="password*" required autocomplete="off">
          <input type="submit" class="fadeIn fourth" value="Log In">
      </form>
    </div>

    <!-- Sign Up Form -->
  
    <!-- Remind Password -->
    <div id="formFooter">
      <a class="underlineHover" href="#">Forgot Password?</a>
      <a class="underlineHover" href="register.php">Register?</a>
    </div>
  </div>
</div>

</body>
</html>
_END;
?>