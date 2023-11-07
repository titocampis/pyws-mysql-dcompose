import mysql.connector
import os
 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!\n"

@app.route('/mysql')
def testConnection():
    # Very important to use as mysql host the name of the mysql service running in Docker Compose
    mydb = mysql.connector.connect(host = "mysql-db", user = os.environ['MYSQL_USER'], password = os.environ['MYSQL_PASSWORD'])
    return str(mydb)+"\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)