import pygame
from settings import *

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.Font('04B_19.ttf',35)

    def score_display(self, screen, game_state):
        
        if game_state == True:
            self.score_surface = self.game_font.render(str(int(self.score)),True,(255,255,255))
            self.score_rect = self.score_surface.get_rect(center = (216,100))
            screen.blit(self.score_surface, self.score_rect)

        if game_state == False:
            if self.score > self.high_score:
                self.high_score = self.score

            self.score_surface = self.game_font.render(f'Score: {int(self.score)}',True,(255,255,255))
            self.score_rect = self.score_surface.get_rect(center = (216,100))
            screen.blit(self.score_surface,self.score_rect)

            self.high_score_surface = self.game_font.render(f'High Score: {int(self.high_score)}',True,(255,255,255))
            self.high_score_rect = self.high_score_surface.get_rect(center = (216,630))
            screen.blit(self.high_score_surface,self.high_score_rect)

    
    def increase_score(self):
        self.score += 1
