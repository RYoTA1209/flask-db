import uuid
from datetime import datetime

from sqlalchemy_utils import UUIDType

from database import db


class Login(db.Model):
	__tablename__ = 'logins'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(UUIDType(binary=True), db.ForeignKey('users.id'))
	token = db.Column(db.String(255), nullable=False)

	created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
	updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
