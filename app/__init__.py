# 从flask包导入Flask类
from flask import Flask
# 导入配置
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
# 配置日志文件
from logging.handlers import RotatingFileHandler
import logging
import os
# 将Flask类的实例，赋值给名为app的变量。这个实例成为app包的成员
app = Flask(__name__)
app.config.from_object(Config)
# print('等会儿（哪个包或模块）在使用我：', __name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# 该变量用来告诉LoginManager控制登录的试图是哪一个
login.login_view = 'login'

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
# 从app包导入模块routes 
# 导入models包用于定义数据库结构
from app import routes, models, errors