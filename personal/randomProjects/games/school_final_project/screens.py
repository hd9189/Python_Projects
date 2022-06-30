import pygame
import os

#defining the fpsm
FPS = 60

#defining the width and height of the window
WIDTH, HEIGHT = 1000, 750



HOME = pygame.image.load(
    os.path.join('Assets', 'home_screen.png'))
HOW_TO_PLAY1 = pygame.image.load(
    os.path.join('Assets', 'how_to_play1.png'))
HOW_TO_PLAY2 = pygame.image.load(
    os.path.join('Assets', 'how_to_play2.png'))
P1_WIN = pygame.image.load(
    os.path.join('Assets', 'p1_won.png'))
P2_WIN = pygame.image.load(
    os.path.join('Assets', 'p2_won.png'))
TIE = pygame.image.load(
    os.path.join('Assets', 'tie.png'))

#----------------------------------------
#setting coordinates of each buttons top left and bottom corners
#----------------------------------------

#HOME SCREEN BUTTONS
CLICK_TO_PLAY_XPOS = (51, 943)
CLICK_TO_PLAY_YPOS = (244, 409)

HOW_TO_PLAY_XPOS = (49, 948)
HOW_TO_PLAY_YPOS = (459, 621)

QUIT_GAMEX = (277, 737)
QUIT_GAMEY = (679, 748)

#HOW TO PLAY BUTTONS

BACK_XPOS = (278, 738)
BACK_YPOS = (672, 748)

BACK2_XPOS = (264, 495)
BACK2_YPOS = (675, 749)

EXIT_XPOS = (507, 732)
EXIT_YPOS = (675, 747)



def home(WINDOW):
    '''
    Runs the home screen and pauses until a click event happens
    Parameters:
        WINDOW: window of game
    Returns:
        screen_number: int value to indicate which screen the user wants to go to
    '''
    #forces function to run until something is returned
    while True:
        WINDOW.blit(HOME, (0,0))
        click = pygame.event.wait()
        #get the position of moise
        mouse_posx, mouse_posy = pygame.mouse.get_pos()

        # if the event is mouse down
        if click.type == pygame.MOUSEBUTTONDOWN:
            if mouse_posx in range(CLICK_TO_PLAY_XPOS[0], CLICK_TO_PLAY_XPOS[1]+1) and mouse_posy in range(CLICK_TO_PLAY_YPOS[0], CLICK_TO_PLAY_YPOS[1]+1):
                return 3
            elif mouse_posx in range(HOW_TO_PLAY_XPOS[0], HOW_TO_PLAY_XPOS[1]+1) and mouse_posy in range(HOW_TO_PLAY_YPOS[0], HOW_TO_PLAY_YPOS[1]+1):
                return 2
            # elif mouse_posx in range(QUIT_GAMEX) and mouse_posy in range(QUIT_GAMEY):
            #     return 0
            elif mouse_posx in range(QUIT_GAMEX[0], QUIT_GAMEX[1]+1) and mouse_posy in range(QUIT_GAMEY[0], QUIT_GAMEY[1]+1):
                return 0

        pygame.display.update()

def how_to_play(WINDOW):
    '''
    Runs the how to play window
    Parameters:
        WINDOW: window
    Returns:
        screen_number: int value to indicate which screen the user wants to go to
    '''
    while True:
        
        #draws screen
        WINDOW.blit(HOW_TO_PLAY1, (0,0))
        click = pygame.event.wait()
        mouse_posx, mouse_posy = pygame.mouse.get_pos()

        if click.type == pygame.MOUSEBUTTONDOWN:
            if mouse_posx in range(BACK2_XPOS[0], BACK_XPOS[1]+1) and mouse_posy in range(BACK_YPOS[0], BACK_YPOS[1]+1):
                return 5

        pygame.display.update()

def how_to_play_next(WINDOW):
    '''
    Runs the next how to play window
    Parameters:
        WINDOW: window
    Returns:
        screen: int
    '''
    while True:
        WINDOW.blit(HOW_TO_PLAY2, (0,0))
        click = pygame.event.wait()
        mouse_posx, mouse_posy = pygame.mouse.get_pos()

        if click.type == pygame.MOUSEBUTTONDOWN:
            if mouse_posx in range(BACK2_XPOS[0], BACK2_XPOS[1]+1) and mouse_posy in range(BACK2_YPOS[0], BACK2_YPOS[1]+1):
                return 2
            elif mouse_posx in range(EXIT_XPOS[0], EXIT_XPOS[1]+1) and mouse_posy in range(EXIT_YPOS[0], EXIT_YPOS[1]+1):
                return 1

        pygame.display.update()

def win(WINDOW, p1_score, p2_score):
    '''
    Runs the how to play window
    Parameters:
        WINDOW: window of pygame
        p1_score: int value of player 1 score
        p2_score: int value of player 2 score
    Returns:
        screen_number: int value to indicate which screen the user wants to go to
    '''
    #deciding on which screen to draw on window depending on score
    if p1_score == p2_score:
        won = TIE
    elif p1_score > p2_score:
        won = P1_WIN
    else: won = P2_WIN
    #runs until something is returned
    while True:
        WINDOW.blit(won, (0,0))
        click = pygame.event.wait()
        mouse_posx, mouse_posy = pygame.mouse.get_pos()

        if click.type == pygame.MOUSEBUTTONDOWN:
            #back button
            if mouse_posx in range(BACK_XPOS[0], BACK_XPOS[1]+1) and mouse_posy in range(BACK_YPOS[0], BACK_YPOS[1]+1):
                return 1

        pygame.display.update()
