from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

#We want to flatten an area and replace 
# the blocks with blocks of air.

air = 0

#walk forward to clear the ground
#this code repeats until you press Ctrl+c
while True:
  x, y, z = mc.player.getPos()
  mc.setBlocks(x-1, y, z-1, x+1, y+10, z+1, air)
  sleep(0.1)