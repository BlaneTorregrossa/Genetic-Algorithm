
# Very messy still needs to be cleaned
class Conjuntion(object):
    def __init__(self, expression):
        self.expression = expression    # chosen expression
        self.pair = []          # pair made of given variables and an operator
        self.numvariables = 0   # number of variables avalible in varlist
        self.varlist = []      # List of a-z and A-Z characters
        self.operatorlist = []  # List of operators used
        self.clause = ''
        # self._setexpression()
        self._setchar()
        self._setoperators()
        self._setpair()
        self._setclause()


    # Set characters to be used in clauses
    def _setchar(self):
        counter = 64
        logtext = open('varList.txt', 'w')
        while counter < 90:
            counter = counter + 1
            self.varlist.append(chr(counter))
            latestvar = self.varlist[counter]
            logtext.writelines(latestvar)

        counter = 96
        while counter < 122:
            counter = counter + 1
            self.varlist.append(chr(counter))
            latestvar = self.varlist[counter]
            logtext.writelines(latestvar)

        self.numvariables = self.varlist.count

    # Set what each operator used would be
    # + - and
    # ! - negation
    # * - or
    def _setoperators(self):
        counter = 0
        logtext = open('operatorList.txt', 'w')
        self.operatorlist = ['!', '+', '*']
        while counter != self.operatorlist.count:
            logtext.write(self.operatorlist[counter])

    # setting the pairs (***)
    def _setpair(self):
        tempvarlist = []
        currentopperator = ''
        for var in self.expression:
            if var == '!':
                currentopperator = '!'
                continue
            if var >= chr(65) and var <= chr(90):       # A Z
                if currentopperator == ord('!'):
                    tempvarlist.append(currentopperator + var)
                    currentopperator = ''
                    continue
                else:
                    tempvarlist.append(var)
                    continue

            if var == '!':
                currentopperator = '!'
                continue
            if var >= chr(97) and var <= chr(122):      # a z
                if currentopperator == ord('!'):
                    tempvarlist.append(currentopperator + var)
                    continue
                else:
                    tempvarlist.append(var)
                    continue

            newpair = '(' + tempvarlist[0] +  '*' + tempvarlist[1] + ')'
            self.pair.append(newpair)
            return self.pair

    # set clause from pairs (*)
    def _setclause(self):
        currentpair = ''
        counter = 0
        size = len(self.pair)
        while counter < len(size):
            if currentpair != '':
                currentpair = currentpair + ' + '
            for _p in self.pair[counter]:
                if _p == chr(41):       # )
                    currentpair = self.pair[counter]
                    continue
            counter = counter + 1
        return self.clause

    # Sets expression (should choose from more than 1 file ***)
    def _setexpression(self):
        givenexpression = open('expressionList.txt', 'r')
        self.expression = givenexpression
        