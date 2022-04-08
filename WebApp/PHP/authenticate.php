<?php // authenticate.php
  require_once 'loginfo.php';
  $con = new mysqli($hn, $username, $password, $db);

  if($con->connect_error){
      die("Error connecting to DB". $con->connect_error);
  }

  if(!empty($_POST['email']) && !empty($_POST['password']))
  {
    $em_temp = sanitizeMySQL($con, $_POST['email']);   //note the login needs to be sanitized first .. very important
    $pw_temp = sanitizeMySQL($con, $_POST['password']);
 
    $query   = "SELECT * FROM users WHERE email='$em_temp'";
    $result  = $con->query($query);

    if ($result->num_rows != 1) die("User not found");
    
    $row = $result->fetch_array(MYSQLI_ASSOC);
    $fn  = $row['FirstName'];
    $ln  = $row['LastName'];
    $em  = $row['email'];
    $pw  = $row['password'];
      
    if (password_verify(str_replace("'", "", $pw_temp), $pw))
    {
      session_start();

      $_SESSION['firstname'] = $fn;
      $_SESSION['lastname'] = $ln;
      $_SESSION['email'] = $em;
      
      header('Location: landingPage.php');
    }
      
    else die("Invalid username/password combination");
  }

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
?>
