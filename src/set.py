# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: viejoemer

HowTo create and use the data structure set in Python?

¿Cómo crear y usar la estructura de datos set en Python?

A set object is an unordered collection of distinct hashable objects.
Common uses include membership testing, removing duplicates from a 
sequence, and computing mathematical operations such as intersection,
union, difference, and symmetric difference.
'''
 
#Create a empty set.
s = set([])
print(type(s))
print(s)

s = set()
print(type(s))
print(s)

#Create a set with values.
s = set([0,1,2,3,4,5,6,7,8,9])
print(s)

#Create a set with differents values.
s = set([1,'string',1.1])
print(s)

#Create a set from a list.
l = ['one','two','three',1,2,3,1.1,2.2,3.3]
s = set(l)
print(s)

#Create a set with {}.
s = {1,2,3,4}
print(type(s))
print(s)
