
"""
resp = requests.get(url)
resp.text       #返回字符串 -> etree.HTML(resp.text)、re.findall(pattern, resp.text)
resp.content    #返回bytes  -> f.write(resp.content)
resp.json()     #json格式化 -> resp.json()["data"]["abc"]
"""

import requests
import re

url = "https://www.baidu.com"
headers = {
    "User-Agent":""
}

resp = requests.get(url, headers=headers)    #发送request请求，返回respond
resp_str = resp.text                         #获取响应字符串string类型

infos = re.findall(r'', resp_str)            #用正则匹配想要的内容，返回list
with open('xiaoshuo.txt', 'w', encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n")

