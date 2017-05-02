from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms import validators

class FormText(Form):
    text = TextAreaField('text', validators=[validators.Required(), validators.Length(min=1,max=100)])
 
