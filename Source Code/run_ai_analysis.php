<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: login.html");
    exit();
}

// Run the Python AI analysis script
$output = [];
$return_var = 0;
exec("python3 ai_analysis.py", $output, $return_var);

if ($return_var === 0) {
    echo "AI analysis completed successfully!";
    echo "<pre>" . implode("\n", $output) . "</pre>";
} else {
    echo "Error running AI analysis. Check server configuration.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Run AI Analysis</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <h1>Run AI Analysis</h1>
        <a href="dashboard.php">Back to Dashboard</a>
    </div>
</body>
</html>
