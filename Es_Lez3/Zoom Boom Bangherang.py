#Stampa tutti i numeri da 1 a 100. Quando stampi un multiplo di 3 stampa Zoom, quando stampa un multipli di 5 stampa Boom, quando stampi un multiplo di 3 e di 5 stampa Bangherang
print("========  Giochino ZOOM BOOM Bangherang =========")

numZ = 0
numB = 0
numBang = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "Bangherang")
        numBang += 1
    elif i % 3 == 0: 
        print(i, "ZOOM")
        numZ += 1
    elif i % 5 == 0:
        print(i, "BOOM")
        numB += 1
    else:
        print(i)