import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import map
import animatronic
import rooms
import keyboard
from tkvideoplayer import TkinterVideo


Map = map.kartaKlass()
freddy = animatronic.Fredrik()

living = ["alive"]

# Fredriks rörelse + ändrar text när man blir jagad
def freddyMove():
    freddy.move()
    if Map.hunted("") == True:
        huntBox.place(relx=0.55, rely=0)
        numberBox.config(text=( str(6 - Map.returnSteps())  + " steg tills Fredrik fångar dig"))
        numberBox.place(relx=0.75, rely=0)
        freddy.chooseLocation(Map.returnLocation())
    elif Map.hunted("") == False:
        freddy.reset()
        huntBox.place(relx=1,rely=1)
        numberBox.place(relx=1, rely=1)
    freddyIcon.place(relx=freddy.position()[0], rely=freddy.position()[1])

# Spelarens rörelse + events
def moving():
    root.after(0, moveIcon)
    choice = Map.movement()
    Map.move(choice)
    
    if Map.returnLocation() == freddy.returnLocation():
        Map.hunted("same")
    if keyboard.is_pressed("esc"):
         root.after(0, quit)
    if Map.run() >= 6:
        living.remove("alive")
        videoplayer = TkinterVideo(master=root, scaled=True)
        videoplayer.load(r"images/freddy.mp4")
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()
        root.after(1160, quit)
    
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
    if Map.returnLocation() == "prishörnan":
            if rooms.prizecorner() == "bought":
                eventBox.config(text=("Du köper en nyckel för 5 mynt"))
            if rooms.prizecorner() == "no":
                 eventBox.config(text=("5 mynt för\nen Nyckel"))
    if Map.returnLocation() == "matsalen" or Map.returnLocation() == "vänster hall":
         eventBox.config(text="")
    if Map.returnExit() == True and rooms.inventorySize() == 4:
     winScreen.place(relx=-0.001, rely=-0.002)
        
    if choice in ["höger", "vänster", "ner", "fram", "högerhall", "vänsterhall"]:
        root.after(0, freddyMove)

# Ändrar text på rörelsetexten
def textChanger():
    moving()
    chosenText = Map.printChoice()
    textBox.config(text=chosenText, justify= LEFT)
    inventoryBox.config(text=rooms.inventory(), justify=LEFT)
    if "alive" in living:
        root.after(150, textChanger)

# flyttar spelar bilden
def moveIcon():
    playerIcon.place(relx=Map.returnPosition()[0], rely=Map.returnPosition()[1])

# Avslutar 
def quit():
     root.destroy()

# Skapar root för tkinter
root = tk.Tk()
root.attributes('-fullscreen', True)


# Skapar alla labels (bilder, text)
img = (Image.open("images/layout.png"))
img = img.resize((int(root.winfo_screenwidth()*(1012/1536)), int(root.winfo_screenheight()*(786/864))))

img = ImageTk.PhotoImage(img)
tk.Label(image=img).place(relx=0.33, rely=0.05)

textBox = tk.Label(text=Map.printChoice(), font=("TkDefaultFont", 23), justify=LEFT)
textBox.place(relx=0, rely=0.05)

huntBox = tk.Label(text="Fredrik jagar dig!", font=("TkDefaultFont", 23), justify=LEFT)
huntBox.place(relx=1,rely=1)
numberBox = tk.Label(text=Map.returnSteps, font=("TkDefaultFont", 23), justify=LEFT)
numberBox.place(relx=1,rely=1)

inventoryBox = tk.Label(text = rooms.inventory(), font=("TkDefaultFont", 23), justify=LEFT)
inventoryBox.place(relx=0, rely=0.5)

eventBox = tk.Label(text ="", font=("TkDefaultFont", 23), justify=LEFT)
eventBox.place(relx=0.15, rely=0.5)

playerImg = PhotoImage(file="images/player.png")
playerIcon = tk.Label(image=playerImg)
playerIcon.place(relx=0.62, rely=0.85)

freddyImg = PhotoImage(file="images/freddy.png")
freddyIcon = tk.Label(image=freddyImg)
freddyIcon.place(relx=0.61, rely=0.1)

winImg = (Image.open("images/escape.png"))
winImg= winImg.resize((int(root.winfo_screenwidth()), int(root.winfo_screenheight())))
winImg = ImageTk.PhotoImage(winImg)
winScreen = tk.Label(image=winImg)
winScreen.place(relx=1, rely=1)


# Loop för fönstret
root.after(50, textChanger)
root.mainloop()