import operator 
dct={'Apple':100,'papaya':60,'Mango':35,'orange':40}
dict_in_ascending_order=dict(sorted(dct.items(),key=operator.itemgetter(1)))
dict_in_decending_order=dict(sorted(dct.items(),key=operator.itemgetter(1),reverse=True))
print('The dictionary arranged in ascending order is : ',dict_in_ascending_order)
print('The dictionary arranged in decending  order is : ',dict_in_decending_order)



# #method1 - to sort the dictionary in ascending order 
# a={'Vishnu':56,'Rishi':48,'Jatin':38}
# b=[]
# for i in a.keys():
#     b.append(i)
# b.sort()
# print(b)

# #method 2 to sort the dictionary ion decending order 
# a={'Vishnu':56,'Rishi':48,'Jatin':38}
# b=[]
# for i in a.keys():
#     b.append(i)
# b.sort(reverse=True)
# print(b)