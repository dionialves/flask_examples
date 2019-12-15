from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
