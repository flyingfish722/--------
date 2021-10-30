from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class DataAnalysisForm(FlaskForm):
    dataList = SelectField('dataset')
    algorithm = SelectField('algorithm')
    submit = SubmitField('next')

class ParameterForm(FlaskForm):
    dataList = StringField('delta')
    algorithm = StringField('alpha')
    submit = SubmitField('submit')