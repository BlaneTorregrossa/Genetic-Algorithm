
# Class for CNF related data
# does not include parser information
class Conjuntion(object):
    def __init__(self):
        self.clausea = ""       # first clause for pair
        self.clauseb = ""       # second clause for pair
        self.pair = ""          # pair made of two given clauses and an operator
        self.numvariables = 0   # number of variables avalible in charList
        self.charlist = []      # List of a-z and A-Z characters
        self.operatorlist = []  # List of operators used
        self._setchar()
        self._setoperators()


    #Set characters to be used in clauses
    def _setchar(self):
        counter = 64
        logtext = open("charList.txt", "w")
        while counter < 90:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.writelines(latestvar)
            print latestvar + " was the last character added to the charlist!"
        counter = 96
        while counter < 122:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.writelines(latestvar)
            print latestvar + " was the last character added to the charlist!"
        self.numvariables = self.charlist.count

    #Set what each operator used would be
    # + - and
    # ! - negation
    # * - or
    # (
    # )
    def _setoperators(self):
        counter = 0
        logtext = open("operatorList.txt", "w")
        self.operatorlist = ["!", "+", "*", "(", ")"]
        while counter != self.operatorlist.count:
            logtext.write(self.operatorlist[counter])

    # Setting clauses made from two given variables and an operator
    def _setclause(self, vara, givenoperator, varb):
        givenstring = vara + givenoperator + varb
        check = False
        if self.clausea == "" & check == False | self.clauseb != "" & self.clausea == "":
            self.clausea = givenstring
            check = True
        if self.clauseb == "" & check == False & self.clausea != "":
            self.clauseb = givenstring
        givenstring = ""

    # For setting a pair of clauses as one string
    def _setpair(self, givenoperator):
        self.pair = self.clausea + givenoperator + self.clauseb
        