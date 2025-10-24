#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch

from cotation_severe import cotation_severe
from cotation_sympa import cotation_sympa
from cotation_personnalisee import cotation_personnalisee

def choix_mode_de_cotation(choix_cotation, q, question, bonne_reponses, reponse_choisie, piege_reponses):
        
    if choix_cotation == "1":
        print()
        print("Cotation choisie : Sympa")
        print()
        
        return cotation_sympa(q, question, bonne_reponses, reponse_choisie)
    
    elif choix_cotation == "2":
        print()
        print("Cotation choisie : Sévère")
        print()
        
        return cotation_severe(q, question, bonne_reponses, reponse_choisie)
    
    elif choix_cotation == "3":
        print()
        print("Cotation choisie : Personnalisée")
        print()
        
        return cotation_personnalisee(q, question, bonne_reponses, reponse_choisie, piege_reponses)
            

