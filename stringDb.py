from builtins import print, eval
import random;

#------------------------StringIO-----------------------

class stringDb:
    """
        @author: Divyeshkumar Balar(40062267)

        Class StringDb is having a list of words with 4 leter and other helper methods.
        successful interpretation of this file needs a data set file with 4 leter words saperated by space.
    """
    listOfWords = [];
    def __init__(self):
        self.loadWordsToList();
        self.totalWords = len(stringDb.listOfWords);


    def getRandomWord(self):
        """
                This method returns random word from the range of wordList
        """
        return stringDb.listOfWords[random.randint(1, self.totalWords)];


    def loadWordsToList(self):
        """
            This method loads the words from file to a list of this class
            Not having dataSet.txt file can cause runtime Exception
        """
        dataFile = open('wordDb.txt', 'r');
        list = [];
        varI = 0;
        while varI < 288:
            strArr = dataFile.readline().strip('\n').split(" ");
            list.append(strArr[0:]);
            varI+=1;

        for i in list:
            for j in i:
                stringDb.listOfWords.append(j);