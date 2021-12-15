#!/bin/python3
# -*- coding: utf-8 -*-
"""
Mineshaft

Mineshaft is a 2D clone/remake of a popluar game called Minecraft.

Important links:
Official Website: https://mineshaft.ml
Contact email: mineshaftgamemusic@gmail.com
Discord chat: https://dsc.gg/mineshaft2d
Official game wiki: https://mineshaft.fandom.com
Github organization: https://github.com/Mineshaft-game


This program is licensed under the Mineshaft License v0.2
The Mineshaft License should have come provided with this program. If not, read it online at github.com/Mineshaft-game/Mineshaft
Copyright 2021 Alexey "LEHAtupointow" Pavlov <pezleha@gmail.com>
Copyright 2021 Sakurai Mayu/Mayu Sakurai
This program comes with ABSOLUTELY NO WARRANTY, OF ANY KIND, and other legal jibber-jabber.

More information about Minecraft can be found online at http://wikipedia.org/wiki/Minecraft or on the official wiki: http://minecraft.fandom.com


Contribution style:
* Use these codetags in comments:
    * TODO: Introduces a general reminder about work that needs to be done.
    * FIXME: Introduces a reminder that this part of the code doesn't entirely work.
    * HACK:  Introduces a reminder that this part of the code works, perhaps barely, but that code should be improved.
    * WARNING: Something does not work.
    * XXX: Major problem.
    * NOTE: A note.
Most text editor plugins/IDEs should automatically import them into tasks.
However, some of them like Eric, import only some (e.g. only TODO, FIXME, WARNING and NOTE).



"""

__version__ = "ms-121221"
__author__ = "Alexey Pavlov"
__credits__ = "All contributors, see __doc__ for the project page"

CONFIG_DIR = ".mineshaft"
CONFIG_FILE = "mineshaft.conf"

# HACK: beautify imports, they're very ugly
# TODO: Sort the imports alphabetically
import os  # used for getting absolute paths and os-related things
import sys  # used for quitting the Python environment without breaking anything
import configparser  # parsing the config
import logging  # the only way to debug properly
import datetime  # used to get the exact date and time as a string
import random  # used for randomizing things

starttime = datetime.datetime.now()  # approximately the time the program started


if not os.path.exists(CONFIG_DIR):  # check if the .mineshaft directory exists
    os.mkdir(CONFIG_DIR)  # if not, create it

config = configparser.ConfigParser()

if os.path.exists(
    os.path.join(CONFIG_DIR, CONFIG_FILE)
):  # check if the configuration file exists
    config.read(os.path.join(CONFIG_DIR, CONFIG_FILE))  # if yes, then read from it

else:
    print(  # if not, print the warnings and create the config
        f"\
    [WARNING] Can't find {CONFIG_DIR}/{CONFIG_FILE},\n\
    [WARNING] creating one instead. Be careful, this configuration\n\
    [WARNING] may be broken or outdated.\n\
    [WARNING] Note that the paths are absolute."
    )
    open(
        os.path.join(CONFIG_DIR, CONFIG_FILE), "w"
    ).write(  # it's extremely ugly in a python script. Please note if you want to edit the default configuration, then edit it here
        "\
    [debug]\n\
    ; normal debug data, initliaziation, language file loading, warnings, etc\n\
    showdebug = 0\n\
    showfps = 0\n\
    \n\
    ; show pygame's adversiment\n\
    showpygame = 0\n\
    ; debug data from every frame, delays a lot. This will work only if you enable showdebug\n\
    showframedebug = 0\n\
    \n\
    \n\
    [display]\n\
    height = 600 \n\
    width = 800\n\
    name = Mineshaft\n\
    sdl_centered = 1\n\
    \n\
    [appearance]\n\
    title_size = 130\n\
    font_size = 90\n\
    \n\
    \n\
    [language]\n\
    translation = en\n\
    "
    )

    config.read(os.path.join(CONFIG_DIR, CONFIG_FILE))

if not os.path.exists(
    os.path.join(CONFIG_DIR, "logs")
):  # check if the logging folder exists
    os.mkdir(os.path.join(CONFIG_DIR, "logs"))

if int(config["debug"]["showdebug"]):
    logging.basicConfig(
        level=logging.DEBUG, format=" %(asctime)s [%(levelname)s] -  %(message)s"
    )
else:
    logging.basicConfig(
        filename=os.path.join(
            CONFIG_DIR, "logs", str(starttime.strftime("%Y-%m-%d %H%M%S")) + ".log"
        ),
        level=logging.INFO,
        format=" %(asctime)s [%(levelname)s] -  %(message)s",
    )


logging.debug("Hey developers, how's the debug working?")

logging.info(
    random.choice(  # this one here is for you to understand ;D
        [
            "The cake is a ~~lie~~ yummy treat.",
            "[Insert Numbers Here]",
            "Aw man, here we go again...",
            "D:",
        ]
    )
)

