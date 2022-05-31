# lst=['Vishnukant','Shubham','Jatin Gupta','Ashish']
# lst.sort(key=lambda lst:sum(ord(i)for i in lst))
# print(lst)
def value(x):
    sum=0
    lst1=[]
    for i in range(x):
        sum=sum+ord(i)
        
    return sum
lst=['Vishnukant','Shubham','Jatin Gupta','Ashish']
out=value(lst)
print(out)