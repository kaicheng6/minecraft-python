import mcpi.minecraft as m  #接入mcpi的文件
import time #
i = 0
zhoukaicheng = m.Minecraft.create()  #给人物创造的能力
zhoukaicheng.postToChat("hallo wold !")  #人物调用打印的能力
while True:
    time.sleep(2)
    pos=zhoukaicheng.player.getTilePos()  #获取人物位置
    zhoukaicheng.postToChat(str(pos.x) + " " + str(pos.y) + " " + str(pos.z))  #打印位置
    if -167<pos.x<-160 and -99<pos.z<-90:
        zhoukaicheng.postToChat("欢迎回家 !")  #人物调用打印的能力
        i=i+1
        if i ==5:
            zhoukaicheng.player.setPos(-180,20,-110)
    else:
        i=0
        
        
        
