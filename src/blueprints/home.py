from flask import Blueprint, render_template, session

from database import db
from models.Logins import Login
from models.Users import User

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
	user = None
	if 'token' in session:
		token = session['token']
		login = find_login_by_token(token)
		user = find_user_by_id(login.user_id)

	return render_template('home.html', user=user)


def find_login_by_token(token):
	return db.session.query(Login).filter(Login.token == token).first()


def find_user_by_id(user_id):
	return db.session.query(User).filter(User.id == user_id).first()

