# -*- coding: utf-8 -*-
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
from sqlalchemy.pool import NullPool
import copy

def Connect_DB():
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'foobar'
    USERNAME = 'foobar'
    PASSWORD = 'foobar'
    DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
    appa = Flask(__name__)
    # 映射数据库
    appa.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    appa.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    appa.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'poolclass': NullPool,
    }
    return  SQLAlchemy(appa)# db为继承了SQLALchemy