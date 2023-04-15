from flask import Flask, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def start_page():
    return render_template("start.html", title=satisfaction_survey.title,
                            instruct=satisfaction_survey.instructions)

@app.route("/questions/<int:num>")
def show_question(num):
    session["nums"] = num
    return render_template("question.html", quest=satisfaction_survey.questions[int(num)].question,
                        op_one = satisfaction_survey.questions[int(num)].choices[0],
                        op_two = satisfaction_survey.questions[int(num)].choices[1], num=num)

@app.route("/answer", methods=["POST"])
def answer():
    answer = request.form["option"]
    num = session["nums"]
    num = num+1
    responses.append(answer) 
    if (num != len(satisfaction_survey.questions)):
        return redirect(f"/questions/{num}")
    else:
        return redirect("/thank_you")
    
@app.route("/thank_you")
def show_thanks():
    return render_template("thank_you.html")