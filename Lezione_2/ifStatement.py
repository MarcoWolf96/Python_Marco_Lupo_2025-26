miaEta = 36
tuaEta = 36

#OPERATORI DI CONFRONTO (producono tutti dei valori booleani)
# == (uguale a)
# != (diverso)
# > oppure >= (maggiore)
# < oppure <= (minore)

condizione = (miaEta == tuaEta)

print(condizione)

#Per poter valutare la condizione utilizzo il costrutto dell'if
if miaEta == tuaEta:
    #il corpo dell'if viene eseguito solo se la condizione risulta essere true
    print("Abbiamo la stessa età") 


suaEta = 17

if suaEta >= 18:
    print("Hai", suaEta ,"anni, quindi sei maggiorenne")
else: #Questo else viene eseguito quando tutte le condizioni precedenti risultano essere false
    print("Hai", suaEta, "anni, quindi sei minorenne")

#Per poter valutare più condizioni uso il costrutto elif (else if)

voto = 28

if voto >= 30:
    print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")    

# ribalto la logica del mio if sopra
if voto < 18:
    print("Insufficiente")
elif voto < 24:
    print("Sufficiente")
elif voto < 30:
    print ("Buono")
else:
    print("Ottimo")

# Elaboro un if con l'utilizzo delle stringhe
nome = "Paolo"

if nome == "Anna":
    print("Benvenuta", nome, ", come stai ?")
else:
    print("Mi spiace, non riconosco il tuo nome")

###### operatore "in" e "not in" per stringhe
frase = "Internet Explorer è il miglior browser al mondo per scaricare Google Chrome"
parola = input("Quale parola vuoi cercare ?")

if parola.lower() in frase.lower():
    print("La parola", parola, "è nella frase")
else:
    print("La parola che cerchi non è nella frase")

if parola.lower() not in frase.lower():
    print("Mi spiace, la parola che cerchi non è nella frase")
else:
    print("La parola cercata è presente nella frase")

## startswith(), endswith(), isdigit(), isalpha()
email = "dario.mennillo@immaginazioneelavoro.it"

if email.startswith("dario"):
    print("l'indirizzo email comincia con dario")

if email.endswith(".it"):
    print("l'indirizzo termina con un dominio .it")

password = "1234"
if password.isdigit():
    print("La password è composta da solo numeri")


codice = "abc1234"
if not codice.isdigit(): #solo numeri
    print("Il codice non è composto da soli numeri")

if codice.isalnum(): #lettere e numeri
    print("Il codice è composto da lettere e numeri")

parola2 = "ciao"
if parola2.isalpha(): #solo lettere
    print("la parola è composta da solo lettere")

#Controllo se una stringa è vuota oppure no (Condizione di esistenza)

corso = ""

if corso:
    print("La stringa del corso non è vuota")
else:
    print("La stringa del corso è vuota")