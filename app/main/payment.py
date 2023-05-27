#-- coding:UTF-8
from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import utils
from app.models import CfgNotify
from app.main.forms import CfgNotifyForm
from . import main
import pymysql
import copy
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, backref
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
import json
#from PIL import Image
import copy
import sys
sys.setdefaultencoding('utf-8')
from app.main.common import Connect_DB
from app.main.auth_login_decorator import jwt_required

from apscheduler.schedulers.background import BackgroundScheduler
from app.main.out_linke_manage import Link_information

db = SQLAlchemy()
db = Connect_DB()


class Global_data:
    data_lastday = 0
    data_today = 0





class User_manage_information(db.Model):
    __tablename__ = 'user_manage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    config_type = db.Column(db.Text)
    config_title = db.Column(db.Text)
    config_explanation = db.Column(db.Text)
    config_content = db.Column(db.Text)


@main.route('/payent_user_manage_show', methods=['GET', 'POST'])
@login_required
def payent_User_manage_show():
    trans_data = {}
    if request.method == "POST":
        db.reflect()
        # 获取所有数据表
        all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
        # 搜索框为空时忽略，不为空时以且的关系进行搜索
        data = db.session.query(all_table['user_manage']).filter(
            User_manage_information.id == request.values['ID']).first()
        trans_data['config_title'] = data.config_title
        trans_data['config_explanation'] = data.config_explanation
        trans_data['config_content'] = data.config_content
        db.session.close()
        return json.dumps(trans_data)

@main.route('/payent_user_manage_data_edit', methods=['GET', 'POST'])
@login_required
def payent_User_manage_data_edit():
    data = User_manage_information();
    data.id = request.form.get('id');
    data = User_manage_information.query.filter_by(id=data.id).first()  # 赋值语句要在去除数据之后
    data.config_title = request.form.get('config_title');
    data.config_explanation = request.form.get('config_explanation');
    data.config_content = request.form.get('config_content');
    db.session.commit()
    db.session.close()
    return '修改成功'

@main.route('/peyment_method', methods=['GET', 'POST'])
@login_required
def getMenu2_submenu2():
    db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    data = db.session.query(all_table['user_manage']).filter_by(config_type="payment").order_by(User_manage_information.id.desc())
    # 当前页码，从第一页开始
    page = int(request.args.get("page", 1))
    # 每页的数量
    per_page = int(request.args.get('per_page', 10))
    paginate = data.paginate(page, per_page, error_out=False)
    content = paginate.items
    print('总共能生成多少页', paginate.pages)  # 总共能生成多少页
    print('当前页码数', paginate.page)  # 当前页码数
    print('True', paginate.has_next)  # True
    print('Flase', paginate.has_prev)  # Flase
    print('获取下一页的页码数', paginate.next_num)  # 获取下一页的页码数
    print('获取上一页的页码数', paginate.prev_num)  # 获取上一页的页码数
    print('获当前页的对象 列表', paginate.items)  # 获当前页的对象 列表

    db.session.close()
    return render_template("menu2/submenu2.html", content=content, data_lastday=Global_data.data_lastday,
                           data_today=Global_data.data_today, paginate=paginate)
















