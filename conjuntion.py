class _conjuntion(object):
    def __init__(self):
        self.variable = ""
        self.currentclause = ""
        self.clausea = ""
        self.clauseb = ""
        self.pair = ""
        self.numvariables = 0
        self.numclauses = 0
        self.charlist = []
        self.operatorlist = []
        self._setchar()
        self._setoperators()

    #Set Char to be used  (***)
    def _setchar(self):
        counter = 64
        logtext = open("charList", "w")
        while counter < 90:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.write(latestvar)
            print latestvar + " was the last character added to the charlist!"
        counter = 96
        while counter < 122:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.write(latestvar)
            print latestvar + " was the last character added to the charlist!"

    #Set what each operator used would be
    # + - and
    # ! - negation
    # * - or
    def _setoperators(self):
        counter = 0
        logtext = open("operatorList.txt", "w")
        self.operatorlist = ["!", "+", "*", "(", ")"]
        while counter != self.operatorlist.count:
            logtext.write(self.operatorlist[counter])

    # Setting clauses
    def _setclause(self, vara, givenoperator, varb):
        givenstring = vara + givenoperator + varb
        check = False
        self.currentclause = givenstring
        if self.clausea == "" & check == False | self.clauseb != "" & self.clausea == "":
            self.clausea = givenstring
            check = True
        if self.clauseb == "" & check == False & self.clausea != "":
            self.clauseb = givenstring
        givenstring = ""

    def _setpair(self, givenoperator):
        self.pair = self.clausea + givenoperator + self.clauseb

