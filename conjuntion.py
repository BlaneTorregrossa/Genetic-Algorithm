class _conjuntion(object):
    def __init__(self):
        self.variables = []
        self.clauses = []
        self.numvariables = []
        self.numclauses = []
        self.pair = []
        self.target = ""
        self.vara = ""
        self._settarget()
        self._setvariables(self.vara)
       # self._setclauses()
       # self._setclausespair()


    def _settarget(self):
        self.target = "Hello World!"

    def _setvariables(self, currentvar):
        prevvar = currentvar
        self.variables = currentvar
        if prevvar == currentvar:
            prevvar = ""
        
    def _setclauses(self, var):
        

    #def _setclausepair(self):
