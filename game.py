import math
import random
import PythonWordGame.stringDb as stringDb


class game:
    """
        @author: Divyeshkumar Balar(40062267)

        Class game is main blueprint of game data structure;
        which includes a static list with the frequency of each character.
        It also include helper methods
    """
    wordFrequency = {
        'E': 12.02,
        'T': 9.10,
        'A': 8.12,
        'O': 7.68,
        'I': 7.31,
        'N': 6.95,
        'S': 6.28,
        'R': 6.02,
        'H': 5.92,
        'D': 4.32,
        'L': 3.98,
        'U': 2.88,
        'C': 2.71,
        'M': 2.61,
        'F': 2.30,
        'Y': 2.11,
        'W': 2.09,
        'G': 2.03,
        'P': 1.82,
        'B': 1.49,
        'V': 1.11,
        'K': 0.69,
        'X': 0.17,
        'Q': 0.11,
        'J': 0.10,
        'Z': 0.07
    }



    def __init__(self):
        s1 = stringDb.stringDb()
        self.word = s1.getRandomWord()
        self.status = 0 #0 for giveup and 1 for success
        self.noOfBadGuess = 0
        self.currentGuess = '----'
        self.score = 0
        self.baseScore = self.getBaseScoreOfWord()


    def getScore(self):
        """
            It  returns the current score
        """
        return self.score


    def getHintChar(self):
        """
            This method returns the random hint character out of 4 leter word
            and deduct the relevent score from total;
            deduction of score is done by other method.
        """
        randVar = random.choice(range(0,4,1))
        tempChar = self.word[randVar]
        while self.isCurrentGuessContains(tempChar):
            randVar = random.choice(range(4))
            tempChar= self.word[randVar]

        k = 0
        tempStr= ''
        for i in self.currentGuess:
            if(k == randVar or self.word[k] == self.word[randVar]):
                tempStr+=tempChar
            else:
                tempStr+=i
            k+=1

        self.currentGuess = tempStr

        if(self.currentGuess == self.word):
            print("Guess a 4 letter word: ", self.currentGuess)
        self.scoreDownForChar(tempChar)
        return tempChar


    def isCorrectWord(self, tempWord):
        """
            This method will return true/false depending on given word
            from user matches to the current word.
            It also call methods to increase or deduct the score accordingly.
        """
        if(tempWord == self.word):
            self.getBaseScoreOfWord()
            self.score+=10
            print("Its not Possible, you are cheating.......... or you are superHuman")
            self.status = 1
            self.currentGuess = tempWord
            return True
        else:
            print("Try again, better luck next time")
            self.deduceScoreForWrongWord()
            return False
        

    def isCurrentGameOver(self):
        """
            Return true is the current game is over
        """
        if self.word == self.currentGuess:
            return True
        else:
            return False


    def isCurrentGuessContains(self, tempChar):
        """
            This method return True if the passed character is \r
            already in currntly guessed string.
            Otherwise returns false
        """
        for i in self.currentGuess:
            if(i == tempChar):
                return True

        return False


    def isCorrectGuess(self, tempChar):
        """
            This method returns true
                if the character entered by user is correct guess
            (means, part of current word)
            It also add or deduct the score accordingly
        """
        k = 0
        flag = False
        tempStr = ''
        if(self.isCurrentGuessContains(tempChar)):
            print("This letter is already guess by you Dumb!!")
            self.noOfBadGuess+=1
            return False

        for i in self.word:
            if(i == tempChar):
                tempStr += tempChar
                self.scoreUpForChar(tempChar)
                flag = True
                k+=1
            else:
                tempStr+=self.currentGuess[k]
                k+=1

        self.currentGuess = tempStr

        if(flag == False):
            self.noOfBadGuess+=1
            self.scoreDownForChar(tempChar)

        if(self.currentGuess == self.word):
            self.status = 1
        return flag


    def deduceScoreForWrongWord(self):
        """
            This method deduct score when the word entered by
            user(Guess by user) is wrong

            deducing score for each wrong 'word'(Not Character) guess
            if the current current score is zero and
            user enter the wrong word
            this method will reduce score by base score
            if score is not zero than it will reduce 10% of
            total basescore from score
        """
        if(self.score == 0):
            self.score -= self.baseScore
        else:
            self.score-=self.baseScore*0.10


    def getBaseScoreOfWord(self):
        """
            This method calculate the base score for
            each rnadom word picked from the data set
            base score is calculated for word
            base score method returns the base score for current word
            sum of max (frequency - frquency of each charater)
            Hence, 'eeee' got the least score and 'zzzz'
            got the highest base score
        """
        temp = 0
        for i in self.word:
            temp+=(float(self.getWordFrequency('E'))-float(self.getWordFrequency(i)))
        return float(temp)


    def getWordFrequency(self, tempChars):
        """
            This method return the probability of given character.
        """
        tempChars = tempChars.upper()
        return game.wordFrequency.get(tempChars)


    def getWordOnDemand(self):
        """
            This method returns the whole word,
            in case when user giveup and press 'X'
            It deduct the score as much as the baseScore of the word
        """
        self.currentGuess = self.word
        self.score-=self.getBaseScoreOfWord()
        self.noOfBadGuess+=1
        self.status = 0
        return self.currentGuess
#---------------------------------------------Scoring up and down ---------------------------

    def scoreDownForChar(self, tempChar):
        """
            This method include the logic to decrease the score
            when the guessed character is wrong

            total score minus (probability of tempchar - max frequency )
            for the most frquent character there will be least deduction and
            for the least frequent character there is high deduction
        """
        tempChar = tempChar.upper()
        probOfChar = float(self.getWordFrequency(tempChar))
        self.score -= (probOfChar - float(self.getWordFrequency('E')))

    def scoreUpForChar(self, tempChar):
        """
            total score plus max probability - probability of character
            scoring up depends on the frequency of character
            the most frequent character will have
            least effect on the total score
            and the least frequent character will add more value to total
        """
        tempChar = tempChar.upper()
        probOfChar = float(self.getWordFrequency(tempChar))
        self.score = self.score +  (float(self.getWordFrequency('E')- probOfChar))
        
