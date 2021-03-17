#!/usr/bin/env python
# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
import os
from datetime import datetime
import common
import random
import china_regions_dict as CRD

orderHeadlist = ['是否APP提现', '合同公司', '出单机构', '合同类型', '账期', '代理人姓名',
                 '代理人手机号', '收款人姓名', '收款人身份证号', '收款人银行账号', '开户行',
                 '开户行支行', '开户行所在省', '开户行所在市', '商业险保单号', '交强险保单号',
                 '商业险总保费', '交强险总保费', '车船税', '商业险佣金', '交强险佣金', '商业险应收',
                 '交强险应收', '支付时间', '商业险起保日期', '交强险起保日期', '车牌号', '车主姓名',
                 'VIN码', '发动机号', '注册日期', '备注']


wb = Workbook()
# 激活 worksheet
ws = wb.active
# headlist分配到第一行中
ws.append(orderHeadlist)

# 交强险，商业险佣金
insMoney = common.money(0, 2000)
musMoney = common.money(0, 500)
province_city_district = CRD.regions()
# 表格内容orderList
orderList = ['否', '北部湾财险', '北部湾财险', 'CCB', '201812', '一休八', '14000000128',
             common.customName(), common.customID(), common.payCard(), common.bankName(),
             common.bankBranch(), province_city_district[0],
             province_city_district[1],
             common.policyNum(), common.policyNum(), common.money(3000, 7999),
             common.money(50, 1000), common.money(0, 100),
             insMoney, musMoney,
             insMoney + random.randint(0, 100),
             musMoney + random.randint(0, 100),
             common.paytime(), common.paytime(), common.paytime(),
             common.carPlate(), common.customName(), common.vinNum(),
             common.engineNo(), common.regTime(), common.remarks(5)
             ]

# 附加orderList，从第一行开始附加x条数据
if __name__ == '__main__':
    x = 10
    # NUM = input('需数据n条：')
    # print('打印%s条数据...' % NUM)
    # x = int(NUM)
    for num in range(x):
        print(orderList)
        ws.append(orderList)
    input('Press Enter to exit...')
# save file
ORDER_FILE = '导单test' + datetime.now().strftime('%Y%m%d%H%M%S') + '.xlsx'
wb.save(ORDER_FILE)
