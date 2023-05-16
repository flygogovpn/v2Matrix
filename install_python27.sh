#!/bin/bash

# 安装编译依赖项
apt update
apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

# 下载 Python 2.7 源代码
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz

# 解压源代码
tar xzf Python-2.7.18.tgz

# 进入解压后的目录
cd Python-2.7.18

# 配置编译选项
./configure --enable-optimizations

# 编译并安装 Python 2.7
make
make altinstall

# 验证安装
python2.7 --version
