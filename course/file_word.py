
#pip install docxtpl
from docxtpl import DocxTemplate

"""
abc.docx
{{name}}
"""
doc = DocxTemplate("abc.docx")      #打开word
context = {"name": "aaa"}           #参数赋值
doc.render(context)                 #渲染
doc.save("aaa.docx")                #保存新文件
