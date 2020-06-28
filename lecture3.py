# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 02:02:48 2020

@author: Ayush Singh
"""
import numpy as np
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2

list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

#LISTcOMPREHENSION
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [print(j*i) for i in range(10) for j in range(10)]

#Here’s a harder question which brings a few things together.

#Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user.

#Write an initialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

print(correct_answer[:50])
old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old
new[0, :2] = 0

print(old)

nOne=np.array([1, 2, 3] * 3)
print(nOne)
nTwo=np.repeat([1, 2, 3], 3)
print(nTwo)

print('New program')
p = np.ones([2, 3], int)
print(p)
print('New program')
print(np.vstack([p, 2*p]))
print('New program')
print(np.hstack([p, 2*p]))


print(['a', 'b', 'c'] + [1, 2, 3])

y=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
y.resize(6,6)
print(y[2:4,2:4])
