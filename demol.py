import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
mc.postToChat("hello word !")
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x=" + str(pos.x) + "  y= " +  str(pos.y) + "   z=" + str(pos.z))
    if pos.x==10 and pos.z==80:
        mc.postToChat("welcome home")
