#encoding=utf-8
import os
import codecs
import ConfigParser


proDir = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(proDir, "config.ini")
# 调用读取配置模块中的类
conf = ConfigParser.ConfigParser()
# 读ini文件
conf.read(configPath)
# 调用get方法，然后获取配置的数据
#获取原始费率excel相关数据
excelpath1=conf.get("Excel","excelpath1")
sheetname=conf.get("Excel","sheetname")
#转换后表
excelpath2=conf.get("Excel","excelpath2")