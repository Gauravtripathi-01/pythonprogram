def vote(a):
    if a>=18:
        return 'He or She is able to vote '
    else:
        return 'He or She is not able to vote'
age=int(input('Enter the age of the person : '))
out=vote(age)
print(out)