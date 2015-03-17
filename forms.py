from flask_wtf import Form
from wtforms import StringField, PasswordField, DateField, RadioField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User, Place

def name_exists(form, field):
    if User.objects(username = field.data):
        raise ValidationError('User with that name already exists!')

def email_exists(form, field):
    if User.objects(email = field.data):
        raise ValidationError('User with that email already exists!')

def place_exists(form, field):
    if Place.objects(name = field.data):
        raise ValidationError('Place with that name already exists!')

def email_place_exists(form, field):
    if Place.objects(email = field.data):
        raise ValidationError('Place with that email already exists!')

class RegisterFormUser(Form):
    username = StringField(
        'Username',
        validators =[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message = ("Username should be one world, letters,"
                            "numbers, and underscores only.")
                ),
            name_exists
        ])
    bday = StringField(
        'Date of Birth',
        validators = [DataRequired()]
        )
    genre = StringField(
        'Genre',
        validators = [DataRequired()]
        )
    address = StringField(
        'Address',
        validators = [DataRequired()]
        )
    city = StringField(
        'City',
        validators = [DataRequired()]
        )
    state = StringField(
        'State',
        validators = [DataRequired()]
        )
    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email(),
            email_exists
        ])
    password = PasswordField(
        'Password',
        validators = [
            DataRequired(),
            Length(min=4),
            EqualTo('confirm_password', message="Passwords must be equals!")

        ])
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [DataRequired()]
        )

class RegisterFormPlace(Form):
    name = StringField(
        'Name',
        validators =[
            DataRequired(),
            place_exists
        ])
    address = StringField(
        'Address',
        validators = [DataRequired()]
        )
    city = StringField(
        'City',
        validators = [DataRequired()]
        )
    state = StringField(
        'State',
        validators = [DataRequired()]
        )
    sport = StringField(
        'Sport',
        validators = [DataRequired()]
        )
    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email(),
            email_place_exists
        ])
    password = PasswordField(
        'Password',
        validators = [
            DataRequired(),
            Length(min=4),
            EqualTo('confirm_password', message="Passwords must be equals!")

        ])
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [DataRequired()]
        )


class LoginForm(Form):
  login_type = RadioField('Type', choices=[('user', 'User'), ('place', 'Place')])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])

