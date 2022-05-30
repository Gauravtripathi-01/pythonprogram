from re import X


first_number=eval(input("Enter the first number : "))
second_number=eval(input("Enter the second number : "))
x = first_number
y=second_number
x,y=y,x 
print(x,y,sep=',')