import pygame

button_width = 100
button_height = 100

class game_button(object):
    def __init__(self, image):
        self.button_image = image

    #draw button on screen
    def draw(self, left, top, screen):
        button = pygame.transform.scale(self.button_image, (button_width, button_height))
        button_rect = pygame.Rect(left, top, button_width, button_height)
        screen.blit(button, button_rect)
        return button_rect


