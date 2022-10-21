#Kod att utgå ifrån - pasta från  Teams-chatten
class Ad:
    def __init__(self, regno,manufacturer,model,year,startprice):
        self.__regno = regno
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.__startprice = startprice
    def Regno(self):
        return self.__regno
    def Manufacturer(self):
        return self.__manufacturer
    def Model(self):
        return self.__model
    def Year(self):
        return self.__year
    def SetYear(self, year):
        self.__year = year 
    def Startprice(self):
        return self.__startprice

def GetAdsFromFile():      
    allAds = []
    with open("cars.txt","r") as filen:
        for line in filen:
            line = line.replace("\n", "")
            parts = line.split(',')
            ad = Ad(parts[0], parts[1],parts[2], int(parts[3]), int(parts[4]) )
            allAds.append(ad)
    return allAds

    
# a = Ad("ABC123","Volvo", "XC60",2018,50000)        
# b = Ad("CCCDDD","Renault", "Megane",2019,40000)        

def SaveAdsToFile(ads):
    #Skriv om hela filen 
    with open("cars.txt", "w") as f:
        for x in ads:
            f.write(f"{x.Regno()},{x.Manufacturer()},{x.Model()},{x.Year()},{x.Startprice()}\n")





def getAd(ads, regno):
    for x in ads:
        if x.Regno() == regno:
            return x
    return None

ads = GetAdsFromFile()
a = getAd(ads, "ABC123")
a.SetYear(1900)
SaveAdsToFile(ads)


def InputThreeParts():
    while True:
        action = input("Action:")
        parts = action.split(' ')
        if len(parts) == 3:
            return parts
        print("Jamen tre delar dummer")


while True: # man inte matat in PAY
    regno = ""
    belopp = 0
    namn = ""

    #ABC123 500 Stefan
    while True:
        try:
            parts = InputThreeParts()
            regno = parts[0]
            theAd = getAd(ads, regno)   
            if theAd == None:
                print("Bilen finns inte") 
            else:
                belopp = int(parts[1])
                namn = parts[2]
                break
        except:
            print("Fel värden")

    print(f"{namn} bjuder {belopp} på {regno}")
    fileName = f"{regno}.txt"
    with open(fileName, "a") as f:
        f.write(f"{regno},{belopp},{namn}\n")



    # regno = input("Ange regno:")
    # ad = getAd(ads,regno)
    # if ad == None:
    #     print("Finns inte")
    # else:
    #     belopp = int(input("Ange bud:"))
    #     user = int(input("Vem är du:")) 


