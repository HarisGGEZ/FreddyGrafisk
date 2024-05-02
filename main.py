import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import map
import animatronic
import webbrowser
import rooms


Map = map.kartaKlass()
freddy = animatronic.Fredrik()

restroomFound = False

def freddyMove():
    freddy.move()
    if Map.hunted("") == True:
        huntBox.place(relx=0.55, rely=0)
        freddy.chooseLocation(Map.returnLocation())
    elif Map.hunted("") == False:
        freddy.reset()
        huntBox.place(relx=1,rely=1)
    freddyIcon.place(relx=freddy.position()[0], rely=freddy.position()[1])

def moving():
    root.after(5, moveIcon)
    choice = Map.movement()
    Map.move(choice)
    if Map.returnLocation() == freddy.returnLocation():
        Map.hunted("same")

    if Map.run() >= 6:
        #root.destroy()
        #webbrowser.open("https://en.wikipedia.org/wiki/Death")
        pass
        
    
    if Map.returnLocation() == "toaletterna":
            if rooms.restrooms() == "found":
                eventBox.config(text="Du hittar \nen Nyckel \noch ett mynt \ni toalleterna")
    
    if Map.returnLocation() == "köket":
            if rooms.kitchen() == "found":
                eventBox.config(text=("Du hittar \ntvå mynt och \n en nummerlapp \ni köket"))
    if Map.returnLocation() == "förrådet":
            if rooms.supplycloset() == "used":
                eventBox.config(text=("Du hittar \ntvå mynt och \n en nyckel \ni kassavalvet"))
            if rooms.supplycloset() == "no":
                 eventBox.config(text=("Du hittar ett kassavalv.\nHär behövs en kod"))
    
    if choice in ["höger", "vänster", "ner", "fram", "högerhall", "vänsterhall"]:
        root.after(5, freddyMove)


def textChanger():
    moving()
    chosenText = Map.printChoice()
    textBox.config(text=chosenText, justify= LEFT)
    inventoryBox.config(text=rooms.inventory(), justify=LEFT)
    root.after(150, textChanger)

    
def moveIcon():
    playerIcon.place(relx=Map.returnPosition()[0], rely=Map.returnPosition()[1])

root = tk.Tk()
root.attributes('-fullscreen', True)



img = (Image.open("layout.png"))
img = img.resize((int(root.winfo_screenwidth()*(1012/1536)), int(root.winfo_screenheight()*(786/864))))
print(int(root.winfo_screenwidth()*(1012/1536)), root.winfo_screenheight()*())


img = ImageTk.PhotoImage(img)
tk.Label(image=img).place(relx=0.33, rely=0.05)

textBox = tk.Label(text=Map.printChoice(), font=("TkDefaultFont", 25), justify=LEFT)
textBox.place(relx=0, rely=0.05)

huntBox = tk.Label(text="Fredrik jagar dig!", font=("TkDefaultFont", 25), justify=LEFT)
huntBox.place(relx=1,rely=1)

inventoryBox = tk.Label(text = rooms.inventory(), font=("TkDefaultFont", 25), justify=LEFT)
inventoryBox.place(relx=0, rely=0.5)

eventBox = tk.Label(text ="", font=("TkDefaultFont", 25), justify=LEFT)
eventBox.place(relx=0.15, rely=0.5)

playerImg = PhotoImage(file="player.png")
playerIcon = tk.Label(image=playerImg)
playerIcon.place(relx=0.62, rely=0.85)

freddyImg = PhotoImage(file="freddy.png")
freddyIcon = tk.Label(image=freddyImg)
freddyIcon.place(relx=0.61, rely=0.1)

root.after(50, textChanger)
root.mainloop()