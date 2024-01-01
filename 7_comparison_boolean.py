# Comparisons and Boolean
a = 7
b = 3
print('a == b is ', a == b) # Output: False
print('a != b is ', a != b) # Output: False
print('a > b is ', a > b) # Output: False
print('a < b is ', a < b) # Output: False
print('a >= b is ', a >= b) # Output: False
print('a <= b is ', a <= b) # we can use ==, >, <, >=, <=. Output: False
print('o' in 'John') # Output: True
print('o' not in 'John') # Output: False
print(a is b) # Output: True
print(id(a), id(b)) # Output: Same memory
a = [3,7,42]
b = [3,7,42]
print(a is b) # Output: False
print(id(a), id(b)) # Output: Different memory
print(int(True)) # Output: 1
print(int(False)) # Output: 0
print(bool('Parrot')) # Output: True
print(bool(' ')) # Output: True
print(bool('')) # Output: False
print(bool(42)) # Output: True
print(bool(0)) # Output: False
print(bool([1,2])) # Output: True
print(bool([])) # Output: False
print(42 + True) # Output: 43
print(42 + False) # Output: 42