""" Program make a simple calculator that can add, subtract, multiply and divide using functions"""
#This  funciton adds two numbers
def add(a,b):
    return a+b
#This funciton subtracts  two numbers
def subtract(a,b):
    return a-b
#This  funciton multiply  two numbers
def multiply(a,b):
    return a*b
#This  funciton divides two numbers
def divide(a,b):
    return a/b
print("1.Add")
print("2.Subtract")
print("3.Mutiply")
print("4.Divide")

#Take input from the user
choice=input("Enter choice (1/2/3/4):")
num1=int(input("Enter fist number:"))
num2=int(input("Enter second number:"))

if choice=='1':
    print(num1,'+',num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,'-',num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,'*',num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,'/',num2,"=",divede(num1,num2))
else:
    print("Invalid input")








