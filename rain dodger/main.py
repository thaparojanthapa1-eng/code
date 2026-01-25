import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT=800, 600
WINDOW=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Dodger")
BG=(0, 0, 0)

PLAYER_HEIGHT, PLAYER_WIDTH=50, 50
PLAYER_VELOCITY=10
DROP_WIDTH=10
DROP_HEIGHT=30
DROP_VEL=10
FONT=pygame.font.SysFont("comicsans", 30)

def draw(player, spent_time, drops):
    WINDOW.fill(BG)
    time_text=FONT.render(f"Time: {round(spent_time)}s", 1, "white")
    WINDOW.blit(time_text, (10,10))
    pygame.draw.rect(WINDOW, "red", player)
    
    for drop in drops:
         pygame.draw.rect(WINDOW, "white", drop)

    pygame.display.update()

def main():
    run=True

    clock=pygame.time.Clock()

    start_time=time.time()
    spent_time=0

    drops_spawn_time=200
    time_since_last_drop=0

    drops=[]
    hit=False

    player=pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        clock.tick(60)
        spent_time=time.time()-start_time
        
        time_since_last_drop+=clock.tick(60)

        if time_since_last_drop>drops_spawn_time:
            for _ in range (5):
                drop_x=random.randint(0, WIDTH-DROP_WIDTH)
                drop=pygame.Rect(drop_x, -DROP_HEIGHT, DROP_WIDTH, DROP_HEIGHT)
                drops.append(drop)

            time_since_last_drop=0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x-PLAYER_VELOCITY>=0:
                player.x-=PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x+PLAYER_VELOCITY+PLAYER_WIDTH<=WIDTH:
                player.x+=PLAYER_VELOCITY

        for drop in drops[:]:
            drop.y+=DROP_VEL
            if drop.y>HEIGHT:
                drops.remove(drop)
            elif drop.y+drop.height>=player.y and drop.colliderect(player):
                drops.remove(drop)
                hit=True
                break

        if hit:
             lost_text=FONT.render("YOU LOST!", 1, "white")
             WINDOW.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2-lost_text.get_height()/2))
             pygame.display.update()
             pygame.time.delay(2000)
             break

        draw(player, spent_time, drops)

    pygame.quit()

if __name__=="__main__":
    main()