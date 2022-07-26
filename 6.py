try:
 print("outer try block")
 n = int(input("enter a number"))
 print(10/n)
except TypeError:
 print("Hello")
else:
 print("outer no excepiton") 
try:
 print("inner try")
 print("anu"+"preet")
except ArithmeticError:
 print(10/5)
else:
 print("inner no exception")

finally:
 print("finally block") 
