# Add all needed Libraries
from math import pi
from math import e
import math
import numpy as np
# The fact class calculates n! of any number
class fact:
    # Takes in value as a parameter
    def __init__(self,val):
        # If the value ends in only .0 then convert it to an integer
        if str(val)[str(val).find(".")+1:len(str(val))] == "0":
            val = int(val)
        self.val = val
        # If value is a positive integer
        if self.val >= 0 and isinstance(self.val, int):
            # Use recursive calculation
            self.fact = self.calc_int(self.val)
        # If value is a negative integer
        elif self.val < 0 and isinstance(self.val, int):
            # It is a Null type because all negative integers of x! are asymptotes
            self.fact =  np.nan
        # Value is a decimal
        else:
            # Use gamma function
            self.fact = self.calc_float(self.val)
    # Uses recursion to calculate factorial
    def calc_int(self, val):
        # if value is equal to 1 or 0
        # 1! and 0! are equal to 1
        if val == 1 or val == 0:
            return 1
        # value is not 1 or 0
        else:
            # Uses recursion until value is equal to 1
            fact = val *self.calc_int(val-1)
            return fact
    # Uses gamma function to calculate x!
    def calc_float(self, val):
        return math.gamma(val + 1)
    # __repr__ and __float__ is how the object is represented
    def __repr__(self):
        return f"{self.fact}"
    def  __float__(self):
        return float(self.fact)
    # The rest of these dunder methods is for calculations
    # For when the object needs to be added, multiplied, subtracted, divided,...
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
# Uses the trapezium rule to find the area under a curve
class integration:
    # Takes in equation, a and b as parameters
    def __init__(self, equation, a, b):
        # Uses 1000 trapeziums
        # delta_X calculates the width of each trapezium
        self.delta_X = (b-a) / 1000
        # Calculates every x value
        self.x_range = [a + (i * self.delta_X) for i in range(1001)]
        # Formula for trapezium rule
        self.trap_sum = sum([2 * eval(equation, {"x": x, "e" : e}) for x in self.x_range[1:-1]
        ], eval(equation, {"x" : self.x_range[0], "e" : e}) + eval(equation, {"x" : self.x_range[-1], "e" : e}))
    # __repr__ and __float__ is how the object is represented
    def __repr__(self):
        return (f"{(self.delta_X/2) * self.trap_sum}")
    def  __float__(self):
        return (f"{(self.delta_X/2) * self.trap_sum}")
# Calculates the log base n to the x of any number
class log:
    # Takes value and base as parameters
    # base is set to 10 if not taken
    def __init__(self,val, base = 10):
        self.val = val
        # You cannot calculate the log of anything less than or equal to 0
        if self.val > 0:
            # Calculate log
            self.log = math.log(self.val, base)
        # Less than or equal to 0
        else:
            # Equal to null type
            self.log = np.nan
    # __repr__ and __float__ is how the object is represented
    def __repr__(self):
        return f"{self.log}"
    def  __float__(self):
        return float(self.log)
    # The rest of these dunder methods is for calculations
    # For when the object needs to be added, multiplied, subtracted, divided,...
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
# Creates a list of values for x between a and b with n number of elements
class range_x:
    # Takes in a, b, n, as parameters
    def __init__(self, a, b, n):
        # Calculates difference between x values
        self.delta_x = (b-a)/n
        # Calculates all x values
        self.x_range = [a + (i * self.delta_x) for i in range(n+1)]
    # Gets spliced value from list
    def __getitem__(self, val):
        return self.x_range[val]  
    # __repr__ is how the object is represented
    def __repr__(self):
        return f"{self.x_range}"
    # Returns the length of the list
    def __len__(self):
        return len(self.x_range)
# Sorts a List using merge sort
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
# Search through a list using Binary search
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
# Calculates sin(x) using the taylor series
class sin:
    # Takes theta as a parameter
    def __init__(self,theta):
        # Taylor series can only calculate between -4pi and 4pi
        # so we make sure the value is always between this number
        while -4*pi >= theta or theta >= 4*pi:
            if theta <= -4*pi:
                theta += 4*pi
            elif theta >= 4*pi:
                theta -= 4*pi
        self.theta = theta
        # Calculate sin(x)
        self.calculate()
    # Calculate using recursion the taylor series of sin(x)
    def calculate(self, n = 0):
        if n == 20:
            return 0
        # Taylor series of sin(x)
        self.sin = self.calculate(n+1) + (((-1)**n)/ fact((2*n)+1)) * ((self.theta)**((2*n)+1))
        return self.sin
    # __repr__ and __float__ is how the object is represented
    def  __float__(self):
        return float(self.sin)
    def __repr__(self):
        return f"{self.sin}"
    # The rest of these dunder methods is for calculations
    # For when the object needs to be added, multiplied, subtracted, divided,...
    def __add__(self, other):
        if isinstance(other, sin):
            return self.sin + other.sin
        elif isinstance(other, (int, float, fact, log)):
            return self.sin + other
        elif isinstance(other,cos):
            return self.sin + other
    def __radd__(self, other):
        return self + other
    def __mul__(self,other):
        if isinstance(other, (sin)):
            return self.sin * other.sin
        elif isinstance(other, (int, float, fact, log)):
            return self.sin * other
        elif isinstance(other,cos):
            return self.sin * other
    def __rmul__(self, other):
        return self * other
    def __sub__(self, other):
        if isinstance(other, sin):
            return self.sin + (-other.sin)
        elif isinstance(other, (int, float, fact, log)):
            return self.sin + (-other)
        elif isinstance(other,cos):
            return self.sin - other
    def __rsub__(self, other):
        return (self * -1) + other
    def __truediv__(self, other):
        if isinstance(other, sin):
            return self.sin / other.sin
        elif isinstance(other, (int, float, fact, log)):
            return self.sin / other
        elif isinstance(other,cos):
            return self.sin / other
    def __rtruediv__(self, other):
        return ((self)**-1) * other
    def __pow__(self, other):
        if isinstance(other, sin):
            return self.sin ** other.sin
        elif isinstance(other, (int, float, fact, log)):
            return self.sin ** other
        elif isinstance(other,cos):
            return self.sin ** other
    def __rpow__(self, other):
        return other ** self.sin
