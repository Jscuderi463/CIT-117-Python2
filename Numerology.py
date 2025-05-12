# Author: Joe Scuderi
# Due Date: 04/20/2025
# Numerology Assignment

class Numerology:

    def __int__(self, sName:str, sDOB:str)->object:

        self.__sName = sName
        self.__sDOB = sDOB.replace("-","").replace("/","")

        self.__dictLetters = {"A":1, "J":1, "S":1,
                              "B":2, "K":2, "T":2,
                              "C":3, "L":3, "U":3,
                              "D":4, "M":4, "V":4,
                              "E":5, "N":5, "W":5,
                              "F":6, "O":6, "X":6,
                              "G":7, "P":7, "Y":7,
                              "H":8, "Q":8, "Z":8,
                              "I":9, "R":9}

    def getName(self):
        return self.__sName

    def getDOB(self):
        return self.__sDOB

    def _reduceNumberDecorator(func):
        def wrapper(self):
            iNumber = func(self)
            while iNumber >= 10:
                sNumber = str(iNumber)
                iNumber = int(sNumber[0] + int(sNumber[1]))
            return iNumber
        return wrapper

    @_reduceNumberDecorator
    def getLifePath(self):
        iTotal = 0

        for sNumber in self.DOB:
            iTotal += int(sNumber)
        return iTotal

    @_reduceNumberDecorator
    def getBirthdayNumber(self):
        return int(self.getDOB()[2:4])

    @_reduceNumberDecorator
    def getAttitude(self):

        sDOBAttitude = self.getDOB()[:4]

        iTotal =0

        for sNumber in sDOBAttitude:
            iTotal += int(sNumber)
        return iTotal

    @_reduceNumberDecorator
    def getSoul(self):

        iTotal = 0

        for sLetter in self.getName().upper():

            if sLetter in "AEIOU":

                iTotal += self.__dictLetters.get(sLetter,0)

        return iTotal

    @_reduceNumberDecorator
    def getPersonality(self):

        iTotal = 0

        for sLetter in self.getName().upper():
            if sLetter not in "AEIOU":

                iTotal += self.__dictLetters.get(sLetter,0)

        return iTotal

    @_reduceNumberDecorator
    def getPower(self):

        return self.getSoul() + self.getPersonality()

    def __str__(self)->str:
        return (f"Name: {self.getName()}\
        \nDOB: {self.getDOB()}\
        \nLife Path: {self.getlifePath}\
        \nBirthday: {self.getBirthdayNumber}\
        \nAttitude: {self.getAttitude()}\
        \nPersonality: {self.getPersonality()}\
        \nSoul: {self.getSoul()}\
        \nPower: {self.getPower()}")















