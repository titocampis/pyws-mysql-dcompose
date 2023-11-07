from flask import Flask
from flask import render_template
import mysql.connector
import os
import socket

app = Flask(__name__)

# Env Vars, very important to use as mysql host the name of the mysql service running in Docker Compose
MYSQL_HOST = "mysql-db"
MYSQL_DATABASE = os.environ['MYSQL_DATABASE'] or "mysql"
MYSQL_USER = os.environ['MYSQL_USER'] or "root"
#MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD'] or "paswrd"
MYSQL_PASSWORD = 'incorrecta'

@app.route("/")
def root():
    return "Welcome to the MySQL DB Tester!\n"

@app.route('/mysql')
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=MYSQL_HOST, database=MYSQL_DATABASE, user=MYSQL_USER, password=MYSQL_PASSWORD)
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)
    return render_template('template.html', debug="Environment Variables: MYSQL_HOST=" + (MYSQL_HOST or "Not Set") + "; MYSQL_DATABASE=" + (MYSQL_DATABASE  or "Not Set") + "; MYSQL_USER=" + (MYSQL_USER  or "Not Set") + "; MYSQL_PASSWORD=" + (MYSQL_PASSWORD  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)