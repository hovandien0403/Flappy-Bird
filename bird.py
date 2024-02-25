import pygame, time
from settings import *

class Bird:
    def __init__(self):
        self.bird_down = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
        self.bird_mid = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
        self.bird_up = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
        self.bird_list= [self.bird_down,self.bird_mid,self.bird_up] #0 1 2
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center = (100,384))
        self.bird_velocity = 0
        self.current_time = 0.0

        
    def flap(self):
        self.bird_velocity = -BIRD_VELOCITY

    def rotate_bird(self, bird1):
        self.new_bird = pygame.transform.rotozoom(bird1,-self.bird_velocity*3,1)
        return self.new_bird
    
    def bird_animation(self):
        if time.time() - self.current_time > BIRD_FLAP_TIME:
            self.current_time = time.time()
            if self.bird_index < 2:
                self.bird_index += 1
            else:
                self.bird_index = 0
        self.new_bird = self.bird_list[self.bird_index]
        self.new_bird_rect = self.new_bird.get_rect(center = (100,self.bird_rect.centery))
        self.new_bird_rect = self.new_bird_rect.inflate(0, 15)
        return self.new_bird, self.new_bird_rect
    
    def update(self):
        self.bird, self.bird_rect = self.bird_animation()
        self.rotated_bird = self.rotate_bird(self.bird)  
        self.bird_velocity += GRAVITY
        self.bird_rect.centery += self.bird_velocity

    def draw(self, screen):
        screen.blit(self.rotated_bird, self.bird_rect)

    def reset_bird(self):
        self.bird_rect.center = (100,384)
        self.bird_velocity = 0