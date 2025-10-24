#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch
import qcm
from piege_reponses import piege_reponses
from reponses import bonne_reponses
import rng
from cotation_severe import cotation_severe
from cotation_sympa import cotation_sympa
from cotation_personnalisee import cotation_personnalisee
from affichage_resultat import choix_affichage
from affichage_resultat import affichage_unique
from affichage_resultat import affichage_comparatif
from choix_mode_de_cotation import choix_mode_de_cotation
from affichage_bareme import affichage_bareme


lettrequest = ["a","b","c","d"] #correspond à la lettre associé, devant chaque proposition de réponse
listerng = [0,1,2,3] #l'indice des réponses pour les mélanger
question = {} # utilisation de {} pour créer un dictionnaire qui permet d'associer 'une clé à une valeur'

#initiation point question
points_sympa = 0
points_severe = 0
points_personnalisee = 0

if __name__ == '__main__':
    filename = "QCM.txt"

    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    
    bareme = input("Voulez-vous voir les différents barème de chaque mode de cotation avant de choisir, 1 pour oui et 0 pour non: ")
    affichage_bareme(bareme)
    
    nombre_question = len(questions)
    print()
    print("Avant de commencer vous devez choisir un affichage: Le mode de cotation unique affiche que son résultat selon la cotation choisie et le mode de cotation comparatif affiche un tableau comparatif des résultats sous tout les types de cotation")
    print()
    mon_choix = input("Quelle type d'affichage vous voulez? Pour unique, taper 0, pour comparatif, taper 1: ")
    
    while mon_choix not in ["0", "1"]:
        print("Le caractère choisi ne correspond à aucun mode d'affichage. Veuillez réessayer !")
        mon_choix = input("Quel type d'affichage vous voulez ? Pour unique, taper 0 ; pour comparatif, taper 1 : ").strip()
    
    mode_comparatif = (mon_choix == "1")
    if mon_choix == "0":
        choix_cotation = input("Veuillez choisir un mode de cotation, 1 pour sympa, 2 pour sévère et 3 pour personnalisée: ")
    
        
    print("Le questionnaire est une liste de questions.")
    
    for q in range(len(questions)):
        question.clear() #vide le dictionnaire question {} à chaque itération
        print("\tQuestion " + str(q+1) + ": " + questions[q][0] + "") #imprime le numéro et le texte de notre question
        x = rng.rng(listerng) #on mélange nos indices via la fonction rng défini ultérieurement
        
        for r in range(len(questions[q][1])): #for r in range len(notre liste de réponses associé à notre question)
            
            print(f"\t\t\t{lettrequest[r]}) " + questions[q][1][x[r]][0] + "")
#f..{}, permet d'insérer une variable dans une chaine de caractères, et ce qui suit permet d'afficher une proposition de réponse dans un ordre aléatoire
            question[lettrequest[r]] = questions[q][1][x[r]][0] #on rajoute dans notre dictionnaire, une clé(lettre) associé à une valeur(proposition de réponse)
            
        if q in [1, 3, 5, 6, 8, 9]:
            print("Pour cette question, plusieurs réponses sont possibles","\n","Veuillez écrire votre réponse en collant les lettres par exemple 'ab'")
        else:
            print("N'écrivez que la lettre de votre réponse")    
       
        reponse_choisie = input("Votre réponse ici: ").lower().replace(" ", "")
        if reponse_choisie == "":
            print("Réponse avec rien. Donc zéro")
            if mon_choix == "0":
                if choix_cotation == "1":
                    points_sympa += 0
                elif choix_cotation == "2":
                    points_severe += 0
                elif choix_cotation == "3":
                    points_personnalisee += 0
            else:
                points_sympa += 0
                points_severe += 0
                points_personnalisee += 0
            continue 
        
        if mon_choix == "0":
            choix_mode_de_cotation(choix_cotation, q, question, bonne_reponses, reponse_choisie, piege_reponses)

            if choix_cotation == "3" and cotation_personnalisee(q, question, bonne_reponses, reponse_choisie, piege_reponses) == "HASARD!":
                points_personnalisee = 0
                break
            elif choix_cotation == "1":
                points_sympa += cotation_sympa(q, question, bonne_reponses, reponse_choisie)
            elif choix_cotation == "2":
                points_severe += cotation_severe(q, question, bonne_reponses, reponse_choisie)
            elif choix_cotation == "3":
                points_personnalisee += cotation_personnalisee(q, question, bonne_reponses, reponse_choisie, piege_reponses)
        
        else:
            points_sympa += cotation_sympa(q, question, bonne_reponses, reponse_choisie)
            points_severe += cotation_severe(q, question, bonne_reponses, reponse_choisie)
            result_personnalisee = cotation_personnalisee(q, question, bonne_reponses, reponse_choisie, piege_reponses, mode_comparatif=True)
            if result_personnalisee == "HASARD!":
                points_personnalisee = 0
            else:
                points_personnalisee += result_personnalisee
        
    choix_affichage(mon_choix, choix_cotation if mon_choix == "0" else None, points_sympa, points_severe, points_personnalisee, nombre_question)        

        
    