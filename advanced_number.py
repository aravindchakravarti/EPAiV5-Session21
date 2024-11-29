class AdvancedNumber:
    def __init__(self, number=0):
        """ Initialize the variable """
        self.value = number

    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed")

    def __str__(self):
        return f"Value: {self.value}"
    
    def __repr__(self):
        return f"AdvancedNumber({self.value})"
    
    def __add__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        sum_value = AdvancedNumber()
        sum_value.value = self.value + other.value

        return sum_value
    
    def __sub__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        sum_value = AdvancedNumber()
        sum_value.value = self.value - other.value

        return sum_value
    
    def __mul__(self, other):
        if (isinstance(self, AdvancedNumber) and isinstance(other, AdvancedNumber)):
            sum_value = AdvancedNumber()
            sum_value.value = self.value * other.value

        elif (isinstance(self, AdvancedNumber) and isinstance(other, (int, float))):
            sum_value = AdvancedNumber()
            sum_value.value = self.value * other
        
        else:
            raise ValueError("Operands must of type AdvancedNumber, int or float")

        return sum_value
    
    def __truediv__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        if other.value == 0:
            raise ValueError("Cannot divide by zero")

        sum_value = AdvancedNumber()
        sum_value.value = self.value / other.value

        return sum_value
    
    def __mod__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        sum_value = AdvancedNumber()
        sum_value.value = self.value % other.value

        return sum_value
    
    def __gt__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        return(self.value > other.value)
    
    def __ne__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        return(self.value != other.value)
    
    def __ge__(self, other):
        if not (isinstance(self, AdvancedNumber) or isinstance(other, AdvancedNumber)):
            raise ValueError("Both operands must of type AdvancedNumber")
        
        return(self.value >= other.value)
    
    def __hash__(self):
        return hash(self.value)
    
    def __call__(self, *args, **kwds):
        if not isinstance(self, AdvancedNumber):
            raise ValueError("Operands must of type AdvancedNumber")
        
        return self.value * self.value
    
    def __bool__(obj):
        if not isinstance(obj, AdvancedNumber):
            raise ValueError("Argument must of type AdvancedNumber")
        
        if obj.value == 0:
            return False
        else:
            return True
        
    def __format__(self, format_spec):
        if not isinstance(self, AdvancedNumber):
            raise ValueError("Argument must of type AdvancedNumber")
        
        return format(self.value, format_spec) 