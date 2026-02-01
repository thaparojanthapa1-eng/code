import pygame
import time
import random
import os
pygame.font.init()

WIDTH, HEIGHT=800, 600
PLAYER_VELOCITY=10
WINDOW=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

RED_SPACE_SHIP=pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP=pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP=pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SPACE_SHIP=pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
RED_LASER=pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER=pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER=pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER=pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
BG=pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x=x
        self.y=y
        self.health=health
        self.player_img=None
        self.laser_img=None
        self.laser=[]
        self.cd_counter=0

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))

    def get_width(self):
         return self.player_img.get_width()
    
    def get_height(self):
         return self.player_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img=YELLOW_SPACE_SHIP
        self.laser_img=YELLOW_LASER
        self.mask=pygame.mask.from_surface(self.player_img)
        self.max_health=health

def main():
    run=True
    FPS=60
    main_font=pygame.font.SysFont("comicsan", 50)
    clock=pygame.time.Clock()
    
    player=Player(300, 500)

    while run:
        clock.tick(FPS)
        redraw_window(player)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x>0:
                player.x-=PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x<WIDTH-player.get_width():
                player.x+=PLAYER_VELOCITY
        if keys[pygame.K_w] and player.y-PLAYER_VELOCITY>0:
                player.y-=PLAYER_VELOCITY
        if keys[pygame.K_s] and player.y+PLAYER_VELOCITY<HEIGHT-player.get_height():
                player.y+=PLAYER_VELOCITY
        

def redraw_window(player):
    WINDOW.blit(BG, (0,0))
    player.draw(WINDOW)
    pygame.display.update()

main()