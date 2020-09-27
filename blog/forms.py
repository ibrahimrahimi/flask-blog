from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    confirm_password = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    cancel = SubmitField('Cancel')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    cancel = SubmitField('Cancel')