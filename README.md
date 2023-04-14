# v2Matrix
## 简介
v2Matrix是一个能够对接v2board后台的简易客户端，相对传统工具来讲，能够直接登录注册，支付订阅，解决了用户留不下，工具无法直接变现的问题  
目前仅开放基础版，处于公测阶段，拿出来免费给大家用，这里是后台的源码和部署教程，完成后台不熟后，可进入飞机群，拿安卓和windows的客户端

## 系统截图
- 登录页  


- 主页  


- 编辑界面  


- 查询界面  



## 第三方依赖
- peewee
- pymysql
- flask
- flask-script
- flask-wtf
- flask-login


## 环境配置
### venv虚拟环境安装配置
```
sudo pip3 install virtualenv
virtualenv venv
. venv/bin/activate
```

### 第三方依赖安装
```
pip3 install -r requirements.txt

```
### 系统参数配置
1. 编辑`config.py`， 修改SECRET_KEY及MySQL数据库相关参数
```
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
DB_HOST = '127.0.0.1'
DB_USER = 'foobar'
DB_PASSWD = 'foobar'
DB_DATABASE = 'foobar'
```

2. 编辑log-app.conf，修改日志路径
```
args=('/path/to/log/flask-rest-sample.log','a','utf8')
```

### 数据库初始化
1. 自动建表
直接运行`python3 models.py`

2. 插入管理员用户（默认admin/admin)
```
INSERT INTO `user` (`id`, `username`, `password`, `fullname`, `email`, `phone`, `status`)
VALUES
	(1, 'admin', 'pbkdf2:sha1:1000$Km1vdx3W$9aa07d3b79ab88aae53e45d26d0d4d4e097a6cd3', '管理员', 'admin@admin.com', '18612341234', 1);
```

### 启动应用
```
nohup ./manage.py runserver 2>&1 &
或
./run_app_dev.py (仅限测试)
```


## 项目目录结构
![](http://oh0ra6igz.bkt.clouddn.com/963uh.jpg)  
- /app/auth  用户认证相关代码
- /app/main  主要功能点相关代码
- /app/static  JS、CSS等静态文件
- /app/template  页面模版
- /app/models.py  Peewee模型
- /app/utils.py  工具模块
- /conf  系统参数及日志配置


## 相关学习文档
- [http://flask.pocoo.org](http://flask.pocoo.org)
- [https://flask-login.readthedocs.io](https://flask-login.readthedocs.io)
- [https://flask-script.readthedocs.io](https://flask-script.readthedocs.io)
- [https://flask-wtf.readthedocs.io](https://flask-wtf.readthedocs.io)
- [http://docs.peewee-orm.com](http://docs.peewee-orm.com)
- [https://almsaeedstudio.com/preview](https://almsaeedstudio.com/preview)

