dct={'Name':'Gaurav','rollno':6,'College':'gla university','College':'Gla university','rollno':65,'Name':'Vishnukant'}
dct1={}
for i in dct:
    if i not in dct1:
        dct1[i]=dct[i]
    #continue
print(dct1)