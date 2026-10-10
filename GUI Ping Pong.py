from tkinter import *
from tkinter import messagebox
PD_1_Y = 5
wd = Tk()
wd.geometry("600x550")
wd.config(background="white")
wd.title("Ping Pong Match")
def Move_PD1(event):
    global PD_1_Y
    print(event.keysym)
    if event.keysym == "w":
         PD_1_Y = -5
    elif event.keysym == "s":
         PD_1_Y = 5
def M_1(PD_1_O, PD_1_Y):
     C.move(PD_1_O,0,PD_1_Y)
     
C = Canvas(wd, bg = "black",bd = 1,highlightthickness= 3,highlightbackground="black", width = 600, height = 550)
C.place(x = 0, y = 0)
C.bind_all("<KeyPress-w>", Move_PD1)
C.bind_all("<KeyPress-s>", Move_PD1)
C.create_line(300,0,300,550,fill = "white")
C.create_oval(250, 215, 350,315,outline = "white")

PD_1_O = C.create_rectangle(0,200,15,280,fill = "orange")

PD_2_G = C.create_rectangle(585,200,596,280,fill = "green")

while True:
     M_1(PD_1_O,PD_1_Y)






wd.mainloop()