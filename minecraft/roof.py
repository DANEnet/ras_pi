from mcpi import minecraft
from time import sleep
import mcpi.block as block
mc = minecraft.Minecraft.create()

AIR = 0
STONE = 1
GOLD = 41
WOOD_PLANK = 5

wall_height = 5

startx, starty, startz = mc.player.getTilePos()
starty=starty+wall_height

nextx = startx
nexty = starty
nextz = startz

mc.camera.setFollow()

while (mc.getBlock(startx, starty, startz) == AIR):
  # we are going to do the start block last
  if (mc.getBlock(nextx+1, nexty, nextz) == AIR and
      not(startx == nextx+1 and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx+1, nexty, nextz, WOOD_PLANK)  
    nextx = nextx +1
    continue
  if (mc.getBlock(nextx-1, nexty, nextz) == AIR and
      not(startx == nextx-1 and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx-1, nexty, nextz, WOOD_PLANK)
    nextx = nextx-1
    continue
  if (mc.getBlock(nextx, nexty, nextz+1) == AIR and
      not(startx == nextx and starty == nexty and startz==nextz+1)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx, nexty, nextz+1, WOOD_PLANK)
    nextz = nextz +1
    continue
  if (mc.getBlock(nextx, nexty, nextz-1) == AIR and
      not(startx == nextx and starty == nexty and startz==nextz-1)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx, nexty, nextz-1, WOOD_PLANK)
    nextz = nextz -1
    continue
  ## ran out of air in that part of roof see if there is anything back by starting place
  if mc.getBlock(startx+1, starty, startz) == AIR: 
    nextx = startx+1
    nexty = starty
    nextz = startz
    continue
  if mc.getBlock(startx-1, starty, startz) == AIR: 
    nextx = startx-1
    nexty = starty
    nextz = startz
    continue
  if mc.getBlock(startx, starty, startz+1) == AIR: 
    nextx = startx
    nexty = starty
    nextz = startz+1
    continue
  if mc.getBlock(startx, starty, startz-1) == AIR: 
    nextx = startx
    nexty = starty
    nextz = startz-1
    continue
  mc.setBlock(startx, starty, startz, WOOD_PLANK)
  
mc.camera.setNormal() 
 
