# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
aa=0
if aa == 0:
    mc.player.setPos(120,100,125)
while True:
    time.sleep(2)
    if pos.x ==12 and pos.z == 2:
        mc.postToChat('欢迎回家')


