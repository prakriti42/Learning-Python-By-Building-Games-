import pygame , sys

pygame.init()   #initilizing the pygame modules 
pygame.draw.circle(screen , "#ffffff" , (int(col * 50 + 50 / 2) , int( row * 50 + 50 / 2)), 20 , 20)

screen = pygame.display.set_mode(size=(200, 200))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(SCREEN_BGCOLOR)


while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
