from math import *
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
    



class intergration:


    def __init__(self, equation, a, b):


        super(intergration).__repr__()

        self.delta_X = (b-a) / 1000

        self.x_range = [a + (i * self.delta_X) for i in range(1001)]

        self.trap_sum = sum([2 * eval(equation, {"x": x}) for x in self.x_range[1:-1]]
        , eval(equation, {"x" : self.x_range[0]}) + eval(equation, {"x" : self.x_range[-1]}))

        
    def __repr__(self):

        return (f"{(self.delta_X/2) * self.trap_sum:.3f}")
    

    def  __float__(self):

        return (f"{(self.delta_X/2) * self.trap_sum:.3f}")
    



class log:


    def __init__(self,val):


        super(log).__repr__()

        self.val = val

        if self.val > 0:

            self.log = math.log(self.val)
        
        else:

            self.log = 0
        
        
    def __repr__(self):

        return f"{self.log}"
    

    def  __float__(self):
        return float(self.log)
    

    def __add__(self, other):

        if isinstance(other, log):

            return self.log + other.log
        
        elif isinstance(other, (int, float)):

            return self.log + other
    

    def __radd__(self, other):

        return self + other
    

    def __mul__(self,other):

        if isinstance(other, (log)):

            return self.log * other.log
        
        if isinstance(other, (int, float)):

            return self.log * other
    

    def __rmul__(self, other):

        return self * other
        

    def __sub__(self, other):

        if isinstance(other, log):
        
            return self.log + (-other.log)
        
        elif isinstance(other, (int, float)):

            return self.log + (-other)
        
    
    def __rsub__(self, other):

        return (self * -1) + other
    

    def __truediv__(self, other):

        if isinstance(other, log):
        
            return self.log / other.log
        
        elif isinstance(other, (int, float)):

            return self.log / other
    

    def __rtruediv__(self, other):

        return self / other
     
    
    def __pow__(self, other):

        if isinstance(other, log):
        
            return self.log ** other.log
        
        elif isinstance(other, (int, float)):

            return self.log ** other

    
    def __rpow__(self, other):

        return other ** self.log




class range_x:


    def __init__(self, a, b, n):


        super(range_x).__repr__()

        self.delta_x = (b-a)/n

        self.x_range = [a + (i * self.delta_x) for i in range(n+1)]


    def __getitem__(self, val):

        return self.x_range[val]  


    def __repr__(self):

        return f"{self.x_range}"
    

    def __len__(self):

        return len(self.x_range)
    

class remove:

    def __init__(self):
        pass

    



lis = ["a","b","c","d"]
remove()

class MergeSort:

    def __init__(self,List):

        self.List = List
    
        self.sorted = self.sort(self.List)

    @classmethod
    def sort(cls,List):

        if len(List) == 1:
            return List

        midpoint = len(List) // 2
        print(midpoint)
        left = List[:midpoint]
        right = List[midpoint:]
        print(left)
        print(right)
        return cls.merge(left, right)


    @staticmethod
    def merge(left, right):
        output = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])

        return output
    
    #def __len__(self):

    #    return len(self.List)
    
    def __getitem__(self, val):

        return self.List[val]

    def __repr__(self):
        
        return f"{self.sorted}"


def randomNumbers():
    List = [random.randint(1,100) for i in range(6)]
    print(MergeSort(List))

randomNumbers()
    

def MergeSort(List):
    
    if len(List) == 1:
        return List

    midpoint = len(List) // 2
    left = MergeSort(List[:midpoint])
    right = MergeSort(List[midpoint:])
    return merge(left, right)


"""
def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output

"""
