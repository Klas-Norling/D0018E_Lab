<?php
    $servername = "utbweb.its.ltu.se";
    $username = "19990730";
    $password = "19990730";
    $dbname = "db19990730";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }

?> 