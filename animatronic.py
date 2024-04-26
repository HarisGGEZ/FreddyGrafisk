from random import choice

class Fredrik():

    def __init__(self):
        self.location = "scen"
        self.old = None
        self.cheat = False
        self.x = ""
        self.y = ""
        
    # Förflyttelse för Fredrik
    def move(self):
        if self.cheat == False:
            if self.location == "scen":
                self.location = "matsalen"
                self.old = "scen"
            elif self.location == "matsalen":
                self.location = choice([self.location, "scen", "vänster hall", "prishörnan", "höger hall", "toaletterna", "köket"])
                self.old = "matsalen"
            elif self.location == "höger hall":
                self.location = choice([self.location, "matsalen"])
                self.old = "höger hall"
            elif self.location == "toaletterna":
                self.location = choice([self.location, "matsalen"])
                self.old = "toaletterna"
            elif self.location == "köket":
                self.location = choice([self.location, "matsalen"])
                self.old = "köket"
            elif self.location ==  "prishörnan":
                self.location = choice([self.location, "matsalen"])
                self.old = "prishörnan"
            elif self.location == "vänster hall":
                self.location = choice([self.location, "matsalen", "förrådet"])
                self.old = "vänster hall"
            elif self.location == "förrådet":
                self.location = choice([self.location, "vänster hall"])
                self.old = "förrådet" 
        else:
            self.location = "scen"
            self.old = "scen"
    
    # Skickar tillbaka platsen.
    def returnLocation(self):
        return self.location
    
    # Printar förflyttelse
    def printMove(self):
        if self.old != self.location:
            print(f"\nFredrik flyttade sig från {self.old} till {self.location}\n")
        else:
            print(f"\nFredrik stannar i {self.old}\n")

    # Aktiverar fusk
    def activateCheat(self):
        self.cheat = True

    def position(self):
        if self.location == "scen":
            self.x = 0.62
            self.y = 0.1
        if self.location == "matsalen":
            self.x = 0.58
            self.y = 0.35
        if self.location == "höger hall":
            self.x = 0.72
            self.y = 0.74
        if self.location == "vänster hall":
            self.x = 0.53
            self.y = 0.74
        if self.location == "förrådet":
            self.x = 0.435
            self.y = 0.675
        if self.location == "toaletterna":
            self.x = 0.88
            self.y = 0.3
        if self.location == "prishörnan":
            self.x = 0.36
            self.y = 0.28
        if self.location == "köket":
            self.x = 0.9
            self.y = 0.68
        return self.x, self.y