import mcpi.minecraft as z
import mcpi.block as block
zhoukaicheng = z.Minecraft.create()
def house():
    pos = zhoukaicheng.player.getTilePos()
    size = int(raw_input('please input size'))
    zhoukaicheng.setBlocks(pos.x,pos.y,pos.z,pos.x+size,pos.y+size,pos.z+size,block.GLASS.id)
    zhoukaicheng.setBlocks(pos.x+size,pos.y+size/2,pos.z,pos.x+size/2,pos.y+size/2,pos.z+size,block.TNT.id)

