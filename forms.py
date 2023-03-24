from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField


##WTForm
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), validators.Email(message="Invalid email format.")])
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=8, max=20, message="Your password must contain at least 8 characters.")
    ])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[
        DataRequired(message="You can't post an empty comment."),
        Length(max=200, message="Max length: 200 characters.")
    ])
    submit = SubmitField("Submit Comment")


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
