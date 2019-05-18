from builtins import print, eval
import random;

#------------------------StringIO-----------------------
class stringDb:
    listOfWords = [];
    def __init__(self):
        self.loadWordsToList();
        self.totalWords = len(stringDb.listOfWords);


    # @staticmethod
    # def getListOfWords(cls):
    #     return cls.listOfWords;

    def getRandomWord(self):
        return stringDb.listOfWords[random.randint(1, self.totalWords)];

    def loadWordsToList(self):
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





# s1 = stringDb();
# s1.loadWordsToList()
# print(stringDb.listOfWords)
