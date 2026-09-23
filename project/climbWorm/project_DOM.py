
"""
步骤一：导入模块
步骤二：发起网络请求
步骤三：解析数据
步骤四：处理数据
"""

##步骤一：导入模块
import requests             #网络请求模块
from lxml import etree      #数据解析模块


def get_first_element(lists):       #功能函数：获取第一个元素
    if lists:
        return lists[0].strip()
    return ""


##步骤二：发起网络请求
urls = [f"https://movie.douban.com/top250?start={x*25}&filter=" for x in range(10)]         #列表生成式：多页url存储到list

headers = {                 #请求头信息：绕过反爬虫                    
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

count = 0                   #计数

for url in urls:
    resp = requests.get(url=url, headers=headers)    #发起请求
    # print(res.status_code)                        #查看状态码，200成功


##步骤三：解析数据
    html = etree.HTML(resp.text)                     #将返回的html文本解析成DOM树              

    #获取所有电影的li元素列表
    # 网页上找到li，复制xpath
    lis = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    # print(len(lis))               #li的个数是25个

    for li in lis:                                  #循环取每个电影的li元素
        #获取标题：网页上找到标题，复制xpath
        # 改成当前路径
        # 获取文本：text()
        # 取第一个元素
        title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        src = li.xpath('./div/div[2]/div[1]/a/@href')[0]                    #获取链接：@href
        director = li.xpath('./div/div[2]/div[2]/p[1]/text()')[0].strip()   #获取导演
        score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]       #获取评分 
        comment = li.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0]     #获取评价
        summary = get_first_element(li.xpath('./div/div[2]/div[2]/p[2]/span/text()'))   #获取简介
        
        count += 1
        print(count, title, src, director, score, comment, summary)

##步骤四：处理数据




