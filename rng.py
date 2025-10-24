#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch
import random

def rng(lettrequest):
    """
       pre: lettrequest est une liste de lettre (a, b, c,  d)
       post: return une listemelange qui reprend les éléments de lettrequest mais à chaque fois dans un ordre différent
    """
    liste = []
    listemelange = [] #va recevoir les éléments de liste dans un ordre aléatoire
    for i in range(len(lettrequest)):
        liste.append(i)
    for j in range(len(lettrequest)):
        a = random.choice(liste) #un élément pris au hazard de la liste
        liste.remove(a) #comme ça chaque pioche est différente, on reprend pas un élément identique
        listemelange.append(a)
    return listemelange