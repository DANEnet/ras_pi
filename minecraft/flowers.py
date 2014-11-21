from mcpi import minecraft
mc = minecraft.Mineraft.create()

flower = 38

while True:
  x, y, z = mc.player.getPos()
  mc.setBlock(x, y, z, flower)
  sleep(0.1)
  
