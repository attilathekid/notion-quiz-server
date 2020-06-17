from app import db
from pickle import dumps, loads

# allows many to many relationship between Questions and Quizzes
questions = db.Table(
    'questions',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(256))  # will support html tags
    questions = db.relationship("Question", secondary=questions, lazy='subquery',
                                backref=db.backref('quizzes', lazy=True))

    def __repr__(self):
        return f"<Quiz: {self.id}>"

    # add questions to a quiz from a list of their ids
    def questions_from_ids(self, q_ids: list):
        try:
            for q_id in q_ids:
                q_id = int(q_id)
                q = Question.query.filter_by(id=q_id).first()
                self.questions.append(q)
            db.session.commit()
        except:
            db.session.rollback()


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128), index=True, unique=True)
    _options = db.Column(db.PickleType)  # list of options
    correct = db.Column(db.Integer)  # index of correct option

    def __init__(self, question: str, options: list, correct: int, *args, **kwargs):
        super().__init__(question=question, _options=dumps(options), correct=correct, *args, **kwargs)

    # use a getter since options are pickled
    def get_options(self):
        return loads(self._options)

    def __repr__(self):
        return f"<Question: {self.id}>"
