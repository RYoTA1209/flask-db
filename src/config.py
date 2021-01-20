class DevelopmentConfig:
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(**{
		'user': 'root',       # 使っている環境に合わせて変更する
		'password': 'root',   # 使っている環境に合わせて変更する
		'host': '127.0.0.1',  # 使っている環境に合わせて変更する
		'database': 'flask_db',    # 使っている環境に合わせて変更する
		'port': '3306'        # 使っている環境に合わせて変更する
	})
	SQLALCHEMY_TRACK_MODIFICATION = False
	SQLALCHEMY_ECHO = True  # SQL実行時にSQL文を表示する


Config = DevelopmentConfig
