#!/bin/python3
"""
Mineshaft

This program was designed to break, but (unfortunately) works, so if it doesn't work at all, ~~don't~~ leave it. 
Who's Joe? Joe Mama!

This program is licensed under the Mineshaft License v0.2
Copyright 2021 Alexey "LEHAtupointow" Pavlov <pezleha@gmail.com>
Copyright 2021 Mayu Sakurai
This program comes with ABSOLUTELY NO WARRANTY, OF ANY KIND, and other legal jibber-jabber.

"""


import os  # used for getting absolute paths and os-related things
import sys  # used for quitting the Python environment without breaking anything
import configparser  # parsing the config
import logging
import datetime
import random  # used for randomizing things

starttime = datetime.datetime.now()


if not os.path.exists(".mineshaft"):
    os.mkdir(".mineshaft")

config = configparser.ConfigParser()

if os.path.exists(os.path.join(".mineshaft", "mineshaft.conf")):
    config.read(os.path.join(".mineshaft", "mineshaft.conf"))

else:
    print(
        "\
    [WARNING] Can't find .mineshaft/mineshaft.conf,\n\
    [WARNING] creating one instead. Be careful, this configuration\n\
    [WARNING] may be broken or outdated.\n\
    [WARNING] Note that the paths are absolute."
    )
    open(
        os.path.join(".mineshaft", "mineshaft.conf"), "w"
    ).write(  # it's extremely ugly in a python script.
        """
        [debug]
        ; normal debug data, initliaziation, language file loading, warnings, etc
        showdebug = 0
        
        ; show pygame's adversiment
        showpygame = 0
        ; debug data from every frame, delays a lot. This will work only if you enable showdebug 
        showframedebug = 0
        
        
        [display]
        height = 600 
        width = 800
        name = Mineshaft 
        
        [appearance]
        title_size = 130
        font_size = 90
        
        
        [language]
        translation = en 
        """
    )

    config.read(os.path.join(".mineshaft", "mineshaft.conf"))


if int(config["debug"]["showdebug"]):
    logging.basicConfig(
        level=logging.DEBUG, format=" %(asctime)s [%(levelname)s] -  %(message)s"
    )
else:
    logging.basicConfig(
        filename=os.path.join(".mineshaft", "logs", str(starttime) + ".log"),
        level=logging.INFO,
        format=" %(asctime)s [%(levelname)s] -  %(message)s",
    )


logging.debug("Hey developers, how's the debug working?")

logging.info(
    random.choice(
        [
            "The cake is a yummy treat.",
            "[Insert Numbers Here]",
            "Aw man, here we go again...",
            "Dark Member",
            "Dank Memer",
            "Woo!",
            "Hope this won't be a crash report...",
            "The only sentence that is interesting a tiny bit is now a bad one.",
            ":(",
            ":)",
            ":D",
            "D:",
        ]
    )
)

HEIGHT = int(config["display"]["height"])
WIDTH = int(config["display"]["width"])

font_size = int(config["appearance"]["font_size"])

translation = str(config["language"]["translation"])

if not int(config["debug"]["showpygame"]):
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    logging.info("Pygame support message disabled")


import pygame

logging.info("Imported pygame")


# import screeninfo # Temporarily unused
import python_lang as lang  # used for translations
import pygame_menu  # used for menu

logging.info("Import python_lang and pygame_menu successful")

# rendering
# from render import Engine
# debug("Imported Engine from render")

# these here are pretty self-explanatory
from libmineshaft.colors import WHITE  # color constants
from libmineshaft.themes import MINESHAFT_DEFAULT_THEME  # menu themes

logging.info("Imported libmineshaft constants")

# index
# from index.blocks import BLOCKS
from index.font import minecraftevenings, minecraftfont
from index.lang import translations

logging.info("imported index")

# translation function
_ = lang.get
logging.debug("Created alias of lang.get as _")

lang_broken = False

# Helper functions
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def lang_not_found(str):
    """Is called when the language files arent found"""
    return str + "⚙"  # add hint that file is not loaded


