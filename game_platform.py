import pygame


class Platform:
    IMG = pygame.image.load('static/platform.png')
    height = IMG.get_rect().height
    width = IMG.get_rect().width

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_rect(self):
        return pygame.Rect(self.x,
                           self.y,
                           self.IMG.get_rect().width,
                           self.IMG.get_rect().height)