#Scrivi un programma per gestire una lista della spesa.
#1. Crea una lista della spesa con almeno 6 prodotti
#2. Mostra i prodotti della lista uno alla volta
#3. Cercare se esiste un prodotto nella lista (dare anche la possibilità all'utente di inserire a mano il prodotto tramite input)
#4. Contare quanti sono i prodotti presenti
#5. Mostrare solo i prodotti con più di 5 lettere
#6. Creare una nuova lista di prodotti con più di 5 lettere

lista_spesa = []
prodotti = ["pane", "detersivo", "carne", "insalata", "croccantini", "the"]

for list in prodotti:
    print(list)


spesa = input("Cosa hai messo nella lista?")
if spesa in prodotti:
    print("ci sta")
else:
    print("non ci sta")

