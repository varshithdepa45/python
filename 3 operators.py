index_count=0
for letter in 'salaar':
    print(f"at index {index_count } the letter is {letter}")
    index_count+=1
#zip
list1=[1,2,3]
list2=['a','b','c']
x=zip(list1,list2)
print(x)
for item in zip(list1,list2):
    print(item)
print(list(zip(list1,list2)))
print('salaar' in {'salaar':45457})
from random import shuffle
mylist=[1,2,3,4,5,6,7]
shuffle(mylist)
print(mylist)
from random import randint
print(randint(0,199))

