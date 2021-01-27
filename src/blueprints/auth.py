from flask import Blueprint, redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash

from database import db
from forms.SignupForm import SignupForm
from forms.SigninForm import SigninForm
from models.Users import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth/')


@auth_bp.route('/', methods=['GET'])
def index():
	return redirect(url_for('auth.sign_in'))


@auth_bp.route('/signin', methods=['GET', 'POST'])
def sign_in():
	form = SigninForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# サインインの処理
			print(form.email.data, form.password.data)
			email = form.email.data
			password = form.password.data

			# emailが登録済みかどうかチェック！
			if not db.session.query(User).filter(User.email == email).first():
				return render_template('signup.html', form=form, title='ログイン', endpoints='auth.sign_in')

			user = db.session.query(User).filter(User.email == email).first()

			# パスワードのチェック！
			if not user.password == password:
				return render_template('signup.html', form=form, title='ログイン', endpoints='auth.sign_in')

			return redirect(url_for('home.home'))
		else:
			print('Invalid input', form.email.errors, form.password.errors, form.submit.errors)
	return render_template('signup.html', form=form, title='ログイン', endpoints='auth.sign_in')


@auth_bp.route('/register', methods=['GET', 'POST'])
def sign_up():
	form = SignupForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# サインアップの処理
			print(form.email.data, form.password.data)
			email = form.email.data
			password = form.password.data
			hashed_password = generate_password_hash(password)  # パスワードのハッシュ化

			# すでにemailが登録されている時は、DBに保存されない
			if db.session.query(User).filter(User.email == email).first():
				return render_template('signup.html', form=form, title='会員登録', endpoints='auth.sign_up')

			# 新規にユーザーを追加する
			new_user = User(email=email, password=hashed_password)
			db.session.add(new_user)
			db.session.commit()

			return redirect(url_for('home.home'))
		else:
			print('Invalid input', form.email.errors, form.password.errors, form.submit.errors)
	return render_template('signup.html', form=form, title='会員登録', endpoints='auth.sign_up')
