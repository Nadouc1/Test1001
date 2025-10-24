#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch
from choix_mode_de_cotation import choix_mode_de_cotation

def choix_affichage(mon_choix, choix_cotation, points_sympa, points_severe, points_personnalisee, nombre_question):
    
    if mon_choix == "0":
        affichage_unique(choix_cotation, points_sympa, points_severe, points_personnalisee, nombre_question)
    elif mon_choix == "1":
        affichage_comparatif(points_sympa, points_severe, points_personnalisee, nombre_question)
def affichage_unique(choix_cotation, points_sympa, points_severe, points_personnalisee, nombre_question):
    if choix_cotation == "1":
        print(f"Mode de cotation = Sympa\nRésultat: {points_sympa}/{nombre_question}")
    elif choix_cotation == "2":
        print(f"Mode de cotation = Sévère\nRésultat: {points_severe}/{nombre_question}")
    elif choix_cotation == "3":
        print(f"Mode de cotation = Personnalisée\nRésultat: {points_personnalisee}/{nombre_question}")
        
def affichage_comparatif(points_sympa, points_severe, points_personnalisee, nombre_question):
    layout = "{:<15} {:>10} {:>10}"
    print()
    print(layout.format("Type de cotation", "Résultat", "  Nombre de question"))
    print()
    print()
    print(layout.format("Sympa", str(points_sympa), str(nombre_question)))
    print(layout.format("Sévère", str(points_severe), str(nombre_question)))
    print(layout.format("Personnalisée", str(points_personnalisee), str(nombre_question)))
    