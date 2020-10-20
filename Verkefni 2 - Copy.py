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