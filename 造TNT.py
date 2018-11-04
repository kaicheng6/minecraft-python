import mcpi.minecraft as z
import mcpi.block as block
import random
zhoukaicheng = z.Minecraft.create()
def house():   
    size = int(raw_input('pleasa input size:'))
    zhoukaicheng.setBlocks(pos.x,pos.y,pos.z,pos.x+size,pos.y+size,pos.z+size,block.WOOL.id,random.randint(0,15))
pos = zhoukaicheng.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
for h in range(5):
    house()
    x = x+size
    
