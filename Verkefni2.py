#Liður1 - MinnstaTala2
tala1 = int(input("Sláðu inn heiltölu: "))
#Forrit biður um fyrstu heiltölu

tala2 = int(input("Sláðu inn aðra heiltölu: "))
#Forrit biður um aðra heiltölu

if (tala2 == tala1):
    tala2 = int(input("Sláðu inn töluna aftur, athugið ekki má slá inn sömu tölu tvisvar: "))
#Forrit biður um heiltölu 2 aftur ef sú sama var slegin inn fyrir heiltölu 1

tala3 = int(input("Sláðu inn aðra heiltölu: "))
#Forrit biður um aðra heiltölu ef sú sama hefur nú þegar verið slegin inn

if (tala3 == tala1 or tala3 == tala2):
    tala2 = int(input("Sláðu inn töluna aftur, athugið ekki má slá inn sömu tölu tvisvar: "))
#Forrit biður um aðra heiltölu ef sú sama hefur nú þegar verið slegin inn

tala123 = [tala1, tala2, tala3]
tala123.sort()
#Forrit býr til lista og sorterar listann

print ("Talan í miðjunni er", tala123[int(len(tala123)/2)])
#Forrit prentar út tölu í miðju listans

#Liður 2 - Tommur í Sentimetra
choice = input("Veldu 1 til að breyta tommum í sentimetra. Veldu 2 til að breyta sentimetrum í tommur: ")
number = float(input("Sláðu inn töluna þína: "))
#Forrit spyr hverju þú vilt breyta í hvað og spyr síðan um töluna sem mun reikna cm eða tommur

if (choice == 1):
    print (number/2.54 ,"tommur",)
else:
    print (number*2.54 ,"cm",)
#Forrit reiknar tommur í cm eða cm í tommur


#Liður 3 - Arstidir
num = int(input("Sláðu inn númer mánaðar: "))
#Forrit biður
if (num == 12):
    print ("Núna styttist í jólin")
elif (num == 11):
    print ("Núna styttist í jólin")
elif (num == 10):
    print ("Núna er haustið gengið í garð.")
elif (num == 9):
    print ("Núna er haustið gengið í garð.")
elif (num == 8):
    print ("Núna er sumarið komið með blóm í haga.")
elif (num == 7):
    print ("Núna er sumarið komið með blóm í haga.")
elif (num == 6):
    print ("Núna er sumarið komið með blóm í haga.")
elif (num == 5):
    print ("Vorið er komið og grundirnar gróa.")
elif (num == 4):
    print ("Vorið er komið og grundirnar gróa.")
elif (num == 3):
    print ("Nú er daginn tekið að lengja.")
elif (num == 2):
    print ("Nú er daginn tekið að lengja.")
elif (num == 1):
    print ("Nú er daginn tekið að lengja.")
#Hér fyrir ofan línur 41-64 getur forrtiðið sagt til um hvað á að segja við hverja tölu sem er slegin inn
else:
    print ("Rangur innsláttur")
#Fyrir ofan (Else:) segir forrtið Rangur innnsláttur ef þú skrifaðir ekki in tölu mánaðar 

#Lður 4 - NafnManadar
nafn = input("Hvað heitir þú? ")
#Forrit biður um nafn notanda
kyn = input("ertu kk eða kvk? ")
#Forrit biður um kyn notanda
x = float(input("Sláðu inn fyrstu tölu "))
y = float(input("Sláðu inn aðra tölu "))
#Forrit biður um 2 tölur frá notanda
if (kyn == "kk"):
    print ("Blessaður",nafn,)
if (kyn == "kvk"):
    print ("Blessuð",nafn,)
else:
    print ("Blessaður eða blessuð ég veit ekki hvors kyns þú ert")
#Forrit heilsar notanda miðað við kyn og nafn notanda
if (x == y):
    print ("Báðar tölur eru jafn stórar")
else:
    largest = x if x > y else y
    print("{0} er stærri".format(largest))
#Forritið segir hvor talnanna er stærri

if (x-y > 99):
    print ("mismunur talnanna er meiri en 100")
if (y-x > 99):
    print ("mismunur talnanna er meiri en 100") 
else:
    print ("mismunur talnanna er minni en 100")
#Forrit segir til um mismun talnanna, hvort það sé meira eða minna en 100 tölu munur


#Liður 5 - Talnabil
a = int(input("Sláðu inn tölu minni en 0 eða stærri en 10: "))
#Forrit biður um tölu minni en 0 eða stærri en 10
if (a > 0 or a < 10):
    print ("Tala er ekki minni en 0 eða stærri en 10")

if (a < 0 or a > 10):
    print ("Vel gert!")
#Forrit segir til um hvort notandi setti inn réttu tölu eða ekki