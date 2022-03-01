from wordleFunction import *
from tkinter import *
import tkinter.font as tkFont

def checkLine(line, lineText, randomWord):
    global currentLine
    global currentIndex

    if len(lineText) <7:
        return
    #Transformation de la liste en mot
    wordTyped = ""
    for letter in lineText:
        wordTyped += letter

    #Gagné :
    if wordTyped==randomWord:
        for cellule in line:
            cellule.config(bg = "green")
        return

    for i in range(len(wordTyped)):
        #Bien placé
        if wordTyped[i] == randomWord[i]:
            line[i].config(bg = "red")

        #Mal placé
        elif wordTyped[i] in randomWord:
            line[i].config(bg = "orange")

    currentIndex =0
    currentLine +=1

    #Bug
    if currentLine == 6:
        currentLine=0
def putLetterInGrid(grid,grilleTexte, value):
    global currentLine
    global currentIndex

    if currentIndex < 7:
        grid[currentLine][currentIndex].create_text(25, 25, text=value, fill="#ffffff", font=robotMediumGrid, tag= "texte")
        grilleTexte[currentLine].append(value)

    currentIndex +=1

fullDictionary = open("dico.txt", "r")  #ouverture du dictionnaire complet
newDictionary = open("newDictionary.txt", "w")  #ouverture d'un fichier pour stocker le nouveau dictionnaire
getDictionnaryWithNumberOfLetter(fullDictionary, 7, newDictionary)  #remplissage du nouveau dictionnaire
randomWord = getRandomWord("newDictionary.txt") #Selection d'un mot aléatoire depuis le nouveau dictionnaire

print(randomWord)

#Création de la fenêtre graphique
window = Tk()

#Fonts
robotoMediumHeader = tkFont.Font(family = 'Roboto Medium', size = 48, weight = 'bold')
robotMediumLetter = tkFont.Font(family = 'Roboto Medium', size = 12)
robotMediumGrid = tkFont.Font(family = 'Roboto Medium', size = 24, weight = 'bold')

#Paramètrage de la fenêtre
window.title("Sutom")   #Création du titre
window.iconbitmap("wordleLogo.ico") #Création du logo
window.config(bg = "#2b2b2b")   #Création de l'arrière plan
window.geometry("1280x720")     #Dimensionnage de la fenêtre
window.columnconfigure(0, weight = 4) #La 1 ère colone prend toute la place

#Header de la page
header = Label(window,text = "SUTOM")   #Texte du header
header.config(bg = "#2b2b2b")   #Arrière plan
header.config(fg = "#ffffff")   #Couleur d'écriture
header.config(pady = 10)    #Marge par le haut
header.config(font=(robotoMediumHeader))  #Police d'écriture
header.grid(row = 0)

#Grille de lettres
grilleContent = []
for i in range(6):
    grilleCurrent = []
    for i in range(7):
        grilleCurrent.append(Canvas(window, bg="#0077c7",height=50, width=50))
    grilleContent.append(grilleCurrent)

n = 0
for i in range(6):
    for case in grilleContent[i-1]:
        case.place(x = n*50+475, y= i*50+150)
        n +=1
    n = 0

#Grille de texte
grilleTexte = [[],[],[],[],[],[]]

#Affichage de la première lettre du mot
currentLine = 5
currentIndex = 0

putLetterInGrid(grilleContent,grilleTexte, randomWord[0])

#Clavier
keyboard = Label(window)
keyboard.grid(row = 2, pady = 450)
keyboard.config(width = 70, height = 11)
keyboard.config(bg = "#2b2b2b")

#First line
buttonAImages = PhotoImage(file = "images/A.png")
buttonLetterA = Button(keyboard, image = buttonAImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "A"), font=robotMediumLetter, bd=0,borderwidth=0)
buttonLetterA.place(x=0, y=0)

