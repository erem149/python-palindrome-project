failed_subjects = str(int(float("6.5")))
pronouns='It\'s'
print(pronouns + " failing " + failed_subjects + " subjects.")
msg='Welcome to Python 101: Strings'
print(len(msg))
print(msg.count('o'))

#slicing
msg1=msg[-10] + ' ' + msg[:7] + ' ' + msg[-5:-1] + ' ' +  msg[8:10] + ' ' + msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1[::-1].title()) # printed "1 Welcome Ring To Tyler" as backwards
print('Python' not in msg) # we can use 'not' or 'not in' commands
                           #to describe whether it's TRUE or FALSE
print(f'[{pronouns.capitalize()} lovely day!]')

# # - Create a distance converter converting Km to miles
# # - Take two inputs from user: Their first name and the distance in km
# # - Print: Greet user by name and show km, and mile values
# # - 1 mile is 1.609 kilometers
# # - hint: use correct types for calculating and print
# # - Did you capitalize the name
# user_name = input('Enter your name : ')
# distance_in_km = input('Enter your distance in km : ')
# distance_in_mi = float(distance_in_km) / 1.609
# print(f'Hi {user_name}! {distance_in_km} km is equivalent to {round(distance_in_mi, 1)} miles.')

#Lists
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911,130,328,535,740,308]
print(friends[1], friends[4])
print(len(friends))
print(friends.index('Eric'))
print(friends.count('Eric'))
friends_sort = sorted(friends) # return the sorted list
print(friends_sort)
friends.sort() # sort the list in place
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(min(cars))
print(min(friends))
print(max(cars))
print(sum(cars))
friends.append('TerryG1') # add word to the last position
print(friends)
friends.insert(1, 'TerryG2') # add word to the current by appointing index we choose
print(friends)
friends[2]='TerryG3' # replcae Terry with TerryG
print(friends)
friends.extend(cars) # join friends + cars lists
print(friends)
friends.remove("Terry")
print(friends)
friends.pop(-1) # pop will remove the last position by default 
                # and pop is stored into memory and can be used it again in the program
print(friends)
# friends.clear() # empty []
# print(friends)
# del friends # remove completely the element
del friends[2] # remove completely the element
print(friends)
new_friends = friends[:]
friends_copy = friends.copy()
friends_list = list(friends)
print(friends)
print(new_friends)
print(friends_copy)
print(friends_list)