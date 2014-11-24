""" clear space and fill with air """

""" connect to the current minecraft game """
from mcpi import minecraft
game = minecraft.Minecraft.create()

""" get the position of the player """
x, y, z = game.player.getPos()

""" set the length, height, width to clear """
length = 10
height = 5
width = 15

""" set the type of block to air """
blockType = 0

""" clear the space """
""" create a variable for the block of length """
for lengthXPosition in range(1, length):

    """ create a variable for each block of width """
    for widthZPosition in range(1, width):

        """ create a variable for each block of height """
        for heightYPosition in range(1, height):

            """ put the block of air into the game """
            setX = x + lengthXPosition
            setY = y + heightYPosition
            setZ = z + widthZPosition
            game.setBlock(setX, setY, setZ, blockType)

    

