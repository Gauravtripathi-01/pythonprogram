from math import fabs

def factorial(x):
    fact=1
    dict ={}
    for i in range(1,x+1):
        fact=fact*i
        dict[i] = fact

    return dict

def feab(n):
  x=0
  y=1
  dict1 = {}
  for i in range(2,n):
      sum=x+y
      dict1[i] = sum
      x = y
      y = sum
      
  return dict1


num=int(input('Enter the number whose factorial you want to calculate : '))
out=factorial(num)
aa = feab(num)
print(aa)
xx = [out,aa]
print('The factorial of the given number is : ',xx)