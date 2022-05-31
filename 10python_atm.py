amount=eval(input("Enter the value: "))
amount = amount-100
a=amount//2000
amount=amount-a*2000
b=amount//500
amount=amount-b*500
amount=amount+100
c=amount//100
amount=amount-c*100
out=f'''The total numbers of 2000 notes is {a}
the total numbers of 500 notes is {b}
the total number of 100 notes is {c}'''
print(out)
© 2022 GitHub, Inc.
