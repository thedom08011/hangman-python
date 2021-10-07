from random import randint
import os 

NUMBER_OF_TRIES_MAX = 10

def getPlayerScore(playerName):
    playerScore = 0
    if os.path.isfile('./score/' + playerName + '.txt'):
        with open('./score/' + playerName + '.txt', 'r') as reader:
            playerScore = reader.readline()
    return playerScore

def setNewPlayerScore(playerName, playerScore) :
    with open('./score/' + playerName + '.txt', 'w') as writer:
        writer.write(str(playerScore))


def getWordFromDictionary():
    randomWord = '' 
    with open('./dictionary.txt', 'r') as reader :
        words = reader.readlines()
        randomWord = words[randint(0, len(words))] 
        if '\n' in randomWord:
            randomWord = randomWord[:len(randomWord)-1]
    return randomWord.lower()


def ChangeStarsInWordToFind(hiddenWord, wordToFind, letterGiven): #sert a ne plus cacher les lettre trouver par le joueur
    newHiddenWords = ''
    if letterGiven in wordToFind:
        for i in range(len(wordToFind)):
            if wordToFind[i] == letterGiven:
                newHiddenWords += letterGiven
            else:
                newHiddenWords += hiddenWord[i]
    else : 
        newHiddenWords = hiddenWord
    return newHiddenWords



def checkIfGameIsOver(numberOfTries, hiddenWord) :
    return (numberOfTries >= NUMBER_OF_TRIES_MAX) or (hiddenWord.find('*') == -1)

#--------------------------------------------------------------------------------------

print('*******************************************************************************')
print('************************** Bienvenue au jeu du pendu **************************')
print('*******************************************************************************')

playerName = input('rentrer votre nom d\'utilisateur : ')
print()

print('vous avez ' + str(NUMBER_OF_TRIES_MAX) + ' tentatives pour trouver le bon mot !')#str est utliser parce que number of tries max est un entier. et on ne peux pas concater des chaine de caractère avec des nombres
print()

wordToFind = getWordFromDictionary()
hiddenWord = '*' * len(wordToFind)
numberOfTries = 0
playerScore = int(getPlayerScore(playerName))

print('votre score actuel s\'élève à : ' + str(playerScore))

while(not checkIfGameIsOver(numberOfTries, hiddenWord)):
    print('voici le mot à trouver : ' + hiddenWord)
    print('Il vous reste ' + str(NUMBER_OF_TRIES_MAX - numberOfTries) + ' tentatives.')
    playerLetter = input('quel est votre lettre ? ')
    hiddenWord = ChangeStarsInWordToFind(hiddenWord, wordToFind, playerLetter.lower())
    numberOfTries += 1
    print()

if numberOfTries < NUMBER_OF_TRIES_MAX:
    print('Félicitations ! Vous avez déviné le mot caché ! : ' + wordToFind)
    playerScore += NUMBER_OF_TRIES_MAX - numberOfTries
    setNewPlayerScore(playerName, playerScore)
else :
    print('Dommage le mot caché était : ' + wordToFind)
