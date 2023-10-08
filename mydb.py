import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "#1Mayobelwa"
)

# Prepare a curser object
curserObject = dataBase.cursor()

# Create a database
curserObject.execute("CREATE DATABASE QuizAdmin")

print("All Done!")

dataBase.close()