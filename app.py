from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        q = request.args['q']
        o = request.args['o']
        c = request.args['c']
        return redirect(f"/quiz?q={q}&o={o}&c={c}")
    except KeyError:
        return render_template('index.html')


@app.route('/quiz')
def quiz():
    try:
        q = request.args['q']
        o = request.args['o'].split(";")
        c = o[int(request.args['c'])]
        return render_template("quiz.html", question=q, options=o, correct=c)
    except KeyError:
        return redirect("/")
