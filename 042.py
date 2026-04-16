class Integer:
    def __init__(self, number):
        if not isinstance(number, str):
            raise ValueError(f"Expected string but given {type(number)}")
        if not str.isdigit(number):
            raise ValueError(f"String must contains digit only")
        self.number = list(str(number))
    
    def __add__(self, other):
        a = None
        b = None
        
        other = (other if isinstance(other, Integer) else Integer(other)).number
        
        if len(self.number) >= len(other):
            a = self.number
            b = other
        else:
            a = other
            b = self.number
        
        result = []
        current_store = 0
        for a_index in range(len(a)):
            add = ""
            if a_index > len(b) - 1:
                add = str(int(a[-(a_index + 1)]) + current_store)
            else:
                add = str(int(a[-(a_index + 1)]) + int(b[-(a_index + 1)]) + current_store)
            
            if len(add) >= 2:
                current_store = int(add[0])
                    
                result.append(add[1])
                if a_index >= len(a) - 1:
                    result.append(add[0])
            else:
                result.append(add[0])
                current_store = 0
        
        result.reverse()
        result = "".join(result)
        return Integer(result)
    
    def __mul__(self, other):
        a = None
        b = None
        
        other = (other if isinstance(other, Integer) else Integer(other)).number
        
        if len(self.number) >= len(other):
            a = self.number
            b = other
        else:
            a = other
            b = self.number
        
        states = []
        for b_index in range(len(b)):
            state = []
            current_store = 0
            for a_index in range(len(a)):
                mul = str(int(a[-(a_index + 1)]) * int(b[-(b_index + 1)]) + current_store)
                
                if len(mul) >= 2:
                    current_store = int(mul[0])
                    
                    state.append(mul[1])
                    if a_index >= len(a) - 1:
                        state.append(mul[0])
                else:
                    state.append(mul[0])
                    current_store = 0
            
            state.reverse()
            for index in range(b_index):
                state.append("0")
            states.append(state)
        
        current_add = Integer("0")
        for state in states:
            current_add = current_add + "".join(state)
        return current_add
        
    def string(self):
        return "".join(self.number)

def factorial(n):
    if len(n.number) == 1 and n.number[0] == '1':
        return Integer("1")
    return 
a = Integer("86744457800976743339")
b = Integer("677656788987667899977721")

print((a * b).string)