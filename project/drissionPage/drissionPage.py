
"""
##准备工作（执行一次即可）
# from DrissionPage import ChromiumOptions
# path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'      #配置浏览器可执行文件路径
# ChromiumOptions().set_browser_path(path).save()

##动作链tab.actions
# 模拟鼠标移动到某个位置

##监听数据包listen
# 当网站加载包含某个特征数据时，可以直接获取响应数据（监听一定要在执行动作之前）

##元素对象ele
# ele()内置了等待，如果元素未加载，它会执行等待，直到元素出现或到达时限（默认timeout=10秒）
"""

from DrissionPage import Chromium, ChromiumOptions
from DrissionPage.common import Keys
from concurrent.futures import ThreadPoolExecutor

##浏览器配置
co = ChromiumOptions()
co.set_browser_path()                           #设置浏览器路径
co.set.user_data_path()                         #设置用户数据文件夹
co.set_local_port(9222)                         #设置DrissionPage与浏览器之间的本地通信端口，默认是9222
co.headless()                                   #无头模式：看不到浏览器，但后台有进程
co.no_imgs(True).mute(True)                     #不加载图片、静音
co.incognito()                                  #无痕模式
co.set_argument('--guest')                      #访客模式
co.set_argument('--start-maximized')            #最大化
co.set_argument('--window-size', '800,600')     #窗口大小


##设置代理
#1.无账号密码形式
co.set_proxy('60.188.78.25:30120')              #网络层，浏览器请求走哪个代理服务器出去
co.auto_port()

#2.有账号密码，需要用插件
co.add_extension(r'D:\proxy_plugin')            #自己做一个Chrome代理插件
browser = Chromium(co)
tab = browser.latest_tab
tab.get('chrome-extension://xxx.html')          #插件地址：打开插件-右击-检查-控制台：location.href
tab.ele('x://input[]').input('xx', clear=True)  #输入ip、port、用户名、密码，然后点击启动代理


##浏览器对象
browser = Chromium(co)
browser.process_id                  #浏览器进程id
browser.set.retry_times(10)         #尝试10次
browser.tabs_count                  #页签个数
# browser.quit()


##保留cookie，保持登录状态下，打开浏览器
#方法一：
cookies = []                        #使用EditThisCookie谷歌插件（插件迷下载）导出cookie信息
for cookie in cookies:
    browser.set.cookies(cookie)     #手动将cookie信息注入到browser中

#方法二：
"""drissionPage会将用户数据（包括cookie信息）保存到用户文件夹中，所以只要登录一回，下次再打开，登录状态还在。"""


##并发多开浏览器（为了环境独立）
#导入多线程包：from concurrent.futures import ThreadPoolExecutor
def multi_tab(url):
    co.auto_port()                  #需要设置不同的通信端口
    browser = Chromium(co)
    browser.quit(del_data=True)     #删除缓存数据
urls = [1,2,3]
with ThreadPoolExecutor(max_workers=2) as tp:           #2个线程
    tp.map(multi_tab, urls)


##页签对象
tab = browser.latest_tab
tab2 = browser.new_tab('http://...', hidden=True)       #隐藏tab（新版本4.2）
tab3 = browser.get_tab(title='')
tab.get('http://www.baidu.com')     #只要浏览器未关闭，可以不用重复打开网址
tab.refresh()                       #刷新
tab.back(1)                         #向后
tab.forward(1)                      #向前
tab.scroll.to_bottom()              #滚动条到底
tab.wait(5)                         #等待5s
tab.save(path='', name='', as_pdf=True)                 #页面保存为pdf格式，若as_pdf=False为mhtml格式
tab.get_screenshot(path='', name='', full_page=True)    #全页面截图
tab.ele('x://body').get_screenshot(path='', name='')    #局部截图
tab.tab_id                          #页签id
tab.title                           #页签标题
tab.url                             #页签url
tab.user_agent
tab.html
tab.json
width, height = tab.rect.window_size            #获取窗口大小
tab.set.window.size(width, int(height/2))       #设置窗口大小
tab.set.window.location(0, 0)                   #设置窗口位置
# tab.close()


##动作链
#模拟按键操作
tab.actions.key_down(Keys.ENTER)        #按下Enter键，代替点击搜索按钮
tab.actions.key_up(Keys.ENTER)          #提起Enter键

#模拟按键输入：type()是逐个字符按下并提起。input()是直接输入一整段文本
tab.actions.click('x://input[@id="kw"]').type('abc', interval=0.2)  #像人一样，先点击输入框再输入
tab.actions.click('x://input[@id="kw"]').type((Keys.LEFT, 'abc'))   #光标左移一位再输入 
# tab.actions.move_to(ele).click()      #先移动到某个元素，再点击也行
tab.actions.show_trail()                #显示鼠标运动轨迹（新版本4.2）


