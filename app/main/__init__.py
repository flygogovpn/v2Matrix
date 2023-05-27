#-- coding:UTF-8
from flask import Blueprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
main = Blueprint('main', __name__, template_folder="app/templates", static_folder="app/static")

from . import views, forms, errors, out_linke_manage,user_manage,payment
