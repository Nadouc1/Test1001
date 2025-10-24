#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch

def cotation_severe(q, question, bonne_reponses, reponse_choisie):
    """
        pre: q est l'indice de la question; question est notre dictionnaire{} associant lettre et réponse;
        bonne_reponses correspond à notre dictionnaire des réponse correcte; reponse_choisie correspond à notre reponse insérer via input
        post: return 1 si la réponse est correcte, -1 sinon
    """
    if reponse_choisie == "":
        return 0
    
    while any(lettre not in question for lettre in reponse_choisie) or reponse_choisie != "":
        print("Votre réponse ne correspond à aucune proposition. Veuillez recommencer!")
        print()
        reponse_choisie = input("Votre réponse ici: ").strip().lower().replace(" ", "")
        
    if q in [1, 3, 5, 6, 8, 9]:

        reponse_choisie = reponse_choisie.lower().replace(" ", "")
        
        if len(reponse_choisie) > 1:
            lisreponsecho = []
            listedecorrection = []
            for f in reponse_choisie:
                lisreponsecho.append(f)
            for e in reponse_choisie:
                if (not question[e] in bonne_reponses[q]) or len(lisreponsecho) != len(bonne_reponses[q]):
                    listedecorrection.append("mauvais")
                else:
                    listedecorrection.append("good")
            
            if "mauvais" in listedecorrection:
                return -1
            else:
                return 1
        else:
            return -1
                 
    else:
            
        reponse_choisie = reponse_choisie.strip().lower().replace(" ", "")
        if len(reponse_choisie) == 1:
            if question[reponse_choisie] in bonne_reponses[q]:
                return 1
            else:
                return -1
        else:
            return -1
