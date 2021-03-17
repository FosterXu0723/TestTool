#coding=utf-8
from openpyxl import load_workbook
from openpyxl import Workbook
import os
import datetime
import common
import random
import china_regions_dict as CRD

agentHeadlist=['代理人姓名','代理人手机号','证件类型','证件号码','推荐人手机号',
               '学历','住址','性别','民族','政治面貌','资格证号','团队名称','团队编码']
wb=Workbook()
# 激活 worksheet
ws=wb.active
#headlist分配到第一行中
ws.append(agentHeadlist)
#表格内容appendList
Num=input('please input num:')
print 'success'
x=int(Num)
for num in range(x):
    agentList=[common.customName(),common.customPhone(),'身份证',common.customID(),common.customPhone(),
               common.education(),common.address(),'男','汉族',common.politicalStatus(),
               common.InsurAgentCerNumber()]
    ws.append(agentList)
AGENT_FILE = u'代理人导入数据test' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.xlsx'
wb.save(AGENT_FILE)
# 附加agentList，从第一行开始附加x条数据
#if __name__ == '__main__':
    #x = 10
    # NUM = input('需数据n条：')
    # print('打印%s条数据...' % NUM)
    # x = int(NUM)

        #print(agentList)
    # input('Press Enter to exit...')
# save file

