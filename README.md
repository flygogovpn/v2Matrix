# v2Matrix
## 简介
- v2Matrix是一个能够对接v2board后台的简易客户端，相对传统工具来讲，能够直接登录注册，支付订阅，解决了用户留不下，工具无法直接变现的问题  
- 目前仅开放基础版，处于公测阶段，拿出来免费给大家用，这里是后台的源码和部署教程，完成后台部署后，可进入飞机群https://t.me/v2matrixshare ，拿安卓和windows的客户端

## 环境准备
- 1.安装宝塔 https://www.hostcli.com/
- 2.创建数据库
-   数据库名称：foobar
-   数据库密码：foobar
-   用户密码：foobar
- 3.导入数据库文件(见附件sql)
- 4.安装python2.7.13和pip9.0.1(centos可使用python项目管理器进行安装)
-   安装python2.7 (pip安装别用这里的)(文章中的“安装依赖的库”,那条yum的指令不用执行，跳过)
-   https://blog.csdn.net/Auspicious_air/article/details/127800463
-   安装pip 9.0.1
-   https://blog.csdn.net/m0_72838865/article/details/126931672
- 备注：一定不要python2和python3同时存在，要用干净得系统，最好是centos7

## 安装第三方依赖
- pip install --upgrade pip
- pip install peewee==3.16.0
- pip install flask==1.1.4
- pip install flask-script==2.0.6
- pip install flask-wtf==0.14.3  
- pip install flask-login==0.5.0
- pip install Flask-SQLAlchemy==2.1
- pip install apscheduler==3.9.1.post1
- pip install PyJWT==1.7.1
- pip install jason
- pip install html==1.16
- pip install requests==2.6.0
- pip install pymysql==0.10.1
- pip install SQLAlchemy==1.3.0


## 系统文件替换(文章末尾处下载)
- 1.替换文件__init__.py 路径：
-   python2.7/site-packages/flask_sqlalchemy/ 替换__init__.py	
- 2.替换文件impl.py 路径：
-   python2.7/site-packages/sqlalchemy/pool/ 替换impl.py
- 3.替换文件util.py 路径：
-   python2.7/site-packages/apscheduler/ 替换util.py
- 4.python2.7/site-packages/playhouse/pool.py
      修改第73行：self._max_connections = make_int(2147483647) //把默认改到最大,这里就是改了一个数值
- 备注：具体目录与python的安装目录有关，可以在根目录搜索flask_sqlalchemy，sqlalchemy，apscheduler进行查找。
  
## 运行
- 1.宝塔中打开端口：3306,5000
- 2.进入到你工程路径下flask-saas-platform-main，运行python run_app_dev.py 或后台运行nohup python run_app_dev.py &   
- 3.首页：http://域名或服务器ip:5000/Fsystem_manage 这里有点问题，如果是退出账号的话，要重新输入首页才能登陆。如果密码怎么都不对，就把首页重新输入一遍
- 4.账号 admin 密码123qwe123
  
## 视频教程
  https://www.youtube.com/playlist?list=PLaf6tB_GEjEzW8s9FDyTxAXY86llYepLm
  
## 群友帮忙整理了一份教程可供参考 
  [c7小白快速部署v2matrix教程.zip](https://github.com/flygogovpn/v2Matrix/files/11262081/c7.v2matrix.zip)

## 其他(非必要)
### 修改数据库密码
```
编辑`config.py`， 修改SECRET_KEY及MySQL数据库相关参数
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret'
DB_HOST = '127.0.0.1'
DB_USER = 'foobar'
DB_PASSWD = 'foobar'
DB_DATABASE = 'foobar'
```
### 添加ssl证书支持https
- 1.宝塔-网站页面，为你的域名申请ssl证书以后，点击设置找到配置文件(如下图)(域名建站的时候记得把你的端口也带上比如 www.v2mtext.com:5000)
- 2.删除第三行，取消监听该端口 listen 5000;
- 3.复制 ssl_certificate 和 ssl_certificate_key后面的路径
- 4.添加到工程启动文件/flask-saas-platform-main/run_app_dev.py 中
    app.run(debug=True,host="0.0.0.0",port=5000,
      ssl_context=('/www/server/panel/vhost/cert/anal.canghaiyib.cn/fullchain.pem', '/www/server/panel/vhost/cert/anal.canghaiyib.cn/privkey.pem'))
<img src="https://user-images.githubusercontent.com/130766519/233315517-cfcd83ca-fbdb-4a32-bad4-f935ed5d660c.png" width="300px">  <img src="https://user-images.githubusercontent.com/130766519/233318833-6e91a44d-f667-44cb-ad03-722d267a2bad.png" width="600px"> 
 



## 后台功能
- 1.系统配置(首页):配置你的面板地址
- 2.广告配置
- 3.套餐配置：
-   1).套餐1名字，套餐2名字，其中的1234对应着客户端4个套餐选项的位置
-   2).套餐名字和付款周期 共同决定这个位置对应你面板上的哪个套餐
-   3).套餐名字需和你面板上的套餐名字一致，付款周期对应关系如下:月付：month_price 季付：quarter_price 半年付：half_year_price 年付：year_price 一次性：onetime_price
![jj](https://user-images.githubusercontent.com/130766519/232080977-ea245a1a-46aa-485b-b5e6-8ae0bc8ce950.PNG)
-   4).组名是为了容纳更多的套餐，其他配置可以理解为标注，在客户端前端仅做显示，是否匹配成功可查验前端对应套餐的价格是否一致

