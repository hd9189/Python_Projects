import pygame
import os

#defining the fpsm
FPS = 60

#defining the width and height of the window
WIDTH, HEIGHT = 1000, 750



HOME = pygame.image.load(
    os.path.join('Assets', 'home_screen.png'))
HOME = pygame.transform.scale(HOME, (WIDTH, HEIGHT))

#----------------------------------------
#setting coordinates of each buttons top left and bottom corners
CLICK_TO_PLAY_XPOS = (288, 738)
CLICK_TO_PLAY_YPOS = (307, 436)

HOW_TO_PLAY_XPOS = (281, 743)
HOW_TO_PLAY_YPOS = (528, 647)

QUIT_GAMEX = ()
QUIT_GAMEY = ()

def home(WINDOW):
    '''
    Parameters:
        None
    Returns:
        screen_number: int value to indicate which screen the user wants to go to
    '''
    while True:
        WINDOW.blit(HOME, (0,0))
        click = pygame.event.wait()
        mouse_posx, mouse_posy = pygame.mouse.get_pos()

        if click.type == pygame.MOUSEBUTTONDOWN:
            if mouse_posx in range(CLICK_TO_PLAY_XPOS[0], CLICK_TO_PLAY_XPOS[1]+1) and mouse_posy in range(CLICK_TO_PLAY_YPOS[0], CLICK_TO_PLAY_YPOS[1]+1):
                return 3
            elif mouse_posx in range(HOW_TO_PLAY_XPOS[0], HOW_TO_PLAY_XPOS[1]+1) and mouse_posy in range(HOW_TO_PLAY_YPOS[0], HOW_TO_PLAY_YPOS[1]+1):
                return 2
            # elif mouse_posx in range(QUIT_GAMEX) and mouse_posy in range(QUIT_GAMEY):
            #     return 0
            else:
                return 1

        pygame.display.update()
