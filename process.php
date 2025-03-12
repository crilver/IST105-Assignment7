<?php
    $a = escapeshellarg($_GET['a']);
    $b = escapeshellarg($_GET['b']);
    $command = escapeshellcmd("python3 bitwise_operations.py $a $b");
    $output = shell_exec($command);

    echo "<h1>Assignment 7:</h1>";
    echo "<h2>Python Script Result</h2>";
    echo "<div>$output</div>";
?>