## 相关学习文档
- [http://flask.pocoo.org](http://flask.pocoo.org)
- [https://flask-login.readthedocs.io](https://flask-login.readthedocs.io)
- [https://flask-script.readthedocs.io](https://flask-script.readthedocs.io)
- [https://flask-wtf.readthedocs.io](https://flask-wtf.readthedocs.io)
- [http://docs.peewee-orm.com](http://docs.peewee-orm.com)
- [https://almsaeedstudio.com/preview](https://almsaeedstudio.com/preview)

## 后台截图
![后台登陆](https://user-images.githubusercontent.com/130766519/232076003-18d55b5e-ee17-4b4d-a80b-9dd1a11dc74f.PNG)

![后台广告配置](https://user-images.githubusercontent.com/130766519/232076018-5becf129-34ae-4c91-81ec-ae72038aaa55.JPG)

![后台套餐配置](https://user-images.githubusercontent.com/130766519/232076042-c911c3a2-867e-423a-8fc1-e88490bef449.JPG)

## 安卓截图
<img src="https://user-images.githubusercontent.com/130766519/232089396-b3c732dd-a5e1-4687-a2c0-dc90432167e0.jpg" width="200px">       <img src="https://user-images.githubusercontent.com/130766519/232089391-fcd15304-b590-4c91-813e-93159ab3cf68.jpg" width="200px">      <img src="https://user-images.githubusercontent.com/130766519/232091422-bd63c9bb-f292-4b04-a968-180b2193aa9e.jpg" width="200px">

## windows截图
<img src="https://user-images.githubusercontent.com/130766519/232096081-4eec96aa-6bbc-4afb-afc9-f7eb3fc871d8.JPG" width="600px">

## 附件
- 后台源码 [source.tar.gz](https://github.com/flygogovpn/v2Matrix/files/11234745/source.tar.gz)
- 数据库模板 [foobar.zip](https://github.com/flygogovpn/v2Matrix/files/11258701/foobar.zip)
- 系统文件替换 [system.zip](https://github.com/flygogovpn/v2Matrix/files/11239546/system.zip)


# v2Matrix运营篇
## v2Matrix解决了什么问题
1.用户留不住问题：用户能够在本地app上进行注册登陆和使用，大大提高用户留存
2.支付转化不高：用户能够在本地app上一键支付，缩短支付过程，大大提高变现能力
3.添加广告收入：5000日活，广告收入大概在8000到1万左右

## v2Matrix提供了免费线路，要不要关掉
建议不要关，v2Matrix提供了免费线路的初衷是为了提高用户留存。有些兄弟上来第一件事就是在后台关掉这个功能，希望用户只看见自己的付费线路，认为用户只会用免费线路，就不会付费了。其实大可不必，让用户试用几天，用户就赖的卸载了，形成依赖才更能促成转化。后台可对此进行配置，比如游客可以使用免费线路3天，3天后强制登陆，已注册用户使用免费线路4天，4天后提示用户免费时间到，只能付费使用优质线路。这样才能提高留存，并进而提高支付转化。而且建站之初，先打出免费使用的旗号聚拢人气，很快就能建起千人大群，到时候再开启付费模式岂不美哉。

## v2board域名被墙，v2Matrix域名被墙，怕不怕，不要怕
- 先说v2board域名被墙，app对接的v2board域名是在v2Matrix后台设置的，即使v2board域名被墙，在v2Matrix后台设置新的域名就可以了，不影响老用户的使用。具体配置位置为：后台-首页-面板地址
- 再说v2Matrix域名被墙，v2Matrix后台可以配置备用域名，如果你体量较大，可以配置备用域名，一旦默认域名被墙，app会尝试链接备用域名。只要及时迁移v2Matrix后台即可。或者同时布置两套甚至三套v2Matrix后台实现无缝衔接也是可以的。

## v2board域名被墙，会对我造成损失吗？
- 及时撤换v2Matrix后台配置的域名，是不会对用户造成损失的。

## v2Matrix域名被墙，会对我造成损失吗？
- 配置了备用域名，不会影响老用户。新用户会受到影响，不过对客户端重新新包即可。

## v2Matrix收费吗？
- 是免费的，如果需要更好的ui和体验，去别家看看吧

## v2Matrix客户端如何获取？
- 进官方飞机群https://t.me/v2matrixshare











