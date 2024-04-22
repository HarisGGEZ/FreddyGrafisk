import tkinter as tk
from tkinter import *

def textChanger():
    chosenText = "text"
    textBox.config(text=chosenText)
    root.after(300, textChanger)



root = tk.Tk()
root.attributes('-fullscreen', True)

img = PhotoImage(file="layout.png")
tk.Label(image=img).place(relx=0.33, rely=0.05)

textBox = tk.Label(text="helloo", font=("TkDefaultFont", 25))
textBox.place(relx=0.1, rely=0.05)





root.after(300, textChanger)
root.mainloop()