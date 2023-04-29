from init_board import *
import pygame

width = 640
height = 640

class game(object):

    def __init__(self, board):
        self.running = True
        self.length = board_length
        self.width = board_width
        self.board_ = board.game_board

    def init_game(self):
        pygame.display.set_caption("GO_Bound")
        screen = pygame.display.set_mode((width, height))
        screen.fill([125, 95, 24])
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
        return screen


    def is_win(self):
        for n in range(self.width):
            winning_flag = 0

            #check horizontal
            for i in range(self.length):
                if self.board_[n][i] == black:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("Black Wins")
                        return True
                else:
                    winning_flag = 0
            winning_flag = 0
            for j in range(self.length):
                if self.board_[n][i] == white:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("White Wins")
                        return True
                else:
                    winning_flag = 0
            winning_flag = 0

            #check vertical
            for i in range(n, self.width):
                if self.board_[n][i] == black:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("Black Wins")
                        return True
                    else:
                        winning_flag = 0
            winning_flag = 0
            for j in range(n, self.width):
                if self.board_[n][i] == white:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("White Wins")
                        return True
                else:
                    winning_flag = 0   
            winning_flag = 0

            #check diagonal
            r = n
            c = 0
            while 0 <= r < self.length and 0 <= c < self.width:
                if self.board_[r][c] == black:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("Black Wins")
                        return True
                else:
                    winning_flag = 0
                r += 1
                c += 1
            winning_flag = 0
            r = n
            c = 0
            while 0 <= r < self.length and 0 <= c < self.width:
                if self.board_[r][c] == white:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("White Wins")
                        return True
                else:
                    winning_flag = 0
                r += 1
                c += 1
            winning_flag = 0
            while 0 <= r < self.length and 0 <= c < self.width:
                if self.board_[r][c] == black:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("Black Wins")
                        return True
                else:
                    winning_flag = 0
                r -= 1
                c += 1
            winning_flag = 0
            while 0 <= r < self.length and 0 <= c < self.width:
                if self.board_[r][c] == white:
                    winning_flag += 1
                    if winning_flag == 5:
                        print("White Wins")
                        return True
                else:
                    winning_flag = 0
                r -= 1
                c += 1
            winning_flag = 0

        return False


                    
            
            
                        


