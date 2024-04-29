from time import sleep
import keyboard

class kartaKlass():
    # Värden som klassen får när den skapas
    def __init__(self):
        self.o = ">-O"
        self.e = "   "
        self.w = "   "
        self.s = "   "
        self.k = "   "
        self.d = "   "
        self.b = "   "
        self.t = "   "
        self.old = None
        self.location = "kontoret"
        self.hunt = False
        self.steps = 0
        self.ner = None
        self.text = ""
        self.fullText = ""
        self.choice = ""
        self.x = ""
        self.y = ""
        
    # Printar en bild av kartan
    def printMap(self):
        print(f'''                                                                                                                                                                                                                                                                                                                                                                                       
                                            ''...............................''                                              
                                            .,.                               .;.    .............                                   
                                            .,.                               .,.    ', \033[91mUtgång\033[0m  .,.                                  
                                            .,.                               .;.    ',         .,.                                  
                                            .:'                               ':.    ,,         .;.                                  
        .,'.........,.  .,..................','...............................','....'.          ...,'                         
        .,  \033[91mPrishörnan\033[0m                                                                            .,                         
        .,                                                                                         .,     .......             
        .,          ,;..;'                                                                         .,  .,,......;'            
        .,          ,'  ''                                                                         .,  .,.      .,            
        .,   {self.b}    ,'  ''                                                                         .:..,;.      .,            
        .,          ,'  ''                                                                                     .,            
        .,          ,'  ''                                                                                      .,   .........
        .,          ,'  ''                                                                         .:..,:.      ':..,c'......:
        .:..........;'  ''                              \033[91mMatsal\033[0m                                     .,  .,.      ':..,:.      ,
        ............   ''                                {self.d}                                       .,  .,.      ':'.;:.      ,
                        ..,,                                                                       .,  .,. {self.t}  ';..':,......:
            .,,.........:,                                                                         .,  .,.      .,   .........
            .,.         ''                                                                         .,  .,.      .,            
            .,.         .'                                                                         .,  .,.      .,            
            .,.         .'                                                                         .,  .,.      .,   .'......'
            .,.         .'                                                                         .,  .,.      ':'.;:.      ;
            .,.         .'                                                                         .,  .,.      ';..';.      ,
            .;,.........;,                                                                         .,  .,.      ':'.;:.      ,
            ...........;:...................      .............................       .........   ....;,  .,,......;,  .,,...;
                           .................      .............................       .......,:   :,..                   ..     
                                        .'          '.                     .'          '.   .;;   ;,.................'.         
                                        ,,          .;.                   .;.          ,,   ,,         \033[91mKöket\033[0m         ,,         
                        ............   ,'          .,.                   .,.          ',   ''                       ''         
                        ';.........';.  ,'          .,.                   .,.          ',   ''                       ',         
                        '' \033[91mFörråd\033[0m  .,.  ,'          .,.                   .,.          ,'   ''                        ',         
                        ',         .,.  ,'          .,.                   .,.          ',   ''        {self.k}           ',         
                        ',         .;;..;'          .,.                   .,.          ',   ''                       ',         
                        ',                          .,.                   .,.          ',   ''                       ''         
                        ''   {self.s}    ,,..;.          .,.                   .,.          ',   ''                       ''         
                        ''         .;;..;'          .,.                   .,.          ',   ,,                       ,,         
                        ''         .,.  ,'          .,.   .............   .,.          ',   .'.......................'.         
                        ''         .,.  ,'          .,.  ,;...........;,  .;.          ',                                       
                        ';.........';.  ,'          .,.  ,'  \033[91mKontor\033[0m   .,  .,.          ',                                       
                        ...........    ,'          .,.  ,'           ',  .,.          ',                                       
                                        ,'          .;,..:'           ':'.,;.          ',                                       
                                        ,'    {self.w}              {self.o}              {self.e}    ',                                       
                                        ,'          .,,.';.           .;'.,,.          ',                                       
                                        ,'          .;,..;'           ';..';.          ',                                       
                                        ,'          .;.  ,'           ',  .;.          ',                                       
                                        ,c,,,,,,,,,,::.  ;c,,,,,,,,,,,c;  .::,,,,,,,,,,c,                                       '''
        )
        
        
    # Förflyttelse beroende på nuvarande plats
    def move(self, move):
        print(self.location)
        
        if move == "vänster" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = "   "
            self.w = ">-O"
            
        elif move == "höger" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = ">-O"
        
        elif move == "vänster" and self.w == ">-O":
            self.old = "väst"
            self.s = ">-O"
            self.w = "   "
            
        elif move == "fram" and (self.e == ">-O" or self.w == ">-O"):
            if self.e == ">-O":
                self.old = "öst"
            if self.w == ">-O":
                self.old = "väst"
            self.d = ">-O"
            self.e = "   "
            self.w = "   "

        elif move == "vänster" and self.e == ">-O":
            self.old = "öst"
            self.o = ">-O"
            self.e = "   "
        
        elif move == "höger" and self.w == ">-O":
            self.old = "väst"
            self.o = ">-O"
            self.w = "   "

        elif move == "höger" and self.s == ">-O":
            self.old = "förråd"
            self.s = "   "
            self.w = ">-O"
            
        elif move == "vänster" and self.d == ">-O":
            self.old = "matsal"
            self.b = ">-O"
            self.d = "   "

        elif move == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "

        elif move == "fram" and self.d == ">-O":
            return "exit attempt"

        elif move == "ner" and self.d == ">-O":
                self.old = "matsal"
                self.k = ">-O"
                self.d = "   "

        elif move == "vänsterhall" and self.d == ">-O":
                self.old = "matsal"
                self.w = ">-O"
                self.d = "   "
        
        elif move == "högerhall" and self.d == ">-O":
                self.old = "matsal"
                self.e = ">-O"
                self.d = "   "
        
            
      
        
        elif move == "höger hall" and self.d == ">-O":
            self.old = "matsal"
            self.w = ">-O"
            self.d = "   "

        elif move == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "
        
        elif move == "höger" and self.b == ">-O":
            self.old = "prishörna"
            self.d = ">-O"
            self.b = "  "
        
        elif move == "vänster" and self.t == ">-O":
            self.old = "toaletter"
            self.d = ">-O"
            self.t = "  "
        
        elif move == "kök" and self.d == ">-O":
            self.old = "matsal"
            self.k = ">-O"
            self.d = "   "

        elif move == "fram":
            if self.old == "kök":
                self.old = "matsal"
                self.k = ">-O"
                self.d = "   "

            elif self.old == "matsal":
                if self.e == ">-O":
                    self.old = "öst"
                if self.w == ">-O":
                    self.old = "väst"
                if self.b == ">-O":
                    self.old = "prishörna"
                if self.t == ">-O":
                    self.old = "toaletter"
                if self.k == ">-O":
                    self.old = "kök"
                self.d = ">-O"
                self.e = "   "
                self.w = "   "
                self.b = "   "
                self.t = "   "
                self.k = "   "

            elif self.old == "förråd":
                self.old = "väst"
                self.s = ">-O"
                self.w = "   "
            
            elif self.old == "väst":
                if self.s == ">-O":
                    self.old = "förråd"
                if self.d == ">-O":
                    self.old = "matsal"
                if self.o == ">-O":
                    self.old = "Kontor"
                self.w = ">-O"
                self.s = "   "
                self.o = "   "
                self.d = "   "
        
            elif self.old == "öst":
                if self.d == ">-O":
                    self.old = "matsal"
                if self.o == ">-O":
                    self.old = "kontor"
                self.e = ">-O"
                self.d = "   "
                self.o = "   "

            elif self.old == "kontor":
                if self.e == ">-O":
                    self.old = "öst"
                if self.w == ">-O":
                    self.old = "väst"
                self.o = ">-O"
                self.e = "   "
                self.w = "   "

            elif self.old == "toaletter":
                self.old = "matsal"
                self.t = ">-O"
                self.d = "   "

            elif self.old == "prishörna":
                self.old = "matsal"
                self.b = ">-O"
                self.d = "   "
    
    # Visar vart man kan röra sig
    def printChoice(self):
        Plats = self.location.capitalize()
        if self.o == ">-O":
           self.text = "(a) Vänster till Vänstra Hallen \n(d) Höger till Högra Hallen"
        if self.w == ">-O":
            self.text =  "(a) Vänster till Förrådet \n(d) Höger till Kontoret \n(w) Fram till Matsalen"
        if self.e == ">-O":
            self.text = "(a) Vänster till Kontoret \n(w) Fram till Matsalen"
        if self.s == ">-O":
            self.text = "(d) Höger till Vänstra Hallen"
        if self.d == ">-O":
            self.text = "(a) Vänster till Prishörnan \n(d) Höger till toaletterna. \n(s) Ner till Köket. \n(q) Ner till vänster hall. \n(e) Ner till höger hall \n(w) Fram till Utgången"
        if self.t == ">-O":
            self.text = "(a) Vänster till Matsalen"
        if self.b == ">-O":
            self.text = "(d) Höger till Matsalen"
        if self.k == ">-O":
            self.text = "(w) Tillbaka till Matsalen"
        return "Du befinner dig i " + Plats + "\n" + "Du kan gå:\n" + self.text
    
    # Skickar tillbaka nuvarande position
    def returnLocation(self):
        if self.o == ">-O":
            self.location = "kontoret"
            self.x = 0.62
            self.y = 0.85
        if self.w == ">-O":
            self.location = "vänster hall"
            self.x = 0.53
            self.y = 0.8
        if self.e == ">-O":
            self.location = "höger hall"
            self.x = 0.72
            self.y = 0.8
        if self.s == ">-O":
            self.location = "förrådet"
            self.x = 0.435
            self.y = 0.725
        if self.d == ">-O":
            self.location = "matsalen"
            self.x = 0.62
            self.y = 0.35
        if self.t == ">-O":
          self.location = "toaletterna"
          self.x = 0.88
          self.y = 0.35
        if self.b == ">-O":
            self.location = "prishörnan"
            self.x = 0.36
            self.y = 0.22
        if self.k == ">-O":
            self.location = "köket"
            self.x = 0.85
            self.y = 0.68
        return self.location
    
    # Kollar ifall man blir jagad.
    def hunted(self, roomStatus):
        if roomStatus == "same":
            self.hunt = True
            print("\033[91mFredrik såg dig!! Skynda dig tillbaka till kontoret!\n\033[0m")
        if self.hunt == True:
            return True
        else:
            return False
    # Skickar tillbaka hur många steg man tagit medan man blir jagad.
    def run(self):
        if self.hunt == True and self.o != ">-O":
            self.steps = self.steps + 1
            print(self.steps)

        if self.o == ">-O":
            self.steps = 0
            print("Du hann undan\n")
            self.hunt = False
        return self.steps
    
    def movement(self):
                    self.choice = " "
                    keyboard.read_key()
                    if keyboard.is_pressed("a"):
                        self.choice = "vänster"
                    elif keyboard.is_pressed("d"):
                        self.choice = "höger"
                    elif keyboard.is_pressed("w"):
                        self.choice = "fram"
                    elif keyboard.is_pressed("s"):
                        self.choice = "ner"
                    elif keyboard.is_pressed("e"):
                        self.choice = "högerhall"
                    elif keyboard.is_pressed("q"):
                        self.choice = "vänsterhall"

                    return self.choice



   
    def returnPosition(self):
        return self.x, self.y
        
    def returnMessage(self):
        return "Fredrik jagar dig!"