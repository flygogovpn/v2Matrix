#-- coding:UTF-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
import sys
sys.setdefaultencoding('utf-8')

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 64), ])
    password = PasswordField('密码', validators=[DataRequired()])
    rememberme = BooleanField('记住我')
    submit = SubmitField('提交')
