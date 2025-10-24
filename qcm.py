#Travail réalisé par : Nadine Benidir; Mehdi Hanoune; Alessio Munzi; Emran Balouch


def build_questionnaire(filename):
    """
        Construit le QCM avec les questions contenue dans le fichier donné.
        :type filename: Un string représentant le nom du fichier à charger.

        :return: Une liste de questions
    """
    questions = []
    wording = None #variable qui contient le texte de la question, initialement : None
    choices = [] #liste vide pour contenir nos réponses
    with open(filename, encoding='utf-8') as file: #ouvre le fichier d'intérêt et le encoding utf-8, permet une interprétation fidèle du texte du fichier
        for line in file.readlines(): #chaque ligne est lue une par une
            if '|' not in line:
                if wording or choices:
                    questions.append([wording, choices]) # quand il ya pas "|", ça veut dire qu'on termine la question en cours on rajouter wording et choice
                wording = None
                choices = [] #on réinitialise
            else:
                parts = line.strip().split('|') #on crée des parts en enlevons les espaces et nous découpons la ligne
                if 1 < len(parts) < 5: 
                    if parts[0] == 'Q':
                        if not wording and not choices: #si n'est pas encore présent nos variables
                            wording = parts[1]
                            choices = []
                        else:
                            questions.append([wording, choices])
                            wording = None
                            choices = []
                    elif parts[0] == 'A':
                        if parts[2] not in ('V', 'X'):
                            print("Error when loading line:\n\t{}".format(line))
                        else:
                            choices.append([parts[1], parts[2] == 'V', parts[3] if len(parts) > 3 else ''])
                    else:
                        print("Error when loading line:\n\t{}".format(line))
                else:
                    print("Error when loading line:\n\t{}".format(line))

                if line.startswith('Q'):
                    wording = parts[1]

    if wording or choices:
        questions.append([wording, choices])
    return questions