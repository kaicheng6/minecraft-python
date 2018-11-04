import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time
while True:
    time.sleep(5)
    pos = mc.player.getTilePos()
    mc.postToChat(pos.x)
    mc.postToChat(pos.y)
    mc.postToChat(pos.z)
