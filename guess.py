import queue
import game
import re
from numpy import inexact


class guess:
    """
        @author: Divyeshkumar Balar(40062267)

        Class guess is the main class including logic for
        storing multiple games in a single session
        one must pass player's name while creating instance of this class
        it includes method named 'play' must be called to start the game.
    """
    def __init__(self, nameOfPlayer):
        self.playerName = nameOfPlayer
        print("WELCOME ", nameOfPlayer, "Lets play HOli")
        self.regEx = re.compile("[a-zA-Z]")
        #self.g1 = game.game("RANDOM WORD")
        self.noOfGames = 0
        self.listOfGames = [] #list of games
        #self.startNewGame()


    def play(self):
        """
            This mehtod is beggining of game;
            one must call to start the game
        """
        self.startNewGame()

    def endGame(self):
        """
            This method will call default exit and end the game
        """
        exit()


    def startNewGame(self):
        """
            This method will start a new game and will
            store the new game instance into session list
        """
        temp = input("Wanna Start a new game.... Y|N: ")
        if temp == 'y' or temp == 'Y':
            self.g1 = game.game()
            print(self.g1.word)
            self.noOfGames += 1
            self.listOfGames.append(self.g1)
            self.getUserInput()
        else:
            print("Good Bye Looser!!!")
            self.getSessionSummery()



    def refreshConsole(self):
        """
            It refresh the console and ask user input
        """
        print("A 4 letter word is : ", self.g1.currentGuess)
        self.getUserInput()


    def printInfo(self):
        """
            printInfo prints the main information and
            characters which system is expecting in input
        """
        print("Press the character shown bellow as a choice to play this game")
        print("G - Guess the whole word | L - Guess a single letter | F - show a hint(fold single letter) \n X - Giveup on word  | Q - Quit and see the summary")
        print("Guess a 4 letter word: ", self.g1.currentGuess)



    def getUserInput(self):
        """
            getUserInput is the main interface between user and system;
            It also validate the input
        """
        if (self.g1.isCurrentGameOver()):
            self.startNewGame()

        print("Press the character shown bellow as a choice to play this game")
        print("G - Guess the whole word | L - Guess a single letter | F - show a hint(fold single letter) "
              "\n X - Giveup on word  | Q - Quit and see the summary  ")
        print("Guess a 4 letter word: ", self.g1.currentGuess)
        inChar = input("Enter your choice: ")

        if inChar == 'G' or inChar == 'g' :
            guessWord = input("Guess the complete 4 letter word")[0:4]
            while not self.regEx.match(guessWord):
                guessWord = input("Enter valid 4 letter word: ")
            if(self.g1.isCorrectWord(guessWord)):
                self.refreshConsole()
            else:
                self.refreshConsole()

        elif inChar == 'L' or inChar == 'l':
            guessLeter = input("Guess any letter of this word")[0]

            while not self.regEx.match(guessLeter):
                guessLeter = input("Enter valid letter: ")
            if(self.g1.isCorrectGuess(guessLeter)):
                print("Good job Champ!")
                self.refreshConsole()
            else:
                print("Try Again mate")
                self.refreshConsole()

        elif inChar == 'Q' or inChar == 'q':
            self.getSessionSummery()

        elif inChar == 'F' or inChar == 'f':
            self.g1.getHintChar()
            if self.g1.isCurrentGameOver():
                self.startNewGame()
            self.refreshConsole()

        elif inChar == 'X' or inChar == 'x':
            self.g1.getWordOnDemand()
            self.refreshConsole()

        else:
            print("Enter valid input")
            self.getUserInput()


    def getSessionSummery(self):
        """
            getSessionSummery will print the statistics of all the games
            played in perticular session.
            This statistics includes Words,Status(0-giveUp | 1-Success),
            # of Bad Guess and Score for individual words.

            This function will be called at the end of session
            OR whenever user wants to quit.
        """
        if(len(self.listOfGames) > 0):
            print("Word ----- Status(0-giveUp | 1-Success) ----- #Bad Guess ----- Score")
            total = 0
            wordCount = 0
            successCount = 0
            badGuessCount = 0

            for g in self.listOfGames[0:len(self.listOfGames)]:
                print(g.word, " ----- ", g.status, " ----- ", g.noOfBadGuess, " ----- ", round(g.getScore()))
                wordCount+=1
                if(g.status == 1):
                    successCount+=1
                badGuessCount+=g.noOfBadGuess
                total+=round(g.getScore())

            print("# of words ----- # of correct ----- # of bad guess ----- Total score")
            print(wordCount, "--------------", successCount, "-----------------", badGuessCount, "-------------------",total, )
            self.endGame()
        else:
            self.endGame()



# gue1 = guess("Divyesh")
# # gue1.play()
