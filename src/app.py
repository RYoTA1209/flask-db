import uuid

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from blueprints.auth import auth_bp
from blueprints.home import home_bp

db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.secret_key = uuid.uuid4().hex

	# db
	app.config.from_object('src.config.Config')
	db.init_app(app)
	Migrate(app, db)

	# register blueprints
	app.register_blueprint(home_bp)
	app.register_blueprint(auth_bp)

	return app


app = create_app()
