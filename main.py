import tkinter as tk
from tkinter import *
import map
import animatronic
from time import sleep
Map = map.kartaKlass()
freddy = animatronic.Fredrik()

def freddyMove():
    freddy.move()
    freddyIcon.place(relx=freddy.position()[0], rely=freddy.position()[1])

def moving():
    root.after(5, moveIcon)
    choice = Map.movement()
    Map.move(choice)
    if choice in ["höger", "vänster", "ner", "fram", "högerhall", "vänsterhall"]:
        root.after(5, freddyMove)
    Map.returnLocation()
    

def textChanger():
    moving()
    chosenText = Map.printChoice()
    textBox.config(text=chosenText, justify= LEFT)
    root.after(300, textChanger)

def moveIcon():
    playerIcon.place(relx=Map.returnPosition()[0], rely=Map.returnPosition()[1])

root = tk.Tk()
root.attributes('-fullscreen', True)

img = PhotoImage(file="layout.png")
tk.Label(image=img).place(relx=0.33, rely=0.05)

textBox = tk.Label(text=Map.printChoice(), font=("TkDefaultFont", 25), justify=LEFT)
textBox.place(relx=0, rely=0.05)

playerImg = PhotoImage(file="player.png")
playerIcon = tk.Label(image=playerImg)
playerIcon.place(relx=0.62, rely=0.85)

freddyImg = PhotoImage(file="freddy.png")
freddyIcon = tk.Label(image=freddyImg)
freddyIcon.place(relx=0.61, rely=0.1)

root.after(300, textChanger)

root.mainloop()