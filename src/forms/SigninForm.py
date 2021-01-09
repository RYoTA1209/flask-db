from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField


class SigninForm(FlaskForm):
	email = EmailField('メールアドレス', validators=[validators.DataRequired(), validators.Email()])
	password = PasswordField('パスワード', validators=[validators.DataRequired(), validators.Length(max=50, message='５０文字以内で入力してください')])
	submit = SubmitField('ログイン')