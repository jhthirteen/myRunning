from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import psycopg2
from cleanOutput import checkIfUser, findClasses, combineInput

app = Flask(__name__)

@app.route("/")
def default():
    return redirect('/home?loginMessage=False')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/user")
def user():
    userInfo = request.args.get('inputData')

    connection = psycopg2.connect(host="localhost", database="hw_db",user="jack", password="fit32114")
    current = connection.cursor()
    current.execute('SELECT username, password FROM users')
    dbOutput = current.fetchall()
    existance = checkIfUser(dbOutput, userInfo)

    current.execute("SELECT id FROM users WHERE username='jackHunter'")
    userId = current.fetchall()

    current.execute('SELECT * FROM userClasses')
    classOutput = current.fetchall()
    listOfClasses = findClasses(classOutput, userId)

    fullData = combineInput(userInfo, listOfClasses)
    print(fullData)

    if( existance ):
        return render_template('user.html', input_data=fullData)
    else:
        return redirect('/home?loginMessage=True')


if __name__ == '__main__':
    app.run(debug=True)