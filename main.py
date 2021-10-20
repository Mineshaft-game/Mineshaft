import pygame
import screeninfo
import os
import random
import pygame_menu
from libmineshaft.colors import *
from libmineshaft.constants import *
from libmineshaft.themes import *
from libmineshaft.music import *


class Mineshaft(object):
    def __init__(self):
        self._pygame_init()
        self.currentpanoramapos = [
            random.randint(-1000, 0), random.randint(-500, 0)]
        self.panorama_x_direction = random.randint(0, 1)
        self.panorama_y_direction = random.randint(0, 1)
        self.panorama_direction = random.randint(0, 1)
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self._menu_init(WIDTH, HEIGHT)
        # MENU1.play(-1)

    @staticmethod
    def _pygame_init():
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        pygame.init()
        pygame.display.set_caption("Mineshaft", "Mineshaft")
        pygame.display.set_icon(pygame.image.load(
            os.path.join("assets", "textures", "blocks", "Grass.png")))
        pygame.mouse.set_visible(False)

    def _menu_init(self, width, height):
        self.menu = pygame_menu.Menu(
            "", width-100, height-100, theme=MINESHAFT_DEFAULT_THEME)
        self.menu.add.button('Start Game',  self.menu.toggle)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

        monitor = screeninfo.get_monitors()[0]

        self.menu.background = pygame.image.load(os.path.join(
            os.path.abspath(os.getcwd()), "assets", "panorama.jpeg"))
        self.menu.background = pygame.transform.scale(
            self.menu.background, (width*2, height*2))
        self.title = pygame.image.load(os.path.join("assets", "mineshaft.png"))
        self.title = pygame.transform.scale(
            self.title, (int(width), int(height/9)))

    def _update_panorama(self, currentpos):
        if currentpos[0] == 0:
            self.panorama_x_direction = 1

        elif currentpos[0] == -600:
            self.panorama_x_direction = 0

        if currentpos[1] == 0:
            self.panorama_y_direction = 1

        elif currentpos[1] == -500:
            self.panorama_y_direction = 0

        if self.panorama_x_direction == 0:
            currentpos[0] += 1

        elif self.panorama_x_direction == 1:
            currentpos[0] -= 1

        if self.panorama_y_direction == 0:
            currentpos[1] += 1

        elif self.panorama_y_direction == 1:
            currentpos[1] -= 1

        return currentpos

    def update_game(self):

        events = pygame.event.get()

        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.QUIT:
                sys.exit(pygame.quit())

        if self.menu.is_enabled():
            window_size = self.screen.get_size()
            self.menu.resize(window_size[0],  window_size[1])
            self.currentpanoramapos = self._update_panorama(
                self.currentpanoramapos)
            self.menu.update(events)

    def draw_game(self):

        self.screen.fill(WHITE)

        if self.menu.is_enabled():
            self.screen.blit(self.menu.background, self.currentpanoramapos)
            self.menu.draw(self.screen)
            self.screen.blit(self.title, [0, 0])

        pygame.display.flip()

        self.clock.tick(60)


game = Mineshaft()


while True:
    game.update_game()
    game.draw_game()
