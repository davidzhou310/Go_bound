import init_board
import game
import pygame

#set FPS
FPS = 40
clock = pygame.time.Clock()

def main():
    #display game page
    pygame.init()
    board = init_board.board()
    go_bound = game.game(board)
    screen = go_bound.init_game()
    board.draw(screen)
    pygame.display.flip()
    is_black, move = True, 0

    #add beginning here
    while go_bound.running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go_bound.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                #sound
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
                    if go_bound.is_win():
                        go_bound.running = False

                    #all place has been occupied
                    if move == board.row * board.col:
                        go_bound.running = False
    #add ending here 
    pygame.quit()


if __name__ == '__main__':
    main()