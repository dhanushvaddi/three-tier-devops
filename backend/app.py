from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend API is running"

@app.route("/db")
def db_check():
    conn = psycopg2.connect(
        host = "db",
        database = "mydb",
        user = "admin",
        password = "admin"
    )
    return "Database Connected Successfully"

app.run(host = "0.0.0.0", port = 5000)