#Tuples - faster Lists you cannot change
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
print(friends[2:4])
print(friends_tuple[2:4])
#Sets - blazingly fast unordered Lists
print(friends_set)
print(friends_set.intersection(my_friends_set)) 
print(friends_set.difference(my_friends_set)) 
print(friends_set.union(my_friends_set)) 
# List < Tuple < Set -> Faster
#empty Lists
empty_list = []
empty_list = list()
#empty Tuple
empty_tuple = ()
empty_tuple = tuple()
#empty Set
empty_set = {} # this is wrong, this is dictionary
empty_set = set()
# Sets - Exercise
#1. Check if 'Eric' and 'John' exist in friends -> using in
#2. Combine or add the two sets -> using union and |
#3. Find names that are in both sets -> using intersection
#4. Find names that are only in friends -> using difference and -
#5. Show only the names who only appear in one of the lists -> using ^ and symmetric_difference
#6. Create a new cars-list without duplicates -> using set and list
friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']
print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
print(friends | my_friends)
print(friends.intersection(my_friends))
print(friends.difference(my_friends))
print(friends - my_friends)
print(my_friends.difference(friends))
print(my_friends - friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl = list(set(cars))
print(cars_no_dupl)