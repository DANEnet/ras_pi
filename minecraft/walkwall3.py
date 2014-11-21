from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

air=0
stone = 1
flower = 38
gold = 41
wall_height = 5

mc.camera.setFollow()
lastx, lasty, lastz = mc.player.getPos()
while True:
  x, y, z = mc.player.getPos()
  mc.setBlocks(x, y, z, lastx, lasty+wall_height, lastz, gold)
  mc.setBlocks(x, y, z, x, lasty+wall_height, z, air)
  lastx =x
  lasty =y
  lastz =z
  sleep(0.3)
  
