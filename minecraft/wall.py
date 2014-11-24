""" build a wall by building a stack of rows of blocks """

""" connect to the current minecraft game """
from mcpi import minecraft
game = minecraft.Minecraft.create()

""" get the position of the player """
x, y, z = game.player.getPos()

""" set the number of blocks to be created in the row and rows in the stack """
numberOfBlocks = 5
numberOfRows = 15

""" set the type of block to use to build the row """
blockType = 21

""" build the wall """
""" create a variable for the current row """
""" use the variable for each row in the stack of rows """
for rowYPosition in range(1, numberOfRows):

    """ these program lines execute once for each row """

    """ create a variable for the current block """
    """ use the variable multiple times from 1 to the number of blocks """
    for blockXPosition in range(1, numberOfBlocks):

        """ these program lines execute once for eacn block """
        """ set the X and Y and Z coordinates of one block to set """
        """ the X position changes for each of the numbers in the range above """
        setX = x + blockXPosition

        """ the Y position is set to the height of the player's feet plus the row number """
        setY = y + rowYPosition

        """ the Z position is 3 blocks away from the player """
        setZ = z + 3

        """ put the block into the game """
        game.setBlock(setX, setY, setZ, blockType)

    

