# import the needed modules
import pygame

# import screeninfo # Temporarily unused
import os #used for getting absolute paths and os-related things
import sys #used for quitting the Python environment without breaking anything
import random #used for randomizing things
import python_lang as lang #used for translations
import pygame_menu #used for menu

#these here are pretty self-explanatory
from libmineshaft.colors import WHITE #color constants
from libmineshaft.constants import WIDTH, HEIGHT #other general constants
from libmineshaft.themes import MINESHAFT_DEFAULT_THEME #menu themes
from libmineshaft.music import MENU1  #music components


#translation function
_ = lang.get 


#the heart and the story of the game
class Mineshaft:
    def __init__(self): #the function called at the creation of the class
        self._lang_init() #initialize the translations
        self._pygame_init() #initialize pygame
        self.currentpanoramapos = [random.randint(-1000, 0), random.randint(-500, 0)] #set up panorama position randomization
        self.panorama_x_direction = random.randint(0, 1) #panorama variables
        self.panorama_y_direction = random.randint(0, 1)
        self.panorama_direction = random.randint(0, 1)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) #the surface object
        self.clock = pygame.time.Clock() #useful for FPS
        self._menu_init(WIDTH, HEIGHT) #initialize the menu
        # MENU1.play(-1)

    @staticmethod
    def _pygame_init():
        os.environ["SDL_VIDEO_CENTERED"] = "1" #the environment variable that fixes issues on some platforms
        pygame.init() #initialize pygame
        pygame.display.set_caption(_("Mineshaft"), _("Mineshaft")) #the display caption
        pygame.display.set_icon( #set the icon
            pygame.image.load(os.path.join("assets", "textures", "blocks", "Grass.png"))
        )
        pygame.mouse.set_visible(False) #disable mouse Visibility

    @staticmethod
    def _lang_init(): #initialize translations
        #translation files
        lang.add(os.path.join("lang", "en.xml"))
        lang.add(os.path.join("lang", "de.xml"))
        lang.add(os.path.join("lang", "ru.xml"))
        #select a translations
        lang.select("en") 

    def _menu_init(self, width, height):
        self.menu = pygame_menu.Menu( #set up the menu
            "", width - 100, height - 100, theme=MINESHAFT_DEFAULT_THEME
        )

        #add buttons
        self.menu.add.button(_("Start Game"), self.menu.toggle)
        self.menu.adandd.button(_("Quit"), pygame_menu.events.EXIT)

        # unused right now
        # monitor = screeninfo.get_monitors()[0]
        
        #set up the panorama
        self.menu.background = pygame.image.load(
            os.path.join(os.path.abspath(os.getcwd()), "assets", "panorama.jpeg")
        )
        self.menu.background = pygame.transform.scale(
            self.menu.background, (width * 2, height * 2)
        )

        #set up title
        self.title = pygame.image.load(os.path.join("assets", "mineshaft.png"))
        self.title = pygame.transform.scale(self.title, (int(width), int(height / 9)))

    def _update_panorama(self, currentpos):
        #finding out where should the panorama float
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
        #get  the events
        events = pygame.event.get()
        #loop for every event
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE: #the screen got resized
                self.screen = pygame.display.set_mode( #reset the screen
                    (event.w, event.h), pygame.RESIZABLE
                )
            elif event.type == pygame.QUIT: #the user clicked the quit button
                sys.exit(pygame.quit()) #safely quit the program

        if self.menu.is_enabled(): #the  menu is enabled
            window_size = self.screen.get_size() #get the surface size
            self.menu.resize(window_size[0], window_size[1]) #resize the menu
            self.currentpanoramapos = self._update_panorama(self.currentpanoramapos) #update  the panorama position
            self.menu.update(events) #make the menu safely update for every other event

    def draw_game(self):

        self.screen.fill(WHITE) #add the background to prevent distortion

        if self.menu.is_enabled(): #the menu is enabled
            self.screen.blit(self.menu.background, self.currentpanoramapos) #blit the panorama
            self.menu.draw(self.screen) #blit menu
            self.screen.blit(self.title, [0, 0]) #blit title

        pygame.display.flip() #fllip the display to show the changes

        self.clock.tick(60) #fps


game = Mineshaft() #create an instance of the game


while True: #main loop
    game.update_game() #update the game
    game.draw_game() #draw the game

