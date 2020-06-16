from flask import render_template, request, redirect
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        q = request.args['q']
        o = request.args['o']
        c = request.args['c']
        return redirect(f"/make_quiz?q={q}&o={o}&c={c}")
    except KeyError:
        return render_template('index.html')


@app.route('/make_quiz')
def make_quiz():
    try:
        q = request.args['q']
        o = request.args['o'].split(";")
        c = o[int(request.args['c'])]
        return render_template("quiz.html", question=q, options=o, correct=c)
    except KeyError:
        return redirect("/")
