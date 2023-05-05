import init_board
import game
import pygame
import button

#set FPS
FPS = 40
clock = pygame.time.Clock()

def main():
    #display game page
    pygame.init()
    board = init_board.board()
    go_bound = game.game(board)
    screen = go_bound.init_game()
    exit = pygame.image.load('image/button_exit.png').convert_alpha()
    restart = pygame.image.load('image/button_restart.png').convert_alpha()
    board.draw(screen)
    pygame.display.flip()
    is_black, move = True, 0

    #add beginning here
    while go_bound.running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go_bound.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed():
                x, y = pygame.mouse.get_pos()
                row = round((y - 40) / 40)
                col = round((x - 40) / 40)
                if board.is_empty(row, col):
                    board.move(row, col, is_black)
                    move += 1
                    is_black = not is_black
                    screen.fill([125, 95, 24])
                    board.draw(screen)
                    pygame.display.flip()
                    message = go_bound.is_win()
 
                    #all place has been occupied
                    if move == board.row * board.col:
                        message = 'tie'
                    if message != '':
                        go_bound.end_game_message(message, screen)
                        exit_button = button.game_button(exit)
                        restart_button = button.game_button(restart)
                        exit_pos = (game.width * 2 / 3 - button.button_width / 2, game.height * 2 / 3 - button.button_height)
                        restart_pos = (game.width / 3 - button.button_width / 2, game.height * 2 / 3 - button.button_height)
                        exit_rect = exit_button.draw(exit_pos[0], exit_pos[1], screen)
                        restart_rect = restart_button.draw(restart_pos[0], restart_pos[1], screen)
                        pygame.display.update()
                        input = go_bound.end_game_instruction(exit_rect, restart_rect)
                        print(input)
                        if input <= 1:
                            go_bound.running = False
                        elif input == 2:
                            board.reset()
                            is_black = True
                            go_bound = game.game(board)
                            screen = go_bound.init_game()
                            board.draw(screen)
                            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()