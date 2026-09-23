
#pip install baidu_aip
from aip import AipFace
import base64

"""人脸识别api"""

client = AipFace(APPID, APIKEY, SECRETKEY)      #创建识别对象

img = base64.b64encode(f.read()).decode()       #base64编码
imageType = "BASE64"
options = {
    "face_field": "age,beauty"              #识别年龄和颜值
}

info  = client.detect(img, imageType, options)
print(info)