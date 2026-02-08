import pygame
import random
import os
pygame.font.init()

WIDTH, HEIGHT=800, 600
PLAYER_VELOCITY=10
enemies=[]
level=0
lives=5
lost=False
main_font=pygame.font.SysFont("comicsan", 50)

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

class Laser:
    def __init__(self, x, y, img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y+=vel

    def off_screen(self, height):
        return not(self.y<=height and self.y>=0)
    
    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN=30

    def __init__(self, x, y, health=100):
        self.x=x
        self.y=y
        self.health=health
        self.ship_img=None
        self.laser_img=None
        self.lasers=[]
        self.cd_counter=0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_laser(self, vel, obj):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health-=10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cd_counter>0:
            self.cd_counter+=1
        if self.cd_counter>=self.COOLDOWN:
            self.cd_counter=0

    def shoot(self):
        if self.cd_counter==0:
            laser=Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cd_counter=1

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img=YELLOW_SPACE_SHIP
        self.laser_img=YELLOW_LASER
        self.mask=pygame.mask.from_surface(self.ship_img)
        self.max_health=health

    def move_laser(self, vel, objs):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs[:]:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

class Enemy(Ship):
    COLOUR_MAP={
        "red":(RED_SPACE_SHIP, RED_LASER),
        "green":(GREEN_SPACE_SHIP, GREEN_LASER),
        "blue":(BLUE_SPACE_SHIP, BLUE_LASER)
    }
    def __init__(self, x, y, colour, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img=self.COLOUR_MAP[colour]
        self.mask=pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y+=vel

    def shoot(self):
        if self.cd_counter==0:
            self.cd_counter=1
            laser=Laser(self.x-15, self.y, self.laser_img)
            self.lasers.append(laser)
        
def collide(obj1, obj2):
    offset_x=obj2.x-obj1.x
    offset_y=obj2.y-obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y))!=None


def main():
    global lives, level, lost

    run=True
    FPS=60
    clock=pygame.time.Clock()

    wave_length=5
    enemy_vel=1
    laser_vel=5
    
    player=Player(300, 500)

    while run:
        clock.tick(FPS)
        if len(enemies)==0:
            level+=1
            wave_length+=5
            for i in range(wave_length):
                enemy=Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), 
                            random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x>0:
                player.x-=PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x<WIDTH-player.get_width():
                player.x+=PLAYER_VELOCITY
        if keys[pygame.K_w] and player.y-PLAYER_VELOCITY>0:
                player.y-=PLAYER_VELOCITY
        if keys[pygame.K_s] and player.y+PLAYER_VELOCITY<HEIGHT-player.get_height():
                player.y+=PLAYER_VELOCITY

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_laser(laser_vel, player)

            if random.randrange(0, 2*FPS)==1:
                enemy.shoot()

            if enemy.y+enemy.get_height()>HEIGHT:
                lives-=1
                enemies.remove(enemy)
            
            player.move_laser(-laser_vel, enemies)

        if lives==0 or player.health==0:
            lost=True

        if not(lost):
            redraw_window(player)
        else:
            lost_text=main_font.render("YOU LOST!", 1, "white")
            restart_text=main_font.render("Press Space Key to Restart", 1, "white")
            WINDOW.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2-lost_text.get_height()/2))
            WINDOW.blit(restart_text, (WIDTH/2-restart_text.get_width()/2, (HEIGHT/2-restart_text.get_height()/2)+50))
            pygame.display.update()
            if keys[pygame.K_SPACE]:
                restart_game()

def redraw_window(player):
    lives_label=main_font.render(f"Lives:{lives}", 1, (255, 255, 255))
    level_label=main_font.render(f"Level:{level}", 1, (255, 255, 255))

    WINDOW.blit(BG, (0,0))
    player.draw(WINDOW)
    
    WINDOW.blit(lives_label, (10, 10))
    WINDOW.blit(level_label, (WINDOW.get_width() - level_label.get_width() - 10, 10))

    for enemy in enemies:
        enemy.draw(WINDOW)

    pygame.display.update()

def restart_game():
    global enemies, level, lives, lost

    enemies=[]
    level=0
    lives=5
    lost=False

if __name__=="__main__":
    main()