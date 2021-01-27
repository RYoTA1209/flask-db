import uuid

from flask import Blueprint, redirect, url_for, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from forms.SignupForm import SignupForm
from forms.SigninForm import SigninForm
from models.Logins import Login
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
			if not check_password_hash(user.password, password):
				return render_template('signup.html', form=form, title='ログイン', endpoints='auth.sign_in')

			# ログインしたという情報をDBに保存
			login_session = Login(user_id=user.id, token=uuid.uuid4().hex)
			db.session.add(login_session)
			db.session.commit()

			# tokenをsessionに保存
			session['token'] = login_session.token

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

			# ログインしたという情報をDBに保存
			login_session = Login(user_id=new_user.id, token=uuid.uuid4().hex)
			db.session.add(login_session)
			db.session.commit()

			# tokenをsessionに保存
			session['token'] = login_session.token

			return redirect(url_for('home.home'))
		else:
			print('Invalid input', form.email.errors, form.password.errors, form.submit.errors)
	return render_template('signup.html', form=form, title='会員登録', endpoints='auth.sign_up')

@auth_bp.route('signout')
def sign_out():
	if 'token' in session:
		session.pop('token', None)

	return redirect(url_for('home.home'))


@auth_bp.route('/mypage')
def mypage():
	# sessionにtokenを持っているとき
	if 'token' in session:
		token = session['token']
		login = db.session.query(Login).filter(Login.token == token).first()
		# idからUserを探す
		user = db.session.query(User).filter(User.id == login.user_id).first()

		return render_template('account.html', user=user)
	else:
		# sessionにtokenを持っていなかったらログイン画面にリダイレクト
		return redirect(url_for('auth.sign_in'))
