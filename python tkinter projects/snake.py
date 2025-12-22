import tkinter
import random

ROWS=25 
COLUMN=25
TILE_SIZE=25

WINDOW_WIDTH=ROWS*TILE_SIZE
WINDOW_HEIGHT=COLUMN*TILE_SIZE

class Tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y

window=tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas=tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                      borderwidth=0, highlightthickness= 0)
canvas.pack()

window.update()

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_X=int((screen_width/2)-(WINDOW_WIDTH/2))
window_Y=int((screen_height/2)-(WINDOW_HEIGHT/2))

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_X}+{window_Y}")

snake=Tile(5*TILE_SIZE, 5*TILE_SIZE)
food=Tile(10*TILE_SIZE, 10*TILE_SIZE)
snake_body=[]
velocityX=0
velocityY=0
game_over=False
score=0
Hiscore=0
new_hiscore=False

def change_direction(e):
    global velocityX, velocityY, game_over, score

    if (game_over):
        return
    
    if e.keysym == "Left" and velocityX!=1:
        velocityX=-1
        velocityY=0
    elif e.keysym == "Right" and velocityX!=-1:
        velocityX=1
        velocityY=0
    elif e.keysym == "Up" and velocityY!=1:
        velocityX=0
        velocityY=-1
    elif e.keysym == "Down" and velocityY!=-1:
        velocityX=0
        velocityY=1

def move():
    global snake, food, snake_body, game_over, score, Hiscore, new_hiscore

    if (game_over):
        return
    
    if (snake.x<0 or snake.x>=WINDOW_WIDTH or snake.y<0 or snake.y>=WINDOW_HEIGHT):
        game_over=True
        return
    
    for tile in snake_body:
        if snake.x==tile.x and snake.y==tile.y:
            game_over=True
            return

    if snake.x==food.x and snake.y==food.y:
        snake_body.append(Tile(food.x,food.y))
        food.x=random.randint(0, COLUMN-1)*TILE_SIZE
        food.y=random.randint(0, ROWS-1)*TILE_SIZE
        score+=1

    for i in range(len(snake_body)-1, -1, -1):
        tile=snake_body[i]
        if (i==0):
            tile.x=snake.x
            tile.y=snake.y
        else:
            prev_tile=snake_body[i-1]
            tile.x=prev_tile.x
            tile.y=prev_tile.y

    snake.x+=velocityX*TILE_SIZE
    snake.y+=velocityY*TILE_SIZE

    if score>Hiscore:
        Hiscore=score
        new_hiscore=True

def draw():
    global snake,  food, snake_body, game_over, score, Hiscore, new_hiscore
    move()

    canvas.delete("all")

    canvas.create_rectangle(food.x, food.y ,food.x+TILE_SIZE, food.y+TILE_SIZE, fill="red")
    canvas.create_rectangle(snake.x, snake.y ,snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="lime green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x+TILE_SIZE, tile.y+TILE_SIZE, fill="lime green")


    if (game_over):
        if new_hiscore==True:
            canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20",
                            text=f"Game Over: {score}\n\nCongratualtions you beat your high score\nNew High Score: {Hiscore}\nPress Space to Restart",
                              fill="white")
        else:
            canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20",
                                text=f"Game Over: {score}\n\nHigh Score: {Hiscore}\nPress Space to Restart", fill="white")
            
    else:
        canvas.create_text(30, 20, font="Arial 10", fill="white", text=f"Score: {score}\nHiscore: {Hiscore}")

    window.after(100, draw)

def restart_game(f):
    global snake, food, game_over, snake_body, velocityX, velocityY, score, new_hiscore
    snake=Tile(5*TILE_SIZE, 5*TILE_SIZE)
    food=Tile(10*TILE_SIZE, 10*TILE_SIZE)
    snake_body=[]
    velocityX=0
    velocityY=0
    game_over=False
    score=0
    new_hiscore=False

draw()

window.bind("<KeyPress>", change_direction)
window.bind("<space>",restart_game)
window.mainloop()
