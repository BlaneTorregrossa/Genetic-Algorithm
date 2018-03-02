
import binascii

from conjuntion import Conjuntion

# all bad scrap next time
class Chromosome(object):
    def __init__(self):
        self.bincharlist = []
        self.charlist = []
        self.resultlist = []

    # what's in conjuntion
    def _setchar(self):
        counter = 64
        logtext = open("charList.txt", "w")
        while counter < 90:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.writelines(latestvar)
        counter = 96
        while counter < 122:
            counter = counter + 1
            self.charlist.append(chr(counter))
            latestvar = self.charlist[counter]
            logtext.writelines(latestvar)

    # More than likely to remain to be useless (***)
    def _setvalues(self):
        counter = 0
        logtext = open("binList.txt", "w")
        while counter != self.charlist.count:
            self.bincharlist.append(binascii.a2b_uu(self.charlist[counter]))
            counter = counter + 1
            latestvar = self.bincharlist[counter]
            logtext.writelines(latestvar)
