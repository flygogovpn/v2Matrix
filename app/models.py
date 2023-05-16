# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from peewee import MySQLDatabase, Model, CharField, BooleanField, IntegerField, TextField, DateTimeField
import json
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login_manager

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../conf'))
from config import config
import os
import datetime



cfg = config[os.getenv('FLASK_CONFIG') or 'default']

#db = MySQLDatabase(host=cfg.DB_HOST, user=cfg.DB_USER, passwd=cfg.DB_PASSWD, database=cfg.DB_DATABASE, port=3306)

# peewee.InterfaceError
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin

class RetryMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    _instance = None

    @staticmethod
    def get_db_instance():
        if not RetryMySQLDatabase._instance:
            print("hello world0")
            RetryMySQLDatabase._instance = RetryMySQLDatabase(
                config.get('db_name', cfg.DB_DATABASE),
                max_connections=32,
                stale_timeout=300,
                host=config.get('db_host', cfg.DB_HOST),
                user=config.get('db_user', cfg.DB_USER),
                password=config.get('db_pwd', cfg.DB_PASSWD),
                port=config.get('db_port', cfg.DB_PORT)
            )
        print("DB_PORT：", cfg.DB_PORT)
        return RetryMySQLDatabase._instance
db = RetryMySQLDatabase.get_db_instance()

class BaseModel(Model):
    class Meta:
        database = db
    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        # return str(r)
        return json.dumps(r, ensure_ascii=False)

# from app.main import main
# @main.before_request
# def _db_connect():
#     db.connect()
# #
# # This hook ensures that the connection is closed when we've finished
# # processing the request.
# @main.teardown_request
# def _db_close(exc):
#     if not db.is_closed():
#         db.close()

# 管理员工号
class User(UserMixin, BaseModel):
    username = CharField()  # 用户名
    password = CharField()  # 密码
    fullname = CharField()  # 真实性名
    email = CharField()  # 邮箱
    phone = CharField()  # 电话
    status = BooleanField(default=True)  # 生效失效标识
    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


# 通知人配置
class CfgNotify(BaseModel):
    check_order = IntegerField()  # 排序
    notify_type = CharField()  # 通知类型：MAIL/SMS
    notify_name = CharField()  # 通知人姓名
    notify_number = CharField()  # 通知号码
    status = BooleanField(default=True)  # 生效失效标识




@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))

#建表
def create_table():
    db.connect()
    db.create_tables([CfgNotify, User])
create_table()

if __name__ == '__main__':
    pass
