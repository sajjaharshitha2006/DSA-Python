a=int(input("enter youe first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third number:"))
if a>=b and a>=c:
    largest =a 
elif b>=a and b>=c:
    largest =b
else:
    largest =c
print("the largest number", largest)