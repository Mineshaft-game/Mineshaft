import pygame
import os


class Cursor:
    def __init__(self, image_path: str, offsetx=0, offsety=0):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.rotate(self.image, 45)
        self.offsetx = offsetx
        self.offsety = offsety


pwd = os.path.abspath(os.getcwd())
DIAMOND_PICKAXE = Cursor(str(pwd)+"/images/DiamondPickaxe.png", 0, 0)
