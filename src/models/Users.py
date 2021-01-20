import uuid
from datetime import datetime

from sqlalchemy_utils import UUIDType

from database import db


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(UUIDType(binary=True), primary_key=True, default=uuid.uuid4)
	email = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)

	created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
	updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
