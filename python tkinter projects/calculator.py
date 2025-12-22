import tkinter

button_values=[
    ["AC","+/-","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","√","="]
]

rightsymbols=["÷","×","-","+","="]
topsymbols=["AC","+/-","%"]
bottomsymbols=[".","√"]

row_count=len(button_values)
column_count=len(button_values[0])


color_grey="#A9A9A9"
color_black="#1C1C1C"
color_orange="#FF9500"
color_white="#FFFFFF"

window=tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame, text="0", font=("Arial",45), 
                    background=color_black, foreground=color_white, 
                    anchor="e",width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value=button_values[row][column]
        button=tkinter.Button(frame, text=value, font=("Arial",30), 
                              width=column_count-1, height=1, 
                              command=lambda value=value: button_clicked(value))
        if value in topsymbols:
            button.config(foreground=color_black, background=color_grey)
        elif value in rightsymbols:
            button.config(foreground=color_white, background=color_orange)
        elif value in bottomsymbols:
            button.config(foreground=color_white, background=color_grey)
        button.grid(row=row+1, column=column)

frame.pack()

A="0"
operator=None
B=None

def clear_all():
    global A, B, operator
    A="0"
    operator=None
    B=None

def format_number(num):
    return f"{num:.7f}".rstrip("0").rstrip(".")


def button_clicked(value):
    global rightsymbols, topsymbols, bottomsymbols, label, A, B, operator

    if value in rightsymbols:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)

                if operator=="+":
                    label["text"]=format_number(numA+numB)
                elif operator=="-":
                    label["text"]=format_number(numA-numB)
                elif operator=="×":
                    label["text"]=format_number(numA*numB)
                elif operator=="÷":
                    label["text"]=format_number(numA/numB)

                clear_all()

        elif value in "-+×÷":
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"

            operator=value
    
    elif value in topsymbols:
        if value=="AC":
            clear_all()
            label["text"]="0"
        elif value=="+/-":
            result=float(label["text"])*-1
            label["text"]=format_number(result)
        elif value=="%":
            result=float(label["text"])/100
            label["text"]=result

    elif value in bottomsymbols:
        if value==".":
            if value not in label["text"]:
                label["text"]+=value
        elif value=="√":
            result=float(label["text"])**(1/2)
            label["text"]=format_number(result)
    
    else:
        if value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value


window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_X=int((screen_width/2)-(window_width/2))
window_Y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_X}+{window_Y}")

window.mainloop()
