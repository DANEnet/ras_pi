from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

air = 0

while True:
  x, y, z = mc.player.getPos()
  mc.setBlocks(x-1, y, z-1, x+1, y+10, z+1, air)
  sleep(0.1)
