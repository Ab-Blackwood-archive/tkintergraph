
from ctypes.wintypes import HBITMAP
import tkinter as tk
from turtle import ht


#custom functions
# shift center point rduce size o
# add slope calculationm 
# difine left and bottom as -
# if x =-(num) then put on left y =-(num) put on bottom otherwise put r or t 10 to 440 = 420 210 each side figure out the convertion ratio 1 = 2.5 px
# break up grid to numbers 100 up by ten 500px wide each sopot 25 px 
# dots for marks markes for numbers  

#y = mx + b                                                                                                                                                           

def position(point):
    if point == "-":#places negaitive number side
        point = 270 - 2.5*point #number entered use blank varianble that changes for each textbox
    elif point > 0:  #places posi tive number
        point = 270 + 2.5*point # number entered
    else: # places 0 at middle
        point= 270

def draw():
    x1 = int(txtX1.get())
    position(x1) # set point to x1
    point =x1 # convert back to x1
    y1 = int(txtY1.get())
    position(y1)
    point =y1
    x2 = int(txtX2.get())
    position(x2)
    point = x2
    y2 = int(txtY2.get())
    position(y2)
    point = y2
    drwline =canvas.create_line(x1,y1,x2,y2, fill = "#009A44")

    return x1
def clear():
    canvas.delete('drwline') #makes it so delete doesnt delete grid spesify lines

def graphline():
    xhs =  20         # x of horz starting point same
    yhs =  20         # y of horz starting point 
    xhe = 520         # x of horz end point same
    yhe = 20 
    xvs = 20          # x of vert starting  point 
    yvs = 20          # y of vert starting point same
    xve = 20          # x of vert end point
    yve = 520
    for i in range(21): # draws horizontal grid lines
        canvas.create_line(xhs, yhs, xhe, yhe)
        yhs = yhs + 25
        yhe = yhe + 25
    for i in range(21): # draws vert grid lines
        canvas.create_line(xvs, yvs, xve, yve)
        xvs = xvs + 25
        xve = xve + 25
    canvas.create_line(270, 10, 270, 530, width =3) # cross demarcation hoz
    canvas.create_line(10, 270, 530, 270, width=3) # cross demarcation vert 
    hd = 45
    vd = 45
    for i in range(19): #draws dashes 
        canvas.create_line(hd,275,hd,265, width = 2) # hoz dash
        canvas.create_line(275,vd,265,vd, width = 2) # vert dash
        hd = hd + 25
        vd = vd + 25
"""""
if draw() == "-":#places negaitive number side
= 270 - 2.5* #number entered
elif draw() >0:  #places posi tive number
= 270 + 2.5* # number entered
else: # places 0 at middle
    = 270
"""
def slope():
    sx = x2 - x1 
    sy = y2 - y1 
# canvas dimentions666
canvas_width = 540
canvas_height = 540

#window properties
window = tk.Tk()
window.title("graphing with Tkinter")
window.geometry("800x800") 

#create lables
lblev = tk.Label( window, text = "X1: ")
lblrv = tk.Label( window, text = "Y1: ")
lblX2 = tk.Label( window, text = "X2: ")
lblY2 = tk.Label( window, text = "Y2: ")
lblslp = tk.Label( window, text = "")

#read textboxs
txtX1 = tk.Entry(window)
txtY1 = tk.Entry(window)
txtX2 = tk.Entry(window)
txtY2 = tk.Entry(window)

#buttons
btn = tk.Button(window, text="Draw!", command= draw)
btnClear = tk.Button(window, text = "Clear", padx= 20, command=clear)
btnslp = tk.Button(window, text = "Find slope")
#canvas
canvas = tk.Canvas(window,  width=canvas_width, height=canvas_height, bg="white")


#add GUI items to grid 
btn.grid(row= 3, column= 3)
btnClear.grid(row= 3, column= 4)
canvas.grid(row= 4, column= 0)
lblev.grid(row= 0, column = 0)
lblrv.grid(row= 1, column = 0)
lblX2.grid(row= 2, column = 0)
lblY2.grid(row= 3, column = 0)
txtX1.grid(row= 0, column = 1)
txtY1.grid(row= 1, column = 1)
txtX2.grid(row= 2, column = 1)
txtY2.grid(row= 3, column = 1)
btnslp.grid(row= 5, column = 0)
lblslp.grid(row= 6, column = 0)

#build window
graphline()
window.mainloop()