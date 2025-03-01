<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="/submit" method="POST">
        <!-- Name Field -->
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <!-- Email Field -->
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <!-- Message Field -->
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>
        
        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>
</body>
</html>
