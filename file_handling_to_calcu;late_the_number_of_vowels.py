f=open('filehandling_to_find_the_number_of_vowels.txt','r')
out=f.read()
count=0
consonant=0
for i in out:
    for j in i:
        if j=='A' or j=='E' or j=='I' or j=='O' or j=='U' or j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            count=count+1
        else:
            consonant=consonant+1
print('The number of vowels present in file : ',count)
print('The number of consonant is : ',consonant)
f.close()