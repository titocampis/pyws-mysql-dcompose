from flask import Flask
from flask import render_template
import mysql.connector
import os
import socket

# Every Flask application is an WSGI instance of the Flask class. Therefore, we need to
# create the instance called app (you can choose the name you want).
# It is needed to pass the reserved variable __name__, which will be __main__ if it is the main
# module, the one executed by the interpreter, not by another python script
app = Flask(__name__)

# Env Vars, very important to use as mysql host the name of the mysql service running in Docker Compose
MYSQL_SERVICE = os.environ['MYSQL_SERVICE']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER'] #or "root"
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
PYTHON_HOST = os.environ['PYTHON_HOST']
PYTHON_PORT = os.environ['PYTHON_PORT']

# Flask makes us transparent the path exposure. So we just need to add decorators to out methods,
# like: app.route("the_route_i_want")
@app.route("/")
def root():
    return "Welcome to the MySQL DB Tester!\n"

@app.route('/mysql')
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=MYSQL_SERVICE, database=MYSQL_DATABASE, user=MYSQL_USER, password=MYSQL_PASSWORD)
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)
    return render_template('template.html', debug="Environment Variables: MYSQL_HOST=" + (MYSQL_SERVICE or "Not Set") + "; MYSQL_DATABASE=" + (MYSQL_DATABASE  or "Not Set") + "; MYSQL_USER=" + (MYSQL_USER  or "Not Set") + "; MYSQL_PASSWORD=" + (MYSQL_PASSWORD  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color)


# When you run the file as a script by passing the file object to your Python interpreter,
# __name__ is __main, therefore the expression expression __name__ == "__main__" returns True
# so the code block under will run. Otherwise it will be False, and nothing will be executed.
if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT)