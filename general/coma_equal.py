"""
Coma equal
"""

numbers = [1, 2, 3, 4, 5]

try:
    a, b, c = numbers
    print(f'{a = } {b = } {c = }')
except ValueError as e:
    print(e.__class__, e)  # <class 'ValueError'> too many values to unpack (expected 3)

try:
    a, b, *c = numbers
    print(f'{a = } {b = } {c = }')  # a = 1 b = 2 c = [3, 4, 5]
except ValueError as e:
    print(e.__class__, e)

try:
    x, y, *k = c
    print(f'{x = } {y = } {k = }')  # x = 3 y = 4 k = [5]
except ValueError as e:
    print(e.__class__, e)

try:
    x, y, k = c
    print(f'{x = } {y = } {k = }')  # x = 3 y = 4 k = 5
except ValueError as e:
    print(e.__class__, e)

number = [100]
n, = number
print(f'{n = }')  # n = 100
