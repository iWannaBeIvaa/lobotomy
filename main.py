import pygame
from random import randint
import time as tm
pygame.init()
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1300, 1000
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, size, center):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.anim = [''] # загрузка твоих картинок для анимации
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.frame = 0 # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 # как быстро кадры меняются

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            
     
            self.image = self.anim[self.frame]

pygame.font.get_fonts()

rect_x = 650
rect_y = 500
speed = 9

plr_sprite = pygame.sprite.Group()
map_sprite = pygame.sprite.Group()

player = pygame.sprite.Sprite(plr_sprite)
plrimg = pygame.image.load('Assets/idle_front.png')
newplrimg = pygame.transform.scale(plrimg, (250, 250))
player.image = newplrimg
player.rect = player.image.get_rect()
player.rect.centerx = rect_x
player.rect.centery = rect_y

idle_back = pygame.transform.scale(pygame.image.load('Assets/idle_back.png'), (250, 250))
run1_back = pygame.transform.scale(pygame.image.load('Assets/run1_back.png'), (250, 250))
run2_back = pygame.transform.scale(pygame.image.load('Assets/run2_back.png'), (250, 250))
run1_front = pygame.transform.scale(pygame.image.load('Assets/run1_front.png'), (250, 250))
run2_front = pygame.transform.scale(pygame.image.load('Assets/run2_front.png'), (250, 250))
idle_left = pygame.transform.scale(pygame.image.load('Assets/run_left.png'), (250, 250))
idle_right = pygame.transform.scale(pygame.image.load('Assets/idle_right.png'), (250, 250))
run_left = pygame.transform.scale(pygame.image.load('Assets/run_left.png'), (250, 250))
run_right = pygame.transform.scale(pygame.image.load('Assets/run_right.png'), (250, 250))

grass = pygame.sprite.Sprite(map_sprite)
grassimg = pygame.image.load('Assets/trava.png')
grass.image = grassimg

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    plr_sprite.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player.rect.centery < 120:
            pass
        else:
            player.rect.centery -= speed
            plr_sprite.update()
            pygame.time.wait(1)
            player.image = run1_back
            plr_sprite.update()
            pygame.time.wait(1)
            player.image = newplrimg
            plr_sprite.update()
            pygame.time.wait(1)
            player.image = run2_back
            plr_sprite.update()
            pygame.time.wait(1)
            player.image = newplrimg
            plr_sprite.update()
            pygame.time.wait()
    elif keys[pygame.K_s]:
        if player.rect.centery > 880:
            pass
        else:
            player.rect.centery += speed
    elif keys[pygame.K_a]:
        if player.rect.centerx < 60:
            pass
        else:
            player.rect.centerx -= speed
    elif keys[pygame.K_d]:
        if player.rect.centerx > 1250:
            pass
        else:
            player.rect.centerx += speed

    


    clock.tick(30)
    pygame.display.update()
pygame.quit()