import numpy as np

palette = np.array([
    [0, 0, 0],         # 索引0：黑色 RGB
    [255, 0, 0],       # 索引1：红色
    [0, 255, 0],       # 索引2：绿色
    [0, 0, 255],       # 索引3：蓝色
    [255, 255, 255]    # 索引4：白色
])
# 形状：(5, 3)
# 第1维：颜色索引编号 0~4
# 第2维：每个索引对应的 RGB 三通道值

image = np.array([[0, 1, 2, 0],         # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
# 形状：(2, 4)
# 数组里每个数字都是 palette 的下标，代表这个像素要取调色板里对应颜色

palette[image]                          # the (2, 4, 3) color image
# 形状：(2, 4, 3)
# 拿image里每一个数字，去palette的第N行取出RGB颜色，替换当前像素，把单通道索引图 → 三通道彩色图
"""
print(palette[image])

array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],

       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
"""