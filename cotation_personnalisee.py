#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch

from reponses import bonne_reponses
from piege_reponses import piege_reponses

def cotation_personnalisee(q, question, bonne_reponses, reponse_choisie, piege_reponses, mode_comparatif=False):
    """
       Reponse vide = 0
       Reponse mauvaise = -1
       Reponse bonne = +1
       Reponse hasard = 0 au test et le test s'arrête si on a choisie mode d'affichage unique
    """
   
    if reponse_choisie == "":  #Reponse vide 
        return 0
    
    while any(lettre not in question for lettre in reponse_choisie) or reponse_choisie != "":
        print("Votre réponse ne correspond à aucune proposition. Veuillez recommencer!")
        print()
        reponse_choisie = input("Votre réponse ici: ").strip().lower().replace(" ", "")
        
    for e in reponse_choisie:   # Réponse au hasard 
        if question[e] in piege_reponses[q]:
            if mode_comparatif:
                return "HASARD!"
            else:
                print()
                print("Le programme a détecté une réponse trop hasardeuse. Vous avez rater votre test!")
                print()
                return "HASARD!"

    if q in [1, 3, 5, 6, 8, 9]: #mult reponse
        liste = []
        for e in reponse_choisie:
            if question[e] in bonne_reponses[q]:
                liste.append("good")
            else:
                liste.append("mauvais")
        if "mauvais" in liste:
            return -1
        else:
            return 1

    
    else: 
        if question[reponse_choisie] in bonne_reponses[q]:    #bonne ou mauvaise reponse
            return 1
        else:
            return -1