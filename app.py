from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

responses = []
@app.route("/")
def start_page():
    return render_template("start.html", title=satisfaction_survey.title,
                            instruct=satisfaction_survey.instructions)

@app.route("/questions/<num>")
def show_question(num):
    return render_template("question.html", quest=satisfaction_survey.questions[int(num)].question,
                        op_one = satisfaction_survey.questions[int(num)].choices[0],
                        op_two = satisfaction_survey.questions[int(num)].choices[1])