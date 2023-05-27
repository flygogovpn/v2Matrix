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
#from PIL import Image
import copy
from app.main.common import Connect_DB
from app.main.auth_login_decorator import jwt_required

from apscheduler.schedulers.background import BackgroundScheduler
from app.main.out_linke_manage import Link_information
import sys
sys.setdefaultencoding('utf-8')


db = SQLAlchemy()
db = Connect_DB()

class Global_data:
    data_lastday_android = 0
    data_today_android = 0
    data_lastday_pc = 0
    data_today_pc = 0
    data_lastday_ios = 0
    data_today_ios = 0
    
    data_lastday_mac = 0
    data_today_mac = 0
    cnt = 0



def update_date_time():
    print("Time Update.")
    Global_data.data_lastday_android = Global_data.data_today_android
    Global_data.data_today_android = 0
    Global_data.data_lastday_ios = Global_data.data_today_ios
    Global_data.data_today_ios = 0
    Global_data.data_lastday_pc = Global_data.data_today_pc
    Global_data.data_today_pc = 0
    Global_data.data_lastday_mac = Global_data.data_today_mac
    Global_data.data_today_mac = 0

sched = BackgroundScheduler(timezone="Asia/Shanghai")  # 指定时区
sched.add_job(update_date_time, 'cron',  hour='21', minute='07')  # 定时启动
sched.start()

 




class User_manage_information(db.Model):
    __tablename__ = 'user_manage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    config_title = db.Column(db.Text)
    config_type = db.Column(db.Text)
    config_explanation= db.Column(db.Text)
    config_content= db.Column(db.Text)



@main.route('/user_manage_show', methods=['GET', 'POST'])
@login_required
def User_manage_show():
    trans_data = {}
    if request.method == "POST":
        db.reflect()
        # 获取所有数据表
        all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
        # 搜索框为空时忽略，不为空时以且的关系进行搜索
        data = db.session.query(all_table['user_manage']).filter(User_manage_information.id ==  request.values['ID']).first()
        trans_data['config_title'] = data.config_title
        trans_data['config_explanation'] = data.config_explanation
        trans_data['config_content'] = data.config_content
        db.session.close()
        return json.dumps(trans_data)




