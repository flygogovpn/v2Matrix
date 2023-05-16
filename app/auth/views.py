#-- coding:UTF-8
from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
import sys
sys.setdefaultencoding('utf-8')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    

    
    form = LoginForm()
    
    print('111111',generate_password_hash('123qwe123'))
 
    
    
    print(form.rememberme.data)
    if form.validate_on_submit():
        try:
            user = User.get(User.username == form.username.data)
            if user.verify_password(form.password.data):
                login_user(user, form.rememberme.data)
                return redirect(request.args.get('next') or url_for('main.system_manage'))
            else:
                flash('用户名或密码错误')
        except:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))
