#coding:utf-8
# 主体功能，当屏幕全白时启动原神
# Created By WhiteCloudCN

from PIL import ImageGrab
import numpy as np
import os,time,cv2

def GenStart():
    genpath = "\"C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe\""
    os.system('start \"\" '+genpath)

ff = int(input("【GenshinStart V1】\n当白屏时自动启动原神\n现在，请选择屏幕检测频率(填数字)\n【0.每0.1s / 2.每0.5s / 3.每1.0s】："))

while True:
    t1=time.time()
    im = ImageGrab.grab()   # 获取当前屏幕截图
    img_L = im.convert('L')     #转为灰度图
    img = np.asarray(img_L)    # 转化为点阵图，并以像素值存储
    avimg = np.mean(img)
    if avimg >= 254:
        print("原神，启动！")
        GenStart()
        break
    else:
        print('Not Started')
        print(avimg)
    '''
    l,h=img.shape
    cnt = 0
    for i in range(l):
        for j in range(h):
            if img[i,j] == 255:
                cnt += 1
    '''
    if ff == 0:
        time.sleep(0.1)
    elif ff == 2:
        time.sleep(1)
    else:
        time.sleep(0.5)
    print('查询所用t/s',time.time()-t1)
# 显示当前截图
# img.show()

print(img)