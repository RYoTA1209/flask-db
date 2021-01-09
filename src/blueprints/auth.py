from flask import Blueprint, redirect, url_for, render_template, request

from forms.SignupForm import SignupForm
from forms.SigninForm import SigninForm
from models import User
from app import db

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
			return redirect(url_for('home.home'))
		else:
			print('Invalid input', form.email.errors, form.password.errors, form.submit.errors)
	return render_template('signup.html', form=form, title='ログイン', endpoints='auth.sign_in')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
	form = SignupForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# サインサップの処理
			print(form.email.data, form.password.data)
			email = form.email.data
			password = form.password.data

			if not db.session.query(User).filter(User.email == email).count():
				user = User(email=email, password=password)
				db.session.add(user)
				db.session.commit()
			return redirect(url_for('home.home'))
		else:
			print('Invalid input', form.email.errors, form.password.errors, form.submit.errors)
	return render_template('signup.html', form=form, title='会員登録', endpoints='auth.sign_up')
