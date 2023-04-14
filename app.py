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