f=open('FILEHANDLINF_TO_PRINt_THE_LINES_START_WITH_A_AND_E.txt','r')
out=f.readlines()
for i in out:
    for j in i:
        if j=='A' or j=='E':
            print(j,end='',file=f)
print(file=f)

f.close()