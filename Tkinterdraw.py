
from ctypes.wintypes import HBITMAP
import tkinter as tk
from turtle import ht


#custom functions
# shift center point rduce size o
# difine left and bottom as -
# if x =-(num) then put on left y =-(num) put on bottom otherwise put r or t 10 to 440 = 420 210 each side figure out the convertion ratio 1 = 2.5 px
# break up grid to numbers 100 up by ten 500px wide each sopot 25 px 
# dots for marks markes for numbers  

#y = mx + b                                                                                                                                                           

def draw():
    Itm1 = int(txti1.get()) * 2.5
    point = Itm1
    x1= 50
    x2= x1 + 50
    y1= 500
    y2= 500 - point
    canvas.create_rectangle(x1,y1,x2,y2)
  
    
    Itm2 = int(txti2.get()) * 2.5
    point = 500 - Itm2
    x1= x2 + 50
    x2= x1 + 50
    y2= 500 - point
    canvas.create_rectangle(x1,y1,x2,y2)
    Itm3 = int(txti3.get()) * 2.5
    point = 500 - Itm3
    x1= x2 + 50
    x2= x1 + 50
    y2= 500 - point
    canvas.create_rectangle(x1,y1,x2,y2)
    Itm4 = int(txti4.get()) * 2.5
    point = 500 - Itm4
    x1= x2 + 100
    x2= x1 + 50
    y2= 500 - point
    canvas.create_rectangle(x1,y1,x2,y2)
   

def graph():
    vd = 500
    for i in range(19): #draws dashes 
        canvas.create_line(35,vd,40,vd, width = 2) # vert dash
        vd = vd - 25
    canvas.create_line(40, 500, 40, 50, width=2) # cross demarcation vert
    canvas.create_line(40, 500, 530, 500, width=2) # cross demarcation hoz
   # vd = 45
   # for i in range(19): #draws dashes 
  #      canvas.create_line(40,vd,40,vd, width = 2) # vert dash  
  #      vd = vd + 25

# canvas dimentions666
canvas_width = 540
canvas_height = 540

#window properties
window = tk.Tk()
window.title("graphing with Tkinter")
window.geometry("800x800") 

#create lables
lbli1 = tk.Label( window, text = "item 1: ")
lbli2 = tk.Label( window, text = "item 2: ")
lbli3 = tk.Label( window, text = "item 3: ")
lbli4 = tk.Label( window, text = "item 4: ")
lblslp = tk.Label( window, text = "")

#read textboxs
txti1 = tk.Entry(window)
txti2 = tk.Entry(window)
txti3 = tk.Entry(window)
txti4 = tk.Entry(window)

#buttons
btn = tk.Button(window, text="Draw!", command= draw)
#btnClear = tk.Button(window, text = "Clear", padx= 20, command=clear)

#canvas
canvas = tk.Canvas(window,  width=canvas_width, height=canvas_height, bg="white")


#add GUI items to grid 
btn.grid(row= 3, column= 3)
#btnClear.grid(row= 3, column= 4)
canvas.grid(row= 4, column= 0)
lbli1.grid(row= 0, column = 0)
lbli2.grid(row= 1, column = 0)
lbli3.grid(row= 2, column = 0)
lbli4.grid(row= 3, column = 0)
txti1.grid(row= 0, column = 1)
txti2.grid(row= 1, column = 1)
txti3.grid(row= 2, column = 1)
txti4.grid(row= 3, column = 1)
lblslp.grid(row= 6, column = 0)

#build window
graph()
window.mainloop()