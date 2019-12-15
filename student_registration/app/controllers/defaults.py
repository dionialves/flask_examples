from flask import render_template, flash, redirect

from app import app, db
from app.models.forms import StudentForm

from app.models.tables import Student


@app.route('/')
def index():
    students = Student.query.filter_by().all()
    return render_template('index.html', students=students)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = StudentForm()
    if form.validate_on_submit():
        studant = Student(
            form.name.data,
            form.email.data,
            form.email.data
        )
        db.session.add(studant)
        db.session.commit()
        flash("Student successfully registered.")
        return redirect('register')
    return render_template('register.html', form=form)
