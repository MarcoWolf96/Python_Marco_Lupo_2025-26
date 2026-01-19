iscrizioneUni = False

if iscrizioneUni:
    print("Caro studente/essa puoi sostenere gli esami !!")
else:
    print("MI spiace, non essendo iscirtto/a non puoi sostenere gli esami")

# Miglioro l'if e per sostenre la laurea devo aver completato gli esami ed essere iscritto


esame1 = 20
esame2 = 30
esame3 = 16

media = (esame1 + esame2 + esame3)/3

if esame1 >= 18 and esame2 >= 18 and esame3 >=18 and iscrizioneUni:
    print("Puoi accedere alla laurea, hai completato tutti gli esami e la tua iscrizione è valida")
elif esame1 >=18 and esame2 >=18 and esame3>=18 and not iscrizioneUni:
    print("Gli esami sono validi ma non sei iscritto, non hai pagato le tasse. Non puoi sostenere la laurea")
else:
    print("Mi spiace, non hai ancora completato gli esami. Non puoi sostenere la laurea")


