import uuid

from flask import Flask


def create_app():
	app = Flask(__name__)
	app.secret_key = uuid.uuid4().hex

	# register blueprints
	from blueprints.auth import auth_bp
	from blueprints.home import home_bp

	app.register_blueprint(home_bp)
	app.register_blueprint(auth_bp)

	return app

app = create_app()
