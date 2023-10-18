import math

class fact:

    def __init__(self,val):

        super(fact).__repr__()

        if str(val)[str(val).find(".")+1:len(str(val))] == "0":
            val = int(val)

        self.val = val

        if self.val >= 0 and isinstance(self.val, int):

            self.fact = self.calc_int(self.val)
        
        elif isinstance(self.val, (float)):

            self.fact = self.calc_float(self.val)
        
        else:

            self.fact = 0
        
        
    @classmethod
    def calc_int(cls, val):

        if val == 1 or val == 0:

            return 1
        
        else:

            fact = val *cls.calc_int(val-1)
            return fact
        

    def calc_float(self, val):

        return math.gamma(val + 1)
    

    def __repr__(self):

        return f"{self.fact}"
    

    def  __float__(self):

        return float(self.fact)
    

    def __add__(self, other):

        if isinstance(other, fact):

            return self.fact + other.fact
        
        elif isinstance(other, (int, float)):

            return self.fact + other
    

    def __radd__(self, other):

        return self + other
    

    def __mul__(self,other):

        if isinstance(other, (fact)):

            return self.fact * other.fact
        
        if isinstance(other, (int, float)):

            return self.fact * other
    

    def __rmul__(self, other):

        return self * other
        

    def __sub__(self, other):

        if isinstance(other, fact):
        
            return self.fact + (-other.fact)
        
        elif isinstance(other, (int, float)):

            return self.fact + (-other)
        
    
    def __rsub__(self, other):

        return (self * -1) + other
    

    def __truediv__(self, other):

        if isinstance(other, fact):
        
            return self.fact / other.fact
        
        elif isinstance(other, (int, float)):

            return self.fact / other
    

    def __rtruediv__(self, other):

        return self / other
     
    
    def __pow__(self, other):

        if isinstance(other, fact):
        
            return self.fact ** other.fact
        
        elif isinstance(other, (int, float)):

            return self.fact ** other

    
    def __rpow__(self, other):

        return other ** self.fact





