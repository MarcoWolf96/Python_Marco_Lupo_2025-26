#Scrivi un programma per gestire una lista della spesa ( inserisci in partenza almeno 6 prodotti). Tutto questo fallo in un menu dal quale l' utente seleziona i comandi
#2. Mostra i prodotti della lista uno alla volta
#3. Cercare se esiste un prodotto nella lista (dare anche la possibilità all'utente di inserire a mano il prodotto tramite input)
#4. Contare quanti sono i prodotti presenti
#5. Mostrare solo i prodotti con più di 5 lettere
#6. Creare una nuova lista di prodotti con più di 5 lettere ma in maiuscolo
#7. Aggiungi un prodotto alla lista chiedendo all'utente il nome del prodotto
#8. Rimuovi un prodotto a scelta dell' utente

# Creazione Menu

print("=== Gestione Lista della Spesa ===\n")

scelta = ""

while scelta != 7:
    print("Azioni disponibili")
    print("1. Mostra la mia lista della spesa")
    print("2. Cerca qualcosa nella lista della spesa")
    print("3. Mostra quanti prodotti sono presenti nella lista della spesa")
    print("4. Mostra prodotti con più di 5 lettere")
    print("5. Aggiungi un prodotto alla lista")
    print("6. Rimuovi un prodotto dalla lista")
    print("7. Esci")

    scelta = int( input("Scegli l'azione desiderata: \n"))

# Creazione lista della spesa
    lista_spesa = []
    prodotti = ["pane", "detersivo", "carne", "insalata", "croccantini", "the"]
    if scelta == 1:
        print("Ecco la lista della spesa:")
        

        for list in prodotti:
            print(list)
        

# Conferma di un prodotto
    elif scelta == 2:
        spesa = input("Cosa hai messo nella lista?")
        if spesa in prodotti:
            print("Prodotto trovato")
        else:
            print("Prodotto non trovato")

# Conteggio prodotti della lista
    elif scelta == 3:
        conteggio_lista = len(prodotti)
        print(f"I prodotti nella lista sono {conteggio_lista}")

# Display dei prodotti con piu di 5 lettere
    elif scelta == 4:
        print("I prodotti con piu di 5 lettere sono:")

        for prodotto in prodotti:
            if len(prodotto) > 5:
                print(prodotto)

# Aggiunta di un prodotto alla lista
    elif scelta == 5:
        aggiunta = input("Devo aggiungere qualcosa alla lista della spesa, cosa vorresti?")
        prodotti.append(aggiunta)
        print("Prodotto aggiunto, ecco la nuova lista:")

        for list in prodotti:
            print(list)

# Rimozione di un prodotto alla lista
    elif scelta == 6:
        rimozione = input("Devo rimuovere qualcosa dalla lista della spesa, cosa tolgo?")
        if rimozione in prodotti:
            prodotti.remove(rimozione)
        else:
            print("Prodotto non trovato")

        print("Prodotto rimosso, ecco la nuova lista:")

        for list in prodotti:
            print(list)
    elif scelta == 7:
        print("Ciao alla prossima")
    else:
        print("Scelta non valida")

print("Programma terminato")