# Calculates cos(x) using the taylor series
class cos:
    # Takes theta as a parameter
    def __init__(self,theta):
        # Taylor series can only calculate between -4pi and 4pi
        # so we make sure the value is always between this number
        while -4*pi >= theta or theta >= 4*pi:
            if theta <= -4*pi:
                theta += 4*pi
            elif theta >= 4*pi:
                theta -= 4*pi
        self.theta = theta
        # Calculate cos(x)
        self.calculate()
    # Calculate using recursion the taylor series of cos(x)
    def calculate(self, n = 0):
        if n == 20:
            return 0
        # Taylor series of sin(x)
        self.cos = self.calculate(n+1) + (((-1)**n)/ fact(2*n)) * ((self.theta)**(2*n))
        return self.cos
    # __repr__ and __float__ is how the object is represented
    def  __float__(self):
        return float(self.cos)
    def __repr__(self):
        return f"{self.cos}"
    # The rest of these dunder methods is for calculations
    # For when the object needs to be added, multiplied, subtracted, divided,...
    def __add__(self, other):
        if isinstance(other, cos):
            return self.cos + other.cos
        elif isinstance(other, (int, float, fact, log)):
            return self.cos + other
        elif isinstance(other,sin):
            return self.cos + other
    def __radd__(self, other):
        return self + other
    def __mul__(self,other):
        if isinstance(other, (cos)):
            return self.cos * other.cos
        elif isinstance(other, (int, float, fact, log)):
            return self.cos * other
        elif isinstance(other,sin):
            return self.cos * other
    def __rmul__(self, other):
        return self * other
    def __sub__(self, other):
        if isinstance(other, cos):
            return self.cos + (-other.cos)
        elif isinstance(other, (int, float, fact, log)):
            return self.cos + (-other)
        elif isinstance(other,sin):
            return self.cos - other
    def __rsub__(self, other):
        return (self * -1) + other
    def __truediv__(self, other):
        if isinstance(other, cos):
            return self.cos / other.cos
        elif isinstance(other, (int, float, fact, log)):
            return self.cos / other
        elif isinstance(other,sin):
            return self.cos / other
    def __rtruediv__(self, other):
        return ((self)**-1) * other
    def __pow__(self, other):
        if isinstance(other, cos):
            return self.cos ** other.cos
        elif isinstance(other, (int, float, fact, log)):
            return self.cos ** other
        elif isinstance(other,sin):
            return self.cos ** other
    def __rpow__(self, other):
        return other ** self.cos
# Calculates tan(x) using sin(x)/cos(x)
class tan:
    # Takes theta as a parameter
    def __init__(self,theta):
        # Calculates asymptotes
        if theta % (pi/2) <= 0.1:
            # tan(x) is Null
            self.tan = np.nan
        else:
            # tan(x) = sin(x)/cos(x)
            self.tan = (sin(theta)/cos(theta))
    # __repr__ and __float__ is how the object is represented
    def  __float__(self):
        return float(self.tan)
    def __repr__(self):
        return f"{self.tan}"
        # The rest of these dunder methods is for calculations
    # For when the object needs to be added, multiplied, subtracted, divided,...
    def __add__(self, other):
        if isinstance(other, tan):
            return self.tan + other.tan
        elif isinstance(other, (int, float, sin, cos, fact, log)):
            return self.tan + other
    def __radd__(self, other):
        return self + other
    def __mul__(self,other):
        if isinstance(other, (tan)):
            return self.tan * other.tan
        if isinstance(other, (int, float, sin, cos, fact, log)):
            return self.tan * other
    def __rmul__(self, other):
        return self * other
    def __sub__(self, other):
        if isinstance(other, tan):
            return self.tan + (-other.tan)
        elif isinstance(other, (int, float, sin, cos, fact, log)):
            return self.tan + (-other)
    def __rsub__(self, other):
        return (self * -1) + other
    def __truediv__(self, other):
        if isinstance(other, tan):
            return self.tan / other.tan
        elif isinstance(other, (int, float, sin, cos, fact, log)):
            return self.tan / other
    def __rtruediv__(self, other):
        return ((self)**-1) * other
    def __pow__(self, other):
        if isinstance(other, tan):
            return self.tan ** other.tan
        elif isinstance(other, (int, float, sin, cos, fact, log)):
            return self.tan ** other
    def __rpow__(self, other):
        return other ** self.tan
