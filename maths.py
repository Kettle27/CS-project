import numpy as np

class fact:

    def __init__(self,val):

        self.val = int(val)

        if self.val >= 0:

            self.fact = self.calc(self.val)
        
        else:

            self.fact = 0
            
    @classmethod
    def calc(cls, val):

        if val == 1 or val == 0:

            return 1
        
        else:

            fact = val *cls.calc(val-1)
            return fact
    

    def __repr__(self):

        return str(self.fact)
    
    

