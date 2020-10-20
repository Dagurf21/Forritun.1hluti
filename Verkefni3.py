#Liður 1


num1 = int(input("Sláðu inn heiltölu: "))

print ("Þú hefur vailð töluna:",num1,)

num2 = input("Villtu slá inn aðra tölu?: ") 
#Forrit fær heiltölu frá notanda og birtir hana á skjáinn, einnig er spurt hvort notandi vilji endurtaka forritið
while num2 == "já":
   
    num3 = int(input("Sláðu inn tölu: "))

    print ("Þú hefur valið töluna:",num3,)

    num2 = input("Villtu slá inn aðra tölu: ")
#Forrit endurtekur sig þangað til að notandi svarar með einhverju öðru

#Liður 2


tala1 = int(input("Sláðu inn lengd ferhyrnings"))

tala2 = int(input("Sláðu inn breidd ferhyrnings"))
#Notandi slær inn lengd og breidd ferhyrnings

utkoma1 = (tala1*tala2)
print ("Flatarmál ferhyrnings er:",utkoma1,)
#Forrit birtir útkomu

svar1 = input("Villtu endurtaka forritið? ")
#Forrit spyr notanda hvort eigi að endurtaka vinnslu

while svar1 == "já":
    
    tala1 = int(input("Sláðu inn lengd ferhyrnings"))

    tala2 = int(input("Sláðu inn breidd ferhyrnings"))

    utkoma1 = (tala1*tala2)
    print ("Flatarmál ferhyrnings er:",utkoma1,)

    svar1 = input("Villtu endurtaka forritið? ")
#Ef notandi svarar játandi endurtekur forrit sig, annars ekki


#Liður 3


passw = "Tskoli.is"

passw = input("Sláðu inn leyniorð: ")
#Forrit biður um leyniorðið (Tskoli.is)
while passw != "Tskoli.is":
    print ("Ekki leyniorð")

    passw = input("Sláðu inn leyniorðið aftur: ")
#Forrit biður notnadan um réttan innslátt þar til rétt leyniorð er slegið inn
if (passw == "Tskoli.is"):
    print ("Rétt leyniorð var slegið inn!")
#Ef notandi slær inn rétt leyniorð segir forritið að rétt leyniorð var slegið inn


#Liður 4


loop=True

while loop:
        kr = int(input("Sláðu inn upphæð í kr"))

        print(kr//10000, "stk 10000kr")
        kr = kr%10000
        print(kr//5000, "stk 5000kr")
        kr = kr%5000
        print(kr//1000, "stk 1000kr")
        kr = kr%1000
        print(kr//500, "stk 500kr")
        kr = kr%500
        print(kr//100, "stk 100")
        kr = kr%100
        print(kr//50, "stk 50")
        kr = kr%50
        print(kr//10, "stk 10 kr")
        kr = kr%10
        print(kr//5, "stk 5 kr")
        kr = kr%5
        print(kr//1, "krónur")
        kr = kr%1

        break


#Liður 5


loop = True

while loop:

    print ("1. Biður um 10 tölur. Finnur  summu þeirra og meðaltal.")
    print ("2. Biður um tölu og athugar hvort talan sé jöfntala eða oddatala.")
    print ("3. Hættir í forritinu og skrifar ’Ég er frábær forritari’ á skjáinn 10 sinnum og tilgreinir hversu oft forritið var keyrt.")

    val = int(input("Veldu tölu [1-3]: "))

    if val==1:
        print ("Þú hefur valið val 1")

        tala1 = int(input("Sláðu inn tölu"))
        tala2 = int(input("Sláðu inn tölu"))
        tala3 = int(input("Sláðu inn tölu"))
        tala4 = int(input("Sláðu inn tölu"))
        tala5 = int(input("Sláðu inn tölu"))
        tala6 = int(input("Sláðu inn tölu"))
        tala7 = int(input("Sláðu inn tölu"))
        tala8 = int(input("Sláðu inn tölu"))
        tala9 = int(input("Sláðu inn tölu"))
        tala10 = int(input("Sláðu inn tölu"))

        summa1 = (tala1+tala2+tala3+tala4+tala5+tala6+tala7+tala8+tala9+tala10)

        medaltal = (summa1/10)

        print ("Summa talnanna er:",summa1, "Meðaltal talnanna er:",medaltal,)

    elif val==2:
        print ("Þú hefur valið val 2")

        tala66 = int(input("Sláðu inn tölu:")) 
        tala66_type = ("Þessi tala er slétttala", "Þessi tala er oddatala") 
        print(tala66_type[tala66%2]) 

    elif val==3:
        print ("Þú hefur valið val 3")

        a = 1
        while a <= 10:
            print ("Ég er frábær forritari")
            a += 1

        print ("Forritið var keyrt 10 sinnum") 

        loop = False

    else:
        input ("Þú hefur ekki slegið inn tölu milli 1 og 3.")