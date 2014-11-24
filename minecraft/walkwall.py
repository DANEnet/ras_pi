from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

#Store the number of some different kinds of blocks 
air = 0
stone = 1
gold = 41
wall_height = 5

# do not do anything for 10 seconds to give the player time to get in position
sleep(10)

# when the 10 seconds are up get the player's position and tell the player we are ready to go
firstx, firsty, firstz = mc.player.getPos()
mc.postToChat('Go')

# Wait another 10 seconds to let the player get to the end of the wall
sleep(10)

# Get the new position
endx, endy, endz = mc.player.getPos()

#build a wall from the first position to the last position that is wall_height tall
mc.setBlocks(firstx, firsty,firstz, endx, endy+wall_height, endz, gold)
#tell the player what we are doing
mc.postToChat('Building')
# move the player to the top of the wall
mc.player.setPos(endx,endy+wall_height,endz)