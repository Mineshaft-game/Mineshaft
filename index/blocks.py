from libmineshaft.blocks import Block, MultipleStateBlock, NoIDBlock


class Air(Block):
    id = 0
    imagecoords = (64, 176)
    resistance = -1
    name = "Air"
    falls = False
    breaktime = -1


class StoneBlock(NoIDBlock):
    imagecoords = (16, 0)
    resistance = 10
    name = "Stone"
    falls = False
    breaktime = 15


class Stone(MultipleStateBlock):
    id = 1
    blocks = [StoneBlock]


class Grass(Block):
    id = 2
    imagecoords = (48, 0)
    resistance = 0
    name = "Grass Block"
    falls = False
    breaktime = 2


class Dirt(Block):
    id = 3
    imagecoords = (32, 0)
    resistance = 0
    name = "Dirt"
    fallse = False
    breaktime = 2


class Cobblestone(Block):
    id = 4
    imagecoords = (
        0,
        0,
    )  # Temporary placeholder, since there is no cobble texture right now
    resistance = 10
    falls = False
    breaktime = 15


class Bedrock(Block):
    id = 7
    imagecoords = (16, 16)
    resistance = -1
    name = "Bedrock"
    falls = False
    breaktime = -1


BLOCKS = {0: Air, 1: Stone, 2: Grass, 3: Dirt, 4: Cobblestone, 7: Bedrock}
