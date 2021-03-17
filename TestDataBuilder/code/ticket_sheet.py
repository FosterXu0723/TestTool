#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
import os
from datetime import datetime
import common
import random
import china_regions_dict as CRD

ticketHeadlist = ['客户公司简称',    '方案名称',   '杭中支',
                  '姓名',  '手机号码',   '发放总金额',  '卡券类型', '备注']


wb = Workbook()
# 激活 worksheet
ws = wb.active
# headlist分配到第一行中
ws.append(ticketHeadlist)
# 附加orderList，从第一行开始附加x条数据
x = 10
# NUM = input('需数据n条：')
# print('打印%s条数据...' % NUM)
# x = int(NUM)

for num in range(x):

    # 表格内容orderList
    ticketList = [common.remarks(6), '内部测试方案', '杭中支',
                  common.customName(), common.customPhone(), common.moneyint(),
                  common.ticketType(), common.remarks(10)
                  ]
    print(ticketList)
    ws.append(ticketList)
# save file
ORDER_FILE = '卡券发放test' + datetime.now().strftime('%Y%m%d%H%M%S') + '.xlsx'
wb.save(ORDER_FILE)
