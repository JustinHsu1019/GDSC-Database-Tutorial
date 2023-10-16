<!-- php -S localhost:8000 -->
<?php

$host = '127.0.0.1';
$db   = 'ctf_challenge';
$user = 'YOUR_MYSQL_USERNAME';
$pass = 'YOUR_MYSQL_PASSWORD';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$opt = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];
$pdo = new PDO($dsn, $user, $pass, $opt);

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    $stmt = $pdo->query("SELECT * FROM users WHERE username='$username' AND password='$password'");

    if ($user = $stmt->fetch()) {
        $flag_stmt = $pdo->query("SELECT * FROM flags");
        $flag = $flag_stmt->fetch();
        $message = "Welcome, " . $user['username'] . "! Here's your flag: " . $flag['flag_content'];
    } else {
        $message = "Incorrect credentials.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>SQL Injection</title>
</head>
<body>
    <h1>Login</h1>
    <form action="" method="post">
        Username: <input type="text" name="username">
        Password: <input type="password" name="password">
        <input type="submit" value="Login">
    </form>
    <p><?php echo $message; ?></p>
</body>
</html>
