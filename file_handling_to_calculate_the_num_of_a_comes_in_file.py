f=open(r'filehandling_to_find_how_many_times_a_come.txt','r')
count=0
char=input('Enter the charter : ')
out=f.read()
for i in out:
    if i==char:
        count=count+1
print(count)