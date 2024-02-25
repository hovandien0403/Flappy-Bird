import pygame
import random, time
from settings import *

class Pipe:
    def __init__(self):
        self.pipe = pygame.image.load('assets/pipe-green.png').convert()
        self.pipe = pygame.transform.scale2x(self.pipe)
        self.pipe_list =[]
        self.pipe_height = PIPE_HEIGHT
        self.current_time = 0.0

    def update(self):
        if time.time() - self.current_time > PIPE_SPAWN_TIME:
                self.current_time = time.time()
                self.pipe_list.extend(self.create_pipe())  
            
        for pipe in self.pipe_list:
            pipe.centerx -= PIPE_VELOCITY
        
    def draw(self, screen):
        for pipe in self.pipe_list:
            if pipe.bottom >= 600 : 
                screen.blit(self.pipe,pipe)
            else:
                self.flip_pipe = pygame.transform.flip(self.pipe,False,True)
                screen.blit(self.flip_pipe,pipe)

    def create_pipe(self):
        self.random_pipe_pos = random.choice(self.pipe_height)
        self.bottom_pipe = self.pipe.get_rect(midtop =(500,self.random_pipe_pos))
        self.top_pipe = self.pipe.get_rect(midtop =(500,self.random_pipe_pos-750))
        return self.bottom_pipe, self.top_pipe
    
    def reset_pipe(self): 
        self.pipe_list.clear()