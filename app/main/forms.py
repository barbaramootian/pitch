from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,EmailField,BooleanField,SelectField,TextAreaField

from wtforms.validators import input_required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

choices=['pickup','interview','product','promotion']

class PitchForm(FlaskForm):
    title=StringField("Pitch Title",validators=[input_required(message='Title required')],render_kw={"placeholder":"Pitch Title"})
    category=SelectField("Pitch Category",choices=choices,validate_choice=True)
    content=StringField("Pitch body",validators=[input_required(message='body required')],render_kw={"placeholder":"Pitch body"})
    submit=SubmitField("POST PITCH")

class CommentForm():
     comment=TextAreaField("Pitch comment",validators=[input_required(message='body required')],render_kw={"placeholder":"Pitch comment"}) 
     submit=SubmitField("Comment")