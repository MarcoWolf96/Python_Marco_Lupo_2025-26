import random
import string

def test_forza(password):
    punteggio = 0
    speciali = ',.:;?!"'
    
    # 1. Lunghezza >= 8
    if len(password) >= 8:
        punteggio += 1
    
    # 2. Esiste almeno una Maiuscola
    if any(c.isupper() for c in password):
        punteggio += 1
        
    # 3. Contiene numeri
    if any(c.isdigit() for c in password):
        punteggio += 1
        
    # 4. Contiene caratteri speciali
    if any(c in speciali for c in password):
        punteggio += 1
    
    # Valutazione finale
    if punteggio <= 2:
        esito = "Debole"
    elif punteggio == 3:
        esito = "Media"
    else:
        esito = "Forte"
        
    return punteggio, esito

def genera_password():
    lettere = string.ascii_letters # a-z e A-Z
    numeri = string.digits          # 0-9
    speciali = ',.:;?!"'
    
    while True:
        print("\n--- GENERATORE DI PASSWORD ---")
        print("1. Genera una Password Semplice (Lettere e Numeri)")
        print("2. Genera una Password Forte (Lettere, Numeri e Caratteri Speciali)")
        print("3. Genera una Password Numerica (Solo Numeri)")
        print("4. Test forza password manuale")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        if scelta == '0': break

        # Lunghezza richiesta
        if scelta in ['1', '2', '3']:
            lunghezza = int(input("Quanto deve essere lunga la password? "))
            
            if scelta == '1':
                pool = lettere + numeri
            elif scelta == '2':
                pool = lettere + numeri + speciali
            else:
                pool = numeri
            
            # Generazione
            password = "".join(random.choice(pool) for _ in range(lunghezza))
            print(f"\nPassword Generata: {password}")
            
            # Test Password
            punti, forza = test_forza(password)
            print(f"Punteggio: {punti}/4 - Forza: {forza}")

        elif scelta == '4':
            pwd_utente = input("Inserisci la password da testare: ")
            punti, forza = test_forza(pwd_utente)
            print(f"Risultato: {punti}/4 - Forza: {forza}")
        else:
            print("Scelta non valida.")

genera_password()