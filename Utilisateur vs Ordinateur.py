from random import *
compteur =  0
Chiffre_entree = int(input("Choissisez un chiffre entre 99 et 999 : "))
chiffre_hasard = randint(99, 999)
while Chiffre_entree != chiffre_hasard:
	chiffre_hasard = randint(99, 999)
	print(chiffre_hasard)
	compteur = compteur + 1
if Chiffre_entree == chiffre_hasard:
	print("Nombre trouver au bout de :",compteur)
	
