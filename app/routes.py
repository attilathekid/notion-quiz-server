from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.models import User, Quiz
from app.forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


@app.route('/embed_quiz', methods=['GET', 'POST'])
def embed_quiz():
    quiz = Quiz.query.filter_by(id=int(request.args['id'])).first()
    if quiz is None:
        return "Quiz not found"
    else:
        return render_template('embed_quiz.html', quiz=quiz)


@app.route('/quiz_designer')
@login_required
def quiz_designer():
    try:
        q = request.args['q']
        o = request.args['o']
        c = request.args['c']
        return redirect(f"/make_quiz?q={q}&o={o}&c={c}")
    except KeyError:
        return render_template('quiz_designer.html')


@app.route('/make_quiz')
def make_quiz():
    try:
        q = request.args['q']
        o = request.args['o'].split(";")
        c = o[int(request.args['c'])]
        return render_template("quiz.html", question=q, options=o, correct=c)
    except KeyError:  # i.e., they want the page,
        return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            flash({'message': 'Invalid username or password', 'class': 'bg-danger text-danger'})
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
