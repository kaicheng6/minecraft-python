import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("hello minecraft world!")
pos = mc.player.getTilePos()
print(pos.x)
print(pos.y)
print(pos.z)
