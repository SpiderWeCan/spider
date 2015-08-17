#!/usr/bin/env python3
__author__ = 'wangxiaodong'

###################################################
# encoding=utf-8
# wangxiaodong
# 20150817
# usge:抓取数据的主要model。完成来抓取配置的解析，抓取任务的执行，做成守护进程来使用。
#
#
###################################################
#
#   版本           时间             描述
#    V1.0         20150718         引入model
#
#  ################################################

import os
import sys
import re
import logging
from datetime import date,datetime
import atexit


