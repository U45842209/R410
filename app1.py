from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "172.17.0.2"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "foo"
app.config["MYSQL_DB"] = "flask"

mysql = MySQL(app)

@app.route("/")
def home():
    return "Hello"

@app.route("/test")
def test():
    return "Test"

@app.route("/render")
def render():
    return render_template('forms.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return "Login via the login Form"
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        cursor = mysql.connection.cursor()
        cursor.execute("""INSERT INTO info_table VALUES(%s,%s)""", (name, age))
        mysql.connection.commit()
        cursor.close()
        return "Done!!"

if __name__ == "__main__":
    app.run()