##滚动条
# 判断全局滚动还是局部滚动，在Chrome-Console-验证js：document.scrollingElement.scrollBy(0,1500)
# 如果页面滚动，则全局滚动，否则局部滚动
# 1.全局滚动
tab.scroll.to_bottom()                  #一般直接滚动到底部
tab.run_js("window.scrollBy(0,1500)")   #by是相对位置，to是绝对位置，x=0，y=1500个像素

# 2.局部滚动
script = """
    ele = document.getElementByClassName("abc");                                #先获取局部滚动元素
    ele[0].scrollIntoView({behavior:"smooth",block:"end",inline:"nearest"});    #再滚动这个元素
"""
tab.run_js(script)

ele = tab.ele('x://div[contains(@class,"abc")]')    #先获取局部滚动元素
tab.actions.scroll(200, 0, ele)                     #再用动作链滚动这个元素

# 穿插两个js函数 #
# const myInter = setInterval(function(){
#       window.scrollBy(0,100)                      #设置定时，每1s向下滚动100px
# }, 1000);
# 
# setTimeout(() => clearInterval(myInter), 2000);   #箭头函数，设置延时，2s后停止定时


##监听http接口数据包
#1.监听1个数据包
tab.listen.start('detail?nodeId=')      #先设置监听接口，在Chrome-Network中搜索页面文字，找到对应接口
tab.get('https://www.baidu.com')        #再打开网址
resp = tab.listen.wait()                #等待响应数据（一次性）
print(resp.response.body)               #获取响应文本

#2.监听全部数据包
tab.listen.start()                      #不设置具体接口
tab.get('https://www.baidu.com')
for resp in tab.listen.steps:           #会一直出于监听状态
    print(resp.response.body)
    break                               #需要手动中断

#3.有翻页的场景
tab.listen.start('detail?nodeId=')      #监听多个接口时，传入list
tab.get('https://www.baidu.com')
while True:
    for resp in tab.listen.steps(count=1):      #只监听1个数据包，且持续监听中
        print(resp.response.body)
    next_page = tab.ele('x://a[@title="下一页"]')
    if next_page:
        next_page.click()
    else:
        break


##并发多开标签页
#导入多线程包：from concurrent.futures import ThreadPoolExecutor
def multi_tab(url):
    new_tab = browser.new_tab(url)
    new_tab.close()
urls = [1,2,3]
with ThreadPoolExecutor(max_workers=2) as tp:   #2个线程
    tp.map(multi_tab, urls)


##元素对象
ele = tab.ele('x://input[@id="su"]')      #推荐xpath语法，在Chrome-Elements中搜索-验证xpath
ele2 = ele.prev()                         #前一个兄弟元素
ele2 = ele.next()                         #后一个兄弟元素
ele.html                                  #获取html
ele.text                                  #获取文本
ele.attr('href')                          #获取href属性值
ele.input("drissionPage", clear=True)     #输入，清除原来的内容
ele.click()                               #模拟真实鼠标点击事件（推荐）
ele.click(by_js=True)                     #直接执行JS：element.click()，可以点击不可见元素

#选择下拉框
tab.ele('x://select[@id="province"]').select("山东")
tab.ele('x://option[text()="河北"]').click()

#选择复选框
tab.ele('x://span[text()="上海市"]').prev().click()     #文本"上海市"的前一个兄弟元素就是复选框，点击

##等待元素加载
#方法一：
ele = tab.ele('x://input[@id="su"]', timeout=3)         #等待元素加载，页面已加载，但元素可能是JS动态生成的
if ele:
    ele.click()

#方法二：
if tab.wait.eles_loaded('x://input[@id="su"]', timeout=3):  #等待元素加载，只想确认元素已经出现在DOM中
    tab.ele('x://input[@id="su"]').click()

#方法三：
tab.wait.load_start()                                   #等待页面开始加载，点击链接后，页面开始白屏转圈


##定位多个元素
lis = tab.eles('x://div/li')
for li in lis:
    li.ele('x://a').attr('href')

##iframe元素定位
iframe = tab.get_frame('x://body/iframe')   #需要先获取iframe元素
ele = iframe.ele('x://div[@class="news"]')  #再用iframe元素获取iframe内的其他元素
#新版本4.2：
tab.ele('x://div[@class="news"]')           #不需要先获取iframe元素，就可以直接获取iframe内的元素

##shadow-root元素定位（完全隔离的DOM树）
shadowroot = tab.ele('x://div[@id="history"]')   #需要先获取shadow-root父节点的元素
ele = shadowroot.sr('x://div[@id="content"]')    #再继续定位shadow-root内的其他元素

