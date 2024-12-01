from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# تنظیمات اتصال به دیتابیس
app.config['MYSQL_HOST'] = 'localhost'  # آدرس هاست دیتابیس
app.config['MYSQL_USER'] = 'root'      # یوزر دیتابیس (برای localhost معمولاً root است)
app.config['MYSQL_PASSWORD'] = ''      # رمز عبور دیتابیس
app.config['MYSQL_DB'] = 'flaskshop'   # نام دیتابیس


from app import routes, models