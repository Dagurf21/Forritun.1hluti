#Liður 1

tala01 = int(input("Sláðu inn heiltölu: "))

if tala01 % 5 == 0:
      print("Þessi tala er í 5 sinnum töflunni")
else:
      print("Þessi tala er ekki í 5 sinnum töflunni")

svar1 = input("Villtu endurtaka vinnslu? ")
#Forritið spyr notanda um heiltölu og checkar hvort talan sé í 5 sinnum töflunni eða ekki. FOrrit spyr svo hvort endurtaka á vinnsluna.

while svar1 == "já":
      tala02 = int(input("Sláðu inn heiltölu: "))

      if tala02 % 5 == 0:
            print("Þessi tala er í 5 sinnum töflunni")
      else: 
            print("Þessi tala er ekki í 5 sinnum töflunni")

      svar1 = input("Villtu endurtaka vinnslu? ")
#Forritið spyr notanda hvort hann vilji endurtaka vinnsluna eða ekki


#Liður 2

hlaupar = int(input("Sláðu inn ártal til að gá hvort það er/var hlaupaár: "))

if hlaupar % 4 == 0 and (hlaupar % 100 != 0 or hlaupar % 400 == 0):
      print ("Árið",hlaupar,"er hláupaár")

else:
      print ("Árið",hlaupar,"er ekki hlaupaár")
      
svar1 = input("Villtu endurtaka vinnslu? ")
#Forritið biður notanda um að slá inn ártal og checka hvort það ár er hlaupaár. Forritið spyr notanda hvort eigi að endurtaka vinnsluna

while svar1 == "já":

      hlaupar = int(input("Sláðu inn ártal til að gá hvort það er/var hlaupaár: "))

      if hlaupar % 4 == 0 and (hlaupar % 100 != 0 or hlaupar % 400 == 0):
            print ("Árið",hlaupar,"er hláupaár")

      else:
            print ("Árið",hlaupar,"er ekki hlaupaár")
            
      svar1 = input("Villtu endurtaka vinnslu? ")
#Forrit endurtekur vinnslu er notandi svara játandi


#Liður 3

summa = int(input("Sláðu inn heiltölu: "))
for tala in range (1,summa):

    summa = summa * tala

print("Margfeldi allra talnanna er:",summa)
#Forrit spyr notanda um heiltölu og tekur allar tölur á milli tölunar og margfaldar þær saman og birtir útkomu.


#Liður 4

h = int(input("SLáðu inn heiltölu á bilinu 1-9"))
for i in range(h + 1):
      print(i * "*")
#Forrit teiknar upp hálfan pýramída miðað við töluna sem notandi slær inn.