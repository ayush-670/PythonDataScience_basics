"""
Created on Tue Apr 21 17:55:24 2020

@author: Ayush Singh
"""





'''
The beauty of PYTHON TYPES & SEQUENCES
Lets us first declare a list 'x' with elements of different data types
'''
x=[1,2,'c']
print(x)
#prints -> [1,2,'c'] 
'''Next let us add or append items, or remove items in our list with different data types.
For this we use, append() function
'''
x.append(99)
print(x)
#prints -> [1,2,'c',99]

x.append('abc')
print(x)
#prints -> [1,2,'c',99,'abc']


x.remove(99)
#prints -> [1,2,'c','abc']
'''
Let us now find the return type of the variable 'x'
For this we use the type() function. This can be used to determine the return type of any variable,
or any constant too.
'''
print(type(x))
#prints -> <class 'list'>

x=(1,2,'c')
print(type(x))
#prints -> <class 'tuple'>

print(type(1.1))
#prints -> <class 'float'>

''' 
We will now iterate through the list/tuple.
Let us figure the two ways through which we can loop through each item
'''
x1=[1,8,'L']
for item in x1:
    print(item, end= " ")
print()
#prints ->1 8 L 

#We can even use the  indexing operator method given below:

x2=[44,'Abc', 67]
i=0
while( i != len(x2) ):
    print(x2[i], end = " ")
    i = i + 1
print()
#prints -> 44 Abc 67 
'''
We even see the len() function here, which simply returns the length of the list, here in the above example.
end= " ", helps us print the elements in the same line.
Next, we will find out what more can we do with lists.
'''
#Let us use + to concatenate lists.
print([1,2] + [3,4])
#prints ->[1, 2, 3, 4]

#repeating lists using '*'
print([1,2,3]*3)
#prints ->[1, 2, 3, 1, 2, 3, 1, 2, 3]

#let us use the 'in' operator
x3= 1 in x1
print(x3)
#prints -> True
# As the 'in' operator checked for us whether 1 is in the list x1 or not  

'''
Moving on, let us work on strings in python.
We will first see how we can slice a string to get its substring
'''
x4 = 'Dr. Abhishek Singh'
print(x4[0]) 
#first character, prints -> D

print(x4[0:1])
#first character, but we have explicitly set the end character, prints ->D

print(x4[0:2])
#first two characters, prints ->Dr

print(x4[4:-7])
# negative numbers can be used to track the string in reverse order, prints -> Abhishe

print(x4[-1])
#This will return the last element of the string, prints -> h

print(x4[-4:-2])
#This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end.
#prints-> in

print(x4[:3])
#This is a slice from the beginning of the string and stopping before the 3rd element, prints ->Dr.

print(x4[3:])
#And this is a slice starting from the 4th element of the string and going all the way to the end, prints->  Abhishek Singh

firstname = 'Robin Guruswamy Arjun Malangam'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Mangalam Alexander Hier Mit Schulz'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
#prints-> Mangalam
print(lastname)
#prints->Schulz
#Note: split returns a list of all the words in a string, or a list split on a specific character.

''' 
Make sure you convert objects to strings before concatenating.
Chris' + 2 , will show us an error as-> TypeError: can only concatenate str (not "int") to str
'''
print('Python' + str(2))
#prints -> Python2


'''
Let us now know about Dictionaries. 
Dictionaries associate keys with values. Hence if we want to access a particular value in the dictionary, we must know the key of the particular value
Let us now work with Dictionaries.
'''


x5 = {'Ayush': 'ayush@x.com', 'Abhishek': 'abhishek.com'}
print(x5['Ayush']) # Retrieve a value by using the indexing operator
#prints->ayush@x.com
print(x5['Abhishek'])
#prints ->abhishek.com

#We can also iterate over all of the keys and values:
for n in x5.keys():
    print(n)
#prints->Ayush Abhishek
    
for n in x5.values():
    print(n)
#prints->ayush@x.com abhishek.com
    
for name, email in x5.items():
    print(name)
    print(email)
#here we can access the keys as well as value, together
''' 
prints-> Ayush
ayush@x.com
Abhishek
abhishek.com
'''

'''
Let us now see Sequence unpacking '''
x6 = ('Ayush', 'Singh', 'singh@x.com')
first, last, email = x6
print(first)
#prints ->Ayush
print(last)
#prints -> Singh
print(email)
#prints -> singh@x.com


'''
Its a wrap! for this code!
More codes on DataScience is available at 
'''
