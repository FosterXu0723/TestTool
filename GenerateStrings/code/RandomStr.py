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
        chars=u'�������ĳ���'
        length=len(chars)-1
        random=Random()
        for i in range(charlength):
            str+=chars[random.randint(0,length)]
        print str
        return str
    if ((chartype!=0) or (chartype!=0)):
        print u"���������������"
if __name__=='__main__':
    cy=input("��������(0����Ӣ�ĺ�����,1��������):")
    rh=input("���볤��:")
    random_str(cy,rh)
    tc=raw_input("�Ƿ����¿�ʼ(Y�������¿�ʼ):")
    while tc=="Y":
        cy=input("��������(0����Ӣ�ĺ�����,1��������):")
        rh=input("���볤��:")
        random_str(cy,rh)
        tc=raw_input("�Ƿ����¿�ʼ(Y�������¿�ʼ):")
    
