
import pygame

#constant
empty = 0
black = 1
white = 2

board_length = 15
board_width = 15

#define color as global
black_color = [0, 0, 0]
white_color = [255, 255, 255]
red_color = [200, 20, 60]


class board(object):
    def __init__(self):
        self.row = board_width
        self.col = board_length
        self.game_board = [[empty] * board_length for _ in range(board_width)]

    #reset the board
    def reset(self):
        for r in range(self.row):
            for c in range(self.col):
                self.game_board[r][c] = empty

    #check location is empty
    def is_empty(self, row, col):
        return self.game_board[row][col] == empty 

    #place a piece
    def move(self, row, col, is_black):
        pieces = pygame.mixer.Sound("music/down.wav")
        pieces.play()
        self.game_board[row][col] = black if is_black else white
    
    #draw the board
    def draw(self, screen):

        #draw the board
        for line in range(1, board_width + 1):
            pygame.draw.line(screen, black_color, [40, line * 40], [600, line * 40])
            pygame.draw.line(screen, black_color, [line * 40, 40], [line * 40, 600])

        #add a frame
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)

        #add small circle
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)

        #draw piece
        for r in range(self.row):
            for c in range(self.col):
                if self.game_board[r][c] == black:
                    pygame.draw.circle(screen, black_color, [40 * (c + 1), 40 * (r + 1)], 18, 0)
                elif self.game_board[r][c] == white:
                    pygame.draw.circle(screen, white_color, [40 * (c + 1), 40 * (r + 1)], 18, 0)