HEIGHT = int(config["display"]["height"])
WIDTH = int(config["display"]["width"])

font_size = int(config["appearance"]["font_size"])

translation = str(config["language"]["translation"])

show_fps = int(config["debug"]["showfps"])

if not int(config["debug"]["showpygame"]):
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    logging.info("Pygame support message disabled")

if int(config["display"]["sdl_centered"]):
    os.environ[
        "SDL_VIDEO_CENTERED"
    ] = "1"  # the environment variable that fixes issues on some platforms

    logging.info("SDL Video centered")


import pygame

logging.info("Imported pygame")


# import screeninfo # Temporarily unused
import python_lang as lang  # used for translations
import pygame_menu  # used for menu

logging.info("Import python_lang and pygame_menu successful")

# rendering
from render import Engine
import render.wrapper.music  as music

logging.debug("Imported Engine from ./render")

# World generation engine (e.g. gen1121, ./gen)
import gen

logging.debug("Imported world generator")

# these here are pretty self-explanatory
from libmineshaft.themes import MINESHAFT_DEFAULT_THEME  # menu themes

logging.info("Imported libmineshaft constants")

# index
from index.blocks import BLOCKS as blockindex
from index.font import minecraftevenings, minecraftfont
from index.lang import translations
from index.music import menu1,  menu2

logging.info("imported index")

# translation function
_ = lang.get
logging.debug("Created alias of lang.get as _")

lang_broken = False


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BG_COLOR = BLACK

# Helper functions
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def lang_not_found(s):
    """Is called when the language files aren't found"""
    return s + "⚙"  # add hint that file is not loaded


