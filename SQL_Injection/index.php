<!-- mysql -h 127.0.0.1 -u YOUR_MYSQL_USERNAME -p -->
<!-- 
ALTER USER 'YOUR_MYSQL_USERNAME'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'YOUR_MYSQL_PASSWORD';
FLUSH PRIVILEGES;
-->
<!-- php -S 0.0.0.0:8000 -->
<?php

$host = '127.0.0.1';
$db = 'ctf_challenge';
$user = 'YOUR_MYSQL_USERNAME';
$pass = 'YOUR_MYSQL_PASSWORD';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$opt = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
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
    <link rel="stylesheet" href="css/styles.css">
</head>

<body>
    <div class="system_name">
        <h2>登入系統</h2>
    </div>

    <div class="login_page">
        <div id="container1">

            <div class="login">
                <h3>登入 Login</h3>
                <form action="" method="post">
                    <input type="text" id="username" name="username" placeholder="帳號" required>
                    <div class="tab"></div>
                    <input type="password" id="password" name="password" placeholder="密碼" required>
                    <div class="tab"></div>
                    <input type="submit" value="登入" class="submit">
                </form>
                <p>
                    <?php echo $message; ?>
                </p>
            </div>
        </div>
    </div>

    <div id="copyright">
        <h4>Copyright</h4>
        <!-- h4>Copyright © 2018 RoseWang All rights reserved</h4 -->
        <!-- 原始位置: https://codepen.io/rosewang0303/pen/mXrEwQ -->
    </div>
</body>

</html>
