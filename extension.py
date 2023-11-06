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
    


class circular_queue:

    queue = [pi/2, pi, 3*pi/2, 2*pi]
    pointer = -1

    
    @staticmethod
    def get():
        if circular_queue.pointer != len(circular_queue.queue)-1:
            circular_queue.pointer += 1
            return circular_queue.queue[circular_queue.pointer]
        
        else:
            circular_queue.pointer = 0
            return circular_queue.queue[circular_queue.pointer]
        


class MergeSort:


    def __init__(self,List):
    
        self.List = self.sort(List)


    @classmethod
    def sort(cls,List):

        if len(List) == 1:
            return List

        midpoint = len(List) // 2
        left = cls.sort(List[:midpoint])
        right = cls.sort(List[midpoint:])
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
    

    def __getitem__(self, val):

        return self.List[val]


    def __repr__(self):
        
        return f"{self.List}"
    
    
    def __len__(self):

        return len(self.List)
    


class Bin_search:

    def __init__(self, arr, find):
        
        self.arr = MergeSort(arr)

        self.find = find

        self.found = self.search(self.arr)


    def search(self, array):

        if len(array) >= 0:
            
            mid = len(array) // 2

            if array[mid] == self.find:
                return mid
            
            elif array [mid] > self.find:
                
                return self.search(array[:mid])
            
            else:

                return self.search(array[mid:])

        else:

            return -1
        

    def __repr__(self):

        return f"{self.found}"


