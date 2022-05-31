a=input('Enter the value which you want to replace  :')
b=input('Enter rhe value which you ewant to enter in the place of replace value : ')
f=open('file_handlind_to_read_the_file_and_then_replace_I_byE.txt','r')
count=0
out=f.readlines()
print(out)
for i in out:
    if a in i:
        replacement=i.replace(a,b)
    out=replacement
    continue
    #count=count+1
print(out)

f.close()