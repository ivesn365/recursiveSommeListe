som = 0
compteur = 0
tab = [1, 2, 7, 8, 9,58,69,254]
taille = len(tab)

while compteur < taille:
    som = som + tab[compteur]
    compteur = compteur + 1

print(som)