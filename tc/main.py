import numpy as np
from random import randint
import pygame,sys
from tkinter import messagebox

pygame.init()
width = 700
height = 700
board_rows = 3
board_cols = 3
board = np.zeros((board_rows, board_cols))
screen = pygame.display.set_mode((700, 700))


def color_rgb():
    return (randint(0, 255),randint(0, 255),randint(0, 255))

circle_color = color_rgb()
cross_color = color_rgb()

changePlayer = lambda player : 2 if player == 1 else 1

def vertical_wining_line(col,player):
    position_x = col * 240 + 100
    color = circle_color if player == 1 else cross_color
    pygame.draw.line(screen,color,(position_x,15),(position_x,height-10),10)
def horizontal_wining_line(row,player):
    position_y = row * 240 + 100
    color = circle_color if player == 1 else cross_color
    pygame.draw.line(screen, color, (10,position_y), (width-10,position_y), 10)

def diagonal_wining_line_top(player):
    color = circle_color if player == 1 else cross_color
    pygame.draw.line(screen, color, (10, height-10), (width-10, 10), 10)


def diagonal_wining_line_bottom(player):
    color = circle_color if player == 1 else cross_color
    pygame.draw.line(screen, color, (10, 10), (height-10, width-10), 10)



def win_check(player):
    flag = True

    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_wining_line(row,player)
            return flag


    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_wining_line(col,player)
            return flag


    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagonal_wining_line_bottom(player)
        return flag

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagonal_wining_line_top(player)
        return flag

    flag = False
    return flag

def draw_board_line(screen,line_color,line_start_position,line_end_position,line_width):
    pygame.draw.line(screen,line_color,line_start_position,line_end_position,line_width)

def marking_spot(row,col,player):
    board[row][col] = player

def available_spots(row,col):
    return board[row][col] == 0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def draw_shapes():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen,circle_color,(int(col*240+100),int(row*240+100)),40,10)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color,(col * 240 + 55, row * 240 + 200 - 55),
                                 (col * 240 + 200 - 55, row * 240 + 55), 20)
                pygame.draw.line(screen, cross_color, (col * 240 + 55, row * 240 + 55),
                                 (col * 240 + 200 - 55, row * 240 + 200 - 55), 20)


def game_play(coordinate_y,coordinate_x,player):
    game_check = False
    if available_spots(coordinate_y, coordinate_x):
            marking_spot(coordinate_y, coordinate_x, player)
            game_check = win_check(player)
            player = changePlayer(player)

    return player,game_check

def game_start(player):
    flag = False
    check = False
    game_check = False
    while flag is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
                check = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinate_x = int(event.pos[0] // 240)
                coordinate_y = int(event.pos[1] // 240)
                player,game_check = game_play(coordinate_y,coordinate_x,player)
                draw_shapes()
            if game_check == True:
                flag = True
                check = False


        pygame.display.update()
        if flag == True and check == False:
            winner = " won the match"
            player = changePlayer(player)
            messagebox.showinfo('                                HURRAY!            ', "Player: {}  have won the Match ".format(player))
        elif is_board_full():
            flag = True
            messagebox.showinfo('                           MATCH DRAWN ','MATCH HAS BEEN DRAWN')


def display_screen():
    line_color = color_rgb()
    background_color = color_rgb()
    line_width = 15
    pygame.display.set_caption( 'TIC TAC TOE')
    screen.fill(background_color)
    draw_board_line(screen,line_color,(0,240),(700,240 ),line_width)
    draw_board_line(screen, line_color, (0,500), (700,500), line_width)
    draw_board_line(screen, line_color, (240, 0), (240, 700), line_width)
    draw_board_line(screen, line_color, (500, 0), (500, 700), line_width)




if __name__ == "__main__":
    player = 1
    display_screen()
    game_start(player)