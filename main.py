import tkinter as tk
from tkinter import *
import map
Map = map.kartaKlass()

def moving():
    choice = Map.movement()
    Map.move(choice)
    Map.returnLocation()
    root.after(300, moveIcon)

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

playerIcon = tk.Label(background="black", height=1, width=2)
playerIcon.place(relx=0.63, rely=0.9)

# koordinater
# kontor 0.63, 0.9
# höger hall  0.725, 0.8
# vänster hall 0.535, 0.8


root.after(300, textChanger)

root.mainloop()