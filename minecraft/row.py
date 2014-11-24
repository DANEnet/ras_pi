""" build a row of blocks """

""" connect to the current minecraft game """
from mcpi import minecraft
game = minecraft.Minecraft.create()

""" get the position of the player """
x, y, z = game.player.getPos()

""" set the number of blocks to be created in the row """
numberOfBlocks = 5

""" set the type of block to use to build the row """
blockType = 22

""" build the row """
""" create a variable for the current block """
""" use the variable multiple times from 1 to the number of blocks """
for blockXPosition in range(1, numberOfBlocks):

    """ set the X and Y and Z coordinates of one block to set """
    """ the X position starts at one up from the position of the player """
    """ and changes for each of the numbers in the range above """
    setX = x + blockXPosition

    """ the Y position is the ground level of the player's feet """
    setY = y

    """ the Z position is 2 blocks away from the player """
    setZ = z + 2

    """ put the block into the game """
    game.setBlock(setX, setY, setZ, blockType)

    

