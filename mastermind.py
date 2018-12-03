#- On importe les différents modules dont on à besoin -#

from random import *
import time

#- Début du programme -#

chiffre = ["- 0","- 1","- 2","- 3","- 4","- 5","- 6","- 7","- 8","- 9"]
initchiffre = [chiffre [i] [2] for i in range(len(chiffre))] #Il va cherche pour chaque caractere de la liste au rang 2 le chiffre.
lcombi = 4
mtenta = 8

#- Création de la combinaison secrete -#

def combis ():
    combisecrete = ""
    for i in range(0, lcombi):
        indexlist = randint(0,len(initchiffre) - 1)
        combisecrete = combisecrete + initchiffre[indexlist]

    return combisecrete 

#- Le joueur entre sa combinaison -#

start_time = time.time() #démarrage du temps d"execution 

def demandecombijoueur():
    mauvais = False 
    combij= input("Entez votre combinaison: ")
    
    if len(combij) != lcombi:
        print("    •Info•    ")
        print("Longueur de la combinaison incorrect rappel ex : '0123' ")
        mauvais = True 
   
    if mauvais == True :
        return ("Erreur")
    else:
        return combij

#- Comparaison entre la combinaison secrete et la combinaison entre par le joueur -#

def comparaison (combientre , combis):
    chiffreg = 0
    chiffreb = 0
    ce = list(combientre)
    cs = list(combis)

    for i in range(0 , len(ce)):
        if  (ce[i] == cs[i]):
            chiffreg = chiffreg + 1
            ce[i] = " A "
            cs[i] = " A "
    for i in range(0 , len(ce)):
        if (ce[i] in cs and ce[i] != " A "):
            chiffreb = chiffreb + 1 
            O = cs.index(ce[i])
            cs[O] = " A "


    return chiffreg , chiffreb

#- On affiche le resultat si le joueur a reussi ou si il a perdu -#

def resultat():
    compt = 0
    decompt = 8
    for i in range(0 , mtenta):
        combiuser = "Erreur"
        while combiuser == "Erreur":
            combiuser = demandecombijoueur()
        chiffrecompare = comparaison(combiuser, combirandom)
        if (chiffrecompare[0] == lcombi):
            compt = compt + 1
            print("• Félicitation, tu as Trouvez la combinaison secrète ! ")
            nom = str(input("• Entre ton Nom :"))
            print("• Félicitation " + str(nom) + " Tu as trouvez la combinaison au bout de " + str(compt) + " éssais •\n" + "• Mais il ta fallut : %s secondes " % (time.time() - start_time) + "Pour trouver la combinaison ! •\n• Retente ta chance Jeune PADAWAN !•" )
            break
        elif (compt == 7):
            print("• Tu as perdu ! • ")
            print("• Retente ta chance Jeune PADAWAN !•")
            break
        else:
            compt = compt + 1
            decompt = decompt - 1 
            print("    •Info•    ")
            print("- Tu as : ", chiffrecompare[0], "Chiffre bien placer et : ", chiffrecompare[1],"mal placer •")
            print("- Il te reste encore : " + str(decompt) + " essais •")

#- On affiche les règles du jeu et son fonctionement et on appelle les fonctions -#

print ("       • Mastermind 1.0 •        ")
print ("• Les règles sont simples, Trouver la bonne combinaison de chiffres en un minimum d'essais et de temps ! •")
print ("• Mais fait attention un même chiffre peut être répété plusieurs fois ! •")
combirandom = combis()
print(combirandom)
resultat()

#- Fin du programme -#

