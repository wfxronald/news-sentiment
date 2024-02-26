from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(Form):
    search_key = StringField("Search Term",validators=[DataRequired()])
    submit = SubmitField("Submit")
