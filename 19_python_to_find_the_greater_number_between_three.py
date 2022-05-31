x= eval(input("Enter the first number : "))
y= eval(input("Enter the second number : "))
z= eval(input("Enter the third number : "))
if x>y and x>z:
    print("{0} is greater {1} and {2}".format(x,y,z))
elif y>x and y>z:
    print("{0} is greater {1} and {2}".format(y,x,z))    
elif z>x and z>y:
    print("{0} is greater {1} and {2}".format(z,x,y))
else :
    print("Any two or more than two values are same so please input correct details")