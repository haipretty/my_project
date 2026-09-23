

#pip install flask
from flask import Flask, render_template, request
"""web服务框架"""

"""
index.html
{% for i in data %}
<tr>
    <td>{{i.id}}</td>
    <td>{{i.name}}</td>
    <td><a href="/dianzan?id={{i.id}}">点赞</a></td>    #带参数的get方法
</tr>
{% endfor %}
"""

app = Flask(__name__)       #创建web服务对象

data = [
    {"id": 0, "name": "中秋节", "num": 0}
]

@app.route("/index")        #访问：http://127.0.0.1:5000/index
def index():
    return render_template("index.html", data=data)    #响应：带数据到index.html页面

@app.route("/dianzan")      #访问：http://127.0.0.1:5000/dianzan?id=...
def dianzan():
    id = request.args.get("id")     #获取参数id
    data[int(id)]["num"] += 1
    return render_template("index.html", data=data)    #响应：带数据到index.html页面

app.run()                   #启动web服务