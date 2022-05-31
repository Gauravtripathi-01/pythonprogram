import random
f=open('file_handling_problem_1.txt','r')
lst1=[]
st=' '
out=f.readline()
out1=random.choices(out,k=5)
print(out,end='\t')
print(out1)
f.close()