import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
x=1
y=2
z=6
mc.player.setTilePos(x,y,z)
pos=mc.player.getTilePos()
mc.postToChat(str(pos.x)+str(pos.y)+str(pos.z))
