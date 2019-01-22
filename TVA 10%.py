def TVA():
	Nb_entree = int(input("Entre le prix HORS TAXE : "))
	Nb_sortie1 = Nb_entree * 0.1
	Nb_sortie = Nb_entree +  Nb_sortie1
	print("le prix TTC est de: ",Nb_sortie,"EUROS et le montant de la TVA est de :",Nb_sortie1,"EUROS")
TVA()