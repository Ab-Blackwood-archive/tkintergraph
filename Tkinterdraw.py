
from ctypes.wintypes import HBITMAP
import tkinter as tk
from turtle import ht


#custom functions
# shift center point rduce size o
# add slope calculationm 
# difine left and bottom as -
# if x-(num) then put on left y-(num) put on bottom otherwise put r or t 10 to 440 = 420 210 each side
# dots for marks markes for numbers 

#y = mx + b                                                                                                                                                           

def draw():
    x1 = int(txtX1.get())
    y1 = int(txtY1.get())
    x2 = int(txtX2.get())
    y2 = int(txtY2.get())
    canvas.create_line(x1,y1,x2,y2)
def clear():
    canvas.delete('all')

def graphline():
    xhs =  20         # x of horz starting point same
    yhs =  20         # y of horz starting point 
    xhe = 440         # x of horz end point same
    yhe = 10  
    xvs = 10          # x of vert starting  point 
    yvs = 10          # y of vert starting point same
    xve = 10          # x of vert end point
    yve = 460
    for i in range(19): # draws horizontal grid lines
        canvas.create_line(xhs, yhs, xhe, yhe)
        yhs = yhs + 25
        yhe = yhe + 25
    for i in range(19): # draws vert grid lines
        canvas.create_line(xvs, yvs, xve, yve)
        xvs = xvs + 25
        xve = xve + 25
    canvas.create_line(210, 10, 210, 470, width =3) # cross demarcation
    canvas.create_line(10, 2, 460, 210, width=3) # cross demarcation 


#def slope

# canvas dimentions666
canvas_width = 480
canvas_height = 480

#window properties
window = tk.Tk()
window.title("graphing with Tkinter")
window.geometry("800x800") 

#create lables
lblev = tk.Label( window, text = "X1: ")
lblrv = tk.Label( window, text = "Y1: ")
lblX2 = tk.Label( window, text = "X2: ")
lblY2 = tk.Label( window, text = "Y2: ")


#read textboxs
txtX1 = tk.Entry(window)
txtY1 = tk.Entry(window)
txtX2 = tk.Entry(window)
txtY2 = tk.Entry(window)

#buttons
btn = tk.Button(window, text="Draw!", command= draw)
btnClear = tk.Button(window, text = "Clear", padx= 20, command=clear)
#canvas
canvas = tk.Canvas(window,  width=canvas_width, height=canvas_height, bg="white")


#add GUI items to grid 
btn.grid(row= 3, column= 3)
btnClear.grid(row= 3, column= 4)
canvas.grid(row=4, column= 0)
lblev.grid(row=0, column = 0)
lblrv.grid(row= 1, column = 0)
lblX2.grid(row =2, column = 0)
lblY2.grid(row= 3, column = 0)
txtX1.grid(row= 0, column = 1)
txtY1.grid(row= 1, column = 1)
txtX2.grid(row =2, column = 1)
txtY2.grid(row= 3, column = 1)



#build window
graphline()
window.mainloop()