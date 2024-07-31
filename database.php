//Creating database and tables, inserting details and editing the tables 

-- Create a new database
CREATE DATABASE mydatabase;

-- Select the database
USE mydatabase;

-- Create a new table for storing user information
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password CHAR(64) NOT NULL, -- SHA-256 hash is 64 characters long
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
//Encrypting the sensitive passwords in the database using SHA-2
-- Insert a new user with a SHA-256 hashed password
INSERT INTO users (username, password) VALUES 
('user1', SHA2('password123', 256)),
('user2', SHA2('mypassword', 256));


//Using php to insert the users in the tables and hashing the passwords

<?php
$servername = "localhost";
$username = "root";
$password = ""; // default XAMPP MySQL password is empty
$dbname = "mydatabase";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to insert a user with encrypted password
function insertUser($conn, $username, $plainPassword) {
    $hashedPassword = hash('sha256', $plainPassword); // Encrypt password using SHA-256
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);
    $stmt->execute();
    $stmt->close();
}

// Example usage
insertUser($conn, 'user3', 'securepassword');

// Close connection
$conn->close();
?>

//Verification of the passwords using php

<?php
$servername = "localhost";
$username = "root";
$password = ""; // default XAMPP MySQL password is empty
$dbname = "mydatabase";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to verify user login
function verifyUser($conn, $username, $plainPassword) {
    $hashedPassword = hash('sha256', $plainPassword); // Encrypt entered password using SHA-256
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $username, $hashedPassword);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
    
    $stmt->close();
}

// Example usage
verifyUser($conn, 'user3', 'securepassword');

// Close connection
$conn->close();
?>



