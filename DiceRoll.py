x = int(input("Sláðu inn tölu: "))
n = int(input("Sláðu inn veldisvísi: "))
y = 1
for a in range (n):
      y = y*x
print (x,"í",n,"veldi er",y,)
svar1 = input("Villtu keyra forrit aftur? j ef já: ")

while svar1 == "j":
      x = int(input("Sláðu inn tölu: "))
      n = int(input("Sláðu inn veldisvísi: "))
      y = 1
      for a in range (n):
            y = y*x
      print (x,"í",n,"veldi er",y,)
      svar1 = input("Villtu keyra forrit aftur? j ef já: ")