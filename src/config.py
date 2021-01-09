"""DBに接続する設定を記述する"""


class DevelopmentConfig:
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/flask_db?charset=utf8'.format(**{
		'user': 'root',
		'password': 'root',
		'host': '127.0.0.1',
		'port': '3306'
	})
	SQLALCHEMY_TRACK_MODIFICATION = False
	SQLALCHEMY_ECHO = True  # SQL実行時にSQL文を表示する


Config = DevelopmentConfig
