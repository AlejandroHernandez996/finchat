from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    joinChat = SubmitField('Join Chat')