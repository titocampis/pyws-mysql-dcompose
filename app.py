from flask import Flask, redirect, url_for, render_template, request
import mysql.connector
import os
import socket

# Every Flask application is an WSGI instance of the Flask class. Therefore, we need to
# create the instance called app (you can choose the name you want).
# It is needed to pass the reserved variable __name__, which will be __main__ if it is the main
# module, the one executed by the interpreter, not by another python script
app = Flask(__name__)

# Env Vars
MYSQL_SERVICE = os.environ['MYSQL_SERVICE']
MYSQL_DATABASE = os.environ['MYSQL_DATABASE']
MYSQL_USER = os.environ['MYSQL_USER'] #or "root"
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
PYTHON_HOST = os.environ['PYTHON_HOST']
PYTHON_PORT = os.environ['PYTHON_PORT']

GREEN='#39b54b'
RED='#ff3f3f'

# Flask makes us transparent the path exposure. So we just need to add decorators to out methods,
# like: app.route("the_route_i_want")
@app.route("/")
def main():
    return "Welcome to the MySQL DB Tester!\n"

# Al definir una URL acabada con el carácter '/', si el usuario accede a esa URL sin dicho
# carácter, Flask lo redirigirá a la URL acabada en '/'. En cambio, si la URL se define sin
# acabar en '/' y el usuario accede indicando la '/' al final, Flask dará un error HTTP 404.
@app.route('/check/<string:db_name>/')
def check_db(db_name=None):
    db_connect_result = False
    err_message = ""
    try:
        # Very important to use as mysql host the name of the mysql service running in Docker Compose
        mysql.connector.connect(host=MYSQL_SERVICE, database=db_name, user=MYSQL_USER, password=MYSQL_PASSWORD)
        color = GREEN
        db_connect_result = True
    except Exception as e:
        color = RED
        err_message = str(e)
    return render_template('template.html', debug="Environment Variables: MYSQL_HOST=" + (MYSQL_SERVICE or "Not Set") + "; MYSQL_DATABASE=" + (db_name  or "Not Set") + "; MYSQL_USER=" + (MYSQL_USER  or "Not Set") + "; MYSQL_PASSWORD=" + (MYSQL_PASSWORD  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color)

# When you run the file as a script by passing the file object to your Python interpreter,
# __name__ is __main, therefore the expression expression __name__ == "__main__" returns True
# so the code block under will run. Otherwise it will be False, and nothing will be executed.
if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT)