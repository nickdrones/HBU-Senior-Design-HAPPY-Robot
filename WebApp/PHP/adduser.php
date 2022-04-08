<?php

    //Start with the PHP code

    $forename = $surname = $username = $password = $age = $email = "";

    if(isset($_POST['forename']))
        $forename = fix_string($_POST['forename']);

    if(isset($_POST['surname']))
        $surname = fix_string($_POST['surname']);

    if(isset($_POST['username']))
        $username = fix_string($_POST['username']);

    if(isset($_POST['password']))
        $password = fix_string($_POST['password']);

    if(isset($_POST['age']))
        $age = fix_string($_POST['age']);

    if(isset($_POST['email']))
        $email = fix_string($_POST['email']);

    $fail = validate_forename($forename);
    $fail += validate_surname($surname);
    $fail += validate_username($username);
    $fail += validate_password($password);
    $fail += validate_age($age);
    $fail += validate_email($email);

?>