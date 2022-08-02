from flask import Flask, render_template,Request,redirect, request,url_for,session
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.secret_key = "12345"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root" 
app.config["MYSQL_PASSWORD"] = "faranu1419IUNC"
app.config["MYSQL_DB"] = "login"
db = MySQL(app)

@app.route("/", methods=['GET','POST'])
def registration():
    if request.method =="POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form["one"]
            email = request.form["two"]
            password = request.form["three"]
            cur = db.connection.cursor(MySQL.cursors.DictCursor)
            cur.execute("INSERT INTO login.logininfo(name,email,password)VALUE(%s,%s,%s)",(username,email,password))
            db.connection.commit()
            
            return redirect(url_for('\profile'))

    return render_template("create.html")

@app.route("/profile")
def profile():
    return render_template("profile.hmtl")

if __name__ == "__main__":
   app.run(debug=True)
