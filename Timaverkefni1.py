#Liður 1

nafn001 = input("Hvaðp heitir þú? ")

met = float(input("Sláðu inn hæð þína í metrum: "))

cm = (met*100)

nidurstada = (200 - cm)

print ("Góðan daginn",nafn001,"Þig vantar",nidurstada,"sentimetra upp í að verða tveggja metra há/r.")


#Liður 2

stig = int(input("Hvað skoraði liðið þitt mörg stig? "))

if  (stig < 25):
    print ("Úps þetta hefur ekki endað vel.")

elif (stig < 50):
    print ("Þetta hefur gengið vel.")

elif (stig < 90):
    print ("Geggjað vel gert. ")

elif (stig < 0 or stig > 90):
    print ("Kjaftæði er þetta! þarft að vanda innsláttinn")


#Liður 3

a = int(input("Sláðu inn fyrstu tölu: "))

b = int(input("Sláðu inn aðra tölu: "))

c = int(input("Sláðu inn þriðju tölu: "))

sum = (a + b) - c
 
print("Niðurstaðan er:", sum)


#Liður 4

kr = 18845

print(kr//5000, "Fimmþúsund króna seðla")
kr = kr%5000
print(kr//1000, "Eitt þúsund króna seðla")
kr = kr%1000
print(kr//500, "fimm hundruð króna seðla")
kr = kr%500
print(kr//100, "Hundrað kallar")
kr = kr%100
print(kr//50, "Fimmtíu kallar")
kr = kr%50
print(kr//1, "Krónur")
kr = kr%1