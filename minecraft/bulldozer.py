from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

# We want to flatten an area and replace 
# the blocks with blocks of air

air = 0

#walk forward to clear the ground
#this code repeats until you press Ctrl+c
while True:
  x, y, z = mc.player.getPos()
  # we change the blocks all around the character (x-1 and z-1 to x+1 and z+1) and 
  #the y+10 makes it go 10 blocks up in the air.
  mc.setBlocks(x-1, y, z-1, x+1, y+10, z+1, air)
  sleep(0.1)