@main.route('/gejlwngewalivawlgwieg', methods=['GET','POST'])
def User_manage_config():
    trans_data = {}
    #if request.method == "GET":
    db.reflect()
    # 获取所有数据表
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    # 搜索框为空时忽略，不为空时以且的关系进行搜索
    data = db.session.query(all_table['user_manage']).filter_by(config_type="system").order_by(User_manage_information.id.desc())
    icnt = 0
    for i in data:
        if icnt == 0:
            trans_data['free_days_visitor'] = i.config_content
        if icnt == 1:
            trans_data['free_days_Registered'] = i.config_content
        if icnt == 2:
            trans_data['freeline_switch'] = i.config_content
        if icnt == 3:
            trans_data['customer_service'] = i.config_content
        if icnt == 4:
            trans_data['gc_number'] = i.config_content
        if icnt == 5:
            trans_data['commercial_number'] = i.config_content
        if icnt == 6:
            trans_data['backstage_addr1'] = i.config_content
        if icnt == 7:
            trans_data['backstage_addr2'] = i.config_content
        if icnt == 8:
            trans_data['backstage_addr3'] = i.config_content
        if icnt == 9:
            trans_data['mainpage_word'] = i.config_content
        if icnt == 10:
            trans_data['board_addr'] = i.config_content
        icnt = icnt + 1

    data = db.session.query(all_table['user_manage']).filter_by(config_type="payment").order_by(
        User_manage_information.id.desc())
    icnt = 0
    for i in data:
        if icnt == 0:
            trans_data['Gp1_name'] = i.config_content
        if icnt == 1:
            trans_data['Gp1_shop_plan_name1'] = i.config_content
        if icnt == 2:
            trans_data['Gp1_shop_plan_name2'] = i.config_content
        if icnt == 3:
            trans_data['Gp1_shop_plan_name3'] = i.config_content
        if icnt == 4:
            trans_data['Gp1_shop_plan_name4'] = i.config_content
        if icnt == 5:
            trans_data['Gp1_shop_plan_describe1'] = i.config_content
        if icnt == 6:
            trans_data['Gp1_shop_plan_describe2'] = i.config_content
        if icnt == 7:
            trans_data['Gp1_shop_plan_describe3'] = i.config_content
        if icnt == 8:
            trans_data['Gp1_shop_plan_describe4'] = i.config_content
        if icnt == 9:
            trans_data['Gp1_shop_plan_title1'] = i.config_content
        if icnt == 10:
            trans_data['Gp1_shop_plan_title2'] = i.config_content
        if icnt == 11:
            trans_data['Gp1_shop_plan_title3'] = i.config_content
        if icnt == 12:
            trans_data['Gp1_shop_plan_title4'] = i.config_content
        if icnt == 13:
            trans_data['Gp1_shoplan_peri1'] = i.config_content
        if icnt == 14:
            trans_data['Gp1_shoplan_peri2'] = i.config_content
        if icnt == 15:
            trans_data['Gp1_shoplan_peri3'] = i.config_content
        if icnt == 16:
            trans_data['Gp1_shoplan_peri4'] = i.config_content

        if icnt == 17:
            trans_data['Gp2_name'] = i.config_content
        if icnt == 18:
            trans_data['Gp2_shop_plan_name1'] = i.config_content
        if icnt == 19:
            trans_data['Gp2_shop_plan_name2'] = i.config_content
        if icnt == 20:
            trans_data['Gp2_shop_plan_name3'] = i.config_content
        if icnt == 21:
            trans_data['Gp2_shop_plan_name4'] = i.config_content
        if icnt == 22:
            trans_data['Gp2_shop_plan_describe1'] = i.config_content
        if icnt == 23:
            trans_data['Gp2_shop_plan_describe2'] = i.config_content
        if icnt == 24:
            trans_data['Gp2_shop_plan_describe3'] = i.config_content
        if icnt == 25:
            trans_data['Gp2_shop_plan_describe4'] = i.config_content
        if icnt == 26:
            trans_data['Gp2_shop_plan_title1'] = i.config_content
        if icnt == 27:
            trans_data['Gp2_shop_plan_title2'] = i.config_content
        if icnt == 28:
            trans_data['Gp2_shop_plan_title3'] = i.config_content
        if icnt == 29:
            trans_data['Gp2_shop_plan_title4'] = i.config_content
        if icnt == 30:
            trans_data['Gp2_shoplan_peri1'] = i.config_content
        if icnt == 31:
            trans_data['Gp2_shoplan_peri2'] = i.config_content
        if icnt == 32:
            trans_data['Gp2_shoplan_peri3'] = i.config_content
        if icnt == 33:
            trans_data['Gp2_shoplan_peri4'] = i.config_content

        if icnt == 34:
            trans_data['Gp3_name'] = i.config_content
        if icnt == 35:
            trans_data['Gp3_shop_plan_name1'] = i.config_content
        if icnt == 36:
            trans_data['Gp3_shop_plan_name2'] = i.config_content
        if icnt == 37:
            trans_data['Gp3_shop_plan_name3'] = i.config_content
        if icnt == 38:
            trans_data['Gp3_shop_plan_name4'] = i.config_content
        if icnt == 39:
            trans_data['Gp3_shop_plan_describe1'] = i.config_content
        if icnt == 40:
            trans_data['Gp3_shop_plan_describe2'] = i.config_content
        if icnt == 41:
            trans_data['Gp3_shop_plan_describe3'] = i.config_content
        if icnt == 42:
            trans_data['Gp3_shop_plan_describe4'] = i.config_content
        if icnt == 43:
            trans_data['Gp3_shop_plan_title1'] = i.config_content
        if icnt == 44:
            trans_data['Gp3_shop_plan_title2'] = i.config_content
        if icnt == 45:
            trans_data['Gp3_shop_plan_title3'] = i.config_content
        if icnt == 46:
            trans_data['Gp3_shop_plan_title4'] = i.config_content
        if icnt == 47:
            trans_data['Gp3_shoplan_peri1'] = i.config_content
        if icnt == 48:
            trans_data['Gp3_shoplan_peri2'] = i.config_content
        if icnt == 49:
            trans_data['Gp3_shoplan_peri3'] = i.config_content
        if icnt == 50:
            trans_data['Gp3_shoplan_peri4'] = i.config_content
            
        if icnt == 51:
            trans_data['Gp4_name'] = i.config_content
        if icnt == 52:
            trans_data['Gp4_shop_plan_name1'] = i.config_content
        if icnt == 53:
            trans_data['Gp4_shop_plan_name2'] = i.config_content
        if icnt == 54:
            trans_data['Gp4_shop_plan_name3'] = i.config_content
        if icnt == 55:
            trans_data['Gp4_shop_plan_name4'] = i.config_content
        if icnt == 56:
            trans_data['Gp4_shop_plan_describe1'] = i.config_content
        if icnt == 57:
            trans_data['Gp4_shop_plan_describe2'] = i.config_content
        if icnt == 58:
            trans_data['Gp4_shop_plan_describe3'] = i.config_content
        if icnt == 59:
            trans_data['Gp4_shop_plan_describe4'] = i.config_content
        if icnt == 60:
            trans_data['Gp4_shop_plan_title1'] = i.config_content
        if icnt == 61:
            trans_data['Gp4_shop_plan_title2'] = i.config_content
        if icnt == 62:
            trans_data['Gp4_shop_plan_title3'] = i.config_content
        if icnt == 63:
            trans_data['Gp4_shop_plan_title4'] = i.config_content
        if icnt == 64:
            trans_data['Gp4_shoplan_peri1'] = i.config_content
        if icnt == 65:
            trans_data['Gp4_shoplan_peri2'] = i.config_content
        if icnt == 66:
            trans_data['Gp4_shoplan_peri3'] = i.config_content
        if icnt == 67:
            trans_data['Gp4_shoplan_peri4'] = i.config_content
        trans_data['data_seccess'] = 'data_seccess'
        icnt=icnt+1

    data = db.session.query(all_table['outlink']).order_by(Link_information.id.desc())
    icnt = 0
    for i in data:
        if icnt == 0:
            trans_data['first_pg_ad_name'] = i.link_name
            trans_data['first_pg_ad_pic'] = i.link_pic
            trans_data['first_pg_ad_address'] = i.link_address
            print('aaaaaaaaaaaaaaaaaa22first_pg_ad_pic：', icnt)
        if icnt == 1:
            trans_data['mainbner1_name'] = i.link_name
            trans_data['mainbner1_pic'] = i.link_pic
            trans_data['mainbner1_address'] = i.link_address
        if icnt == 2:
            trans_data['mainbner2_name'] = i.link_name
            trans_data['mainbner2_pic'] = i.link_pic
            trans_data['mainbner2_address'] = i.link_address
        if icnt == 3:
            trans_data['mainbner3_name'] = i.link_name
            trans_data['mainbner3_pic'] = i.link_pic
            trans_data['mainbner3_address'] = i.link_address
        if icnt == 4:
            trans_data['mainbner4_name'] = i.link_name
            trans_data['mainbner4_pic'] = i.link_pic
            trans_data['mainbner4_address'] = i.link_address
        if icnt == 5:
            trans_data['mainbner5_name'] = i.link_name
            trans_data['mainbner5_pic'] = i.link_pic
            trans_data['mainbner5_address'] = i.link_address
        if icnt == 6:
            trans_data['mainbner6_name'] = i.link_name
            trans_data['mainbner6_pic'] = i.link_pic
            trans_data['mainbner6_address'] = i.link_address
        if icnt == 7:
            trans_data['midber_name'] = i.link_name
            trans_data['midber_pic'] = i.link_pic
            trans_data['midber_address'] = i.link_address
        if icnt == 8:
            trans_data['office_1_1_name'] = i.link_name
            trans_data['office_1_1_pic'] = i.link_pic
            trans_data['office_1_1_address'] = i.link_address
        if icnt == 9:
            trans_data['office_1_2_name'] = i.link_name
            trans_data['office_1_2_pic'] = i.link_pic
            trans_data['office_1_2_address'] = i.link_address
        if icnt == 10:
            trans_data['office_1_3_name'] = i.link_name
            trans_data['office_1_3_pic'] = i.link_pic
            trans_data['office_1_3_address'] = i.link_address
        if icnt == 11:
            trans_data['office_1_4_name'] = i.link_name
            trans_data['office_1_4_pic'] = i.link_pic
            trans_data['office_1_4_address'] = i.link_address
        if icnt == 12:
            trans_data['office_2_1_name'] = i.link_name
            trans_data['office_2_1_pic'] = i.link_pic
            trans_data['office_2_1_address'] = i.link_address
        if icnt == 13:
            trans_data['office_2_2_name'] = i.link_name
            trans_data['office_2_2_pic'] = i.link_pic
            trans_data['office_2_2_address'] = i.link_address
        if icnt == 14:
            trans_data['office_2_3_name'] = i.link_name
            trans_data['office_2_3_pic'] = i.link_pic
            trans_data['office_2_3_address'] = i.link_address
        if icnt == 15:
            trans_data['office_2_4_name'] = i.link_name
            trans_data['office_2_4_pic'] = i.link_pic
            trans_data['office_2_4_address'] = i.link_address
        if icnt == 16:
            trans_data['office_3_1_name'] = i.link_name
            trans_data['office_3_1_pic'] = i.link_pic
            trans_data['office_3_1_address'] = i.link_address
        if icnt == 17:
            trans_data['office_3_2_name'] = i.link_name
            trans_data['office_3_2_pic'] = i.link_pic
            trans_data['office_3_2_address'] = i.link_address
        if icnt == 18:
            trans_data['office_3_3_name'] = i.link_name
            trans_data['office_3_3_pic'] = i.link_pic
            trans_data['office_3_3_address'] = i.link_address
        if icnt == 19:
            trans_data['office_3_4_name'] = i.link_name
            trans_data['office_3_4_pic'] = i.link_pic
            trans_data['office_3_4_address'] = i.link_address
        if icnt == 20:
            trans_data['frend_1_1_name'] = i.link_name
            trans_data['frend_1_1_pic'] = i.link_pic
            trans_data['frend_1_1_address'] = i.link_address
        if icnt == 21:
            trans_data['frend_1_2_name'] = i.link_name
            trans_data['frend_1_2_pic'] = i.link_pic
            trans_data['frend_1_2_address'] = i.link_address
        if icnt == 22:
            trans_data['frend_1_3_name'] = i.link_name
            trans_data['frend_1_3_pic'] = i.link_pic
            trans_data['frend_1_3_address'] = i.link_address
        if icnt == 23:
            trans_data['frend_1_4_name'] = i.link_name
            trans_data['frend_1_4_pic'] = i.link_pic
            trans_data['frend_1_4_address'] = i.link_address
        if icnt == 24:
            trans_data['pc1_client_name'] = i.link_name
            trans_data['pc1_client_pic'] = i.link_pic
            trans_data['pc1_client_address'] = i.link_address
        if icnt == 25:
            trans_data['pc2_client_name'] = i.link_name
            trans_data['pc2_client_pic'] = i.link_pic
            trans_data['pc2_client_address'] = i.link_address


        icnt = icnt + 1
    
    
    if request.method == "POST":
        device = request.json['device']
        if device == "ios":
            Global_data.data_today_ios = Global_data.data_today_ios + 1
        if device == "pc":
            Global_data.data_today_pc = Global_data.data_today_pc + 1
        if device == "android":    
            Global_data.data_today_android = Global_data.data_today_android + 1
        if device == "mac":    
            Global_data.data_today_mac = Global_data.data_today_mac + 1    
    else:
        Global_data.data_today_android = Global_data.data_today_android + 1
        
        
    Global_data.cnt = Global_data.cnt + 1
    print(Global_data.cnt)

    db.session.close()
    return json.dumps(trans_data)


