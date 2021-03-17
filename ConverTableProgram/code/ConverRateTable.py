#coding=utf-8
import xlrd
import sys
import readConfig
import xlsxwriter

class ExcelTool():
    def TransFormRateExcel(self):
        excelPath=readConfig.excelpath1
        sheetName=readConfig.sheetname
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取excel行数
        self.rowNum = self.table.nrows
        #获取excel列数
        self.colNum = self.table.ncols
        print self.rowNum
        print self.colNum

        #建立新表模版
        self.filename=readConfig.excelpath2
        workbook=xlsxwriter.Workbook(self.filename) 
        worksheet=workbook.add_worksheet('sheet1')
        headings=[u'年龄',u'费率',u'保障期限',u'缴费期限',u'性别']
        worksheet.write_row('A1',headings)

        #读取年龄
        age_list=[]
        for j in range(1,self.colNum):
            for i in range(5,self.rowNum):
                self.age=int(self.table.cell(i,0).value)
                self.age1=self.age+1
                self.age2=str(self.age)+'y'+'-'+str(self.age1)+'y'
                age_list.append(self.age2)
        #print age_list
        
        #读取费率
        rate_list=[]
        for j in range(1,self.colNum):
            for i in range(5,self.rowNum):
                self.rate=str(self.table.cell(i,j).value)
                rate_list.append(self.rate)
        '''print rate_list'''

        #读取保障期限
        gperiod_list=[]
        for j in range(1,self.colNum):
            for i in range(5,self.rowNum):
                self.gperiod=self.table.cell(2,j).value
                if self.gperiod==u'终身':
                    self.gperiod2=self.gperiod.replace(u'终身','t999y')
                else:
                    self.gperiod2=self.gperiod.replace(u'年','y').replace(u'至','t').replace(u'岁','y')
                gperiod_list.append(self.gperiod2)
        '''print gperiod_list'''

        #读取缴费期限
        payperiod_list=[]
        for j in range(1,self.colNum):
            for i in range(5,self.rowNum):
                self.payperiod=self.table.cell(3,j).value
                if self.payperiod==u'一次性付清':
                    self.payperiod2=self.payperiod.replace(u'一次性付清','0y')
                elif self.payperiod==u'趸交':
                    self.payperiod2=self.payperiod.replace(u'趸交','0y')
                else:
                    self.payperiod2=self.payperiod.replace(u'年','y')
                payperiod_list.append(self.payperiod2)
        '''print payperiod_list'''

        #性别
        sex_list=[]
        for j in range(1,self.colNum):
            for i in range(5,self.rowNum):
                self.sex=self.table.cell(4,j).value
                if self.sex==u'男':
                    self.sex2=self.sex.replace(u'男','1')
                elif self.sex==u'女':
                    self.sex2=self.sex.replace(u'女','2')
                sex_list.append(self.sex2)
        '''print sex_list'''

        #拼装数据
        data=[age_list,rate_list,gperiod_list,payperiod_list,sex_list]
        
        #写入数据
        worksheet.write_column('A2',data[0])
        worksheet.write_column('B2',data[1])
        worksheet.write_column('C2',data[2])  
        worksheet.write_column('D2',data[3])
        worksheet.write_column('E2',data[4])

        #保存数据
        workbook.close()


if __name__ == "__main__":
    ExcelTool().TransFormRateExcel()
    