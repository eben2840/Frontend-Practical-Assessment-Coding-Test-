from wtforms import DateField, Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
# from app import Person


class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=10, message="Your number shouldn't be less than 10")])
    email = StringField('email',validators=[(DataRequired() )])
    faculty = SelectField('faculty',  choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    hallofresidence = SelectField('hallofresidence',  choices=[('Halls','Halls'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Adduser(FlaskForm):
    product_name = StringField('product_name', validators=[(DataRequired())])
    cat= SelectField('tag', choices=[('Tag','Tag'),('1', '1'), ('2','2'), ('3','3') ], default=None )
    desc=  StringField('desc', validators=[(DataRequired())])
    variant= StringField('variant', validators=[(DataRequired())])
    price = StringField('price', validators=[(DataRequired())])
    size = StringField('size', validators=[(DataRequired())])
    image_file = StringField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
    

    
class LogForm(FlaskForm):
    tag = SelectField('tag', choices=[('Tag','Tag'),('High', 'High'), ('Medium','Medium'), ('Low','Low') ], default=None )
    activity = StringField('activity')
    implementation = StringField('implementation')
    email = StringField('Email', validators=[DataRequired()])
    challenges = StringField('challenges')
    future = StringField('future')
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Send')
    


    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    

 