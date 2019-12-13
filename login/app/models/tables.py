from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    remember_me = db.Column(db.Boolean)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User %r" % self.email
