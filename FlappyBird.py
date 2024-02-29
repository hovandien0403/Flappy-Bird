import pygame, time
import sys
from bird import Bird
from pipe import Pipe
from floor import Floor
from score import Score
from sound import *
from settings import *

class FlappyBird:
    def __init__(self):

        #Tạo hàm cho trò chơi
        pygame.init()
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        #Chèn background
        self.bg = pygame.image.load('assets/background-night.png').convert()
        self.bg = pygame.transform.scale2x(self.bg)
        
        #Chèn Menu
        self.game_menu_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
        self.game_menu_rect = self.game_menu_surface.get_rect(center=(216,384))

        #Tạo biến
        self.game_active = False 
        self.game_over_timer = 0

        #Tạo âm thanh
        self.flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
        self.hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
        self.score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
        self.background_music = pygame.mixer.Sound('sound/background_music.mp3')

        #Tạo đối tượng
        self.bird = Bird()
        self.pipes = Pipe()
        self.floor = Floor()
        self.score = Score()

    def run(self):
        while True:
            self.handle_events()
            self.clock.tick(FPS)
            self.background_music.play()

            if self.game_active: 
                self.update()
                self.render()
                self.background_music.stop()
            else:
                self.background_music.play()
                self.show_menu(self.screen)
                if self.game_over_timer == 0:
                    self.game_over_timer = time.time()
           
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_active:
                    self.bird.flap()
                    self.flap_sound.play()
                if event.key == pygame.K_SPACE and self.game_active == False:
                    if time.time() - self.game_over_timer > 1:
                        self.game_active = True 
                        self.pipes.reset_pipe()
                        self.bird.reset_bird()              
                        self.score.score = 0
                        self.game_over_timer = 0

    def update(self):
            self.bird.update()
            self.floor.update()
            self.pipes.update()
            if self.collision_check() == False:
                self.game_active = False
            
            if self.check_pass_pipe() == True:
                self.score.increase_score()

    def render(self):
        self.screen.blit(self.bg,(0,0))
        self.bird.draw(self.screen)
        self.pipes.draw(self.screen)
        self.floor.draw(self.screen)
        self.score.score_display(self.screen, self.game_active)
        pygame.display.update()

    def show_menu(self, screen):
        self.screen.blit(self.bg,(0,0)) 
        self.floor.update()
        self.floor.draw(screen)
        screen.blit(self.game_menu_surface, self.game_menu_rect)
        self.score.score_display(self.screen, self.game_active)
        pygame.display.update()

    def collision_check(self):
        if self.bird.bird_rect.top <= -75 or self.bird.bird_rect.bottom >= 630:
            self.hit_sound.play()
            return False
        for pipe in self.pipes.pipe_list:
            if self.bird.bird_rect.colliderect(pipe):
                self.hit_sound.play()
                return False
        return True
    
    def check_pass_pipe(self):
        for pipe in self.pipes.pipe_list:
            if pipe.centerx == 100:
                self.score_sound.play()
                return True
        return False
    
def main():
    flappyBird = FlappyBird()
    flappyBird.run()

if __name__ == "__main__":
    main()
