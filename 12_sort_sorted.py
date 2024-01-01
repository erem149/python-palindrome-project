# Sort and Sorted
print('sort() and sorted()')
print('Immutability and return values')

my_list = [1, 5, 3, 7, 2]
my_dict = {'car':4, 'dog':2, 'add':3, 'bee':1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

print(my_list, 'original - sorted')
print(my_list.sort())
print(my_list,'new - sort')
print(my_list.reverse())
print(my_list,'new - reverse')
print(my_list, 'original - sorted')
print(sorted(my_list))
print(my_list,'new - sorted')
mylist_sorted = sorted(my_list)
print(mylist_sorted, 'mylist_sorted_var')

print(my_tuple, 'original - tuple')
print(sorted(my_tuple))
print(my_tuple, 'new - mytuple')

print(my_string, 'original - string')
print(sorted(my_string))
print(my_string, 'new - mystring')

print(my_dict, 'original - dict')
print(sorted(my_dict))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ items')
print(sorted(my_dict.items()))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ values')
print(sorted(my_dict.values()))
print(my_dict, 'new - mydict')

print(my_dict, 'original - dict w/ values')
print(sorted(my_dict.values(), reverse=True))
print(my_dict, 'new - mydict w/ val & reverse')

print(my_list, 'original - reversed w/ list')
print(list(reversed(my_list))) # same result
print(my_list,'new - reversed w/ list')
print(my_list[::-1]) # same result

my_list = [1, 5, -3, 7, -2]
my_llist = [['car',4,65], ['dog',2,30], ['add',3,10], ['bee',1,24]]
print(sorted(my_list, key = abs)) # we can added any function to this key
print(sorted(my_llist, key = lambda item : item[2]))