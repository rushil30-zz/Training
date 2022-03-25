class Cannotadd(Exception):
    def __init__(self, message = "Cannot add Even and odd numbers"):
        self.message = message
        super().__init__(self.message)  

num1 = float(input("Enter first number:"))        
num2 = float(input("Enter second number:"))
res = num1 + num2
if (num1 % 2 == 0):
    if(num2 % 2 != 0):
        raise Cannotadd()

elif(num2 % 2 ==0):
    if(num1 % 2 !=0):
        raise Cannotadd()    

print("The Sum is:", res)               
