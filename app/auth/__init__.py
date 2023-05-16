#-- coding:UTF-8
from flask import Blueprint
import sys
sys.setdefaultencoding('utf-8')
auth = Blueprint('auth', __name__)

from . import views