buttonZImages = PhotoImage(file = "images/Z.png")
buttonLetterZ = Button(keyboard, image = buttonZImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "Z"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterZ.place(x=50, y=0)

buttonEImages = PhotoImage(file = "images/E.png")
buttonLetterE = Button(keyboard, image = buttonEImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "E"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterE.place(x=100, y=0)

buttonRImages = PhotoImage(file = "images/R.png")
buttonLetterR = Button(keyboard, image = buttonRImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "R"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterR.place(x=150, y=0)

buttonTImages = PhotoImage(file = "images/T.png")
buttonLetterT = Button(keyboard, image = buttonTImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "T"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterT.place(x=200, y=0)

buttonYImages = PhotoImage(file = "images/Y.png")
buttonLetterY = Button(keyboard, image = buttonYImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "Y"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterY.place(x=250, y=0)

buttonUImages = PhotoImage(file = "images/U.png")
buttonLetterU = Button(keyboard, image = buttonUImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "U"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterU.place(x=300, y=0)

buttonIImages = PhotoImage(file = "images/I.png")
buttonLetterI = Button(keyboard, image = buttonIImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "I"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterI.place(x=350, y=0)

buttonOImages = PhotoImage(file = "images/O.png")
buttonLetterO = Button(keyboard, image = buttonOImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "O"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterO.place(x=400, y=0)

buttonPImages = PhotoImage(file = "images/P.png")
buttonLetterP = Button(keyboard, image = buttonPImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "P"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterP.place(x=450, y=0)

#Second line
buttonQImages = PhotoImage(file = "images/Q.png")
buttonLetterQ = Button(keyboard, image = buttonQImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "Q"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterQ.place(x=0, y=50)

buttonSImages = PhotoImage(file = "images/S.png")
buttonLetterS = Button(keyboard, image = buttonSImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "S"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterS.place(x=50, y=50)

buttonDImages = PhotoImage(file = "images/D.png")
buttonLetterD = Button(keyboard, image = buttonDImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "D"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterD.place(x=100, y=50)

buttonFImages = PhotoImage(file = "images/F.png")
buttonLetterF = Button(keyboard, image = buttonFImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "F"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterF.place(x=150, y=50)

buttonGImages = PhotoImage(file = "images/G.png")
buttonLetterG = Button(keyboard, image = buttonGImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "G"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterG.place(x=200, y=50)

buttonHImages = PhotoImage(file = "images/H.png")
buttonLetterH = Button(keyboard, image = buttonHImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "H"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterH.place(x=250, y=50)

buttonJImages = PhotoImage(file = "images/J.png")
buttonLetterJ = Button(keyboard, image = buttonJImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "J"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterJ.place(x=300, y=50)

buttonKImages = PhotoImage(file = "images/K.png")
buttonLetterK = Button(keyboard, image = buttonKImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "K"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterK.place(x=350, y=50)

buttonLImages = PhotoImage(file = "images/L.png")
buttonLetterL = Button(keyboard, image = buttonLImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "L"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterL.place(x=400, y=50)

buttonMImages = PhotoImage(file = "images/M.png")
buttonLetterM = Button(keyboard, image = buttonMImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "M"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterM.place(x=450, y=50)

#Third line
buttonWImages = PhotoImage(file = "images/W.png")
buttonLetterW = Button(keyboard, image = buttonWImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "W"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterW.place(x=58, y=100)

buttonXImages = PhotoImage(file = "images/X.png")
buttonLetterX = Button(keyboard, image = buttonXImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "X"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterX.place(x=108, y=100)

buttonCImages = PhotoImage(file = "images/C.png")
buttonLetterC = Button(keyboard, image = buttonCImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "C"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterC.place(x=158, y=100)

buttonVImages = PhotoImage(file = "images/V.png")
buttonLetterV = Button(keyboard, image = buttonVImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "V"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterV.place(x=208, y=100)

buttonBImages = PhotoImage(file = "images/B.png")
buttonLetterB = Button(keyboard, image = buttonBImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "B"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterB.place(x=258, y=100)

buttonNImages = PhotoImage(file = "images/N.png")
buttonLetterN = Button(keyboard, image = buttonNImages, command= lambda: putLetterInGrid(grilleContent,grilleTexte, "N"), font=robotMediumLetter, bd=0, borderwidth=0)
buttonLetterN.place(x=308, y=100)

buttonEffacerImages = PhotoImage(file = "images/Effacer.png")
buttonEffacer = Button(keyboard, image = buttonEffacerImages,command= lambda: checkLine(grilleContent[currentLine], grilleTexte[currentLine], currentIndex), font=robotMediumLetter, bd=0, borderwidth=0)
buttonEffacer.place(x=358, y=100)

buttonEnterImages = PhotoImage(file = "images/Enter.png")
buttonEnter = Button(keyboard, image = buttonEnterImages, command= lambda: checkLine(grilleContent[currentLine], grilleTexte[currentLine], randomWord), font=robotMediumLetter, bd=0, borderwidth=0)
buttonEnter.place(x=421,y=100)

window.mainloop()