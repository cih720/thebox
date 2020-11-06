#! /usr/bin/env bash
# -*- coding:utf-8 -*-
###############################################
# File Name: box.sh
# Author: Rocket
# Mail: 2453530993@qq.com
# Created Time: 2020-10-03 12:48:00
###############################################


dpkg -s lolcat &> /dev/null
if [ $? -ne 0 ]; then
    echo -e "检测到未安装 lolcat\n正在为您安装 lolcat"
    apt install lolcat -y
fi

/root/Box/box.py | lolcat
