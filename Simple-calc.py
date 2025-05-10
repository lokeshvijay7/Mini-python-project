print("Please Enter a choice for calculate")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division ")
def add(a,b):
  return a+b
  
def sub(e,f):
  return e-f
 
def mult(g,h):
 return g*h
 
def div(i,j):
  return i/j
while True:
    choice =int(input("choice :"))
    if choice == 1:
        print ("Enter a two number to add ")
        a = int(input("Enter a first number :"))
        b = int(input("Enter a second number :"))
        print("After add two number :",add(a,b))

    if choice == 2:
        print ("Enter a two number to sub ")
        e = int(input("Enter a first number :"))
        f = int(input("Enter a second number :"))
        print("After subract two number :",sub(e,f))

    if choice == 3:
        print ("Enter a two number to multi ")
        g = int(input("Enter a first number :"))
        h = int(input("Enter a second number :"))    
        print("After multiplay two number :",mult(g,h))

    if choice == 4:
          print ("Enter a two number to div ")
          i = int(input("Enter a first number :"))
          j = int(input("Enter a second number :"))    
          print("After divide two number :",div(i,j))

