from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/user")
def user():
    inputName = request.args.get('inputData')
    return render_template('user.html', input_data=inputName)

@app.route("/workouts")
def workouts():
    return "workouts page in progress"

@app.route("/trainingplans")
def trainingplans():
    return "training plans page in progress"

if __name__ == '__main__':
    app.run(debug=True)