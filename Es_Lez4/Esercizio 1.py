#Funzioni operazioni
def addizione(x, y):
    return x + y

def sottrazione(x, y):
    return x - y

def moltiplicazione(x, y):
    return x * y

def divisione(x, y):
    return x / y

# Input e menù
print("=== Calcolatrice ===\n")

scelta = ""

while scelta != "Q":
    print("Seleziona operazione:")
    print("A.Somma")
    print("B.Sottrazione")
    print("C.Moltiplicazione")
    print("D.Divisione")
    print("Q.Esci")

    scelta = input("Inserisci numero scelta: ")
    if scelta != "Q":
        primoN = float(input("Inserisci primo numero: "))
        secondoN = float(input("Inserisci secondo numero: "))

        if scelta == 'A':
            print("Risultato:", addizione(primoN, secondoN))
        elif scelta == 'B':
            print("Risultato:", sottrazione(primoN, secondoN))
        elif scelta == 'C':
            print("Risultato:", moltiplicazione(primoN, secondoN))
        elif scelta == 'D':
            print("Risultato:", divisione(primoN, secondoN))
        else:
            print("Scelta non valida")
    else:
        print("Chiusura programma")
    
