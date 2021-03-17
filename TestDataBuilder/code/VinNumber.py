#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string

'''
VIN第9位校验码计算规则：
1、 删除现有VIN码的正则表达式校验规则；

2、 VIN码只能录入数字和字母，且不能含I、O、Q;

3、 VIN码第9位加权算法如下，若不符合VIN录入规则需提示“车辆识别码可能有误，请检查后重试。确认无误继续报价”。

1） 用户点击“确认无误继续报价”后可跳过该限制继续下单；

PS：篡改VIN码可能有误，此部分业务保险公司允许承保，喂小保不限制；

PS：“确认无误继续下单”埋点统计用户数据

2） 首先将其它16位中的字母按下列关系转换成数字： 

A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8 J=1 K=2 L=3 M=4 N=5 P=7 R=9 S=2 T=3 U=4 V=5 W=6 X=7 Y=8 Z=9

3） 每个位置都有个加权数： 
位置：1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
权值：8 7 6 5 4 3 2 10 * 9 8 7 6 5 4 3 2 

4） 最后将检验位之外的16位每一位的加权系数乘以此位的对应值，再将各乘积相加，求得的和除以11，所得的余数就是检验位（第9位）的数值。如果余数为10，则检验位为字母“X”。
'''


def getValidateCheckout(id16):
    # 获得校验码算法
    weight = [8, 7, 6, 5, 4, 3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]  # 16位数字本体码权重
    validate = ['0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', 'X']  # 对应校验码字符值
    sum = 0
    mode = 0
    for i in range(0, len(id16)):
        sum = sum + int(id16[i]) * weight[i]
    mode = sum % 11
    return validate[mode]


def GetRandomVinNum():

    # 随机生成字符个数为16个
    Ofnum = random.randint(1, 16)
    Ofletter = 16 - Ofnum
    # 选中ofnum个数字
    slcNum = [random.choice(string.digits) for i in range(Ofnum)]
    # 选中ofletter个字母
    Vin_uppercase = 'ABCDEFGHJKLMNPRSTUVWXYZ'
    slcLetter = [random.choice(Vin_uppercase)
                 for i in range(Ofletter)]
    # print(slcLetter)
    # 打乱组合
    slcChar = slcLetter + slcNum
    random.shuffle(slcChar)
    # print(slcChar)
    # 生成16位随机数
    getRNG = ''.join(str(i) for i in slcChar)

    getVinNum = getRNG
    return getVinNum


def GetRandomVin():
    # 字母按字典转换成数字
    VinChangeDict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'J': 1, 'K': 2,
                     'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9, 'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9,
                     '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    Vin0 = GetRandomVinNum()
    Vin1 = [VinChangeDict[Vin0[i]] for i in range(len(Vin0))]
    # 获取校验码
    Vin3 = getValidateCheckout(Vin1)
    # print([Vin0, Vin1, Vin3])
    RandomVin = list(Vin0)
    # 第9位为校验位，插入校验码
    RandomVin.insert(8, Vin3)
    # print(RandomVin)
    return ''.join(RandomVin)

if __name__ == '__main__':
    # print(getValidateCheckout('1231231233331211'))
    # print(GetRandomVinNum())
    # print(GetRandomVin())
    # NUM = input('需数据n条：')
    # print('打印%s条数据...' % NUM)
    # x = int(NUM)
    x = 5
    for num in range(x):
        print(GetRandomVin())
    # input('Press Enter to exit...')
