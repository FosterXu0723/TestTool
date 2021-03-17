# 作者       ：zhanfei
# 创建时间   ：2021/2/20
import os
from xmind2testcase.zentao import xmind_to_zentao_csv_file

def XMindToCSV():
	while True:
		filepath=input("请输入文件地址:")
		if os.path.exists(filepath)==True:
			xmind_file=filepath
			print('开始转换xmind文件: %s' % xmind_file)
			zentao_csv_file=xmind_to_zentao_csv_file(xmind_file)
			print('转换xmind变成禅道csv文件成功: %s' % zentao_csv_file)
			break
		else:
			print("输入的文件地址不正确")
			continue
	input("按回车键退出")
		
if __name__=='__main__':
	XMindToCSV()
