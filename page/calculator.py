

class Stack(): 
    #Constructor to create a stack 
    def __init__(self, limit=20): 
        self.stk = [] # Create an empty stack 
        self.limit = limit  
    
    #Return True if the stack is empty 
    def getData(self):
        return self.stk
    
    def isEmpty(self): 
        return len(self.stk) <= 0 
    #Return True if the stack is full 
    def isFull(self): 
        return len(self.stk) >= self.limit 
    #Add item to the top of the stack 
    def push(self, item): 
        if self.isFull(): #Check if the stack is full 
            print ('Stack Overflow!') 
        else: 
            self.stk.append(item) 
            print ('Stack after Push', self.stk)
    def pop(self): 
        if self.isEmpty(): #Check if the stack is empty 
            print ('Stack Underflow!') 
            return 0 
        else: 
            return self.stk.pop() 
 #Return (but do not remove) item at the top of the stack  
    def peek(self): 
        if self.isEmpty(): 
            print ('Stack Underflow!') 
            return 0 
        else: 
            return self.stk[-1] 
 #Return the number of items in the stack  
    def size(self): 
        return len(self.stk) 

class Calculator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def calMath(op, op1, op2): 
        if op == "*": 
            return op1 * op2 
        elif op == "/": 
            return op1 / op2 
        elif op == "+": 
            return op1 + op2 
        else: 
            return op1 - op2 

    def postfixEval(self, postfixExpr): 
        operandStack = Stack() 
        tokenList = postfixExpr
        for token in tokenList: 
            if token == " ":
                continue
            elif token in "0123456789": 
                operandStack.push(int(token)) 
            else: 
                operand2 = operandStack.pop()
                operand1 = operandStack.pop() 
                result = Calculator.calMath(token, operand1, operand2) 
                operandStack.push(result) 

        return operandStack.pop()

    def calcInfixToPostfix(self, infixexpr):
        prec = {} 
        prec["*"] = 3 
        prec["/"] = 3 
        prec["+"] = 2 
        prec["-"] = 2 
        prec["("] = 1 
        opStack = Stack() 
        postfixList = [] 
        tokenList = infixexpr.split() 
        for token in tokenList: 
            if token in " ":
                continue
            elif token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":  
                postfixList.append(token) 
            elif token == '(': 
                opStack.push(token) 
            elif token == ')': 
                topToken = opStack.pop() 
                while topToken != '(': 
                    postfixList.append(topToken) 
                    topToken = opStack.pop() 
            else: 
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]): 
                    postfixList.append(opStack.pop()) 
                opStack.push(token) 
        while not opStack.isEmpty(): 
            postfixList.append(opStack.pop()) 
        return " ".join(postfixList)

    def calcInfixToPrefix(self):
        pass

    def convertToBase10(self, number="1010" ,base=3, to=14):
        if base < 1 or base > to:
            raise ValueError("Base must be between 1 and 10")
        
        if base == 1:
            return len(number)
        else:
            return int(number, base)
        
    def convertFromBase10(self, number, to):
        number = int(number)
        if to < 1 or to > 10:
            raise ValueError("Target base must be between 1 and 10")
        
        if to == 1:
            # For base 1, return a string of '1's equal in length to the number
            return '1' * number
        else:
            # Convert number from base 10 to to (2-10)
            result = ""
            while int(number) > 0:
                result = str(int(number) % to) + result
                number //= to
            return result or "0"

# Examples of conversions
# print("Base 10 (3) to Base 1:", convert_from_base_10(3, 1))  # Should print '111'
# print("Base 10 (10) to Base 2:", convert_from_base_10(10, 2))  # Should print '1010'
# print("Base 10 (11) to Base 3:", convert_from_base_10(11, 3))  # Should print '102'
# print("Base 10 (10) to Base 10:", convert_from_base_10(10, 10))  # Should print '10'





        

convertor = Calculator()
# print(convertor.calcInfixToPostfix("A + ( B - C * D )/ E"))
# print(convertor.postfixEval('5 6 2 / 4 * +8-'))
print(convertor.convertToBase10('1010', base=9, to=10)) # Should print 10
print(convertor.convertFromBase10('10', to=9)) # Should print 10
