from libmineshaft.blocks import Block, MultipleStateBlock, NoIDBlock

air = Block(
    0,
    image=["assets", "images", "blocks", "air.png"],
    resistance=-1,
    name="Air",
    falls=False,
    breaktime=-1,
)
stone = MultipleStateBlock(
    1,
    [
        NoIDBlock(
            ["assets", "images", "blocks", "stone.png"],
            resistance=10,
            name="Stone",
            falls=False,
            breaktime=15,
        )
    ],
)

grass = Block(
    2,
    ["assets", "images", "blocks", "grass.png"],
    resistance=0,
    name="Grass Block",
    falls=False,
    breaktime=2,
)

dirt = Block(
    3,
    ["assets", "images", "blocks", "dirt.png"],
    resistance=0,
    name="Dirt",
    falls=False,
    breaktime=2,
)

cobblestone = Block(
    4,
    ["assets", "images", "blocks", "cobblestone.png"],
    resistance=10,
    name="Cobblestone",
    falls=False,
    breaktime=15,
)

bedrock = Block(
    7,
    ["assets", "images", "blocks", "bedrock.png"],
    resistance=-1,
    name="Bedrock",
    falls=False,
    breaktime=-1,
)


BLOCKS = {0: air, 1: stone, 2: grass, 3: dirt, 4: cobblestone}
