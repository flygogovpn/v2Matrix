#-- coding:UTF-8
from flask import render_template
from . import main
import sys
sys.setdefaultencoding('utf-8')

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
