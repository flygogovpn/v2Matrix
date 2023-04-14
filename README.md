# v2Mtrix
client for v2board 能够对接v2board的客户端，这里是后台源码
环境：
安装python2.7.13
安装pip 9.0.1

前期准备
1.安装宝塔 https://www.hostcli.com/ 
2.创建数据库
  数据库名：foobar
  用户名：foobar
  密码：foobar
3.导入数据库备份(见附件)
4.安装python2.7
  安装python2.7.13 (pip安装别用这里的)
  https://blog.csdn.net/Auspicious_air/article/details/127800463
  安装pip 9.0.1
  https://blog.csdn.net/m0_72838865/article/details/126931672
  
部署安装
1.安装flask依赖
  pip install peewee
  pip install flask
  pip install flask-script
  pip install flask-wtf  
  pip install flask-login
  pip install Flask-SQLAlchemy==2.1
  pip install apscheduler
  pip install PyJWT 
  pip install jason
  pip install --upgrade pip
  pip install html
  pip install requests
  pip install pymysql
2.系统文件替换
  1)替换文件__init__.py，路径：/site-packages/flask_sqlalchemy/__init__.py
  
  2)替换文件impl.py，路径：/site-packages/sqlalchemy/pool/impl.py
  
  3)替换文件util.py，路径：/usr/lib/python2.7/site-packages/apscheduler
  备注：具体路径是根据python的安装目录各有不同，可以在根目录搜索flask_sqlalchemy进行查找
 
3.打开端口：3306,5000(宝塔里设置一下)

4.运行
  打开指令窗口，进入到你工程路径下flask-saas-platform-main，运行python run_app_dev.py
  首页：http://域名或服务器ip:5000/Fsystem_manage
  账号：admin
  密码：123qwe123

其他
1.修改数据库密码：flask-saas-platform-main/conf/config.py
2.后台运行指令
  nohup python run_app_dev.py &  运行程序
  ps aux |grep python 查看后台进程






