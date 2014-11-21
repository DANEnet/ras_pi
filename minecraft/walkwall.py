from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

air = 0
stone = 1
gold = 41
wall_height = 5


sleep(10)

firstx, firsty, firstz = mc.player.getPos()
mc.postToChat('Go')

sleep(10)

endx, endy, endz = mc.player.getPos()
mc.setBlocks(firstx, firsty,firstz, endx, endy+wall_height, endz, gold)
mc.postToChat('Building')
mc.player.setPos(endx+1,endy,endz+1)