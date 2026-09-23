
from curl_cffi import requests
from lxml import etree

url = "https://www.netbian.com/mei/index_47.htm"

resp = requests.get(url=url, impersonate="chrome110")   #模拟真实浏览器的TLS/JA3/HTTP2完整指纹，绕过WAF
if resp.status_code == 200:
    resp.encoding = "gbk"               #gbk中文编码

    e = etree.HTML(resp.text)
    imgs = e.xpath('//div[@id="main"]/div[@class="list"]/ul/li/a/img/@src')
    names = e.xpath('//div[@id="main"]/div[@class="list"]/ul/li/a/img/@alt')

    for img, name in zip(imgs, names):
        img_resp = requests.get(img)
        img_name = name.split("，")[0]+".jpg"
        with open(f"./image/{img_name}", "wb") as f:
            f.write(img_resp.content)

