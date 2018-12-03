print("* Fruit V1 *")
#---------------------------------------------------------------------------#

liste_initial = []
liste_fruit = []

#---------------------------------------------------------------------------#

def demande_utilisateur(liste1):
	while True:
		choix=input ("Souhaiter vous ajouter un fruit ?(Y/N):").upper()
		if (choix=="Y"):
			ajout_fruit=input("Quelle fruit souhaiter vous ajouter ?:")
			liste_initial.append(ajout_fruit)
			print(ajout_fruit,"a éte ajouter à votre liste de fruit !")
		elif (choix=="N"):
			break
		else : 
			print("Erreur : Il faut répondre par Y=Oui ou N=Non ")
	return liste_initial 
#---------------------------------------------------------------------------#

def nombre_de_caractere(liste1,liste_fruit):
	for i in range(0,len(liste_initial)):
		ajout_fruit=len(liste_initial[i])
		if (ajout_fruit>4):
			liste_fruit.append(liste_initial[i])
	return liste_fruit

#---------------------------------------------------------------------------#	

demande_utilisateur(liste_initial)
print ("Votre liste de fruit est la suivante : ", liste_initial)
affichage_liste=nombre_de_caractere(liste_initial,liste_fruit)
print ("les fruits possédant 5 caractères ou plus sont les suivants :", affichage_liste)