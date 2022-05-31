First_number=eval(input("Enter the first number : "))
Second_number= eval(input("Enter the second number : "))
# out=(First_number-Second_number)*(First_number>Second_number)+(Second_number-First_number)*(Second_number>First_number)

# method 2- 
out=[First_number-Second_number,Second_number-First_number][Second_number>First_number]
print(out)