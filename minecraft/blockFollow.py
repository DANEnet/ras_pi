#This line adds the ability to talk to minecraft
from mcpi import minecraft
#This line adds the ability to use the sleep function
from time import sleep

#Next use the stuff you imported in the first line to connect to the minecraft game
mc = minecraft.Minecraft.create()

#This is where you decide what kind of block should follow you
block = 38

#This code will repeat until you press Ctrl+c
#to press Cntl+c you have to press the tab key to get the mouse away from Minecraft 
#and then go to the window *Python Shell*
while True:
  x, y, z = mc.player.getPos()
  mc.setBlock(x, y, z, block)
  sleep(0.1)