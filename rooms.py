import random
import time
#import ascasciimodule
import keyboard

inventoryList = []
coinList = []
codeReal = str(random.randint(1000, 9999))
text = "hello"
itemsUsed = []

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
                    if "closet" not in itemsUsed:
                       if codeReal in inventoryList: 
                            inventoryAdd("Nyckel 1")
                            coinList.append("coin")
                            coinList.append("coin")
                            itemsUsed.append("closet")
                            return "used"       
                       if codeReal not in inventoryList:
                            return "no"

# går man in i köket får man alternativet att leta runt, väljs det får man 2 myn samt koden till kassavalvet
def kitchen():
            if "kitchen" not in itemsUsed:
                inventoryAdd(codeReal)
                coinList.append("coin")
                coinList.append("coin")
                itemsUsed.append("kitchen")
                return "found"

        

# likadant som ovanför fast här hittar du en till nyckel som läggs in i listan (inventory)
def restrooms():
    if "restrooms" not in itemsUsed:
        inventoryAdd("Nyckel 2")
        coinList.append("coin")
        itemsUsed.append("restrooms")
        return "found"
        
# i prishörnan kan du välja att köpa en nyckel, koden berättar om du kan köpa eller inte har råd, köper du en nyckel blir antalet nycklar 1 fler samt dina coins blir 3 färre
def prizecorner():
    if "prizecorner" not in itemsUsed:
        if len(coinList) == 5:
            coinList.clear()
            inventoryAdd("Nyckel 3")
            itemsUsed.append("prizecorner")
            return "bought"
        else: 
            return "no"
        


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


# Skickar tillbaka koden
def returnCode():
     return codeReal


# Skickar tillbaka storleken på inventoriet
def inventorySize():
     return len(inventoryList)