# Classes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# the heart and the story of the game
class Mineshaft:
    """The Heart and The Story of The Game"""

    # TODO: add __repr__ and __str__ methods to this class along with other useful dunder methods

    def __init__(self):  # the function called at the creation of the class
        """Initialize the class"""
        self._lang_init()  # initialize the translations
        self._pygame_init()  # initialize pygame
        self._render_init()
        self.currentpanoramapos = [0, 0,]  # set up panorama position 

        self.panorama_x_direction = random.randint(0, 1)  # panorama variables
        self.panorama_y_direction = random.randint(0, 1)
        self.panorama_direction = random.randint(0, 1)
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT), pygame.RESIZABLE
        )  # the surface object
        logging.info(f"Surface is created ({self.screen})")
        self.clock = pygame.time.Clock()  # useful for FPS
        logging.info("FPS counter is created")

        self.show_fps = show_fps

        self.show_df_intro()

        self.show_polarin_intro()
        
        music.init_music()

        self.show_lusteria_intro()

        self._menu_init(WIDTH, HEIGHT)  # initialize the menu
        logging.info(f"Menu initialized ({self.menu})")
        # TODO: Add music to menu

    @staticmethod
    def _pygame_init():
        """Initialize Pygame"""
        pygame.init()  # initialize pygame
        logging.info("pygame initialization is sucessful")
        pygame.display.set_caption(
            _("Mineshaft"), _("Mineshaft")
        )  # the display caption
        pygame.display.set_icon(  # set the icon
            pygame.image.load(os.path.join("assets", "textures", "blocks", "grass.png"))
        )
        logging.debug("Icon is set")
        # FIXME: It is still visible in pygame-menu
        pygame.mouse.set_visible(False)  # disable mouse Visibility
        logging.debug("Mouse is invisible")
        
    

    def _render_init(self):
        """Initialize the rendering engine"""
        self.engine = Engine(blockindex=blockindex)
        # TODO: Make it render

    def show_df_intro(self):

        """Show the Double Fractal title screen"""
        MOVEMENT_SPEED = 5

        introended = False

        df1 = pygame.image.load(os.path.join("assets", "logo", "df-1.png"))
        df2 = pygame.image.load(os.path.join("assets", "logo", "df-2.png"))

        df1_pos = -105
        df2_pos = 500

        waits = 0

        self.do_break_intro = False

        while not introended:

            if df1_pos == 200 and df2_pos == 200:
                waits += 1

                if waits >= 120:
                    introended = True

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_l:
                        self.show_fps = 1

                    elif event.key == pygame.K_q:
                        self.do_break_intro = True

            if self.do_break_intro:
                break

            self.screen.fill(BLACK)
            if df1_pos < 200:
                df1_pos += MOVEMENT_SPEED

            if df2_pos > 200:
                df2_pos -= MOVEMENT_SPEED
            self.screen.blit(df1, (200, df1_pos))
            self.screen.blit(df2, (305, df2_pos))

            pygame.display.flip()
            self.clock.tick(60)

    def show_polarin_intro(self):
        """Show the Polarin title screen"""
        MOVEMENT_SPEED = 5

        polarin_x_pos = -500

        polarin_logo = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "logo", "polarin.png")), (300, 300)
        )

        introended = False

        waits = 0

        while not introended:

            if polarin_x_pos < 200:
                polarin_x_pos += MOVEMENT_SPEED

            else:
                waits += 1

                if waits >= 120:
                    introended = True

            if self.do_break_intro:
                break

            self.screen.fill((242, 186, 5))
            self.screen.blit(polarin_logo, (polarin_x_pos, 160))
            pygame.display.flip()

            self.clock.tick(60)

    def show_lusteria_intro(self):

        lusteria_img = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "logo", "racuniverse.png")),
            (600, 600),
        )

        introended = False

        waits = 0
        
        x_pos = 100

        while not introended:

            waits += 1

            if waits == 60:
                break

            if self.do_break_intro:
                break
                
            
            if x_pos >= 110:
                x_pos -= random.randint(1, 10)
            
            elif x_pos <= 90 :
                x_pos += random.randint(1, 10)
            
            else:
                x_pos += random.randint(-5,  10)

            self.screen.fill(BLACK)

            self.screen.blit(lusteria_img, (x_pos, -50))

            pygame.display.flip()
            self.clock.tick(60)

    @staticmethod
    def _lang_init():  # initialize translations
        """Initialize the language loader"""
        global lang_broken, _

        for language in translations:
            if os.path.exists(translations[language]):
                lang.add(translations[language])
                logging.info(f"Load {language} translation")

            else:
                logging.warning(
                    f"Translation for {language} not found, setting _ to lang_not_found"
                )
                # TODO: Search for translations, and notify the user if they are not found on GUI start

                _ = lang_not_found
                lang_broken = True
                break

        # select a translation
        if not lang_broken:
            lang.select(translation)
            logging.info(f"{translation.title()} translation is selected")

    def _menu_init(self, width, height):
        """Initialize the menu"""
        self.menu = pygame_menu.Menu(  # set up the menu
            "", width - 100, height - 100, theme=MINESHAFT_DEFAULT_THEME
        )
        logging.debug("Menu object created")

        # set up title
        # TODO: Make the label and buttons resize with menu
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
            self._menu_singleplayer,
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
        logging.debug("Add buttons to menu")

        # TODO: add more buttons

        # unused right now
        # NOTE: This will be used for the TODO in the _update_panorama, see the function for details
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
        
        music.load_music(random.choice((menu1,  menu2)))
        music.play_music()

    def _update_panorama(self, currentpos):
        """Update the panorama position"""
        # finding out where should the panorama float
        # TODO: Make panorama understand the current window size and adapt to it
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

    def _menu_singleplayer(self):
        """Enter the singleplayer menu"""
        self.menu.toggle()
        self.world = gen.generateWorld()
        # TODO: Make this an actual singleplayer menu

    def update_game(self):
        """Update the game"""
        # get  the events
        events = pygame.event.get()
        # loop for every event
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:  # the screen got resized
                self.screen = pygame.display.set_mode(  # reset the screen
                    (event.w, event.h), pygame.RESIZABLE
                )
                logging.debug(f"Screen is resized to {event.w}x{event.h}")
            elif event.type == pygame.QUIT:  # the user clicked the quit button
                logging.info("Quitting, goodbye!")
                sys.exit(pygame.quit())  # safely quit the program

        if self.menu.is_enabled():  # the  menu is enabled
            window_size = self.screen.get_size()  # get the surface size
            self.menu.resize(window_size[0], window_size[1])  # resize the menu
            logging.debug("Resized the menu")
            self.currentpanoramapos = self._update_panorama(
                self.currentpanoramapos
            )  # update  the panorama position
            logging.debug("Update the panorama position")
            self.menu.update(
                events
            )  # make the menu safely update for every other event
            logging.debug("Updated the menu")
            
            self.fps = str(int(self.clock.get_fps()))
            logging.debug("Update fps")
            
            if not music.get_busy():
                music.load_music(random.choice((menu1,  menu2)))

    def draw_game(self):
        """Draw the game"""
        self.screen.fill(BG_COLOR)  # add the background to prevent distortion

        if self.menu.is_enabled():  # the menu is enabled
            self.screen.blit(
                self.menu.background, self.currentpanoramapos
            )  # blit the panorama
            logging.debug(f"Blit the panorama at {self.currentpanoramapos}")
            self.menu.draw(self.screen)  # blit menu
            logging.debug("Draw the menu")

        else:
            self.engine.render(self.screen, self.world)

        if self.show_fps:
            fps_text = pygame.font.Font(minecraftfont, 50).render(
                "FPS: " + self.fps, 1, (255, 255, 255)
            )
            self.screen.blit(fps_text, (0, 0))

        pygame.display.flip()  # fllip the display to show the changes
        logging.debug("Flipped the display")

        self.clock.tick(-1)  # fps


def main():
    """The function called when the module is run but not imported"""
    game = Mineshaft()  # create an instance of the game
    logging.debug(f"{game} is created")
    while True:  # main loop
        game.update_game()  # update the game
        logging.debug("Update the game (Events)")
        game.draw_game()  # draw the game
        logging.debug("Drew the game")


if __name__ == "__main__":
    main()
