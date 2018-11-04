# encoding: utf-8
import mcpi.minecraft as m  #接入mcpi的文件
import time #
zhoukaicheng = m.Minecraft.create()  #给人物创造的能力
zhoukaicheng.postToChat("hallo wold !")  #人物调用打印的能力
z = 0
while True:
    time.sleep(2)
    pos=zhoukaicheng.player.getTilePos()  #获取人物位置
    zhoukaicheng.postToChat(str(pos.x) + " " + str(pos.y) + " " + str(pos.z))  #打印位置
    if -167<pos.x<-160 and -99<pos.z<-90:
        zhoukaicheng.postToChat("Welcome Home!") #人物调用打印的能力ww
        z = z+1
        if z == 5:
            zhoukaicheng.player.setTilePos(-180,20,-110)
            z = 0

