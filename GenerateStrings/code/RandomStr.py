# -*- coding: cp936 -*-
from random import Random
def random_str(chartype,charlength):
    if chartype==0:
        str=''
        chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        length=len(chars)-1
        random=Random()
        for i in range(charlength):
            str+=chars[random.randint(0,length)]
        print str
        return str
    if chartype==1:
        str=''
        chars=u'测试中文长度'
        length=len(chars)-1
        random=Random()
        for i in range(charlength):
            str+=chars[random.randint(0,length)]
        print str
        return str
    if ((chartype!=0) or (chartype!=0)):
        print u"您输入的类型有误"
if __name__=='__main__':
    cy=input("输入类型(0代表英文和数字,1代表中文):")
    rh=input("输入长度:")
    random_str(cy,rh)
    tc=raw_input("是否重新开始(Y代表重新开始):")
    while tc=="Y":
        cy=input("输入类型(0代表英文和数字,1代表中文):")
        rh=input("输入长度:")
        random_str(cy,rh)
        tc=raw_input("是否重新开始(Y代表重新开始):")
    
