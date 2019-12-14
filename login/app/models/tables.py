from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


class User(UserMixin, db.Model):
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

    def check_password(self, password):
        if self.password == password:
            return True
        return False
