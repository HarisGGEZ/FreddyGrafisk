import tkinter as tk
from tkinter import *
import map
Map = map.kartaKlass()

def moving():
    choice = Map.movement()
    Map.move(choice)
    Map.returnLocation()

def textChanger():
    moving()
    chosenText = Map.printChoice()
    textBox.config(text=chosenText, justify= LEFT)
    root.after(300, textChanger)



root = tk.Tk()
root.attributes('-fullscreen', True)

img = PhotoImage(file="layout.png")
tk.Label(image=img).place(relx=0.33, rely=0.05)

textBox = tk.Label(text="helloo", font=("TkDefaultFont", 25))
textBox.place(relx=0.05, rely=0.05)




root.after(300, textChanger)

root.mainloop()