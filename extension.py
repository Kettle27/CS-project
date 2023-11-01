import math
import numpy as np




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

            self.log = np.log(self.val)
        
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
    



"""fig = plt.figure()
ax = fig.add_subplot()


fx = "1/x"

X = range_x(-5, 5, 10)

y = []
for x in X:
    try:
        eval(fx)
        y.append(eval(fx))
    
    except ZeroDivisionError:
        print(x)
        X.remove(x)





# y = [eval(fx) for x in x if eval(fx) != ZeroDivisionError]

print(X)
print(y)

#graph = ax.plot(X, y)

plt.show()
"""
