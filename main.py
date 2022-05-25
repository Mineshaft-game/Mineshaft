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


This program is licensed under the MIT License with additional restrictions.
The MIT License (With additional restrictions) should have come provided with this program. If not, read it online at github.com/Mineshaft-game/Mineshaft
Copyright 2021-2022 Alexey "LEHAtupointow" Pavlov <pezleha@gmail.com>
Copyright 2021 Sakurai Mayu/Mayu Sakurai

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
However, some of them like Eric, import only a few (e.g. only TODO, FIXME, WARNING and NOTE).



"""

__version__ = "ms-241221"
__author__ = "Alexey Pavlov"
__credits__ = "All contributors, see __doc__ for the project page"

CONFIG_DIR = ".mineshaft"
CONFIG_FILE = "config.dat"

# HACK: beautify imports, they're very ugly
# TODO: Sort the imports alphabetically
import os  # used for getting absolute paths and os-related things
import sys  # used for quitting the Python environment without breaking anything
import pickle  # parsing the config
import logging  # the only way to debug properly
import datetime  # used to get the exact date and time as a string
import time  # Getting the exact timestamp
import random  # used for randomizing things
import traceback
import pynbt

starttime = datetime.datetime.now()  # approximately the time the program started
starttimestamp = time.time()


if not os.path.exists(CONFIG_DIR):  # check if the .mineshaft directory exists
    os.mkdir(CONFIG_DIR)  # if not, create it

if os.path.exists(
    os.path.join(CONFIG_DIR, CONFIG_FILE)
):  # check if the configuration file exists
    config = pynbt.NBTFile(
        open(os.path.join(CONFIG_DIR, CONFIG_FILE), "rb")
    )  # if yes, then read from it

else:
    print(  # if not, print the warnings and create the config
        f"\
    [WARNING] Can't find {CONFIG_DIR}/{CONFIG_FILE},\n\
    [WARNING] creating one instead. Be careful, this configuration\n\
    [WARNING] may be broken or outdated. This happens at the first run.\n\
    [WARNING] When a directory should be created. Note that the paths are absolute."
    )
    defconfig = {
        "showdebug": pynbt.TAG_Int(0),
        "showfps": pynbt.TAG_Int(0),
        "showpygame": pynbt.TAG_Int(0),
        "showframedebug": pynbt.TAG_Int(0),
        "height": pynbt.TAG_Long(600),
        "width": pynbt.TAG_Long(850),
        "name": pynbt.TAG_String("Mineshaft"),
        "sdl_centered": pynbt.TAG_Int(1),
        "panorama_enabled": pynbt.TAG_Int(1),
        "fps": pynbt.TAG_Long(-1),
        "title_size": pynbt.TAG_Long(130),
        "font_size": pynbt.TAG_Long(90),
        "translation": pynbt.TAG_String("en"),
        "presence_id": pynbt.TAG_Long(923723525578166353),
        "assets_dir": pynbt.TAG_String("assets"),
    }

    with open(os.path.join(CONFIG_DIR, CONFIG_FILE), "wb") as dumpfile:
        pynbt.NBTFile(value=defconfig).save(dumpfile)

    with open(os.path.join(CONFIG_DIR, CONFIG_FILE), "rb") as openfile:
        config = pynbt.NBTFile(openfile)

if not os.path.exists(
    os.path.join(CONFIG_DIR, "logs")
):  # check if the logging folder exists
    os.mkdir(os.path.join(CONFIG_DIR, "logs"))

if config["showdebug"].value == 1:
    logging.basicConfig(
        level=logging.DEBUG, format=" %(asctime)s [%(levelname)s] -  %(message)s"
    )
else:
    logging.basicConfig(
        filename=os.path.join(
            CONFIG_DIR, "logs", str(starttime.strftime("%Y-%m-%d--%H%M%S")) + ".log"
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

HEIGHT = int(config["height"].value)
WIDTH = int(config["width"].value)

font_size = int(config["font_size"].value)

translation = str(config["translation"].value)

show_fps = int(config["showfps"].value)

panorama_enabled = int(config["panorama_enabled"].value)

if not int(config["showpygame"].value) == 0:
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
    logging.info("Pygame support message disabled")

if int(config["sdl_centered"].value) == 1:
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
import render
import render.wrapper.music as music

logging.debug("Imported Engine from ./render")

# World generation engine (e.g. gen1121, ./gen)
import gen

logging.debug("Imported world generator")


# index
from index.blocks import BLOCKS as blockindex
from index.font import minecraftfont
from index.lang import translations
from index.music import MENU
from index.themes import MINESHAFT_DEFAULT_THEME, MINESHAFT_SUBMENU_THEME

logging.info("imported index")


import pypresence

logging.info("Imported pypresence")

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


def save_config():
    with open(os.path.join(CONFIG_DIR, CONFIG_FILE)) as file:
        pickle.dump(config, file)


def set_config(key: str, value):
    config[key] = value


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
        self.currentpanoramapos = [0, 0]  # set up panorama position

        self.panorama_x_direction = random.randint(0, 1)  # panorama variables
        self.panorama_y_direction = random.randint(0, 1)
        self.panorama_direction = random.randint(0, 1)
        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT), pygame.RESIZABLE
        )  # the surface object
        logging.info(f"Surface is created ({self.screen})")
        self.clock = pygame.time.Clock()  # useful for FPS
        logging.info("FPS counter is created")
        self.blocks_sheet = pygame.image.load(
            os.path.join("assets", "textures", "terrain.png")
        )
        pygame.display.set_icon(  # set the icon
            pygame.transform.scale(
                self.blocks_sheet.subsurface(blockindex[2].imagecoords, (16, 16)),
                (128, 128),
            )
        )
        logging.debug("Icon is set")

        self.show_fps = show_fps

        self.show_df_intro()

        music.init_music()

        logging.info("Music wrapper initialized.")

        self._menu_sound_init()

        self.show_lusteria_intro()

        self._menu_init(WIDTH, HEIGHT)  # initialize the menu
        logging.info(f"Menu initialized ({self.menu})")
        # TODO: Add music to menu

        self._presence_init()
        self.position = [0, 0]

    def _presence_init(self):
        """Initialze the presence."""
        try:
            self.RPC = pypresence.Presence(
                int(config["presence_id"].value)
            )  # Initialize the client class
            self.RPC.connect()  # Start the handshake loop

            self.RPC_names = ["dirt", "grass", "bedrock", "stone"]

            self.RPC.update(
                state="RenderMite version " + render.__version__,
                details=__version__,
                small_image=random.choice(self.RPC_names),
                large_image="winter",
                buttons=[
                    {
                        "label": "Visit Mineshaft Website",
                        "url": "https://github.com/mineshaft-game",
                    }
                ],
                start=starttimestamp,
            )

            logging.info("Discord rich presence initialized")

        except:
            logging.warning("Could not initialize Discord rich presence, skipping.")
            logging.warning("The error was: " + traceback.format_exc())
            logging.info(
                "This can probably be ignored, if Discord is not present or there is no internet connection."
            )

    def _pygame_init(self):
        """Initialize Pygame"""
        pygame.init()  # initialize pygame
        logging.info("pygame initialization is sucessful")
        pygame.display.set_caption(
            _("Mineshaft"), _("Mineshaft")
        )  # the display caption

        # FIXME: It is still visible in pygame-menu
        pygame.mouse.set_visible(False)  # disable mouse Visibility
        logging.debug("Mouse is invisible")

    def _render_init(self):
        """Initialize the rendering engine"""
        self.engine = Engine(
            blockindex=blockindex, assets_dir=str(config["assets_dir"])
        )
        # TODO: Make it render

    def _menu_sound_init(self):
        self.soundengine = pygame_menu.sound.Sound()
        self.soundengine.set_sound(
            pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE,
            os.path.join("assets", "audio", "sound", "menu", "click.ogg"),
        )
        self.soundengine.set_sound(
            pygame_menu.sound.SOUND_TYPE_ERROR,
            os.path.join("assets", "audio", "sound", "menu", "error.ogg"),
        )

    def show_df_intro(self):
        """Show the Double Fractal title screen"""
        FREEZE_TIME = 30

        FPS = 60

        MOVEMENT_SPEED = 5

        introended = False

        df1 = pygame.image.load(os.path.join("assets", "logo", "df-1.png"))
        df2 = pygame.image.load(os.path.join("assets", "logo", "df-2.png"))
        logging.debug("Load Double Fractal title screen images")

        df1_pos = -105
        df2_pos = 500

        waits = 0

        self.do_break_intro = False

        while not introended:

            if df1_pos == 200 and df2_pos == 200:
                waits += 1

                if waits >= FREEZE_TIME:
                    introended = True

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_f:
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
            self.clock.tick(FPS)

    def show_lusteria_intro(self):
        FREEZE_TIME = 60

        lusteria_img = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "logo", "racuniverse.png")),
            (600, 600),
        )

        introended = False

        waits = 0

        x_pos = 100

        while not introended:

            waits += 1

            if waits == FREEZE_TIME:
                break

            if self.do_break_intro:
                break

            if x_pos >= 110:
                x_pos -= random.randint(1, 10)

            elif x_pos <= 90:
                x_pos += random.randint(1, 10)

            else:
                x_pos += random.randint(-5, 10)

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

        self.menu.set_sound(self.soundengine, recursive=True)

        logging.debug("Menu object created")

        self._submenu_settings_init(width, height)

        # set up title
        # TODO: Make the label and buttons resize with menu
        self.menu.add.image(os.path.join("assets", "logo", "mineshaft.png"))
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
            _("Settings"),
            self.settings_submenu,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
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

        music.load_music(random.choice(MENU))
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
        self.world = gen.generateSuperflatWorld()
        # TODO: Make this an actual singleplayer menu

    def _submenu_settings_init(self, width, height):
        """Initialize the settings submenu"""

        self.settings_submenu = pygame_menu.Menu(
            "", width, height, theme=MINESHAFT_SUBMENU_THEME
        )

        self._submenu_settings_display_init(width, height)

        self.settings_submenu.add.button(
            "Display",
            self.settings_submenu_display,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
            font_shadow_color=(255, 255, 255),
            align=pygame_menu.locals.ALIGN_LEFT,
        )
        self.settings_submenu.add.button(
            "Back",
            pygame_menu.events.BACK,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
            font_shadow_color=(255, 255, 255),
        )

        self.settings_submenu.disable()

        logging.debug("Disabled the settings submenu")

    def _submenu_settings_display_init(self, width, height):
        """The function that initializes the settings>display menu"""
        self.settings_submenu_display = pygame_menu.Menu(
            "", width, height, theme=MINESHAFT_SUBMENU_THEME
        )

        fps_discrete_range = {
            0: "Auto",
            15: "15",
            30: "30",
            60: "60",
            120: "120",
            200: "200",
        }

        self.settings_submenu_display.add.range_slider(
            "FPS",
            60,
            list(fps_discrete_range.keys()),
            value_format=lambda x: fps_discrete_range[x],
            width=500,
            font_color=(0, 0, 0),
            font_name=minecraftfont,
            font_size=font_size,
            range_text_value_tick_color=WHITE,
            slider_text_value_color=WHITE,
            slider_text_value_enabled=True,
            range_text_value_color=WHITE,
        )

        self.settings_submenu_display.add.button(
            "Back",
            pygame_menu.events.BACK,
            font_name=minecraftfont,
            font_size=font_size,
            font_color=(255, 255, 255),
            font_shadow_color=(255, 255, 255),
        )

        self.settings_submenu_display.disable()

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
                try:
                    self.RPC.clear()
                    self.RPC.close()
                except:
                    pass
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
                music.queue_music(random.choice(MENU))
        else:
            print("e")
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_w:
                        self.position[0] += 1

                    elif event.key == pygame.K_d:
                        self.position[1] -= 1
                        print("d")

        if self.settings_submenu.is_enabled():
            window_size = self.screen.get_size()  # get the surface size
            self.settings_submenu.resize(
                window_size[0], window_size[1]
            )  # resize the menu

    def draw_game(self):
        """Draw the game"""
        self.screen.fill(BG_COLOR)  # add the background to prevent distortion

        if self.menu.is_enabled():  # the menu is enabled
            if panorama_enabled:
                self.screen.blit(
                    self.menu.background, self.currentpanoramapos
                )  # blit the panorama
                logging.debug(f"Blit the panorama at {self.currentpanoramapos}")
            self.menu.draw(self.screen)  # blit menu
            logging.debug("Draw the menu")

        else:
            self.engine.render(self.screen, self.world, pos=self.position)

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
    try:
        main()
    except:
        logging.critical(
            "An error occured. The full output is: " + traceback.format_exc()
        )
        sys.exit(pygame.quit())
