
#test to be removed once I've gotten used to python again
class testing(object):
    def _init_(self):
        self.nums = 2
        self.title = ""
        self.check = False
        
    #function to call the other functions
    def testRun(self):
        checknums(10)

    #Modify nums if requirment not met
    def checknums(self, modifier):
        self.modifier = modifier
        if nums < self.modifier:
            nums = nums * 2
            checknums(10)
    
    def PrintTitle(self): 
        title = str(nums)
        print(title);

    if __name__ = '___init___':
        testRun();
