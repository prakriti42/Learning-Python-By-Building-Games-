
import pygame
import numpy as np 

pygame.init()   #initilizing the pygame modules 
running  = True
FRAME_WIDTH = 600
FRAME_HEIGHT = 600
SCREEN_BGCOLOR = "#112A46"
LINE_COLOR = "#ACC8E5"
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 60 
CIRCLE_WIDTH = 15
SPACE = 55

screen = pygame.display.set_mode(size=(FRAME_WIDTH, FRAME_HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(SCREEN_BGCOLOR)

#pygame.draw.line(screen ,LINE_COLOR, (10,10) , (300,300) , 10, )  #starting precision, ending precision and width 


#board for the game 
board = np.zeros((BOARD_ROWS , BOARD_COLUMNS))


def drawLines():
        #first vertical lines 
        pygame.draw.line(screen ,LINE_COLOR, (200,10) , (200,590) , LINE_WIDTH )  #starting precision, ending precision and width 
        pygame.draw.line(screen ,LINE_COLOR, (400,10) , (400,590) , LINE_WIDTH )  #starting precision, ending precision and width 
        #for horizontal lines 
        pygame.draw.line(screen ,LINE_COLOR, (10,200) , (590,200) , LINE_WIDTH )  #starting precision, ending precision and width 
        pygame.draw.line(screen ,LINE_COLOR, (10,400) , (590,400) , LINE_WIDTH )  #starting precision, ending precision and width 

def markSquare(row, column , player):
    board[row][column] = player  

def availableSquare(row , column ):
    if board[row][column] == 0:
        return True
    else:
        return False 
def filled():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0: 
                return False 
    return True 

def drawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                print(row , col)
                pygame.draw.circle(screen , LINE_COLOR , ((col * 200 + 100 ) , ( row * 200 + 200 / 2 )), CIRCLE_RADIUS , CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, LINE_COLOR , (col * 200 + SPACE , row * 200 + 200 - SPACE ) , (col * 200 + 200 - SPACE , row * 200 + SPACE) , 15)
                pygame.draw.line(screen, LINE_COLOR , (col * 200 + SPACE , row * 200 + SPACE) , (col * 200 + 200 - SPACE , row * 200 + 200 - SPACE) , 15) 


drawLines()   
color = LINE_COLOR

def check_win(player):
    #vertical win check 
    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_wining_line(col, player)
            return True 

    #horizontal win check 
    for row in range(BOARD_ROWS):
        if board[row][0] ==player and board[row][1] ==player and board[row][2]==player:
            draw_horizontal_winning_line(row, player)
            return True  

    #for ascending diagonal win 
    if board[2][0] == player and board[1][1] == player and board[0][2] == player: 
           draw_asc_diagonal(player)
           return True 
    
     #for descending diagonal win 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: 
           draw_desc_diagonal(player)
           return True 

    return False 

def draw_vertical_wining_line(col , player):
    posX = col * 200 + 100 
    color = LINE_COLOR
    if (player == 1):
        color = LINE_COLOR
    elif (player == 2):
        color = LINE_COLOR

    pygame.draw.line(screen, LINE_COLOR , (posX , 15) , (posX, FRAME_HEIGHT -15) , 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100 
    if (player == 1):
        color = LINE_COLOR
    elif (player == 2):
        color = LINE_COLOR

    pygame.draw.line(screen, LINE_COLOR , (15, posY) , (FRAME_WIDTH - 15 , posY) , 15)

def draw_asc_diagonal(player):
    if (player == 1):
        color = LINE_COLOR
    elif (player == 2):
        color = LINE_COLOR

    pygame.draw.line(screen , LINE_COLOR , (15 , FRAME_HEIGHT - 15) , (FRAME_WIDTH - 15 , 15) , 15)
    

def draw_desc_diagonal(player):
    color = LINE_COLOR
    if (player == 1):
        color = LINE_COLOR
    elif (player == 2):
        color = LINE_COLOR

    pygame.draw.line(screen , LINE_COLOR , (15 , 15) , (FRAME_WIDTH - 15 , FRAME_HEIGHT- 15) , 15)

def restartGame():
    screen.fill(SCREEN_BGCOLOR)
    drawLines()
    player = 1 
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
           board[row][col] = 0  
drawLines()

print(board)
player = 1 
GameOver = False 

#main loop 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #This closes the screen upon pressing the close button
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not GameOver: #checks if we are clicking the screen
            mouseX = event.pos[0]
            mouseY = event.pos[1]
 
            clicked_row = mouseY // 200
            clicked_column = mouseX // 200

            print(clicked_row , clicked_column)

            if availableSquare(clicked_row , clicked_column):
                markSquare(clicked_row , clicked_column , player)
                if check_win(player):
                    GameOver = True 
                player = player % 2 + 1 
        

                drawFigures()

        if event.type == pygame.KEYDOWN:
            print("Key is down")
            if event.key == pygame.K_r:
                restartGame()
                GameOver= False 
        
        


    pygame.display.update()
