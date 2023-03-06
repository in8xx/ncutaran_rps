# File created by Nathan Cutaran
 
# imports funcions from libraries

from time import sleep

from random import randint

import pygame as pg

import os


# location of file
game_folder = os.path.dirname(__file__)
print(game_folder)


# colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (255, 255, 255)


# display window and frames
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
FPS = 30
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

# rps images, converting images into variables, making variables available throughout code base
global rock_image
rock_image = pg.image.load(os.path.join(game_folder, "rock.png")).convert()
global rock_rect
rock_rect = rock_image.get_rect()

global paper_image
paper_image = pg.image.load(os.path.join(game_folder, "paper.jpg")).convert()

global paper_rect
paper_rect = paper_image.get_rect()
paper_rect.y = SCREEN_WIDTH/2.2

global scissors_image
scissors_image = pg.image.load(os.path.join(game_folder, "scissors.png")).convert()
global scissors_rect
scissors_rect = scissors_image.get_rect()
scissors_rect.x = SCREEN_WIDTH-400

global pick_image
pick_image = pg.image.load(os.path.join(game_folder, "pick.png")).convert()
global pick_rect
pick_rect = pick_image.get_rect()
pick_rect.x = SCREEN_WIDTH-275
pick_rect.y = SCREEN_HEIGHT-125

global winner_image
winner_image = pg.image.load(os.path.join(game_folder, "winner1.png")).convert()
global winner_rect 
winner_rect = winner_image.get_rect()
winner_rect.x = SCREEN_WIDTH-200
winner_rect.y = SCREEN_HEIGHT-200

global loser_image
loser_image = pg.image.load(os.path.join(game_folder, "loser1.jpg")).convert()
global loser_rect
loser_rect = loser_image.get_rect()
loser_rect.x = SCREEN_WIDTH-200
loser_rect.y = SCREEN_HEIGHT-150

global draw_image
draw_image = pg.image.load(os.path.join(game_folder, "draw1.png")).convert()
global draw_rect
draw_rect = draw_image.get_rect()
draw_rect.x = SCREEN_WIDTH-200
draw_rect.y = SCREEN_HEIGHT-100


# creates a pygame display window with the assigned width and height
pg.init()
screen = pg.display.set_mode((700, 500))

# defines the button perameters, boarder, font, size etc...
def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pg.font.SysFont("Cascadia Code", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pg.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pg.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pg.draw.rect(screen, bg, (x, y, w , h))
    return screen.blit(text_render, (x, y)) 

# defines the buttons on the menu and what pygame does when each of the buttons are clicked on respectfully
def menu():
    pg.display.set_caption("menu")
    # creates what is displayed on the buttons
    b0 = button(screen, (10, 10), "Do you wanna play rock paper scissors?", 50, "white on black")
    b1 = button(screen, (150, 300), "Na", 40, "red on blue")
    b2 = button(screen, (450, 300), "Let's play", 40, "purple on green")

    # loop of the menu
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # quits pygame
                if b1.collidepoint(pg.mouse.get_pos()):
                    pg.quit()
                elif b2.collidepoint(pg.mouse.get_pos()):
                    play()
        pg.display.update()
    pg.quit()

# when button 2 is clicked, 'play' method is called upon is the same window
def play():
    pg.display.set_caption("rps game")

    # defines what choices can be chosen
    choices0 = ["rock", "paper", "scissors"]
    
    # randomizes the what the cpu chooses
    def cpu_choice():
        return choices0[randint(0,2)]
    
    # compares the user choice with the cpu choice and determines the winner based on the input of the user
    # blit essentially draws what images are being called
    def checkWin():
        if user_choice == "rock" and cpu_choice == "scissors":
            screen.blit(winner_image, winner_rect)
        elif user_choice == "rock" and cpu_choice == "paper":
            screen.blit(loser_image, loser_rect)
        elif user_choice == "paper" and cpu_choice == "rock":
            screen.blit(winner_image, winner_rect)
        elif user_choice == "paper" and cpu_choice == "scissors":
            screen.blit(loser_image, loser_rect) 
        elif user_choice == "scissors" and cpu_choice == "paper":
            screen.blit(winner_image, winner_rect) 
        elif user_choice == "scissors" and cpu_choice == "rock":
            screen.blit(loser_image, loser_rect) 
        elif user_choice == cpu_choice:
            screen.blit(draw_image, draw_rect)
        


            
    # main loop of rps
    cpu_screen = False
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONUP:
                global mouse_coords
                # get function gets the mouse cordinates location
                mouse_coords = pg.mouse.get_pos()
                # collide point is a selection tool through click mousepad
                # if rock is selected, then rock is user choice
                # the cpu then can compare with the user choice to the cpu choice through checkWin because the cpu_screen turns True
                if rock_rect.collidepoint(mouse_coords): 
                    user_choice = "rock"
                    print("you chose rock")
                    cpu_choice = choices0[randint(0,2)]
                    cpu_screen = True
                    checkWin()
                # if paper is selected, then paper is user choice
                # the cpu then can compare with the user choice to the cpu choice through checkWin because the cpu_screen turns True
                elif paper_rect.collidepoint(mouse_coords):
                    user_choice = "paper"
                    print("you chose paper")
                    cpu_choice = choices0[randint(0,2)]
                    cpu_screen = True
                    checkWin()
                # if scissors is selected, then scissors is user choice
                # the cpu then can compare with the user choice to the cpu choice through checkWin because the cpu_screen turns True
                elif scissors_rect.collidepoint(mouse_coords):
                    user_choice = "scissors"
                    print("you chose scissors")
                    cpu_choice = choices0[randint(0,2)]
                    cpu_screen = True
                    checkWin()
                else:
                    print("you clicked on nothing...")
            
            # after the user clicks on choice, the cpu choice displays itself
            screen.fill(BLACK)
            if cpu_screen:
                checkWin()
                if cpu_choice == "scissors":
                    # draws cpu choice as scissors
                    screen.blit(scissors_image, scissors_rect)
                    
                if cpu_choice == "paper":
                    # draws cpu choice as paper
                    screen.blit(paper_image, paper_rect)
                    
                if cpu_choice == "rock":
                    # draws cpu choice as rock
                    screen.blit(rock_image, rock_rect)
                         
                # button 3 is an option to quit and terminate pygame
                b3 = button(screen, (533, 260), "click here to quit", 30, "red on blue")
                if b3.collidepoint(mouse_coords):
                    print('quit')
                    pg.quit()

                # button 4 is an option to play again, restarting the play method
                b4 = button(screen, (410, 295), "click here twice to play again", 30, "purple on green")
                if b4.collidepoint(mouse_coords):
                    print('playagain')
                    play()

                b5 =  button(screen, (0,300), "cpu chose:", 40, "white on black")

            # draws the images and rectangles after button 2 is clicked
            else:
                screen.blit(scissors_image, scissors_rect)
                screen.blit(paper_image, paper_rect)
                screen.blit(rock_image, rock_rect)
                screen.blit(pick_image, pick_rect)
            # enables the images and rectangles to be shown
            pg.display.flip()

# calls the menu method to start python file
menu()
