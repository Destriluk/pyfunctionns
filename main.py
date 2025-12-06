print("###############################")
print("*******Functions*********")
print("###############################")
def sub(a,b,c):
    return a-b-c

def add(a,b,c):
    return a+b+c

def divide(a,b,c):
    if c != 0 :
        return a/b/c
    else :
        return "cannot divide by zero"
    
def multiply(a,b,c):
    return a*b*c    

print("Addition :",add(5,79,1023))
print("subtraction :",sub(78,45,884))
print("Division :",divide(85,76,805))
print("Multiplication :",multiply(88,65,907))