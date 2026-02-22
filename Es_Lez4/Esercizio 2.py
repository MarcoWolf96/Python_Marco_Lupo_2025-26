def mostra_menu():
    print("\n--- GESTIONE LISTA DELLA SPESA ---")
    print("1. Aggiungi un prodotto")
    print("2. Mostra la lista")
    print("3. Rimuovi un prodotto")
    print("4. Conta i prodotti presenti")
    print("5. Pulisci la lista")
    print("0. Esci")

def gestisci_spesa():
    lista_spesa = []

    while True:
        mostra_menu()
        scelta = input("Seleziona un'opzione: ")

        # 1. AGGIUNTA PRODOTTI
        if scelta == '1':
            prodotto = input("Inserisci il nome del prodotto da aggiungere: ")
            lista_spesa.append(prodotto)
            print(f"'{prodotto}' aggiunto alla lista.")

        # 2. MOSTRA LISTA PRODOTTI
        elif scelta == '2':
            if not lista_spesa:
                print("La lista è attualmente vuota.")
            else:
                print("\nProdotti nella tua lista:")
                for i in range(len(lista_spesa)):
                    print(f"{i + 1}. {lista_spesa[i]}")

        # 3. RIMUOVI PRODOTTO
        elif scelta == '3':
            prodotto = input("Quale prodotto vuoi rimuovere? ")
            if prodotto in lista_spesa:
                lista_spesa.remove(prodotto)
                print(f"'{prodotto}' rimosso con successo.")
            else:
                print(f"Errore: '{prodotto}' non è presente nella lista.")

        # 4. CONTA PRODOTTI
        elif scelta == '4':
            quantita = len(lista_spesa)
            print(f"Ci sono {quantita} prodotti nella lista.")

        # 5. PULISCI LISTA DELLA SPESA
        elif scelta == '5':
            conferma = input("Sei sicuro di voler svuotare tutta la lista? (s/n): ")
            if conferma.lower() == 's':
                lista_spesa.clear()
                print("Lista svuotata completamente.")

        # 0. ESCI
        elif scelta == '0':
            print("Chiusura del programma. Buona spesa!")
            break
        
        else:
            print("Opzione non valida")


gestisci_spesa()