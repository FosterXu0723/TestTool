#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import calendar
import random
import itertools
import re
import string
import china_regions_dict as CRD
import IdCardNumber
import CN_name
import bankCard
import VinNumber


# 姓名


def customName():
    return CN_name.fullname()
# print(customName())

# 手机号


def customPhone():
    phonenumber_prefixes = [134, 135, 136, 137, 138, 139, 147, 150,
                            151, 152, 157, 158, 159, 182, 187, 188,
                            130, 131, 132, 145, 155, 156, 185, 186,
                            145, 133, 153, 180, 181, 189]

    phonenumber = str(random.choice(phonenumber_prefixes)) + \
        ''.join(str(random.choice(range(10))) for _ in range(8))
    return phonenumber

# print(customPhone())

# 银行卡号


def payCard():
    return bankCard.cardNo
# print(payCard())

# 身份证号


def customID():
    return IdCardNumber.getRandomIdNumber(0)
# print(customID())

# 开户行


def bankName():
    bank_names = ['中国工商银行', '中国农业银行股份有限公司', '中国银行', '中国建设银行', '交通银行',
                  '中信银行股份有限公司', '中国光大银行', '华夏银行股份有限公司总行', '中国民生银行',
                  '广发银行股份有限公司', '平安银行', '招商银行股份有限公司', '兴业银行总行', '上海浦东发展银行']
    return random.choice(bank_names)
# print(bankName())

# 开户行支行


def bankBranch():
    return CRD.regions()[1] + "分行"
# print(bankBranch())


# 中文字符


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    # GBK2312收录了6千多常用汉字,在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    body = random.randint(0xa1, 0xf9)
    val = '{0:x} {1:x}'.format(head, body)
    word = bytes.fromhex(val).decode('gb2312')
    return word

# 备注中文字符x为字符数


def remarks(x):
    text = ''
    for i in range(x):
        text += GBK2312()
    return text

# print(remarks(10))

# 车牌号


def carPlate():
    provincelist = ['京', '沪', '津', '渝', '黑', '吉', '辽', '蒙', '冀', '新', '甘', '青', '陕', '宁',
                    '豫', '鲁', '晋', '皖', '鄂', '湘', '苏', '川', '黔', '滇', '桂', '藏', '浙', '赣', '粤', '闽']
    cha_num = 'ABCDEFGHJKLMNPQRSTUVWXYZ0123456789'
    return random.choice(provincelist) + "".join(random.choice('ABCDEFG')) + "".join(random.choice(cha_num) for i in range(5))

# print(carPlate())

# 车辆识别号VIN


def vinNum():
    vin_num = VinNumber.GetRandomVin()
    return vin_num
# print(vinNum())

# 发动机号


def engineNo():
    engine_num = 'ABCDEFGHJKLMNPRSTUVWXYZ0123456789'
    return "".join(random.choice(engine_num)for i in range(15))
# print(engineNo())

# 行驶城市
province_city_district = CRD.regions()


def cityName():
    return province_city_district[1]
# print(cityName())

# 省份


def provinceName():
    return province_city_district[0]
# print(provinceName())

# 返回今天日期


def getToday():
    return datetime.datetime.now().date()

# 将字符串转换成datetime类型


def strtodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
# 时间转换成字符串,格式为2008-08-02


def datetostr(date):
    return str(date)[0:10]
# 两个日期相隔多少天，例：2008-10-03和2008-10-01是相隔两天


def datediff(beginDate, endDate):
    format = "%Y-%m-%d"
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    count = 0
    while bd != ed:
        ed = ed - oneday
        count += 1
    return count

# 获取两个时间段的所有时间,返回list


def getDays(beginDate, endDate):
    format = "%Y-%m-%d"
    bd = strtodatetime(beginDate, format)
    ed = strtodatetime(endDate, format)
    oneday = datetime.timedelta(days=1)
    num = datediff(beginDate, endDate) + 1
    li = []
    for i in range(0, num):
        li.append(datetostr(ed))
        ed = ed - oneday
    return li

# 车辆注册时间


def regTime():
    reg_time = getDays('2010-1-1', datetostr(getToday()))
    return "".join(random.choice(reg_time))
# print(getToday())
# print(regTime())

