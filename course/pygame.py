
import pygame

"""
画板显示
画蛇
蛇移动
改变方向
设置食物
判断死亡
显示提示信息，重新开始
"""
pygame.init()                                   #初始化模块
screen = pygame.display.set_mode([w,h])         #设置画板
pygame.display.update()                         #更新显示
pygame.Rect(left,top,width,height)              #画正方形
pygame.draw.rect(screen,(RGB),Rect,width=0)     #绘制
clock = pygame.time.Clock()                     #游戏帧数（刷新频率）
clock.tick(10)
pygame.quit()