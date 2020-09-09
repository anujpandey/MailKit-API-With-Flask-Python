from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskott.models import User
#from flaskott.forms import EmailForm

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class EmailForm(FlaskForm):
    #global client_id
    client_id = StringField('Client_ID',
                        validators=[DataRequired()])
    client_md5 = StringField('Client_MD5',
                        validators=[DataRequired()])
    ID_Message = StringField('ID_Message',
                        validators=[DataRequired()])
    submit = SubmitField('Campaign List')

class Create_mailkit_campaigns(FlaskForm):
    #global client_id
    client_id = StringField('Client_ID',
                        validators=[DataRequired()])
    client_md5 = StringField('Client_MD5',
                        validators=[DataRequired()])
    name_of_campaign = StringField('Name of Campaign',
                        validators=[DataRequired()])
    subject_of_campaign = StringField('Subject of Campaign',
                        validators=[DataRequired()])
    type_message = StringField('Type of message',
                        validators=[DataRequired()])
    submit = SubmitField('Create Campaign List')


class SendEmailMail_Form(FlaskForm):
    #global client_id
    client_id = StringField('Client_ID',
                        validators=[DataRequired()])
    client_md5 = StringField('Client_MD5',
                        validators=[DataRequired()])
    campaign_ID = StringField('Campaign ID',
                        validators=[DataRequired()])
    Send_to = StringField('Email',
                        validators=[DataRequired(), Email()])
    subject = StringField('Subject',
                        validators=[DataRequired()])
    content = StringField('Body',
                        validators=[DataRequired()])
    submit = SubmitField('Send Email List')
