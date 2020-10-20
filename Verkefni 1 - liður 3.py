kr = int(input("Sláðu inn fjölda króna"))

while (kr > 10000):
    print (kr//10000,"Stk 10000kr")
    kr = kr%10000
    print(kr//5000, "Stk 5000kr")
    kr = kr%5000
    print(kr//1000, "Stk 1000kr")
    kr = kr%1000
    print(kr//500, "Stk 500kr")
    kr = kr%500
    print(kr//100, "Stk 100kr")
    kr = kr%100
    print(kr//50, "Stk 50kr")
    kr = kr%50
    print(kr//10, "Stk 10kr")
    kr = kr%10
    print(kr//5, "Stk 5kr")
    kr = kr%5
    print(kr//1, "Krónur")
    kr = kr%1