# 到期时间


def endTime():
    end_time = getDays('2018-1-1', '2019-12-30')
    return "".join(random.choice(end_time))
# print(endTime())

# 时间格式2018/11/11 00:00:00


def paytime():
    dt = datetime.datetime.now()
    return dt.strftime('%Y/%m/%d %H:%M:%S')
# print(paytime())

# 保险公司


def companyName():
    company_list = ['中国人保', '太平洋保险', '英大财险', '众安保险', '泰康保险', '阳光保险']
    return "".join(random.choice(company_list))
# print(companyName())

# 保单号


def policyNum():
    policy_num = 'TBYD0123456789'
    return "".join(random.choice(policy_num)for i in range(20))
# print(policyNum())


# 客户标签


def customTag():
    custom_taglist1 = ['微信', '朋友介绍', '公司客户',
                       '名片分享', '4s店', '线下门店', '汽修厂', '其他']
    custom_taglist2 = ['核心', '重要', '一般']
    custom_taglist3 = ['潜在', '流失', '跟进中', '已成交']
    taglist0 = [random.choice(custom_taglist1), random.choice(
        custom_taglist2), random.choice(custom_taglist3)]
    # taglist0不允许重复出现的组合，即custom_taglist1，custom_taglist2，custom_taglist3的3阶全集
    randomTag_list = []
    for i in range(len(taglist0) + 1):
        randomTag_list += list(itertools.combinations(taglist0, i))

    # print(randomTag_list)

    # 随机取得组合并转换成string

    custom_tags = random.choice(randomTag_list)
    custom_tagstr = str(custom_tags)
    # print(random.choice(randomTag_list))
    # print(custom_tags)
    # print(len(custom_tags))
    # 只有一项或空时去符号，多项时保留逗号
    if len(custom_tags)is 1:
        custom_taglist = re.sub(
            '[\s+\.\!\/_$%^*(+\"\')]+|[+——()?【】“”！,。？、~@#￥%……&*（）]+', "", custom_tagstr)
    else:
        custom_taglist = re.sub(
            '[\s+\.\!\/_$%^*(+\"\')]+|[+——()?【】“”！。？、~@#￥%……&*（）]+', "", custom_tagstr)

    return custom_taglist
# print(customTag())

# 卡券类型


def ticketType():
    ticketTypelist = ['洗车券', '代驾券', '年检代办券', '道路救援券', '代驾券A', '代驾券B']
    return random.choice(ticketTypelist)

# print(ticketType())

# 金额x~y范围的数值


def money(x, y):
    money = random.uniform(x, y)
    # 控制随机数的精度round(数值，精度)
    return round(money, 2)
# print(money(1000, 4999))

# 卡券发放金额大于50整数


def moneyint():
    moneyint = random.randint(5, 10) * 10
    return moneyint

# print(moneyint())

# GetRandomLengthNum()自定义随机(字母+数字)长度,如8位密码


def GetRandomLengthNum(length):
    # 随机生成数字个数
    Ofnum = random.randint(1, length)
    Ofletter = length - Ofnum
    # 选中ofnum个数字
    slcNum = [random.choice(string.digits) for i in range(Ofnum)]
    # 选中ofletter个大写字母
    slcLetter = [random.choice(string.ascii_letters)
                 for i in range(Ofletter)]
    # 打乱组合
    slcChar = slcLetter + slcNum
    random.shuffle(slcChar)
    # print(slcChar)
    # 生成随机数
    getRNG = ''.join(str(i) for i in slcChar)
    return getRNG
# print(GetRandomLengthNum(8))

#学历类型
def education():
    educationTypelist=['初中','高中','专科','本科','硕士研究生','博士研究生']
    return random.choice(educationTypelist)

#住址
def address():
    address='浙江省杭州市西湖区蒋村街道西溪银座'+bytes(random.randint(1,1000))+'号'
    return address

#政治面貌
def politicalStatus():
    politicalStatuslist=['党员','团员','群众','无党派人士']
    return random.choice(politicalStatuslist)

#保险代理人资格证号
def InsurAgentCerNumber():
    InsurAgentCerNumber='0020140341080000'+bytes(random.randint(1000,9999))
    return InsurAgentCerNumber
    
