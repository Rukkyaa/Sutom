import random

def getDictionnaryWithNumberOfLetter(fullDictionary, lenghtOfWords, newDictionary):
    """
    :param fullDictionary: a text file with all the words
    :param lenghtOfWords: the lenght of the words wanted in the dictionary
    :param newDictionary: an empty text file to stock the new dictionary

    fonction permettant de créer un nouveau dictionnaire d'après un premier, selon un nombre de lettres données
    """

    #On parcours les mots du fichier de texte 1 par 1
    for word in fullDictionary:
        if len(word) == lenghtOfWords+1:
            # On passe les mots en majuscules
            word = word.upper()

            #On enlève les accents
            specialLetterA = "ÂÄÀ"
            specialLetterE = "ÊËÉÉÈ"
            specialLetterI = "ÎÏ"
            specialLetterO = "ÔÖ"
            specialLetterU = "ÛÜÙ"

            for specialA in specialLetterA:
                word = word.replace(specialA, "A")

            for specialE in specialLetterE:
                word = word.replace(specialE, "E")

            for specialI in specialLetterI:
                word = word.replace(specialI, "I")

            for specialO in specialLetterO:
                word = word.replace(specialO, "O")

            for specialU in specialLetterU:
                word = word.replace(specialU, "U")

            if "Ç" in word:
                word = word.replace("Ç", "C")

            #On rajoute le mot (sans accent et en majuscule) dans le dictionnaire
            newDictionary.writelines(word)

def getRandomWord(dictionary):
    """
    :param dictionary: text file
    :return: string

    fonction permettant de retourner un mot aléatoire depuis un dictionnaire de mots
    """
    lines = open(dictionary).read().splitlines()
    randomWord = random.choices(lines)[0]

    return randomWord