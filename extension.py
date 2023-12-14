from math import pi
from math import e
import math
import numpy as np



class fact:


    """Returns the Factorial of a number or a list of numbers:
    
    Case 1:
    If the number is a positive integer then we do normal recursion
    to find the factorial

    Case 2:
    If the number is not a positive integer (either a decimal and or 
    a negative number) then we use the gamma function

    """


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
        
        

    def calc_int(self, val):


        if val == 1 or val == 0:


            return 1
        

        else:

            fact = val *self.calc_int(val-1)


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


        return ((self)**-1) * other
     
    
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


        self.trap_sum = sum([2 * eval(equation, {"x": x}) for x in self.x_range[1:-1]
        ], eval(equation, {"x" : self.x_range[0]}) + eval(equation, {"x" : self.x_range[-1]}))

        
    def __repr__(self):


        return (f"{(self.delta_X/2) * self.trap_sum:.3f}")
    

    def  __float__(self):


        return (f"{(self.delta_X/2) * self.trap_sum:.3f}")
    



class log:


    def __init__(self,val, base = 10):


        super(log).__repr__()


        self.val = val


        if self.val > 0:


            self.log = math.log(self.val, base)
        

        else:


            self.log = np.nan
        
        
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


        return ((self)**-1) * other
     
    
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




class sin:


    def __init__(self,theta):


        super(log).__repr__()


        while -4*pi >= theta or theta >= 4*pi:


            if theta <= -4*pi:


                theta += 4*pi
            
            elif theta >= 4*pi:


                theta -= 4*pi


        self.theta = theta
    

        self.calculate()


    def calculate(self, n = 0):


        if n == 20:


            return 0


        self.sin = self.calculate(n+1) + (((-1)**n)/ fact((2*n)+1)) * ((self.theta)**((2*n)+1))
        

        return self.sin
    

    def  __float__(self):


        return float(self.sin)
    
    def __repr__(self):


        return f"{self.sin}"
    

    def __add__(self, other):


        if isinstance(other, sin):


            return self.sin + other.sin
        
        
        elif isinstance(other, (int, float)):


            return self.sin + other


        elif isinstance(other,cos):


            return self.sin + other
    

    def __radd__(self, other):


        return self + other
    

    def __mul__(self,other):


        if isinstance(other, (sin)):


            return self.sin * other.sin
        

        if isinstance(other, (int, float)):


            return self.sin * other
    

    def __rmul__(self, other):


        return self * other
        

    def __sub__(self, other):


        if isinstance(other, sin):
        

            return self.sin + (-other.sin)
        

        elif isinstance(other, (int, float)):


            return self.sin + (-other)
        
    
    def __rsub__(self, other):


        return (self * -1) + other
    

    def __truediv__(self, other):


        if isinstance(other, sin):
        

            return self.sin / other.sin
        

        elif isinstance(other, (int, float)):


            return self.sin / other


        elif isinstance(other,cos):


            return self.sin / other
    

    def __rtruediv__(self, other):


        return ((self)**-1) * other
     
    
    def __pow__(self, other):


        if isinstance(other, sin):
        

            return self.sin ** other.sin
        

        elif isinstance(other, (int, float)):


            return self.sin ** other

    
    def __rpow__(self, other):


        return other ** self.sin
    



class cos:


    def __init__(self,theta):


        super(cos).__repr__()


        while -4*pi >= theta or theta >= 4*pi:


            if theta <= -4*pi:


                theta += 4*pi
            
            elif theta >= 4*pi:


                theta -= 4*pi


        self.theta = theta
    

        self.calculate()


    def calculate(self, n = 0):


        if n == 20:


            return 0


        self.cos = self.calculate(n+1) + (((-1)**n)/ fact(2*n)) * ((self.theta)**(2*n))
        

        return self.cos
    

    def  __float__(self):


        return float(self.cos)
    
    def __repr__(self):


        return f"{self.cos}"
    

    def __add__(self, other):


        if isinstance(other, cos):


            return self.cos + other.cos
        
        
        elif isinstance(other, (int, float)):


            return self.cos + other
        
        
        elif isinstance(other,sin):


            return self.cos + other
    

    def __radd__(self, other):


        return self + other
    

    def __mul__(self,other):


        if isinstance(other, (cos)):


            return self.cos * other.cos
        

        if isinstance(other, (int, float)):


            return self.cos * other
    

    def __rmul__(self, other):


        return self * other
        

    def __sub__(self, other):


        if isinstance(other, cos):
        

            return self.cos + (-other.cos)
        

        elif isinstance(other, (int, float)):


            return self.cos + (-other)
        
    
    def __rsub__(self, other):


        return (self * -1) + other
    

    def __truediv__(self, other):


        if isinstance(other, cos):
        

            return self.cos / other.cos
        

        elif isinstance(other, (int, float)):


            return self.cos / other
    

    def __rtruediv__(self, other):


        return ((self)**-1) * other
     
    
    def __pow__(self, other):


        if isinstance(other, cos):
        

            return self.cos ** other.cos
        

        elif isinstance(other, (int, float)):


            return self.cos ** other

    
    def __rpow__(self, other):


        return other ** self.cos
    

class tan:


    def __init__(self,theta):


        self.tan = (sin(theta)/cos(theta))


    def  __float__(self):


        return float(self.tan)
    

    def __repr__(self):


        return f"{self.tan}"
    

    def __add__(self, other):


        if isinstance(other, tan):


            return self.tan + other.tan
        

        elif isinstance(other, (int, float)):


            return self.tan + other
        

        elif isinstance(other,sin):


            return self.tan + other
    

    def __radd__(self, other):


        return self + other
    

    def __mul__(self,other):


        if isinstance(other, (tan)):


            return self.tan * other.tan
        

        if isinstance(other, (int, float)):


            return self.tan * other
    

    def __rmul__(self, other):


        return self * other
        

    def __sub__(self, other):


        if isinstance(other, tan):
        

            return self.tan + (-other.tan)
        

        elif isinstance(other, (int, float)):


            return self.tan + (-other)
        
    
    def __rsub__(self, other):


        return (self * -1) + other
    

    def __truediv__(self, other):


        if isinstance(other, tan):
        

            return self.tan / other.tan
        

        elif isinstance(other, (int, float)):


            return self.tan / other
    

    def __rtruediv__(self, other):


        return ((self)**-1) * other
     
    
    def __pow__(self, other):


        if isinstance(other, tan):
        

            return self.tan ** other.tan
        

        elif isinstance(other, (int, float)):


            return self.tan ** other

    
    def __rpow__(self, other):


        return other ** self.tan
    

