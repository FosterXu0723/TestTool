#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
import os
import datetime
import common
import china_regions_dict as CRD

customerHeader = ['车牌号',	'VIN码',	'发动机号',	'注册日期',	'过户日期',
                  '厂牌型号',	'车型描述', '车辆种类',	'号牌种类',	'使用性质',	'车主名称',
                  '证件类型',	'证件号码',	'投保人名称',	'投保人证件类型',	'投保人证件号码',
                  '被保险人名称',	'被保险人证件类型',	'被保险人证件号码'
                  ]
wb = Workbook()
# 激活 worksheet
ws = wb.active
# headlist分配到第一行中
ws.append(customerHeader)
# 表格内容appendList
appendList = [common.carPlate(), common.vinNum(),
              common.engineNo(), common.regTime(), common.regTime(), '宝马BMW7301GL(BMW528Li)轿车',
              '宝马BMW7301(BMW530i)轿车 华晨宝马5系 2005款 530i豪华型 3.0L 手自一体 5座',
              '客车', '小型汽车号牌', '家庭自用汽车', common.customName(), '身份证',
              common.customID(), common.customName(), '身份证',
              common.customID(), common.customName(), '身份证', common.customID(),
              ]

# 附加appendList，从第一行开始附加x条数据
if __name__ == '__main__':
    x = 10
    # NUM = input('需数据n条：')
    # print('打印%s条数据...' % NUM)
    # x = int(NUM)

    for num in range(x):
        print(appendList)
        ws.append(appendList)
    # input('Press Enter to exit...')
# save file
ORDER_FILE = '离线客户导入test' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.xlsx'
wb.save(ORDER_FILE)
