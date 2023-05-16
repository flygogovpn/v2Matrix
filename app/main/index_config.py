#-- coding:UTF-8
from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import utils
from app.models import CfgNotify
from app.main.forms import CfgNotifyForm
from . import main
import sys
sys.setdefaultencoding('utf-8')
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


