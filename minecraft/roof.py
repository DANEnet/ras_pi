from mcpi import minecraft
from time import sleep
include mcpi.block as block
mc = minecraft.Minecraft.create()

air = 0
stone = 1
gold = 41
wall_height = 5
wood = 5


sleep(10)

startx, starty, startz = mc.player.getPos()
starty=starty+wall_height

nextx = startx
nexty = starty
nextz = startz

while mc.getBlock(startx, starty, startz) == block.AIR:    # we are going to do the start block last
  if (mc.getBlock(nextx+1, nexty, nextz) == block.AIR and
      not(startx == nextx and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx+1, nexty, nextz, mc.Block.WOOD_PLANKS)
    nextx = nextx +1
    continue
  if (mc.getBlock(nextx-1, nexty, nextz) == block.AIR and
      not(startx == nextx and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx-1, nexty, nextz, mc.Block.WOOD_PLANKS)
    nextx = nextx-1
    continue
  if (mc.getBlock(nextx, nexty, nextz+1) == block.AIR and
      not(startx == nextx and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx, nexty, nextz+z, mc.Block.WOOD_PLANKS)
    nextz = nextz +1
    continue
  if (mc.getBlock(nextx, nexty, nextz-1) == block.AIR and
      not(startx == nextx and starty == nexty and startz==nextz)):      # check to see if we have already done that part of roof
    mc.setBlock(nextx, nexty, nextz-1, mc.Block.WOOD_PLANKS)
    nextz = nextz -1
    continue
  ## ran out of air in that part of roof see if there is anything back by starting place
  if mc.getBlock(startx+1, starty, startz) == block.AIR: 
    nextx = startx+1
    nexty = starty
    nextz = startz
  if mc.getBlock(startx-1, starty, startz) == block.AIR: 
    nextx = startx-1
    nexty = starty
    nextz = startz
    continue
  if mc.getBlock(startx, starty, startz+1) == block.AIR: 
    nextx = startx
    nexty = starty
    nextz = startz+1
    continue
  if mc.getBlock(startx, starty, startz-1) == block.AIR: 
    nextx = startx
    nexty = starty
    nextz = startz-1
    continue
  mc.setBlock(startx, starty, startz, mc.Block.WOOD_PLANKS)
  
  
 