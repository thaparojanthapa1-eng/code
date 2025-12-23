import tkinter

playerX="X"
playerO="O"
currentplayer=playerX
board=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def set_tile(row, column):
    global currentplayer, turns

    if (game_over):
        return

    if board[row][column]["text"]=="":
        board[row][column]["text"]=currentplayer
        turns+=1

        if currentplayer==playerX:
            currentplayer=playerO
        else:
            currentplayer=playerX
        
        label["text"]=f"{currentplayer}'s turn"
    else:
        return
    check_winner()

def check_winner():
    global turns, game_over
    for row in range (3):
        if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]
             and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range (3):
                board[row][column].config(background=color_lightgrey, foreground=color_yellow)
            game_over=True
            return
        
    for column in range (3):
        if (board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]
            and board[0][column]["text"]!=""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range (3):
                board[row][column].config(background=color_lightgrey, foreground=color_yellow)
            game_over=True
            return
        
    if board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!="":
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range (3):
            board[i][i].config(background=color_lightgrey, foreground=color_yellow)
        game_over=True
        return
    
    if board[2][0]["text"]==board[1][1]["text"]==board[0][2]["text"] and board[2][0]["text"]!="":
        label.config(text=board[2][0]["text"]+" is the winner!", foreground=color_yellow)
        board[2][0].config(background=color_lightgrey, foreground=color_yellow)
        board[1][1].config(background=color_lightgrey, foreground=color_yellow)
        board[0][2].config(background=color_lightgrey, foreground=color_yellow)
        game_over=True
        return
    
    if (turns==9):
        game_over=True
        label.config(text="Tie!", foreground=color_yellow)

def restartgame():
    global turns, game_over

    turns=0
    game_over=False

    label.config(text=f"{currentplayer}'s turn", foreground="white")

    for row in range (3):
        for column in range (3):
            board[row][column].config(text="", foreground=color_blue, background=color_grey)

color_blue="#4584B6"
color_yellow="#ffde57"
color_grey="#343434"
color_lightgrey="#646464"

turns=0
game_over=False

window=tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame, text=f"{currentplayer}'s turn", font=("consolas",20),
                     background=color_grey, fg="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range (3):
    for column in range(3):
        board[row][column]=tkinter.Button(frame, text="", font=("Consolas",50,"bold"), 
                                          background=color_grey, foreground=color_blue, width=4, height=1,
                                          command=lambda row=row, column=column: set_tile(row,column))
        board[row][column].grid(row=row+1, column=column)

button=tkinter.Button(frame, text="Restart", font=("Consolas",20,"bold"), 
                      background=color_grey, foreground="white", 
                      command=lambda: restartgame())
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_X=int((screen_width/2)-(window_width/2))
window_Y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_X}+{window_Y}")

window.mainloop()