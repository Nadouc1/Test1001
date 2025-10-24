def affichage_bareme(bareme):
    
    while bareme not in ["0", "1"]:
        print()
        print("Choix incorrecte. Veuillez réessayer!")
        print()
        bareme =  input("Voulez-vous voir les différents barème de chaque mode de cotation avant de choisir, 1 pour oui et 0 pour non:")
    if bareme == "1":
        layout = "{:<15} {:<10} {:<10} {:<10} {:>10}"
        print()
        print("Aperçu des barèmes des différentes cotations")
        print()
        print("Si QRM, le point n'est obtenu que si toutes les bonnes réponses sont sélectionnées")
        print()
        print()
        print(layout.format("Type", "Bonne", "Mauvaise", "Vide", "Supplément"))
        print()
        print(layout.format("Sympa", "+ 1", "- 0", "- 0", "")) #layout.format, voir syllabus, chapitre string
        print()
        print(layout.format("Sévère", "+ 1", "- 1", "- 0", ""))
        print()
        print(layout.format("Personnalisée", "+ 1", "- 1", "- 0", "si réponse choisie au hasard, la note est 0 et le test s'arrête"))
        print()
    elif bareme == "0":
        print()
        print("Vous avez choisie de ne pas voir les barêmes")
        print()
            
        
        