
   
# Number=eval(input("Enter the Number : "))
# if Number > 1:
#     for i in range(2,Number+1):
#         if Number%i==0:
#             print("Given number is not prime number")
#         else:
#             print("Given number is prime number")
#         break
# else:
#     print("Enter number is not prime number")

def prime(x):
    if x>1:
        for i in range(2,x+1):
            if x%i==0:
                return False
            else:
                return True

num=eval(input('Enter the number : '))
out=prime(num)
print(out)