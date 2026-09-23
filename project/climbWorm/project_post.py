
import requests
from lxml import etree

#获取cookie
cookie_url = "abc"
cookie_resp = requests.get(cookie_url, headers="")

url = "https://www1.rmfysszc.gov.cn/ProjectHandle.shtml"

#加一些加密的header
headers = {
    #模拟浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36", 
    #防跨域攻击
    "Origin": "https://www1.rmfysszc.gov.cn",         
    #防盗链                      
    "Referer": "https://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1",  
    #用户身份信息：一般会在第一个链接set-cookie（可以删除后重新获取）
    #"Cookie": "abc",    
    #加密数据                                            
    'Sec-Ch-Ua':'"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"', 
    'Sec-Ch-Ua-Mobile':'?0', 
    'Sec-Ch-Ua-Platform':'"Windows"', 
    'Sec-Fetch-Dest':'empty', 
    'Sec-Fetch-Mode':'cors', 
    'Sec-Fetch-Site':'same-origin', 
    'X-Requested-With':'XMLHttpRequest'
}

#notepad++正则表达式替换(\w+):(.*) -> '\1':'\2',
form_data = {           
    'type':'1', 
    'name':'', 
    'area':'', 
    'city':'不限', 
    'city1':'', 
    'city2':'', 
    'xmxz':'0', 
    'state':'0', 
    'money':'', 
    'money1':'', 
    'number':'0', 
    'fid1':'', 
    'fid2':'', 
    'fid3':'', 
    'order':'0', 
    'page':'1', 
    'include':'0', 
    'kdk':'0'
}

#post请求多了个data表单数据，设置cookies
resp = requests.post(url=url, data=form_data, headers=headers, cookies=cookie_resp.cookies)  

e = etree.HTML(resp.text)                                                   #DOM树

titles = e.xpath('//div[@class="product"]/div[@class="p_img"]/a/@title')    #xpath
auction_prices = e.xpath('//div[@class="prod-guj"]/p/strong/text()')
eval_prices = e.xpath('//div[@class="prod-guj"]/p[2]/span/text()')

for title, auction, eval in zip(titles, auction_prices, eval_prices):       #zip拉链函数
    print(f"{title} ---> 起拍价：{auction}，评估价：{eval}")

