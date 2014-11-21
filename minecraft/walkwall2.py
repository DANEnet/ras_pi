from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

air = 0
stone = 1
gold = 41
wall_height = 5

mc.events.clearAll()
while len(mc.events.pollBlockHits()) < 1:
  sleep(0.10)
mc.postToChat("Starting")  
firstx, firsty, firstz = mc.player.getPos()
mc.events.clearAll()

while len(mc.events.pollBlockHits()) < 1:
  sleep(0.1)

lastx, lasty, lastz = mc.player.getPos()

mc.setBlocks(firstx, firsty, firstz, lastx, lasty+5, lastz, gold)
mc.postToChat("Done")

