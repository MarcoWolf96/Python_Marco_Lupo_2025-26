# AND logico. Serve a mettere insieme più condizioni da soddisfare CONTEMPORANEAMENTE

# Range di voto - affinché il voto venga registrato si deve trovare tra 18 e 30

voto = 300

if voto >= 18 and voto <= 30:
#if 18 <= voto <= 30:
    print("Voto valido")
else:
    print("Voto non valido")

# Esempio ingresso nel locale. Devo dimostrare di essere maggiorenne e avere un invito

eta = 30
has_invito = False

if eta >= 18 and has_invito:
    print("Benvenuto, puoi entrare !!")
else:
    print("Mi spiace, non puoi entrare")

#Esempio: devo fare una gita: devono esserci più di 20 gradi, deve esserci il sole e deve essere un weekend

temperatura = 25
is_weekend = False
is_sole = False

if temperatura >= 20 and is_weekend and is_sole:
    print("Oggi si va in gita")
elif temperatura < 20 and is_weekend and is_sole:
    print("Niente gita, non c'è la giusta temperatura")
elif temperatura >= 20 and not is_weekend and is_sole:
    print("Niente gita, sei in mezzo alla settimana")
elif temperatura >= 20 and is_weekend and not is_sole:
    print("Niente gita, non c'è il sole")
else:
    print("Oggi me ne sto a casa")


#Validazione della email
email = "darioemail.com"

if "@" in email and "." in email and email.endswith((".com", ".it", ".org")) and len(email) > 8:
    print("Email valida")
else:
    print("Email non valida")