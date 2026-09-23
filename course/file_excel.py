
#pip install openpyxl
from openpyxl import load_workbook
"""操作Excel文件"""

# wb = load_workbook("gongzi.xlsx")       #加载excel
# sheet1 = wb.active                      #获取激活的工作簿

# datas = []
# for row in sheet1.iter_rows():          #获取行数据 
#     data = []
#     for col in row:                     #获取列数据
#         data.append(col.value)
#     datas.append(data)
# print(datas)

#为后面发送邮件好看，写成html格式
# datas = ["<table border='1'>"]
# for row in sheet1.iter_rows():
#     data = "<tr>"
#     for col in row:
#         data += f"<td>{col.value}</td>"
#     data += "</tr>"
#     datas.append(data)
# datas.append("</table>")
# print(datas)

#pip install xlrd
import xlrd
"""操作Excel工具"""

excel = xlrd.open_workbook("名单.xlsx")      #打开excel
sheet  = excel.sheets()[0]                   #选择第一个sheet页
for i in range(sheet.nrows):                #有几行
    sheet.cell_value(i, 0)                  #取第i行的第一列

