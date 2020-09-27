from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User


class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    confirm_password = PasswordField('Confrim Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    cancel = SubmitField('Cancel')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose another one!')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist. Please choose another one!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    cancel = SubmitField('Cancel')