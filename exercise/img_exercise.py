from PIL import Image   #pip install pillow
import os

names = os.listdir("./image")               #取所有文件名
img = Image.open(f"./image/{names[0]}")     #打开一张图片，保存宽、高
w, h = img.size

total_row = 3           #画布大小
total_col = 6
new_img = Image.new("RGB", (w*total_col, h*total_row))  #新建图片

for row in range(total_row):                    #一行一行画
    for col in range(total_col):
        img = Image.open(f"./image/{names[total_col*row+col]}") #顺序打开图片
        new_img.paste(img, (w*col, h*row))      #粘贴图片到指定位置(left, upper)
new_img.save("./image/==拼接图片==.jpg")