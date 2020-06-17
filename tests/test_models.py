import unittest
from app import models, db


class IsItBreathing(unittest.TestCase):
    def test_questions(self):
        question = models.Question(
            question='What is the answer to life?',
            options=['sex', 'god', '42'],
            correct=2
        )
        db.session.add(question)
        db.session.commit()

        self.assertIsNotNone(question.id)
        db.session.delete(question)
        db.session.commit()

    def test_quiz(self):
        quiz = models.Quiz(
            name='Test quiz',
            description='foo'
        )
        quiz.questions_from_ids(
            [models.Question.query.first().id]
        )
        db.session.add(quiz)
        db.session.commit()

        self.assertIsNotNone(quiz.id)
        db.session.delete(quiz)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