@main.route('/piclwngewalivawlgwieg', methods=['GET'])
def picUser_manage_config():
    trans_data = {}
    # if request.method == "GET":
    db.reflect()
    # 获取所有数据表
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}

    data = db.session.query(all_table['outlink']).order_by(Link_information.id.desc())
    icnt = 0
    for i in data:
        if icnt == 0:
            trans_data['first_pg_ad_name'] = i.link_name
            trans_data['first_pg_ad_pic'] = i.link_pic
            trans_data['first_pg_ad_address'] = i.link_address
            print('aaaaaaaaaaaaaaaaaaaa111afirst_pg_ad_pic：', trans_data['first_pg_ad_address'])
        if icnt == 1:
            trans_data['mainbner1_name'] = i.link_name
            trans_data['mainbner1_pic'] = i.link_pic
            trans_data['mainbner1_address'] = i.link_address
        if icnt == 2:
            trans_data['mainbner2_name'] = i.link_name
            trans_data['mainbner2_pic'] = i.link_pic
            trans_data['mainbner2_address'] = i.link_address
        if icnt == 3:
            trans_data['mainbner3_name'] = i.link_name
            trans_data['mainbner3_pic'] = i.link_pic
            trans_data['mainbner3_address'] = i.link_address
        if icnt == 4:
            trans_data['mainbner4_name'] = i.link_name
            trans_data['mainbner4_pic'] = i.link_pic
            trans_data['mainbner4_address'] = i.link_address
        if icnt == 5:
            trans_data['mainbner5_name'] = i.link_name
            trans_data['mainbner5_pic'] = i.link_pic
            trans_data['mainbner5_address'] = i.link_address
        if icnt == 6:
            trans_data['mainbner6_name'] = i.link_name
            trans_data['mainbner6_pic'] = i.link_pic
            trans_data['mainbner6_address'] = i.link_address
        if icnt == 7:
            trans_data['midber_name'] = i.link_name
            trans_data['midber_pic'] = i.link_pic
            trans_data['midber_address'] = i.link_address
        if icnt == 8:
            trans_data['office_1_1_name'] = i.link_name
            trans_data['office_1_1_pic'] = i.link_pic
            trans_data['office_1_1_address'] = i.link_address
        if icnt == 9:
            trans_data['office_1_2_name'] = i.link_name
            trans_data['office_1_2_pic'] = i.link_pic
            trans_data['office_1_2_address'] = i.link_address
        if icnt == 10:
            trans_data['office_1_3_name'] = i.link_name
            trans_data['office_1_3_pic'] = i.link_pic
            trans_data['office_1_3_address'] = i.link_address
        if icnt == 11:
            trans_data['office_1_4_name'] = i.link_name
            trans_data['office_1_4_pic'] = i.link_pic
            trans_data['office_1_4_address'] = i.link_address
        if icnt == 12:
            trans_data['office_2_1_name'] = i.link_name
            trans_data['office_2_1_pic'] = i.link_pic
            trans_data['office_2_1_address'] = i.link_address
        if icnt == 13:
            trans_data['office_2_2_name'] = i.link_name
            trans_data['office_2_2_pic'] = i.link_pic
            trans_data['office_2_2_address'] = i.link_address
        if icnt == 14:
            trans_data['office_2_3_name'] = i.link_name
            trans_data['office_2_3_pic'] = i.link_pic
            trans_data['office_2_3_address'] = i.link_address
        if icnt == 15:
            trans_data['office_2_4_name'] = i.link_name
            trans_data['office_2_4_pic'] = i.link_pic
            trans_data['office_2_4_address'] = i.link_address
        if icnt == 16:
            trans_data['office_3_1_name'] = i.link_name
            trans_data['office_3_1_pic'] = i.link_pic
            trans_data['office_3_1_address'] = i.link_address
        if icnt == 17:
            trans_data['office_3_2_name'] = i.link_name
            trans_data['office_3_2_pic'] = i.link_pic
            trans_data['office_3_2_address'] = i.link_address
        if icnt == 18:
            trans_data['office_3_3_name'] = i.link_name
            trans_data['office_3_3_pic'] = i.link_pic
            trans_data['office_3_3_address'] = i.link_address
        if icnt == 19:
            trans_data['office_3_4_name'] = i.link_name
            trans_data['office_3_4_pic'] = i.link_pic
            trans_data['office_3_4_address'] = i.link_address
        if icnt == 20:
            trans_data['frend_1_1_name'] = i.link_name
            trans_data['frend_1_1_pic'] = i.link_pic
            trans_data['frend_1_1_address'] = i.link_address
        if icnt == 21:
            trans_data['frend_1_2_name'] = i.link_name
            trans_data['frend_1_2_pic'] = i.link_pic
            trans_data['frend_1_2_address'] = i.link_address
        if icnt == 22:
            trans_data['frend_1_3_name'] = i.link_name
            trans_data['frend_1_3_pic'] = i.link_pic
            trans_data['frend_1_3_address'] = i.link_address
        if icnt == 23:
            trans_data['frend_1_4_name'] = i.link_name
            trans_data['frend_1_4_pic'] = i.link_pic
            trans_data['frend_1_4_address'] = i.link_address
        if icnt == 24:
            trans_data['pc1_client_pic'] = i.link_pic
            trans_data['pc1_client_address'] = i.link_address
        if icnt == 25:
            trans_data['pc2_client_pic'] = i.link_pic
            trans_data['pc2_client_address'] = i.link_address
        icnt = icnt + 1

    print('4444444444444444444444444444')
 
    db.session.close()
    return json.dumps(trans_data)
#User_manage_config()

@main.route('/user_manage_data_edit', methods=['GET', 'POST'])
@login_required
def User_manage_data_edit():
        data = User_manage_information();
        data.id = request.form.get('id');
        data = User_manage_information.query.filter_by(id=data.id).first()  # 赋值语句要在去除数据之后
        data.config_title = request.form.get('config_title');
        data.config_explanation = request.form.get('config_explanation');
        data.config_content = request.form.get('config_content');
        db.session.commit()
        db.session.close()
        return '修改成功'

@main.route('/system_manage', methods=['GET', 'POST'])
@login_required
def getuser_manage():
    db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    data = db.session.query(all_table['user_manage']).filter_by(config_type="system").order_by(User_manage_information.id.desc())
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
    return render_template("menu3/user_manage.html", content=content,
    data_lastday_android=Global_data.data_lastday_android,
    data_today_android=Global_data.data_today_android,
    data_lastday_ios=Global_data.data_lastday_ios,
    data_today_ios=Global_data.data_today_ios,
    data_lastday_pc=Global_data.data_lastday_pc,
    data_today_pc=Global_data.data_today_pc,
    data_lastday_mac=Global_data.data_lastday_mac,
    data_today_mac=Global_data.data_today_mac,
    paginate=paginate)
















