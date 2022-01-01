from libmineshaft.blocks import Block, MultipleStateBlock, NoIDBlock


class Air(Block):
    id = 0
    image = ["textures", "blocks", "air.png"]
    resistance = -1
    name = "Air"
    falls = False
    breaktime = -1


class StoneBlock(NoIDBlock):
    image = ["textures", "blocks", "stone.png"]
    resistance = 10
    name = "Stone"
    falls = False
    breaktime = 15


class Stone(MultipleStateBlock):
    id = 1
    blocks = [StoneBlock]


class Grass(Block):
    id = 2
    image = ["textures", "blocks", "grass.png"]
    resistance = 0
    name = "Grass Block"
    falls = False
    breaktime = 2


class Dirt(Block):
    id = 3
    image = ["textures", "blocks", "dirt.png"]
    resistance = 0
    name = "Dirt"
    fallse = False
    breaktime = 2


class Cobblestone(Block):
    id = 4
    image = ["textures", "blocks", "cobblestone.png"]
    resistance = 10
    falls = False
    breaktime = 15


class Bedrock(Block):
    id = 7
    image = ["textures", "blocks", "bedrock.png"]
    resistance = -1
    name = "Bedrock"
    falls = False
    breaktime = -1


BLOCKS = {0: Air, 1: Stone, 2: Grass, 3: Dirt, 4: Cobblestone}
