def menu():
	while True:
		print("**Carnet de contact v1**")
		print("Que souhaiter vous faire ? ")
		print("A - rechercher")
		print("B - ajouter")
		print("C - supprimer")
		print("D - Quitter")
		choix = input("Lettre: ").upper()
		if (choix == "A"):
			rechercher()
		elif (choix == "B"):
			getuserinfo()
		if(choix == "C"):
			supprimer()
		if (choix== "D"):
			print("/--- Merci de votre visite à bientot ! ---\ ")
			break 

def rechercher():
	mots = input("/--- Saisissez le nom de votre contact (Bonus : Taper 'tous' pour voir l'ensemble de vos contact) ---\ :")
	file = open("agenda.csv", "r")
	res = 0

	for line in file :
		tab = line.split(";")
		if (mots in tab[0] or mots in tab[1] or mots in tab[2] or mots in tab[3]) :
			print("Votre contact :", tab[0] ,tab[1], tab[2], tab[3])
			res = 1
		if (mots == "tous"):
			print("Vos contact :" ,tab[0])
			res = 1
	if (res == 0):
		print("#------ Ce contact n'est pas dans la liste ------#")
		getuserinfo()

def supprimer():
	chaine = input("/--- Nom du contact que vous souhaiter supprimer ---\ : ") 
	contenu = ""
 
	fichier = open("agenda.csv","r")
	for ligne in fichier:
		if not(chaine in ligne):
			contenu += ligne
	fichier = open("agenda.csv","w")
	fichier.write(contenu)
	print("#------ Votre contact ayant pour nom : " + str(chaine)+ " à été supprimer ! ------# ")
	
def addfile(nom ,prenom,numero,adresse):
	file = open("agenda.csv","a")
	file.write("{};{};{};\n".format(nom,prenom,numero,adresse))
	file.close() 

def getuserinfo():
	addnew = input("/--- Voulez vous ajouter un nouveau contact ? (oui/non) ---\ :")
	if (addnew=="non"):
		menu()
	elif (addnew=="oui"):
		nom= input("\nNom:")
		prenom = input("\nPrénom:")
		numero= int(input("\nNuméro:"))
		adresse = input("\nEmail:")
		addfile(nom, prenom, numero,adresse)
	else:
		print("#------ Erreur : Veuillez choisir entre 'oui' ou 'non' ------# ")
		getuserinfo()
menu()
