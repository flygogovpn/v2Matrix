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
from sqlalchemy import or_,ForeignKey
from sqlalchemy.orm import  relationship
from sqlalchemy.orm import  sessionmaker,backref
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
import json
from app.main.common import Connect_DB
import copy
import sys
sys.setdefaultencoding('utf-8')
db = SQLAlchemy()
db = Connect_DB()


def Close_DB():
    db.session.close()

class Link_information(db.Model):
    __tablename__ = 'outlink'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link_name = db.Column(db.Text)
    link_type = db.Column(db.Text)
    link_address = db.Column(db.Text)
    link_describe = db.Column(db.Text)
    link_pic = db.Column(db.Text)

def get_advertice_bytype(type):
    db.reflect()
    # 获取所有数据表
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # 搜索框为空时忽略，不为空时以且的关系进行搜索
    data = db.session.query(all_table['outlink']).filter(Link_information.link_type == type)
    Close_DB()
    return data

@main.route('/link_show', methods=['GET', 'POST'])
@login_required
def link_show():
    trans_data = {}
    if request.method == "POST":
        db.reflect()
        # 获取所有数据表
        all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
        # 搜索框为空时忽略，不为空时以且的关系进行搜索
        data = db.session.query(all_table['outlink']).filter(Link_information.id ==  request.values['ID']).first()
        trans_data['link_name'] = data.link_name
        trans_data['link_type'] = data.link_type
        trans_data['link_address'] = data.link_address
        trans_data['link_describe'] = data.link_describe
        trans_data['link_pic'] = data.link_pic
        print('link_address', data.link_address)
        print('link_pic',data.link_pic)

        Close_DB()
        return json.dumps(trans_data, ensure_ascii=False)

#session = sessionmaker(bind=engine)()
@main.route('/link_form_add', methods=['GET', 'POST'])
@login_required
def link_data_add():
        data = Link_information();
        data.link_name = request.form.get('link_name');
        data.link_type = request.form.get('link_type');
        data.link_address = request.form.get('link_address');
        data.link_describe = request.form.get('link_describe');
        data.link_pic = request.form.get('link_pic');

        data = Link_information(
        link_name = data.link_name,
        link_type = data.link_type,
        link_address=data.link_address,
        link_describe=data.link_describe,
        link_pic=data.link_pic,
        )
        db.session.add(data)
        db.session.commit()
        Close_DB()
        return '11新增成功'

@main.route('/link_form_edit', methods=['GET', 'POST'])
@login_required
def link_data_edit():
        data = Link_information();
        data.id = request.form.get('id');
        data = Link_information.query.filter_by(id=data.id).first()#赋值语句要在去除数据之后
        # data.link_name = request.form.get('link_name');
        # data.link_type = request.form.get('link_type');
        data.link_address = request.form.get('link_address');
        data.link_describe = request.form.get('link_describe');
        data.link_pic = request.form.get('link_pic');
        db.session.commit()
        Close_DB()
        return '修改成功'

@main.route('/link_form_del', methods=['GET', 'POST'])
@login_required
def link_data_del():
        data = Link_information();
        data.id = request.form.get('row_del');
        data = Link_information.query.filter_by(id=data.id).delete()
        db.session.commit()
        Close_DB()
        print('我要删了删了data id=',data)
        return '删除成功'

@main.route('/menu2_submenu1', methods=['GET', 'POST'])
@login_required
def getMenu2_submenu1():
    db.reflect()
    # 获取所有数据表
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # 搜索框为空时忽略，不为空时以且的关系进行搜索
    data = db.session.query(all_table['outlink'])
    # 当前页码，从第一页开始
    page = int(request.args.get("page", 1))
    print('读取的页数读取的页数读取的页数读取的页数读取的页数读取的页数读取的页数：', page)
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

    Close_DB()
    return render_template("menu2/submenu1.html", content=content, paginate=paginate)

@main.route('/hraserhrshershtrrtj', methods=['GET'])
def link_data_config():
    trans_data = {}
    #if request.method == "GET":
    db.reflect()
    # 获取所有数据表
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # 搜索框为空时忽略，不为空时以且的关系进行搜索
    data = db.session.query(all_table['outlink']).order_by(Link_information.id.desc())
    icnt = 0
    for i in data:
        if icnt == 0:
            first_pg_ad = i.config_content
        if icnt == 1:
            main_banner1 = i.config_content
        if icnt == 2:
            main_banner2 = i.config_content
        if icnt == 3:
            main_banner3 = i.config_content
        if icnt == 4:
            main_banner4 = i.config_content
        if icnt == 5:
            main_banner5 = i.config_content
        if icnt == 6:
            main_banner6 = i.config_content
        if icnt == 7:
            discover_banner = i.config_content
        if icnt == 8:
            office_1_1 = i.config_content
        if icnt == 9:
            office_1_2 = i.config_content
        if icnt == 10:
            office_1_3 = i.config_content
        if icnt == 11:
            office_1_4 = i.config_content
        if icnt == 12:
            office_2_1 = i.config_content
        if icnt == 13:
            office_2_2 = i.config_content
        if icnt == 14:
            office_2_3 = i.config_content
        if icnt == 15:
            office_2_4 = i.config_content
        if icnt == 16:
            office_3_1 = i.config_content
        if icnt == 17:
            office_3_2 = i.config_content
        if icnt == 18:
            office_3_3 = i.config_content
        if icnt == 19:
            office_3_4 = i.config_content
        if icnt == 20:
            frend_1_1 = i.config_content
        if icnt == 21:
            frend_1_2 = i.config_content
        if icnt == 22:
            frend_1_3 = i.config_content
        if icnt == 23:
            frend_1_4 = i.config_content
        icnt=icnt+1

    trans_data['first_pg_ad'] = first_pg_ad
    trans_data['main_banner1'] = main_banner1
    trans_data['main_banner2'] = main_banner2
    trans_data['main_banner3'] = main_banner3
    trans_data['main_banner4'] = main_banner4
    trans_data['main_banner5'] = main_banner5
    trans_data['main_banner6'] = main_banner6
    trans_data['discover_banner'] = discover_banner
    trans_data['office_1_1'] = office_1_1
    trans_data['office_1_2'] = office_1_2
    trans_data['office_1_3'] = office_1_3
    trans_data['office_1_4'] = office_1_4
    trans_data['office_2_1'] = office_2_1
    trans_data['office_2_2'] = office_2_2
    trans_data['office_2_3'] = office_2_3
    trans_data['office_2_4'] = office_2_4
    trans_data['office_3_1'] = office_3_1
    trans_data['office_3_2'] = office_3_2
    trans_data['office_3_3'] = office_3_3
    trans_data['office_3_4'] = office_3_4
    trans_data['frend_1_1'] = frend_1_1
    trans_data['frend_1_2'] = frend_1_2
    trans_data['frend_1_3'] = frend_1_3
    trans_data['frend_1_4'] = frend_1_4

    return json.dumps(trans_data, ensure_ascii=False)