tala1 = int(input("Sláðu inn heiltölu: "))



tala2 = int(input("Sláðu inn aðra heiltölu: "))

if (tala2 == tala1):
    tala2 = int(input("Sláðu inn töluna aftur, athugið ekki má slá inn sömu tölu tvisvar: "))

tala3 = int(input("Sláðu inn aðra heiltölu: "))

if (tala3 == tala1 or tala3 == tala2):
    tala2 = int(input("Sláðu inn töluna aftur, athugið ekki má slá inn sömu tölu tvisvar: "))

tala123 = [tala1, tala2, tala3]

tala123.sort()

print ("Talan í miðjunni er", tala123[int(len(tala123)/2)])