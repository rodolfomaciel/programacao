#! /usr/bin/python
# codings: utf-8

items = [1,2,3,4,5,6,7,8,9]
squared = list(map(lambda x: x**2, items))
print(squared)
# Output:[1, 4, 9, 16, 25, 36, 49, 64, 81]


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
