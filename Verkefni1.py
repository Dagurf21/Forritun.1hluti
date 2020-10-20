#Liður 1

nafn1 = input ("Hvað heitir þú? ")
#Forrit biður um nafn notanda

afangi = input ("Hvað er uppáhalds fagið þitt?")
#Forrit biður um uppáhaldsfag notanda

print ("Velkomin í áfangan",afangi,"."" Þetta verður skemmtileg önn hjá okkur",nafn1, ".")
#Lína fyrir ofan prentar út texta með svörum notanda


#Liður 2

tala2 = float(input("Sláðu inn tölu hærri en 100:"))
#Forrit biður um tölu hærri en 100
tala3 = (tala2/5.5)
#tala3 er tala notanda deilt í 5.5

print ("{0:.2f}".format(tala3))
#Forrit birtir tala3 með 2 aukastöfum


#Liður 3

tala1 = float(input ("Sláðu inn heiltölu:"))
#Forrit biður um heiltölu frá notanda
tala2 = float(input ("Sláðu inn aðra tölu:"))
#Fottir biður um aðra heiltölu frá notanda

print (tala1*tala2, "margföldun")
#Forrit reiknar margföldun tveggja talnanna
print (tala1-tala2, "Frádráttur")
#Forrit reiknar frádrátt tveggja talnanna


#Liður 4

hæd = float(input ("Hæð kassa:"))
#Forrit biður um hæð kassa
lengd = float(input ("Lengd kassa:"))
#Forrit biður um lengd kassa
breidd = float(input ("Breidd kassa:"))
#Forrit biður um breidd kassa frá

print ("Kassin þinn er" ,hæd*lengd*breidd, "m3")
#Forrtit reiknar rúmmál kassa og birtir svarinu á skjáinn í rúmmetrum


#Liður 5
aldur4 = float(input("Hver er aldur þinn? "))
#Forrit biður notanda um aldur sinn
aldur5 = float(input("Hver er aldur faðir þíns? "))
#Forrit biður notanda um aldur faðir síns
aldurfadir = (aldur5-aldur4)
#Forrit reiknar aldur föðurs þegar sonur fæðist

print ("Faðir þinn var",aldurfadir,"þegar þú fæddist") 
#Forrit birtit aldur faðirs á skjá


#Liður 6

nemi1 = float(input ("Hver er aldur þinn?"))
#Forrit biður um aldur einstaklings 1
nemi2 = float(input ("Hver er aldur þinn?"))
#Forrit biður um aldur einskalings 2
nemi3 = float(input ("Hver er aldur þinn?"))
#Forrit biður um aldur einstaklings 3

summaaldur = (nemi1+nemi2+nemi3)
#Forrit reiknar summu aldurs þeirra
medalaldur = float(summaaldur/3)
#Forrit reiknar meðalaldur einstkalinganna
print ("Meðalaldur ykkar er:",medalaldur,)
#Forrit birtir meðalaldur einstaklinganna


print ("Gaman að geta aðstoðað þig við þessa útreikninga",nafn1,".")
#Forrit kveður