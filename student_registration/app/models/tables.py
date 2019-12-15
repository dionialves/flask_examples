from app import db


class Student(db.Model):
    __tablename__ = 'studens'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    course = db.Column(db.String)

    def __init__(self, name, email, course):
        self.name = name
        self.email = email
        self.course = course

    def __repr__(self):
        return "Student %r" % self.name