# Classes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# the heart and the story of the game
class Mineshaft:
    def __init__(self):  # the function called at the creation of the class
        self._lang_init()  # initialize the translations
        self._pygame_init()  # initialize pygame
        self.currentpanoramapos = [
            random.randint(-1000, 0),
            random.randint(-500, 0),
        ]  # set up panorama position randomization
        self.panorama_x_direction = random.randint(0, 1)  # panorama variables
        self.panorama_y_direction = random.randint(0, 1)
        self.panorama_direction = random.randint(0, 1)
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT), pygame.RESIZABLE
        )  # the surface object
        logging.info(f"Surface is created ({self.screen})")
        self.clock = pygame.time.Clock()  # useful for FPS
        logging.info("FPS counter is created")
        self._menu_init(WIDTH, HEIGHT)  # initialize the menu
        logging.info(f"Menu initialized ({self.menu})")
        # MENU1.play(-1)

    @staticmethod
    def _pygame_init():
        os.environ[
            "SDL_VIDEO_CENTERED"
        ] = "1"  # the environment variable that fixes issues on some platforms
        pygame.init()  # initialize pygame
        logging.info("pygame initialization is sucessful")
        pygame.display.set_caption(
            _("Mineshaft"), _("Mineshaft")
        )  # the display caption
        pygame.display.set_icon(  # set the icon
            pygame.image.load(os.path.join("assets", "textures", "blocks", "grass.png"))
        )
        logging.debug("Icon is set")
        pygame.mouse.set_visible(False)  # disable mouse Visibility
        logging.debug("Mouse is invisible")

    # def _render_init(self):
    #    self.engine = Engine(blockindex=BLOCKS)

    @staticmethod
    def _lang_init():  # initialize translations
        global lang_broken, _

        for language in translations:
            if os.path.exists(translations[language]):
                lang.add(translations[language])
                logging.info(f"Load {language} translation")

            else:
                logging.warning(
                    f"Translation for {language} not found, setting _ to lang_not_found"
                )

                _ = lang_not_found
                lang_broken = True
                break

        # select a translation
        if not lang_broken:
            lang.select(translation)
            logging.info(f"{translation.title()} translation is selected")

    def _menu_init(self, width, height):
        self.menu = pygame_menu.Menu(  # set up the menu
            "", width - 100, height - 100, theme=MINESHAFT_DEFAULT_THEME
        )
        logging.debug("Menu object created")

        # set up title
        self.menu.add.label(
            "Mineshaft",
            font_name=minecraftevenings,
            font_size=130,
            font_color=(0, 0, 0),
            font_shadow_color=(255, 255, 255),
        )
        logging.debug("Add title label")

        # add buttons
        self.menu.add.button(
            _("Start Game"),
            self.menu.toggle,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
            font_shadow_color=(255, 255, 255),
        )

        self.menu.add.button(
            _("Quit"),
            pygame_menu.events.EXIT,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
            font_shadow_color=(255, 255, 255),
        )
        logging.debug("Add buttons")

        # unused right now
        # monitor = screeninfo.get_monitors()[0]

        # set up the panorama
        self.menu.background = pygame.image.load(
            os.path.join("assets", "panorama.jpeg")
        )
        logging.debug("Load panorama")
        self.menu.background = pygame.transform.scale(
            self.menu.background, (width * 2, height * 2)
        )
        logging.debug("Resize panorama")

    def _update_panorama(self, currentpos):
        # finding out where should the panorama float
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
        # get  the events
        events = pygame.event.get()
        # loop for every event
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:  # the screen got resized
                self.screen = pygame.display.set_mode(  # reset the screen
                    (event.w, event.h), pygame.RESIZABLE
                )
            elif event.type == pygame.QUIT:  # the user clicked the quit button
                logging.info("Quitting, goodbye!")
                sys.exit(pygame.quit())  # safely quit the program

        if self.menu.is_enabled():  # the  menu is enabled
            window_size = self.screen.get_size()  # get the surface size
            self.menu.resize(window_size[0], window_size[1])  # resize the menu
            self.currentpanoramapos = self._update_panorama(
                self.currentpanoramapos
            )  # update  the panorama position
            self.menu.update(
                events
            )  # make the menu safely update for every other event

    def draw_game(self):

        self.screen.fill(WHITE)  # add the background to prevent distortion

        if self.menu.is_enabled():  # the menu is enabled
            self.screen.blit(
                self.menu.background, self.currentpanoramapos
            )  # blit the panorama
            self.menu.draw(self.screen)  # blit menu

        pygame.display.flip()  # fllip the display to show the changes

        self.clock.tick(60)  # fps


game = Mineshaft()  # create an instance of the game


while True:  # main loop
    game.update_game()  # update the game
    game.draw_game()  # draw the game
