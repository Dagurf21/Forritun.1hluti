# Liður 1

cm = int(input("Sláðu inn lengd í sentimetrum: "))

print (cm//100,"metrar")
cm = cm%100
print (cm//10,"desimetrar")
cm = cm%10
print (cm,"sentimetrar")

svar = input("Villtu keyra forrit aftur? Sláðu inn j ef já: ")

while svar == "j":

    cm = int(input("Sláðu inn lengd í sentimetrum: "))

    print (cm//100,"metrar")
    cm = cm%100
    print (cm//10,"desimetrar")
    cm = cm%10
    print (cm,"sentimetrar")

    svar = input("Villtu keyra forrit aftur? Sláðu inn j ef já: ")

# Liður 2

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