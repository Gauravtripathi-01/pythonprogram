n=int(input('Enter the number of terms : '))
lst=[]
lst1=[]
lst2=[]
for i in range(1,n+1):
    lst.append(i)
for i in range(1,n+1):
    element=i*i
    lst1.append(element)
out=dict(zip(lst,lst1))
print(out)