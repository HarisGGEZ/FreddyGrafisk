import random
import time
#import ascasciimodule
from playsound import playsound
import keyboard

inventoryList = []
coinList = []
codeReal = str(random.randint(1000, 9999))
text = "hello"
restroomFound = False
kitchenFound = False
supplyUsed = False

def inventory():
    inventoryList.sort()
    listText = "\n".join(inventoryList)
    text = ("I din väska:\n" + listText + "\nDu har " + str(len(coinList)) + " mynt")
    return text

def exit():
    if "Nyckel 1" in inventoryList and "Nyckel 2" in inventoryList and "Nyckel 3" in inventoryList:
        return True

# menyn till spelet
def intro():
    #asciimodule.menu()
    while True:
        keyboard.read_key()
        if keyboard.is_pressed("1"):
            break
        if keyboard.is_pressed("2"):
            return "option"

# inuti inställningar
def options():
    maxCoins = False
    maxKeys = False
    while True:
        time.sleep(0.3)
        print("\n1. Fusk")
        print("2. Backa\n")
        keyboard.read_key()
        if keyboard.is_pressed("1"):
            while True:
                    print("\n\n1. Stäng av Fredrik")
                    print("2. Alla Mynt")
                    print("3. Alla Nycklar")
                    print("4. Tillbaka\n")
                    time.sleep(0.3)
                    keyboard.read_key()
                    if keyboard.is_pressed("1"):
                            print("\nFredrik är avstängd.")
                            time.sleep(0.3)
                            return "cheat"  
                    if keyboard.is_pressed("2"):
                        if maxCoins == False:
                            print("\nDu har alla mynt.")
                            coinList.append("coin")
                            coinList.append("coin")
                            coinList.append("coin")
                            coinList.append("coin")
                            coinList.append("coin")
                            maxCoins = True
                    if keyboard.is_pressed("3"):
                        if maxKeys == False:
                            maxKeys = True
                            print("\nDu har alla nycklar.")
                            inventoryAdd("Nyckel 1")
                            inventoryAdd("Nyckel 2")
                            inventoryAdd("Nyckel 3")
                    if keyboard.is_pressed("4"):
                        break
                    time.sleep(0.3)
        if keyboard.is_pressed("2"):
             break
            


# lägger till objekt i listan
def inventoryAdd(object):
    inventoryList.append(object)

def codeUsed():
    codeReal = "used"
    return codeReal

# Event i förrådet där man kan skriva in en kod
def supplycloset():
                    global supplyUsed
                    if supplyUsed == False:
                       if codeReal in inventoryList: 
                            inventoryAdd("Nyckel 1")
                            coinList.append("coin")
                            coinList.append("coin")
                            supplyUsed = True
                            return "used"       
                       if codeReal not in inventoryList:
                            return "no"

# går man in i köket får man alternativet att leta runt, väljs det får man 2 myn samt koden till kassavalvet
def kitchen():
            global kitchenFound
            if kitchenFound == False:
                print(f"Du hittade 2 mynt och en lapp med numret {codeReal}")
                inventoryAdd(codeReal)
                coinList.append("coin")
                coinList.append("coin")
                kitchenFound = True
                return "found"

        

# likadant som ovanför fast här hittar du en till nyckel som läggs in i listan (inventory)
def restrooms():
    global restroomFound
    if restroomFound == False:
        inventoryAdd("Nyckel 2")
        coinList.append("coin")
        restroomFound = True
        return "found"
        
# i prishörnan kan du välja att köpa en nyckel, koden berättar om du kan köpa eller inte har råd, köper du en nyckel blir antalet nycklar 1 fler samt dina coins blir 3 färre
def prizecorner():
    global prizeBought
    if prizeBought == False:

        if len(coinList) == 5:
            coinList.clear()
            inventoryAdd("Nyckel 3")
            prizeBought = True
            return "bought"
            
        else: 
            return "no"
        
def dead():
    #asciimodule.death()
    try:
        playsound("freddy.mp3")
    except:
         pass

# Tar bort alla items
def itemsReset():
    while len(coinList) != 0:
        coinList.remove("coin")
    try:
        inventoryList.remove("Nyckel 1")
        inventoryList.remove("Nyckel 2")
        inventoryList.remove("Nyckel 3")
    except:    
         print("")


def returnCode():
     return codeReal