#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)#host可以是域名，也可以是127.0.0.1 0.0.0.0 外网无法访问，可能因为本地80端口被占用，换一个就好了
