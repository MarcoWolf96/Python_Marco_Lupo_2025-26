import random

def gioco():
    while True:
        print("\n--- NUMBER GUESSER: INDOVINA IL NUMERO ---")
        print("1. Easy Mode (1-50, Tentativi illimitati)")
        print("2. Hard Mode (1-100, Max 10 tentativi)")
        print("0. Esci")
        
        scelta = input("Seleziona una modalità di gioco ")

        if scelta == '1':
            target = random.randint(1, 50)
            tentativi_max = float('inf')
            print("\nEasy Mode attivata! Indovina il numero tra 1 e 50.")
            avvia_partita(target, tentativi_max)
            
        elif scelta == '2':
            target = random.randint(1, 100)
            tentativi_max = 10
            print("\nHard Mode attivata! Indovina il numero tra 1 e 100. Hai 10 tentativi!")
            avvia_partita(target, tentativi_max)
            
        elif scelta == '0':
            print("Grazie per aver giocato. A presto!")
            break
        else:
            print("Scelta non valida")

def avvia_partita(numero_segreto, max_tentativi):
    tentativi_fatti = 0
    vinto = False

    while tentativi_fatti < max_tentativi:
        try:
            mossa = int(input(f"Inserisci il tuo numero: "))
            tentativi_fatti += 1

            if mossa < numero_segreto:
                print("Troppo BASSO!")
            elif mossa > numero_segreto:
                print("Troppo ALTO!")
            else:
                print(f"Complimenti! Hai indovinato in {tentativi_fatti} tentativi.")
                vinto = True
                break
            
            if max_tentativi != float('inf'):
                print(f"Tentativi rimasti: {max_tentativi - tentativi_fatti}")

        except ValueError:
            print("Per favore, inserisci un numero valido.")

    if not vinto:
        print(f"Peccato! Hai esaurito i tentativi. Il numero era {numero_segreto}.")

gioco()