from init_board import *
import pygame

width = 640
height = 640

winning = 5

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
        pygame.mixer.music.load("music/music.mp3")
        pygame.mixer.music.play(-1)
        return screen

    def end_game_message(self, message, screen):
        font_style = "image/Sigmar-Regular.ttf"
        font = pygame.font.Font(font_style, 72)
        if message == 'Black' or message == 'White':
            text = font.render(message + '   Wins', True, red_color)
        else:
            text = font.render(message, True, red_color)
        text_rect = text.get_rect(center = (width / 2, height / 3))
        screen.blit(text, text_rect)

    def end_game_instruction(self, exit_rect, restart_rect):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
                        nx, ny = pygame.mouse.get_pos()
                        if exit_rect.collidepoint(nx, ny):
                            return 1
                        elif restart_rect.collidepoint(nx, ny):
                            return 2

    def is_win(self):
        for n in range(self.width):
            winning_flag = 0

            #check horizontal
            for i in range(self.length):
                if self.board_[n][i] == black:
                    winning_flag += 1
                    if winning_flag == winning:
                        print("Black Wins")
                        return 'Black'
                else:
                    winning_flag = 0
            winning_flag = 0
            for j in range(self.length):
                if self.board_[n][j] == white:
                    winning_flag += 1
                    if winning_flag == winning:
                        print("White Wins")
                        return "White"
                else:
                    winning_flag = 0
            winning_flag = 0

            #check vertical
            x = n
            for i in range(self.length):
                for _ in range(winning):
                    if self.board_[x][i] == black:
                        winning_flag += 1
                        x += 1
                        if winning_flag == winning:
                            print("Black Wins")
                            return 'Black'
                    else:
                        winning_flag = 0
            winning_flag = 0
            x = n
            for i in range(self.length):
                for _ in range(winning):
                    if self.board_[x][i] == white:
                        winning_flag += 1
                        x += 1
                        if winning_flag == winning:
                            print("White Wins")
                            return "White"
                    else:
                        winning_flag = 0
            winning_flag = 0

            #check diagonal
            r = n
            for c in range(self.length - winning):
                for _ in range(winning):
                    if self.board_[r][c] == black:
                        winning_flag += 1
                        r += 1
                        c += 1
                        if winning_flag == winning:
                            print("Black Wins")
                            return 'Black'
                    else:
                        winning_flag = 0
            winning_flag = 0
            r = n
            for c in range(self.length - winning):
                for _ in range(winning):
                    if self.board_[r][c] == white:
                        winning_flag += 1
                        r += 1
                        c += 1
                        if winning_flag == winning:
                            print("White Wins")
                            return 'White'
                    else:
                        winning_flag = 0
            winning_flag = 0
            r = n
            for c in range(self.length - 1, winning - 1, -1):
                for _ in range(winning):
                    if self.board_[r][c] == black:
                        winning_flag += 1
                        r += 1
                        c -= 1
                        if winning_flag == winning:
                            print("Black Wins")
                            return 'Black'
                    else:
                        winning_flag = 0
            winning_flag = 0
            r = n
            for c in range(self.length - 1, winning - 1, -1):
                for _ in range(winning):
                    if self.board_[r][c] == white:
                        winning_flag += 1
                        r += 1
                        c -= 1
                        if winning_flag == winning:
                            print("White Wins")
                            return 'White'
                    else:
                        winning_flag = 0
            winning_flag = 0

        return ''


                    
            
            
                        


