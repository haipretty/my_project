import requests

url = "https://kw-bj.kuwo.cn/0588ddb3ec2befeea4a4fd28496706c6/6a7db1c8/cy/resource/n3/8/65/3915377363.mp3"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)

with open("xuehua.mp3", "wb") as f:
    f.write(resp.content)               #返回响应内容bytes类型

