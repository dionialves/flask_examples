from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user

from app.models.forms import LoginForm
from app.models.tables import User
from app import login_manager


@app.route('/')
@login_required
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        print(form.email.data)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
