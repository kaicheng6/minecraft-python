import mcpi.minecraft as m  #����mcpi���ļ�
import time #
i = 0
zhoukaicheng = m.Minecraft.create()  #�����ﴴ�������
zhoukaicheng.postToChat("hallo wold !")  #������ô�ӡ������
while True:
    time.sleep(2)
    pos=zhoukaicheng.player.getTilePos()  #��ȡ����λ��
    zhoukaicheng.postToChat(str(pos.x) + " " + str(pos.y) + " " + str(pos.z))  #��ӡλ��
    if -167<pos.x<-160 and -99<pos.z<-90:
        zhoukaicheng.postToChat("��ӭ�ؼ� !")  #������ô�ӡ������
        i=i+1
        if i ==5:
            zhoukaicheng.player.setPos(-180,20,-110)
    else:
        i=0
        
        
        
