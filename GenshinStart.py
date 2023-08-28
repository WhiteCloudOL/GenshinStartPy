#coding:utf-8
# 主体功能，当屏幕全白时启动原神
# Created By WhiteCloudCN

from PIL import ImageGrab
import numpy as np
import os,time

#定义原神启动函数，genpath存放原神路径
def GenStart():
    genpath = "\"C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe\""
    os.system('start \"\" '+genpath)

#设置屏幕检测频率
ff = int(input("【GenshinStart V1】\n当白屏时自动启动原神\n现在，请选择屏幕检测频率(填数字)\n【0.每0.1s / 1.每0.5s / 2.每1.0s】："))

while True:
#   t1=time.time()
    im = ImageGrab.grab()   # 获取当前屏幕截图
    img_L = im.convert('L')     #转为灰度图
    img = np.asarray(img_L)    # 转化为点阵图，并以像素值存储
    avimg = np.mean(img)    #计算平均像素值
    if avimg >= 254:
        print("检测到白屏！\n原神，启动！")
        GenStart()
        break
    else:
        print('未检测到白屏(当前像素值:%s)'%avimg)
        print()
    if ff == 0:
        time.sleep(0.1)
    elif ff == 2:
        time.sleep(1)
    else:
        time.sleep(0.5)
#   print('查询所用t/s',time.time()-t1)

os.system("pause")
