#Le liste (anche chiamate array) sono dei contenitori di elementi simili tra loro, cioè elementi dello stesso tipo. Queste liste sono 0-based, cioè la conta parte

mia_lista = []

numeri = [4,2,8,3,6,1]

parole = ["Ciao", "Dario", "Arrivederci", "Oggi"]

studenti = ["Cristina", "Marco", "Ioas", "Franco", "Andrei"]

#lista mista: non ha molto senso logico pur essendo fattibile

mista = [2, "Parola", True, "Ciao", 23, "23"]
studente = ["Paolo", "Rossi", 25, True, "TSS"]

#L' indice mi serve per poter richiamare il valore dell' array(lista) in quell'esatta posizione
print(studenti[0])

#propr len : mi dice quanti sono gli elementi in una lista
numStud = len(studenti)
print(f"In classe ci sono {numStud} studenti")


primoStud = studenti[0]
ultimoStud = studenti[len(studenti) - 1]

print(f"L'ultimo studente dell'elenco è {ultimoStud}")

#Per poter stampare tutti gli elementi uno alla volta uso il FORIN
# stud è una var locale che crei al volo nel costrutto
for stud in studenti:
    print(stud)


colori = ["rosso", "giallo", "blu", "nero", "bianco"]

for i in range(len(colori)):
    print(f"posizione {i} : {colori[i]}")