from app import db

questions = db.Table(
    'questions',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questions = db.relationship("Question", secondary=questions, lazy='subquery',
                                backref=db.backref('quizzes', lazy=True))

    def __repr__(self):
        return f"<Quiz: {id}>"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128), index=True, unique=True)
    options = db.Column(db.PickleType)
    correct = db.Column(db.Integer)

    def __repr__(self):
        return f"<Question: {id}>"
