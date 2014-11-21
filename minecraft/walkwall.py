from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

air = 0
stone = 1
gold = 41
wall_height = 5
lastx, lasty, lastz = mc.player.getPos()

while True:
  x, y, z = mc.player.getPos()
  mc.setBlocks(x-1, y, z-1, x+1, y+10, z+1, air)
  mc.setBlocks(lastx, lasty,lastz, lastx, lasty+5, lastz, gold)
  mc.setBlock(lastx-1, lasty-1, lastz-1, lastx+1, lasty-1, lastz+1, stone)
  lastx = x
  lasty = y
  lastz = z
  sleep(0.1)
