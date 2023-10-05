import pygame


class Player:
    IMG_LEFT = pygame.image.load('static/corgi-left.png')
    IMG_RIGHT = pygame.image.load('static/corgi-right.png')
    width = IMG_RIGHT.get_rect().width
    height = IMG_RIGHT.get_rect().height
    speed = 25
    default_jump_cap = 12

    def __init__(self, start_pos_x, start_pos_y):
        self.x = start_pos_x
        self.y = start_pos_y
        self.orientation = 'R'
        self.jump_cap = self.default_jump_cap
        self.fall_cap = 0

    def image(self):
        if self.orientation == 'R':
            return self.IMG_RIGHT
        else:
            return self.IMG_LEFT

    def move(self, orientation):
        if orientation == 'R' or orientation == 'L':
            if self.orientation != orientation:
                self.orientation = orientation

            if self.orientation == 'R':
                self.x += self.speed
            else:
                self.x -= self.speed
        else:
            raise ValueError

    def update(self):
        if self.jump_cap:
            self.y -= self.jump_cap
            self.jump_cap -= 1
        else:
            self.y += self.fall_cap
            self.fall_cap += 1

    def bounce(self):
        self.jump_cap = self.default_jump_cap
        self.fall_cap = 0

    def get_rect(self):
        return pygame.Rect(self.x,
                           self.y,
                           self.image().get_rect().width,
                           self.image().get_rect().height)
