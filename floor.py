import pygame
from settings import *

class Floor:
    def __init__(self):
        self.floor = pygame.image.load('assets/floor.png').convert()
        self.floor = pygame.transform.scale2x(self.floor)
        self.floor_x = FLOOR_X_POS

    def update(self):
        self.floor_x -= 3
        if self.floor_x <= -432:
            self.floor_x = 0

    def draw(self, screen):
        screen.blit(self.floor,(self.floor_x,650))
        screen.blit(self.floor,(self.floor_x+432,650))
