""" build a slab on the ground by building a row of rows of blocks """

""" connect to the current minecraft game """
from mcpi import minecraft
game = minecraft.Minecraft.create()

""" get the position of the player """
x, y, z = game.player.getPos()

""" set the number of blocks to be created in the row and rows in the slab """
numberOfBlocks = 10
numberOfRows = 10

""" set the type of block to use to build the row """
blockType = 21

""" build the slab """
""" create a variable for the current row """
""" use the variable for each row in the stack of rows """
for rowZPosition in range(1, numberOfRows):

    """ these program lines execute once for each row """

    """ create a variable for the current block """
    """ use the variable multiple times from 1 to the number of blocks """
    for blockXPosition in range(1, numberOfBlocks):

        """ these program lines execute once for eacn block """
        """ set the X and Y and Z coordinates of one block to set """
        """ the X position changes for each of the numbers in the range above """
        setX = x + blockXPosition

        """ the Y position is set one below the player's feet to make a flor """
        setY = -1

        """ the Z position starts by the player """
        setZ = z + rowZPosition

        """ put the block into the game """
        game.setBlock(setX, setY, setZ, blockType)

    

