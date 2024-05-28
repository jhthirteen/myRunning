from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import psycopg2
from cleanOutput import checkIfUser

app = Flask(__name__)

@app.route("/")
def default():
    return redirect('/home')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/user")
def user():
    inputName = request.args.get('inputData')

    connection = psycopg2.connect(host="localhost", database="hw_db",user="jack", password="fit32114")
    current = connection.cursor()
    current.execute('SELECT username, password FROM users')
    dbOutput = current.fetchall()
    existance = checkIfUser(dbOutput, inputName)

    if( existance ):
        return render_template('user.html', input_data=escape(inputName))
    else:
        return redirect('/home')


if __name__ == '__main__':
    app.run(debug=True)