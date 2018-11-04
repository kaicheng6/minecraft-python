import mcpi.minecraft as z
import mcpi.block as block
zhoukaicheng = z.Minecraft.create()
pos = zhoukaicheng.player.getTilePos()
for a in range(0,17,2):
    zhoukaicheng.setBlock(pos.x,pos.y+a,pos.z,block.GOLD_BLOCK.id)
